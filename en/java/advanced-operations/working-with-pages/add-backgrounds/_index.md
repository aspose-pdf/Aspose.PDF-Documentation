---
title: Add background to PDF 
linktitle: Add backgrounds
type: docs
weight: 110
url: /java/add-backgrounds/
description: Learn how to add backgrounds to PDF documents using Aspose.PDF for Java. Follow this step-by-step guide for creative customization.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add background images in PDF documents using the Aspose.PDF library for Java
Abstract: The article discusses the use of background images in PDF documents using the Aspose.PDF library for Java. It highlights how background images can serve as watermarks or subtle design elements in documents. In Aspose.PDF, a PDF document comprises a collection of pages, each containing artifacts. The article introduces the `BackgroundArtifact` class, which facilitates the addition of background images to individual page objects within a PDF. A Java code snippet is provided, demonstrating the process of adding a background image to a PDF page. The example includes creating a new `Document` object, adding a page, creating a `BackgroundArtifact` object, setting an image as the background, and saving the document. The code is part of a sample project and includes references for further examples and data files.
SoftwareApplication: java
---

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for Java, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) class can be used to add a background image to a page object.

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
