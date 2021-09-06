---
title: Working with Artifacts with Java
linktitle: Working with Artifacts
type: docs
weight: 110
url: /androidjava/artifacts/
description: This page describes how to work with Artifact class using Aspose.PDF for Java. Code snippets show how to add a background image to PDF pages and how to get each watermark on the first page of a PDF file.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Artifacts are generally graphics objects or other markings that are not part of the authored content. In your PDF examples of artifacts include different information, there are page header or footer, lines or other graphics separating sections of the page, or decorative images.

The [Artifact](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Artifact) class contains:

- [Artifact.Type](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactType) – gets the artifact type (supports values of the Artifact.ArtifactType enumeration where values include Background, Layout, Page, Pagination and Undefined).
- [Artifact.Subtype](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactSubtype) – gets artifact subtype (supports the values of the Artifact.ArtifactSubtype enumeration where values include Background, Footer, Header, Undefined, Watermark).

A watermark created with Adobe Acrobat is called an artifact (as described in 14.8.2.2 Real Content and Artifacts of the PDF specification). In order to work with artifacts, Aspose.PDF has two classes: [Artifact](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Artifact) and [ArtifactCollection](https://apireference.aspose.com/pdf/java/com.aspose.pdf/ArtifactCollection).

In order to get all artifacts on a particular page, the [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) class has the Artifacts property. This topic explains how to work with artifact in PDF files.

The following code snippet shows how to set watermark on the first page of a PDF file.

```java

 public class ExamplesArtifacts {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Artifacts/";

    public static void SetWatermark(){
        Document doc = new Document(_dataDir + "sample.pdf");
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(new FormattedText("WATERMARK", java.awt.Color.BLUE, 
                            FontStyle.Courier,
                            EncodingType.Identity_h, true, 72));
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }
```

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for Java, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://apireference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) class can be used to add a background image to a page object.

The following code snippet shows how to add a background image to PDF pages using the BackgroundArtifact object.

```java

    public static void SetBackground() throws FileNotFoundException {

        // Open document
        Document pdfDocument = new Document();
                
        // Add a new page to document object
        Page page = pdfDocument.getPages().add();

        // Create Background Artifact object
        BackgroundArtifact background = new BackgroundArtifact();

        // Specify the image for backgroundartifact object
        background.setBackgroundImage(new java.io.FileInputStream(new java.io.File(_dataDir + "background.png")));
        
        // Add BackgroundArtifact to artifacts collection of page
        page.getArtifacts().add(background);

        // Save modified PDF
        pdfDocument.save(_dataDir + "ImageAsBackground_out.pdf");

    }
```

## Programming Samples: Getting Watermark

The following code snippet shows how to get each watermark on the first page of a PDF file.

```java
    public static void GettingWatermarks() {
        // Open document
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        // Iterate through and get sub-type, text and location of artifact
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            System.out.println(artifact.getSubtype() + " " + artifact.getText() + " " + artifact.getRectangle().toString());
        }
```

## Programming Samples: Counting Artifacts of a Particular Type

To calculate the total count of artifacts of a particular type (for example, the total number of watermarks), use the following code:

```java
    public static void CountingArtifacts() {
        // Open document
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        int count = 0;
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            // If artifact type is watermark, increate the counter
            if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) count++;
        }
        System.out.println("Page contains " + count + " watermarks");
    }
```
