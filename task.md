# Task List

## Overview
Build a Django web application to manage item data. The application should allow users to upload CSV files containing item information, store the data in a MySQL database, and provide functionalities to search, filter, and export the data in various formats.

## Data Model
- [x] Create a Django model to represent the item data from the CSV file.
  - [x] Item Name (TextField)
  - [x] Item Description (TextField)
  - [x] Item Code (TextField)
  - [x] Item Qty (IntegerField)
  - [x] Item Price (DecimalField)
  - [x] Vendor Name (TextField)

## CSV Upload Page
- [x] Create a Django form to handle CSV file uploads.
  - [x] Include a file upload field to select and upload a CSV file.
  - [x] Optional: Support Drag and Drop.
- [x] Implement a view to handle the form submission.
- [ x] Parse the uploaded CSV file to extract item data.
- [x] Validate the extracted data to ensure it matches the model fields.
- [ x] Create model instances for each item and save them to the database.
- [ x] Provide feedback to the user on the upload process.
  - [x ] Success or error messages.
  - [x ] Statistics of how many records were read, written to the database, and failed (due to error).

## Data Search and Filtering Page
- [ ] Create a Django view to display a search form with filter options.
  - [ ] Include search fields for Item Name, Item Code, and Vendor Name.
- [ ] Implement search and filter logic to query the database based on user input.
- [ ] Display search results in a tabular format.
  - [ ] Include pagination for large datasets.

## Data Export Page
- [ ] Create a Django view to handle data export requests.
  - [ ] Allow users to select the desired export format (PDF or Excel).
- [ ] Implement export logic to generate the selected file format based on search and filter criteria.
  - [ ] Use a suitable library for PDF generation.
  - [ ] Use a suitable library for Excel generation.
- [ ] Provide download links for the generated files.

## Additional Considerations
- [ ] Error Handling: Implement proper error handling for file uploads, data validation, and database operations.
- [ ] Data Validation: Ensure data integrity by validating CSV data before importing.
- [ ] User Interface: Design user-friendly interfaces for all pages.
- [ ] Testing: Perform unit tests to ensure code quality.
