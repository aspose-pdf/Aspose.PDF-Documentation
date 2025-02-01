---
title: Add watermark to PDF 
linktitle: Add watermark
type: docs
weight: 90
url: /java/add-watermarks/
description: This article explains the features of working with artifacts and getting watermarks in PDFs using  programmatically the Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: 
Abstract: The article discusses how to add watermarks to PDF documents using the Aspose.PDF for Java library, focusing on the concept of artifacts as defined in the PDF specification. It introduces two key classes for handling artifacts: `Artifact` and `ArtifactCollection`. The `Page` class has an `Artifacts` property, which is used to access all artifacts on a specific page. The article details various properties of the `Artifact` class, such as `Type`, `Subtype`, `Contents`, `Form`, `Image`, `Text`, `Rectangle`, `Rotation`, and `Opacity`, each providing different functionalities and characteristics of an artifact. The article highlights that watermarks created with Adobe Acrobat are classified as artifacts with the type `Pagination` and subtype `Watermark`. Additionally, a code example is provided, illustrating how to retrieve and manipulate watermarks on the first page of a PDF using Java. The sample code demonstrates opening a PDF document, creating a watermark artifact with specified text, alignment, rotation,
---

**Aspose.PDF for Java** allows adding watermarks to your PDF document using Artifacts. Please check this article to resolve your task.

A watermark created with Adobe Acrobat is called an artifact (as described in 14.8.2.2 Real Content and Artifacts of the PDF specification). In order to work with artifacts, Aspose.PDF has two classes: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) and [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection).

In order to get all artifacts on a particular page, the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) class has the Artifacts property. This topic explains how to work with artifact in PDF files.

## Working with Artifacts

The [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) class contains following properties:

**Artifact.Type** – gets the artifact type (supports values of the Artifact.ArtifactType enumeration where values include Background, Layout, Page, Pagination and Undefined).
**Artifact.Subtype** – gets artifact subtype (supports the values of the Artifact.ArtifactSubtype enumeration where values include Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Please note that watermarks created with Adobe Acrobat have the type Pagination and subtype Watermark.

{{% /alert %}}

**Artifact.Contents** – Gets a collection of artifact internal operators. Its supported type is System.Collections.ICollection.
**Artifact.Form** – Gets an artifact's XForm (if XForm is used). Watermarks, header, and footer artifacts contains XForm which shows all artifact contents.
**Artifact.Image** – Gets an artifact's image (if an image is presents, else null).
**Artifact.Text** – Gets an artifact's text.
**Artifact.Rectangle** – Gets an position of an artifact on the page.
**Artifact.Rotation** – Gets an artifact's rotation (in degrees, positive value indicates counter-clockwise rotation).
**Artifact.Opacity** – Gets an artifact's opacity. Possible values are in the range 0…1, where 1 is completely opaque.

## Programming Samples: Getting Watermarks

The following code snippet shows how to get each watermark on the first page of a PDF file with Java.

```java
 package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.EncodingType;
import com.aspose.pdf.facades.FontStyle;
import com.aspose.pdf.facades.FormattedText;

public class ExampleWatermark {
    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {

        // Open document
        Document doc = new Document(_dataDir + "text.pdf");      
        FormattedText formattedText = new FormattedText("Watermark", java.awt.Color.BLUE,FontStyle.Courier, EncodingType.Identity_h, true, 72.0F);
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(formattedText);        
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }

}  
```
