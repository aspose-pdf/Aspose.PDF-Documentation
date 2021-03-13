---
title: Add watermark to PDF using C#
linktitle: Add watermark
type: docs
weight: 90
url: /net/add-watermarks/
description: This article explains the features of working with artifacts and getting watermarks in PDFs using  programmatically the C#.
lastmod: "2020-12-22"
aliases:
    - /net/working-with-existing-watermarks/
    - /net/adding-multi-line-watermark-to-existing-pdf/
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for .NET** allows adding watermarks to your PDF document using Artifacts. Please check this article to resolve your task.

A watermark created with Adobe Acrobat is called an artifact (as described in 14.8.2.2 Real Content and Artifacts of the PDF specification). In order to work with artifacts, Aspose.PDF has two classes: [Artifact](https://apireference.aspose.com/pdf/net/aspose.pdf/artifact) and [ArtifactCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

In order to get all artifacts on a particular page, the [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) class has the Artifacts property. This topic explains how to work with artifact in PDF files.

## Working with Artifacts

The [Artifact](https://apireference.aspose.com/pdf/net/aspose.pdf/artifact) class contains following properties:

**Artifact.Type** – gets the artifact type (supports values of the Artifact.ArtifactType enumeration where values include Background, Layout, Page, Pagination and Undefined).
**Artifact.Subtype** – gets artifact subtype (supports the values of the Artifact.ArtifactSubtype enumeration where values include Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Please note that watermarks created with Adobe Acrobat have the type Pagination and subtype Watermark.

{{% /alert %}}

**Artifact.Contents** – Gets a collection of artifact internal operators. Its supported type is System.Collections.ICollection.
**Artifact.Form** – Gets an artifact’s XForm (if XForm is used). Watermarks, header, and footer artifacts contains XForm which shows all artifact contents.
**Artifact.Image** – Gets an artifact’s image (if an image is presents, else null).
**Artifact.Text** – Gets an artifact’s text.
**Artifact.Rectangle** – Gets an position of an artifact on the page.
**Artifact.Rotation** – Gets an artifact’s rotation (in degrees, positive value indicates counter-clockwise rotation).
**Artifact.Opacity** – Gets an artifact’s opacity. Possible values are in the range 0…1, where 1 is completely opaque.

## Programming Samples: Getting Watermarks

The following code snippet shows how to get each watermark on the first page of a PDF file with C#.

```csharp 
   Document doc = new Document(_inDataDir + "text.pdf");
            WatermarkArtifact artifact = new WatermarkArtifact();
            artifact.SetText(new FormattedText("WATERMARK", System.Drawing.Color.Blue, FontStyle.Courier,
   EncodingType.Identity_h, true, 72));
            artifact.ArtifactHorizontalAlignment = HorizontalAlignment.Center;
            artifact.ArtifactVerticalAlignment =VerticalAlignment.Center;
            artifact.Rotation = 45;
            artifact.Opacity = 0.5;
            artifact.IsBackground = true;
            doc.Pages[1].Artifacts.Add(artifact);
            doc.Save(_outDataDir + "watermark.pdf");
```
