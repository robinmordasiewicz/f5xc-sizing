#!/usr/bin/env python3
"""Test pymupdf-layout to analyze PDF structure and compare with standard PyMuPDF."""

import json
import sys
import fitz

# Check for layout module
HAS_LAYOUT = False
try:
    import pymupdf.layout
    pymupdf.layout.activate()
    HAS_LAYOUT = True
    print("✅ pymupdf-layout activated")
except ImportError as e:
    print(f"⚠️  pymupdf-layout not available: {e}")

# Check for pymupdf4llm
HAS_LLM = False
try:
    import pymupdf4llm
    HAS_LLM = True
    print("✅ pymupdf4llm imported")
except ImportError:
    print("⚠️  pymupdf4llm not available, using standard PyMuPDF methods")

# Open the PDF
pdf_path = "/docs/site/pdf/document.pdf"
doc = fitz.open(pdf_path)
print(f"\n📄 Opened: {pdf_path}")
print(f"   Pages: {len(doc)}")

# Test pages - select pages likely to have tables/forms
test_pages = [4, 5, 8, 10, 15, 20, 30]

for page_num in test_pages:
    if page_num >= len(doc):
        continue

    page = doc[page_num]
    print(f"\n{'='*70}")
    print(f"📄 PAGE {page_num + 1}")
    print('='*70)

    # Get text dict with detailed structure
    text_dict = page.get_text("dict")
    print(f"\n📐 Page dimensions: {text_dict.get('width', 'N/A'):.1f} x {text_dict.get('height', 'N/A'):.1f}")

    blocks = text_dict.get('blocks', [])

    # Count block types (0=text, 1=image)
    block_types = {0: 0, 1: 0}
    for block in blocks:
        btype = block.get('type', 0)
        block_types[btype] = block_types.get(btype, 0) + 1
    print(f"\n📊 Blocks: {len(blocks)} total (text: {block_types.get(0, 0)}, image: {block_types.get(1, 0)})")

    # ============================================================
    # TABLE DETECTION - Compare standard vs layout-enhanced
    # ============================================================
    print(f"\n🗃️  TABLE DETECTION:")

    # Standard PyMuPDF table detection
    tables = page.find_tables()
    print(f"   Standard find_tables(): {len(tables.tables)} tables")

    for i, table in enumerate(tables.tables):
        print(f"\n   Table {i+1}:")
        print(f"      Bbox: ({table.bbox[0]:.1f}, {table.bbox[1]:.1f}, {table.bbox[2]:.1f}, {table.bbox[3]:.1f})")
        print(f"      Size: {table.row_count} rows × {table.col_count} cols")

        # Extract and analyze table content
        try:
            content = table.extract()
            if content:
                # Count cells with form patterns
                empty_cells = 0
                underscore_cells = 0
                checkbox_cells = 0
                radio_cells = 0

                for row in content:
                    for cell in row:
                        cell_text = str(cell) if cell else ''
                        if not cell_text.strip():
                            empty_cells += 1
                        if '___' in cell_text:
                            underscore_cells += 1
                        if '[ ]' in cell_text:
                            checkbox_cells += 1
                        if '( )' in cell_text:
                            radio_cells += 1

                total_cells = table.row_count * table.col_count
                print(f"      Cells: {total_cells} total")
                if empty_cells:
                    print(f"         Empty: {empty_cells}")
                if underscore_cells:
                    print(f"         With '___': {underscore_cells}")
                if checkbox_cells:
                    print(f"         With '[ ]': {checkbox_cells}")
                if radio_cells:
                    print(f"         With '( )': {radio_cells}")

                # Show first few rows
                print(f"      Sample content:")
                for j, row in enumerate(content[:2]):
                    row_preview = [str(c)[:20] if c else '(empty)' for c in row[:4]]
                    print(f"         Row {j}: {row_preview}")

        except Exception as e:
            print(f"      Error extracting: {e}")

    # ============================================================
    # FORM PATTERN SEARCH - with positions
    # ============================================================
    print(f"\n✏️  FORM PATTERN POSITIONS:")

    form_patterns = [
        ('[ ]', 'checkbox'),
        ('( )', 'radio'),
        ('___', 'text input')
    ]

    for pattern, ptype in form_patterns:
        rects = page.search_for(pattern)
        if rects:
            print(f"\n   '{pattern}' ({ptype}): {len(rects)} found")
            # Show positions grouped by Y coordinate (same row)
            by_row = {}
            for r in rects:
                row_key = round(r.y0 / 15) * 15  # Group by ~15px rows
                if row_key not in by_row:
                    by_row[row_key] = []
                by_row[row_key].append(r)

            print(f"      Rows: {len(by_row)} distinct")
            for row_y, row_rects in sorted(by_row.items())[:3]:
                print(f"         Y≈{row_y}: {len(row_rects)} items at X=[{', '.join(f'{r.x0:.0f}' for r in row_rects[:5])}]")

    # ============================================================
    # DETAILED BLOCK STRUCTURE (for layout understanding)
    # ============================================================
    print(f"\n📝 TEXT BLOCK STRUCTURE (first 3 blocks):")

    text_blocks = [b for b in blocks if b.get('type') == 0][:3]
    for i, block in enumerate(text_blocks):
        bbox = block.get('bbox', [0, 0, 0, 0])
        lines = block.get('lines', [])
        print(f"\n   Block {i+1}: bbox=({bbox[0]:.0f},{bbox[1]:.0f},{bbox[2]:.0f},{bbox[3]:.0f}), {len(lines)} lines")

        for j, line in enumerate(lines[:2]):
            spans = line.get('spans', [])
            line_bbox = line.get('bbox', [0, 0, 0, 0])
            line_text = ''.join(s.get('text', '') for s in spans)[:60]
            print(f"      Line {j}: '{line_text}' ({len(spans)} spans)")

# ============================================================
# SUMMARY STATISTICS
# ============================================================
print(f"\n{'='*70}")
print("📊 DOCUMENT-WIDE SUMMARY")
print('='*70)

total_checkboxes = 0
total_radios = 0
total_textfields = 0
total_tables = 0

for page_num in range(len(doc)):
    page = doc[page_num]
    total_checkboxes += len(page.search_for("[ ]"))
    total_radios += len(page.search_for("( )"))
    total_textfields += len(page.search_for("___"))
    total_tables += len(page.find_tables().tables)

print(f"\n   Total '[ ]' checkboxes: {total_checkboxes}")
print(f"   Total '( )' radios: {total_radios}")
print(f"   Total '___' text fields: {total_textfields}")
print(f"   Total tables: {total_tables}")

# ============================================================
# Test pymupdf4llm JSON output if available
# ============================================================
if HAS_LLM:
    print(f"\n{'='*70}")
    print("📋 PYMUPDF4LLM JSON OUTPUT (Page 5)")
    print('='*70)

    json_data = pymupdf4llm.to_json(doc, pages=[4])
    data = json.loads(json_data) if isinstance(json_data, str) else json_data

    if isinstance(data, list) and data:
        page_data = data[0]
        print(f"\n   Top-level keys: {list(page_data.keys())}")

        blocks = page_data.get('blocks', [])
        print(f"   Blocks: {len(blocks)}")

        # Check block types
        btypes = set(b.get('type') for b in blocks)
        print(f"   Block types: {btypes}")

        # Sample block
        if blocks:
            print(f"\n   Sample block keys: {list(blocks[0].keys())}")

doc.close()
print("\n✅ Analysis complete")
