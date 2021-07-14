---
title: Add background to PDF with Java
linktitle: Add backgrounds
type: docs
weight: 110
url: /java/add-backgrounds/
descriptions: Add background image to the your PDF file with Java. Use the BackgroundArtifact object.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for Java, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://apireference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) class can be used to add a background image to a page object.

The following code snippet shows how to add a background image to PDF pages using the BackgroundArtifact object with Java.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.BackgroundArtifact;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;

public class ExampleAddBackground {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() throws FileNotFoundException {
        // For complete examples and data files, please go to
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        String myDir = "";
        // Create a new Document object
        Document doc = new Document();
        // Add a new page to document object
        Page page = doc.getPages().add();
        // Create BackgroundArtifact object
        BackgroundArtifact background = new BackgroundArtifact();
        // Specify the image for backgroundartifact object
        background.setBackgroundImage(new FileInputStream(myDir + "logo.png"));
        // Add backgroundartifact to artifacts collection of page
        page.getArtifacts().add(background);
        // Save the document
        doc.save(_dataDir + "BackGround.pdf");
    }
}
```
