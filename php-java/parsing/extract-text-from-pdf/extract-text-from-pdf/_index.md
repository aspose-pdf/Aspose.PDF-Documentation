---
title: Extracting raw text from PDF file 
linktitle: Extract text from PDF
type: docs
weight: 10
url: /php-java/extract-text-from-all-pdf/
description: This article describes various ways to extract text from PDF documents using Aspose.PDF for PHP. From entire pages, from a specific part, based on columns, etc.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract Text From All the Pages of a PDF Document

Extracting text from a PDF document is a common requirement. In this example, you'll see how Aspose.PDF for PHP allows extracting text from all the pages of a PDF document.
To extract text from all the PDF pages:

1. Create an object of the [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) class.
1. Open the PDF using [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class and call the [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) method of the [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) collection.
1. The [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) class absorbs the text from the document and returns in [getText() method](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/#getText--).

The following code snippet shows you how to extract text from all pages of PDF document.

```php

    // Create a new Document object from the input PDF file.
    $document = new Document($inputFile);

    // Create a new TextAbsorber object to extract text from the document.
    $textAbsorber = new TextAbsorber();

    // Extract text from the document.
    $textAbsorber->visit($document);

    // Get the extracted text content.
    $content = $textAbsorber->getText();

    // Save the extracted text to the output file.
    file_put_contents($outputFile, $content);
```
