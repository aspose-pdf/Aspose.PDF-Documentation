---
title: Merge PDF programmatically
linktitle: Merge PDF files
type: docs
weight: 50
url: /php-java/merge-pdf-documents/
description: This page explain how to merge PDF documents into a single PDF file using PHP.
lastmod: "2024-06-05"
---

Now, merging pdf files is one of the most demanded tasks.
This article shows how to merge multiple PDF files into a single PDF document using Aspose.PDF for PHP via Java. The example is written in Java, but the API can be used in other programming languages. PDF files are merged such that the first one is joined at the end of the other document.

## Merge PDF Files using PHP

{{% alert color="primary" %}}

You can merge PDF files using Aspose.PDF and get the results online at this link: [Merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

To concatenate two PDF files:

1. Create two [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) objects, each containing one of the input PDF files.
1. Then call the [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) collection's Add method for the Document object you want to add the other PDF file to.
1. Pass the PageCollection collection of the second Document object to the first PageCollection collection's Add method.
1. Finally, save the output PDF file using the Save method.

The following code snippet shows how to concatenate PDF files using PHP.

```php
    // Open first document
    $document1 = new Document($inputFile1);
    
    // Open second document
    $document2 = new Document($inputFile2);

    // Add pages of second document to the first
    $document1->getPages()->add($document2->getPages());

    // Save concatenated output file
    $document1->save($outputFile);
    $document1->close();
    $document2->close();
```
