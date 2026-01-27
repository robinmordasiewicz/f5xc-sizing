#!/usr/bin/env python3
"""Add language specifier to fenced code blocks."""

import os
import re

for root, dirs, files in os.walk('docs'):
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            with open(path, 'r') as file:
                content = file.read()

            # Replace standalone ``` at start of line with ```text
            # But only opening code fences (not closing ones)
            lines = content.split('\n')
            new_lines = []
            in_code_block = False
            changed = False

            for line in lines:
                stripped = line.strip()
                if stripped == '```' and not in_code_block:
                    # Opening fence without language
                    new_lines.append('```text')
                    in_code_block = True
                    changed = True
                elif stripped == '```' and in_code_block:
                    # Closing fence
                    new_lines.append(line)
                    in_code_block = False
                elif stripped.startswith('```') and len(stripped) > 3 and not in_code_block:
                    # Opening fence with language already
                    new_lines.append(line)
                    in_code_block = True
                else:
                    new_lines.append(line)

            if changed:
                with open(path, 'w') as file:
                    file.write('\n'.join(new_lines))
                print(f'Fixed: {path}')

print('Done')
