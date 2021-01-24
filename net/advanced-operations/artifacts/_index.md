---
title: Working with Artifacts in .NET
linktitle: Working with Artifacts
type: docs
weight: 110
url: /net/artifacts/
description: This page describes how to work with Artifact class using Aspose.PDF for .NET. Code snippets show how to add a background image to PDF pages and how to get each watermark on the first page of a PDF file. 
lastmod: "2020-12-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The [Artifact](https://apireference.aspose.com/pdf/net/aspose.pdf/artifact) class contains following properties:

- **Artifact.Type** – gets the artifact type (supports values of the Artifact.ArtifactType enumeration where values include Background, Layout, Page, Pagination and Undefined).
- **Artifact.Subtype** – gets artifact subtype (supports the values of the Artifact.ArtifactSubtype enumeration where values include Background, Footer, Header, Undefined, Watermark).
- **Artifact.Image** – Gets an artifact’s image (if an image is presents, else null).
- **Artifact.Text** – Gets an artifact’s text.

A watermark created with Adobe Acrobat is called an artifact (as described in 14.8.2.2 Real Content and Artifacts of the PDF specification). In order to work with artifacts, Aspose.PDF has two classes: [Artifact](https://apireference.aspose.com/pdf/net/aspose.pdf/artifact) and [ArtifactCollection](https://apireference.aspose.com/pdf/net/aspose.pdf/artifactcollection).

In order to get all artifacts on a particular page, the [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) class has the Artifacts property. This topic explains how to work with artifact in PDF files.

The following code snippet shows how to get each watermark on the first page of a PDF file.

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

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for .NET, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://apireference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) class can be used to add a background image to a page object.

The following code snippet shows how to add a background image to PDF pages using the BackgroundArtifact object.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Create a new Document object
Document doc = new Document();

// Add a new page to document object
Page page = doc.Pages.Add();

// Create Background Artifact object
BackgroundArtifact background = new BackgroundArtifact();

// Specify the image for backgroundartifact object
background.BackgroundImage = File.OpenRead(dataDir + "aspose-total-for-net.jpg");

// Add backgroundartifact to artifacts collection of page
page.Artifacts.Add(background);

dataDir = dataDir + "ImageAsBackground_out.pdf";
// Save the document
doc.Save(dataDir);
```

## Working with Existing Watermarks

A watermark created with Adobe Acrobat is called an artifact (as described in 14.8.2.2 Real Content and Artifacts of the PDF specification). In order to work with artifacts, Aspose.PDF has two classes: [Artifact](https://apireference.aspose.com/net/pdf/aspose.pdf/artifact) and [ArtifactCollection](https://apireference.aspose.com/net/pdf/aspose.pdf/artifactcollection).

In order to get all artifacts on a particular page, the [Page](https://apireference.aspose.com/net/pdf/aspose.pdf/page) class has the Artifacts property. This topic explains how to work with artifact in PDF files.

### Working with Artifacts

The [Artifact](https://apireference.aspose.com/net/pdf/aspose.pdf/artifact) class contains following properties:

- **Artifact.Type** – gets the artifact type (supports values of the Artifact.ArtifactType enumeration where values include Background, Layout, Page, Pagination and Undefined).
- **Artifact.Subtype** – gets artifact subtype (supports the values of the Artifact.ArtifactSubtype enumeration where values include Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Please note that watermarks created with Adobe Acrobat have the type Pagination and subtype Watermark.

{{% /alert %}}

- **Artifact.Contents** – Gets a collection of artifact internal operators. Its supported type is System.Collections.ICollection.
- **Artifact.Form** – Gets an artifact's XForm (if XForm is used). Watermarks, header, and footer artifacts contains XForm which shows all artifact contents.
- **Artifact.Image** – Gets an artifact's image (if an image is presents, else null).
- **Artifact.Text** – Gets an artifact's text.
- **Artifact.Rectangle** – Gets an position of an artifact on the page.
- **Artifact.Rotation** – Gets an artifact's rotation (in degrees, positive value indicates counter-clockwise rotation).
- **Artifact.Opacity** – Gets an artifact's opacity. Possible values are in the range 0...1, where 1 is completely opaque.

#### Programming Samples: Getting Watermarks

The following code snippet shows how to get each watermark on the first page of a PDF file.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Stamps-Watermarks-GetWatermark-GetWatermark.cs" >}}

#### Programming Samples: Counting Artifacts of a Particular Type

To calculate the total count of artifacts of a particular type (for example, the total number of watermarks), use the following code:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Stamps-Watermarks-CountingArtifacts-CountingArtifacts.cs" >}}