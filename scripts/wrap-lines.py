#!/usr/bin/env python3
"""Wrap long lines in markdown files while preserving structure."""

import os
import re
import textwrap

MAX_LINE_LENGTH = 80


def should_preserve_line(line: str, in_code_block: bool, in_table: bool) -> bool:
    """Check if a line should be preserved as-is."""
    stripped = line.strip()

    # Always preserve empty lines
    if not stripped:
        return True

    # Preserve code blocks
    if in_code_block:
        return True

    # Preserve table lines
    if stripped.startswith('|') or in_table:
        return True

    # Preserve headings
    if stripped.startswith('#'):
        return True

    # Preserve list items with checkboxes (they are forms)
    if re.match(r'^-\s*\[', stripped):
        return True

    # Preserve lines that start with ! (admonitions, images)
    if stripped.startswith('!'):
        return True

    # Preserve horizontal rules
    if stripped in ['---', '***', '___']:
        return True

    # Preserve link-only lines
    if re.match(r'^\[.*\]\(.*\)(\{.*\})?$', stripped):
        return True

    return False


def wrap_paragraph(text: str) -> str:
    """Wrap a paragraph while preserving markdown links."""
    if len(text) <= MAX_LINE_LENGTH:
        return text

    # Use textwrap but preserve long URLs
    wrapper = textwrap.TextWrapper(
        width=MAX_LINE_LENGTH,
        break_long_words=False,
        break_on_hyphens=False
    )

    wrapped = wrapper.fill(text)
    return wrapped


def process_file(filepath: str) -> bool:
    """Process a markdown file to wrap long lines."""
    with open(filepath, 'r') as f:
        content = f.read()

    lines = content.split('\n')
    result_lines = []
    in_code_block = False
    changed = False
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Track code blocks
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result_lines.append(line)
            i += 1
            continue

        # Check if we're in a table
        in_table = stripped.startswith('|')

        # Preserve lines that shouldn't be wrapped
        if should_preserve_line(line, in_code_block, in_table):
            result_lines.append(line)
            i += 1
            continue

        # Check if line is too long and is a paragraph
        if len(line) > MAX_LINE_LENGTH:
            # Wrap the line
            wrapped = wrap_paragraph(line)
            if wrapped != line:
                changed = True
            result_lines.append(wrapped)
        else:
            result_lines.append(line)

        i += 1

    if changed:
        with open(filepath, 'w') as f:
            f.write('\n'.join(result_lines))
        return True

    return False


def main():
    docs_dir = 'docs'
    fixed_count = 0

    for root, dirs, files in os.walk(docs_dir):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                if process_file(filepath):
                    print(f'Wrapped: {filepath}')
                    fixed_count += 1

    print(f'\nTotal files fixed: {fixed_count}')


if __name__ == '__main__':
    main()
