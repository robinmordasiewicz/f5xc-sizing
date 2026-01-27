#!/usr/bin/env python3
"""Fix markdown table formatting to compact style (single space around pipes)."""

import re
import sys
from pathlib import Path


def fix_table_line(line: str) -> str:
    """Fix a single table line to have consistent compact spacing."""
    if not line.strip().startswith('|') and not line.strip().endswith('|'):
        return line

    # Split by pipe, preserving structure
    parts = line.split('|')

    # Process each cell - trim whitespace and add single space
    fixed_parts = []
    for i, part in enumerate(parts):
        if i == 0 and part.strip() == '':
            # Leading empty part before first pipe
            fixed_parts.append('')
        elif i == len(parts) - 1 and part.strip() == '':
            # Trailing empty part after last pipe
            fixed_parts.append('')
        else:
            # Content cell - single space on each side
            content = part.strip()
            if content:
                fixed_parts.append(f' {content} ')
            else:
                fixed_parts.append('  ')  # Empty cell gets two spaces

    return '|'.join(fixed_parts)


def is_separator_line(line: str) -> bool:
    """Check if line is a table separator (e.g., |---|---|)."""
    stripped = line.strip()
    if not stripped.startswith('|'):
        return False
    # Remove pipes and check if only dashes, colons, and spaces remain
    content = stripped.replace('|', '').replace('-', '').replace(':', '').replace(' ', '')
    return content == ''


def fix_separator_line(line: str, header_line: str) -> str:
    """Fix separator line to match header column count."""
    if not is_separator_line(line):
        return line

    # Count columns from header
    header_parts = [p for p in header_line.split('|') if p.strip() or header_line.split('|').index(p) in [0, len(header_line.split('|'))-1]]

    # Parse separator to preserve alignment markers
    sep_parts = line.split('|')
    fixed_parts = []

    for i, part in enumerate(sep_parts):
        stripped = part.strip()
        if i == 0 and stripped == '':
            fixed_parts.append('')
        elif i == len(sep_parts) - 1 and stripped == '':
            fixed_parts.append('')
        elif stripped:
            # Preserve alignment markers (:--- :---: ---:)
            if stripped.startswith(':') and stripped.endswith(':'):
                fixed_parts.append(' :---: ')
            elif stripped.startswith(':'):
                fixed_parts.append(' :--- ')
            elif stripped.endswith(':'):
                fixed_parts.append(' ---: ')
            else:
                fixed_parts.append(' --- ')
        else:
            fixed_parts.append(' --- ')

    return '|'.join(fixed_parts)


def fix_markdown_file(filepath: Path) -> bool:
    """Fix tables in a markdown file. Returns True if changes were made."""
    content = filepath.read_text()
    lines = content.split('\n')
    fixed_lines = []
    in_table = False
    table_start = -1
    changes_made = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Detect table start
        if stripped.startswith('|') and not in_table:
            in_table = True
            table_start = i

        if in_table:
            if stripped.startswith('|'):
                # Fix the line
                if is_separator_line(line) and table_start < i:
                    fixed_line = fix_separator_line(line, lines[table_start])
                else:
                    fixed_line = fix_table_line(line)

                if fixed_line != line:
                    changes_made = True
                fixed_lines.append(fixed_line)
            else:
                # End of table
                in_table = False
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)

        i += 1

    if changes_made:
        filepath.write_text('\n'.join(fixed_lines))

    return changes_made


def main():
    docs_dir = Path('docs')
    if not docs_dir.exists():
        print("Error: docs/ directory not found")
        sys.exit(1)

    total_fixed = 0
    for md_file in docs_dir.rglob('*.md'):
        if fix_markdown_file(md_file):
            print(f"Fixed: {md_file}")
            total_fixed += 1

    print(f"\nTotal files fixed: {total_fixed}")


if __name__ == '__main__':
    main()
