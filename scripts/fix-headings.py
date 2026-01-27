#!/usr/bin/env python3
"""Remove redundant patterns from documentation."""

import os
import re


def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    changed = False
    i = 0

    while i < len(lines):
        line = lines[i]

        # Remove !!! question "What is..." and "Protection Modes" admonition blocks
        # These blocks may have multi-line content with wrapped text (no indent)
        if re.match(r'^!!!\s+question\s+"(What is|Protection Modes)', line):
            changed = True
            i += 1
            # Skip indented content (4-space indent)
            while i < len(lines) and lines[i].startswith('    '):
                i += 1
            # Skip wrapped continuation lines (not blank, not a new structural element)
            while i < len(lines):
                curr = lines[i]
                # Stop at blank line - marks end of admonition
                if curr.strip() == '':
                    break
                # Stop at new structural elements
                if (curr.startswith('#') or curr.startswith('!!!') or
                    curr.startswith('- ') or curr.startswith('| ') or
                    curr.startswith('```')):
                    break
                # Otherwise it's a wrapped continuation line - skip it
                i += 1
            continue

        # Remove "Section X: " prefixes: "## Section 1: Title" -> "## Title"
        match = re.match(r'^(#{1,4})\s+Section\s+\d+:\s+(.+)$', line)
        if match:
            new_line = f"{match.group(1)} {match.group(2)}"
            new_lines.append(new_line)
            changed = True
            i += 1
            continue

        # Remove numbered prefixes: "### 1.2 Title" -> "### Title"
        match = re.match(r'^(#{1,4})\s+\d+\.\d+\s+(.+)$', line)
        if match:
            if 'Do You Need' in match.group(2):
                changed = True
                i += 1
                continue
            new_line = f"{match.group(1)} {match.group(2)}"
            new_lines.append(new_line)
            changed = True
            i += 1
            continue

        # Remove "Do you need...?" question lines and their Yes/No answers
        if re.match(r'^Do you need\s+.+\?$', line, re.IGNORECASE):
            changed = True
            i += 1
            # Skip following blank lines and Yes/No responses
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line == '' or re.match(r'^-\s*\[\s*\]\s*(Yes|No)', next_line):
                    i += 1
                    continue
                break
            continue

        # Remove standalone Yes/No checkbox pairs at start of sections
        # Pattern: "- [ ] Yes - description" followed by "- [ ] No"
        if re.match(r'^-\s*\[\s*\]\s*Yes\s*-\s*(We need|We have|We handle|We experience|We require|Monitor|Enable|Include)', line):
            changed = True
            i += 1
            # Skip following No line if present
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line == '' or re.match(r'^-\s*\[\s*\]\s*No', next_line) or re.match(r'^-\s*\[\s*\]\s*Unsure', next_line):
                    i += 1
                    continue
                break
            continue

        # Remove "- [ ] No - Skip this section" type lines
        if re.match(r'^-\s*\[\s*\]\s*No\s*-\s*Skip', line, re.IGNORECASE):
            changed = True
            i += 1
            continue

        new_lines.append(line)
        i += 1

    # Collapse multiple consecutive blank lines
    result_lines = []
    prev_blank = False
    for line in new_lines:
        is_blank = line.strip() == ''
        if is_blank and prev_blank:
            changed = True
            continue
        result_lines.append(line)
        prev_blank = is_blank

    if changed:
        with open(filepath, 'w') as f:
            f.write('\n'.join(result_lines))
        return True
    return False


def main():
    docs_dir = 'docs'
    for root, dirs, files in os.walk(docs_dir):
        for f in files:
            if f.endswith('.md'):
                path = os.path.join(root, f)
                if fix_file(path):
                    print(f'Fixed: {path}')


if __name__ == '__main__':
    main()
