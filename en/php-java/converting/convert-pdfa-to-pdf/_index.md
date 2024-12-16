---
title: Convert PDF/A to PDF format 
linktitle: Convert PDF/A to PDF format
type: docs
weight: 110
url: /php-java/convert-pdfa-to-pdf/
lastmod: "2024-05-20"
description: This topic show you how to Aspose.PDF allows to convert PDF/A file to PDF document with PHP library. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convert PDF/A document to PDF

Convert PDF/A document to PDF means removing <abbr title="Portable Document Format Archive">PDF/A</abbr> restriction from the original document. Class [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) has method removePdfaCompliance(..) to remove
the PDF compliance information from input/source file.

```php
// Create a new instance of the Document class with the input file
$document = new Document($inputFile);

// Remove the PDF/A compliance from the document
$document->removePdfaCompliance();

// Save the modified document to the output file
$document->save($outputFile);
```

This info also removes if you make any changes in the document (e.g. add pages). In the following example, the output document loses PDF/A compliance after the page adding.

```php
// Create a new instance of the Document class with the input file
$document = new Document($inputFile);

// Remove the PDF/A compliance from the document
$document->getPages()->add();

// Save the modified document to the output file
$document->save($outputFile);
```
