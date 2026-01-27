#!/bin/sh
# Startup script for mkdocs with PDF generation

set -e

echo "Generating PDF documentation..."
ENABLE_PDF_EXPORT=1 mkdocs build --site-dir /tmp/pdf-build

# Ensure pdf directory exists and copy the generated PDF
mkdir -p /docs/docs/pdf
cp /tmp/pdf-build/pdf/document.pdf /docs/docs/pdf/document.pdf
echo "PDF generated: docs/pdf/document.pdf"

# Clean up build directory
rm -rf /tmp/pdf-build

echo "Starting mkdocs serve..."
exec mkdocs serve --dev-addr 0.0.0.0:8000
