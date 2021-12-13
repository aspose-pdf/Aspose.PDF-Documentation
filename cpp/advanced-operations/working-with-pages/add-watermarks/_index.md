---
title: Add watermark to PDF using C++
linktitle: Add watermark
type: docs
weight: 90
url: /cpp/add-watermarks/
description: This article explains the features of working with artifacts and getting watermarks in PDFs using  programmatically the C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A Watermark is a translucent image that usually contains a logo or seal to identify who created the document or image.

**Aspose.PDF for C++** allows adding watermarks to your PDF document using Artifact class. Please check this article to resolve your task.

A watermark created with Adobe Acrobat is called an artifact (as described in 14.8.2.2 Real Content and Artifacts of the PDF specification). In order to work with artifacts, Aspose.PDF has two classes: [Artifact](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) and [ArtifactCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

In order to get all artifacts on a particular page, the [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) class has the Artifacts property. This topic explains how to work with artifact in PDF files.

## Working with Artifacts

The [Artifact](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) class contains following properties:

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

## Programming Samples: How To Add Watermark On PDF Files

The following code snippet shows how to get each watermark on the first page of a PDF file with C++.

```cpp
void GettingWatermarks() {
	
	String _dataDir("C:\\Samples\\");
	String inputFileName("watermark.pdf");
	String outputFileName("watermark_out.pdf");

	auto document = MakeObject<Document>(_dataDir + inputFileName);

	auto artifact = MakeObject<WatermarkArtifact>();
	auto textState = MakeObject<TextState>();
	textState->set_FontSize(72);
	textState->set_ForegroundColor(Color::get_Blue());
	textState->set_Font(FontRepository::FindFont(u"Courier"));
	artifact->SetTextAndState(u"WATERMARK", textState);
	artifact->set_ArtifactHorizontalAlignment (HorizontalAlignment::Center);
	artifact->set_ArtifactVerticalAlignment (VerticalAlignment::Center);
	artifact->set_Rotation(45);
	artifact->set_Opacity(0.5);
	artifact->set_IsBackground(true);

	document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
	
	document->Save(_dataDir + outputFileName);
}
```
