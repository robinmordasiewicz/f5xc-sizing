/**
 * Form Styling Script
 *
 * Transforms plain text form patterns in table cells into interactive HTML form elements:
 * - [ ] becomes interactive checkbox
 * - ( ) becomes interactive radio button (grouped by row)
 * - ___ becomes text input field
 *
 * This provides a modern, interactive form experience in the HTML documentation
 * while the PDF version gets its own form widgets via add_pdf_forms.py
 */

document.addEventListener('DOMContentLoaded', function() {
  let checkboxCount = 0;
  let textFieldCount = 0;

  // Process all table cells
  document.querySelectorAll('.md-typeset td').forEach(function(td) {
    let html = td.innerHTML;
    let modified = false;

    // Get row index for radio button grouping
    const row = td.closest('tr');
    const rowIndex = row ? row.rowIndex : 0;

    // Transform [ ] into actual checkboxes
    // Match [ ] followed by text (the label)
    const checkboxPattern = /\[\s*\]\s*([^[\]()_\n<]+?)(?=\s*(?:\[\s*\]|\(\s*\)|___|\s*$|<))/g;
    html = html.replace(checkboxPattern, function(match, label) {
      modified = true;
      const trimmedLabel = label.trim();
      const name = 'cb_' + checkboxCount++;
      return '<label class="form-checkbox-label">' +
        '<input type="checkbox" class="form-checkbox" name="' + name + '">' +
        '<span class="form-checkbox-mark"></span>' +
        '<span class="form-checkbox-text">' + trimmedLabel + '</span>' +
        '</label>';
    });

    // Handle standalone [ ] without label
    html = html.replace(/\[\s*\](?!\s*[a-zA-Z0-9])/g, function() {
      modified = true;
      const name = 'cb_' + checkboxCount++;
      return '<label class="form-checkbox-label">' +
        '<input type="checkbox" class="form-checkbox" name="' + name + '">' +
        '<span class="form-checkbox-mark"></span>' +
        '</label>';
    });

    // Transform ( ) into actual radio buttons
    // Radio buttons in the same row share the same group name
    const radioPattern = /\(\s*\)\s*([^[\]()_\n<]+?)(?=\s*(?:\[\s*\]|\(\s*\)|___|\s*$|<))/g;
    let radioCount = 0;
    const groupName = 'rg_row_' + rowIndex;

    html = html.replace(radioPattern, function(match, label) {
      modified = true;
      const trimmedLabel = label.trim();
      const radioId = groupName + '_opt_' + radioCount++;
      return '<label class="form-radio-label">' +
        '<input type="radio" class="form-radio" name="' + groupName + '" id="' + radioId + '">' +
        '<span class="form-radio-mark"></span>' +
        '<span class="form-radio-text">' + trimmedLabel + '</span>' +
        '</label>';
    });

    // Handle standalone ( ) without label
    html = html.replace(/\(\s*\)(?!\s*[a-zA-Z0-9])/g, function() {
      modified = true;
      const radioId = groupName + '_opt_' + radioCount++;
      return '<label class="form-radio-label">' +
        '<input type="radio" class="form-radio" name="' + groupName + '" id="' + radioId + '">' +
        '<span class="form-radio-mark"></span>' +
        '</label>';
    });

    // Transform ___ (3+ underscores) into text inputs
    html = html.replace(/_{3,}/g, function() {
      modified = true;
      const name = 'tf_' + textFieldCount++;
      return '<input type="text" class="form-text-input" name="' + name + '" placeholder="Enter value">';
    });

    // Only update if we made changes
    if (modified) {
      td.innerHTML = html;
    }
  });

  // Log summary for debugging (can be removed in production)
  if (checkboxCount > 0 || textFieldCount > 0) {
    console.log('Form styling applied: ' + checkboxCount + ' checkboxes, ' + textFieldCount + ' text fields');
  }
});
