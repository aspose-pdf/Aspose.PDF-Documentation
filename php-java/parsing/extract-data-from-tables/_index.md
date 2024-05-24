---
title: Extract Table Data from PDF 
linktitle: Extract Table Data
type: docs
weight: 40
url: /php-java/extract-data-from-table-in-pdf/
description: Learn how to extract tabular from PDF using Aspose.PDF for PHP
lastmod: "2021-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract Tables from PDF programmatically

Extracting tables from PDFs is not a trivial task because the table can be created variously.

Aspose.PDF for Java has a tool to make it easy to retrieve tables. To extract table data, you should perform the following steps:

1. Open the PDF document - instantiate a [Document](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/Document) object;
1. Create a TableAbsorber [TableAbsorber](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/tableabsorber) object to extract tables from the document.
1. Iterate through each page of the document.
1. Decide which pages to be analyzed and apply [visit](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) to the desired pages. The tabular data will be scanned, and the result will be saved in a list of [AbsorbedTable](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedTable). We can get this list through [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--) method.
1. To get the data iterate throught `TableList` and handle list of [absorbed rows](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow) and list of absorbed cells. We can access to the first list by calling [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--) method and to the second by calling [getCellList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow#getCellList--).
1. Each [AbsorbedCell](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedCell) contains [TextFragmentCollections](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TextFragmentCollection). You can process it for your own purposes.

The following example shows table extraction from the all pages:

```php
$document = new Document($inputFile);
$tableAbsorber = new TableAbsorber();


for ($pageIndex = 1; $pageIndex <= java_values($pages->size()); $pageIndex++) {
    $page = $pages->get_Item($pageIndex);
    $tableAbsorber->visit($page);
    $tableList = $tableAbsorber->getTableList();
    $tableIterator = $tableList->iterator();

    while (java_values($tableIterator->hasNext())) {
        $table = $tableIterator->next();
        $tableRowList = $table->getRowList();
        $tableRowListIterator = $tableRowList->iterator();

        while (java_values($tableRowListIterator->hasNext())) {
            $row = $tableRowListIterator->next();
            $cellList = $row->getCellList();
            $cellListIterator = $cellList->iterator();

            // Iterate through each cell in the row.
            while (java_values($cellListIterator->hasNext())) {
                $cell = $cellListIterator->next();
                $fragmentList = $cell->getTextFragments();

                // Iterate through each text fragment in the cell.
                for ($fragmentIndex = 1; $fragmentIndex <= java_values($fragmentList->size()); $fragmentIndex++) {
                    $fragment = $fragmentList->get_Item($fragmentIndex);
                    $segments = $fragment->getSegments();

                    // Iterate through each segment in the text fragment.
                    for ($segmentIndex = 1; $segmentIndex <= java_values($segments->size()); $segmentIndex++) {
                        $segment = $segments->get_Item($segmentIndex);
                        $responseData .= $segment->getText();
                    }
                }
                $responseData .= "|";
            }
            $responseData .= PHP_EOL;
        }
    }
}

// Save the table data to the output file.
file_put_contents($outputFile, $responseData);

// Close the PDF document.
$document->close();
```

## Extract Table Data from PDF and store it in CSV file

The following example shows how to extract table and store it as CSV file.
To see how to convert PDF to Excel Spreadsheet please refer to [Convert PDF to Excel](/pdf/php-java/convert-pdf-to-excel/) article.

```php
// Load the input PDF document using the Document class.
$document = new Document($inputFile);

// Create an instance of the ExcelSaveOptions class to specify the save options.
$saveOption = new ExcelSaveOptions();

// Set the output format to CSV.
$saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$CSV);

// Save the PDF document as an Excel file using the specified save options.
$document->save($outputFile, $saveOption);
```
