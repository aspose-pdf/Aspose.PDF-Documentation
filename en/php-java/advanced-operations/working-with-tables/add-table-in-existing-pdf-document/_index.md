---
title: Create or Add Table In PDF 
linktitle: Create or Add Table
type: docs
weight: 10
url: /php-java/add-table-in-existing-pdf-document/
description: Learn how to create or add table to a PDF document, applying cell style, splitting table on pages and customize the rows and columns etc.
lastmod: "2024-05-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adding Table in Existing PDF Document

To add a table to an existing PDF file with Aspose.PDF for PHP, take the following steps:

1. Load the source file.
1. Initialize a table
1. Set the table border color as LightGray
1. Set the border for table cells
1. Create a loop to add 10 rows
1. Add table object to first page of input document
1. Save the file.

The following code snippets show how to add text in an existing PDF file.

```php

    // Open document
    $document = new Document($inputFile);        
    // Initializes a new instance of the Table
    $table = new Table();
    $colors= new Color();
    // Set the table border color as LightGray
    $borderSide = new BorderSide();
    $borderInfo = new BorderInfo($borderSide->All, 0.5, $colors->getLightGray());
    $table->setBorder($borderInfo);
    // set the border for table cells
    $table->setDefaultCellBorder($borderInfo);
    // create a loop to add 10 rows
    for ($row_count = 1; $row_count < 10; $row_count++) {
        // add row to table
        $row = $table->getRows()->add();
        // add table cells
        $row->getCells()->add("Column (" . $row_count . ", 1)");
        $row->getCells()->add("Column (" . $row_count . ", 2)");
        $row->getCells()->add("Column (" . $row_count . ", 3)");
    }
    // Add table object to first page of input document
    $document->getPages()->add()->getParagraphs()->add($table);

    // Save resulting PDF document.    
    $document->save($outputFile);
    $document->close();
```

