---
title: Split PDF programmatically
linktitle: Split PDF files
type: docs
weight: 60
url: /java/split-document/
description: This topic shows how to split PDF pages into individual PDF files in your Java applications. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

You can split PDF files using Aspose.PDF and get the results online at this link: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

This topic shows how to split PDF pages with Aspose.PDF for Java into individual PDF files in your Java applications. To split PDF pages into single page PDF files using Java, the following steps can be followed:

1. Loop through the pages of PDF document through the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object's [PageCollection](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) collection.
1. For each iteration, create a new Document object and add the individual [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) object into the empty document.
1. Save the new PDF using Save method.

The following Java code snippet shows you how to split PDF pages into individual PDF files.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleSplit {
    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {
        
        // Open document
        Document pdfDocument = new Document(_dataDir + "SplitToPages.pdf");

        int pageCount = 1;

        // Loop through all the pages
        for(Page pdfPage : pdfDocument.getPages())
        {
            Document newDocument = new Document();
            newDocument.getPages().add(pdfPage);
            newDocument.save(_dataDir + "page_" + pageCount + "_out" + ".pdf");
            pageCount++;
        }
    }

}
```
