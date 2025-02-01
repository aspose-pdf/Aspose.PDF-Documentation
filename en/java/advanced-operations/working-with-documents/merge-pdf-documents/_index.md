---
title: Merge PDF programmatically
linktitle: Merge PDF files
type: docs
weight: 50
url: /java/merge-pdf-documents/
description: This page explain how to merge PDF documents into a single PDF file with Java.
lastmod: "2021-06-05"
TechArticle: true 
AlternativeHeadline: 
Abstract: The article provides a guide on merging multiple PDF files into a single document using Aspose.PDF for Java. It highlights the demand for PDF merging and offers a step-by-step method to accomplish this task programmatically. The process involves creating `Document` objects for each PDF, utilizing the `PageCollection`'s `Add` method to combine them, and saving the final merged document. The article includes a Java code snippet demonstrating the merging process, where pages from one document are appended to another. Additionally, it mentions that Aspose.PDF can be used in other programming languages and provides an online tool for merging PDFs.
---

Now, merging pdf files is one of the most demanded tasks. 
This article shows how to merge multiple PDF files into a single PDF document using Aspose.PDF for Java. The example is written in Java, but the API can be used in other programming languages. PDF files are merged such that the first one is joined at the end of the other document.

## Merge PDF Files using Java

{{% alert color="primary" %}}

You can merge PDF files using Aspose.PDF and get the results online at this link: [products.aspose.app/pdf/merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

To concatenate two PDF files:

1. Create two [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) objects, each containing one of the input PDF files.
1. Then call the [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) collection's Add method for the Document object you want to add the other PDF file to.
1. Pass the PageCollection collection of the second Document object to the first PageCollection collection's Add method.
1. Finally, save the output PDF file using the Save method.

The following code snippet shows how to concatenate PDF files with Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMerge {
    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Merge() {
        
        // Open first document
        Document pdfDocument1 = new Document(_dataDir + "Concat1.pdf");
        // Open second document
        Document pdfDocument2 = new Document(_dataDir + "Concat2.pdf");

        // Add pages of second document to the first
        pdfDocument1.getPages().add(pdfDocument2.getPages());

        // Save concatenated output file
        pdfDocument1.save(_dataDir+"ConcatenatePdfFiles_out.pdf");

    }

}
```


