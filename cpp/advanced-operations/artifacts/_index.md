---
title: Working with Artifacts in C++
linktitle: Working with Artifacts
type: docs
weight: 110
url: /cpp/artifacts/
description: This page describes how to work with Artifact class using Aspose.PDF for C++. Code snippets show how to add a background image to PDF pages and how to get each watermark on the first page of a PDF file.
lastmod: "2021-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## How to get Watermark in PDF?

**What is an artifact in PDF?**

According to the PDF / UA ISO reference, content that is not important or does not appear in the background does not carry relevant information, should be flagged as an artifact so that assistive technologies can ignore it.
If artifacts cannot be identified in the program to create, this must be done manually using Aspose.PDF for C++.

The [Artifact](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) class contains following properties:

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

For an example of working with artifacts in a PDF file, let's take a watermark.

A watermark created with support for Adobe Acrobat is referred to as an artifact (as described in 14.8.2.2 Present Content and PDF Specification Artifacts). For working with artifacts Aspose.PDF contains 2 classes:
[Artifact](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) and [ArtifactCollection](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

In order to get all artifacts on a particular page, the [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) class has the Artifacts property. This topic shows how to work with Watermark artifact in PDF files.

The following code snippet shows how to get each watermark on the first page of a PDF file wiuth C++:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
void Artifacts::SetWatermark() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto artifact = MakeObject<WatermarkArtifact>();
    String text(u"WATERMARK");    
    artifact->set_Text(text);
    artifact->get_TextState()->set_ForegroundColor(Color::get_Blue());
    artifact->get_TextState()->set_FontSize(72);
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment(VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(_dataDir + u"watermark.pdf");
}
```

Background images can be used to add watermarks or exclusive designs to PDF documents. Aspose.PDF for C++ uses the [BackgroundArtifact](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) class to add a background image to the page object.

The next code snippet shows you how to add a background image to PDF pages with the BackgroundArtifact object:

```cpp
void Artifacts::SetBackground() {

    String _dataDir("C:\\Samples\\");

    // Open document
    auto pdfDocument = MakeObject<Document>();

    // Add a MakeObject<page to document object
    auto page = pdfDocument->get_Pages()->Add();

    // Create Background Artifact object
    auto background = MakeObject<BackgroundArtifact>();

    // Specify the image for backgroundartifact object
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // Add BackgroundArtifact to artifacts collection of page
    page->get_Artifacts()->Add(background);

    // Save modified PDF
    pdfDocument->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```

### Programming Samples: Getting Watermarks

The following code snippet shows how to get each watermark on the first page of a PDF file.

```cpp
void Artifacts::GettingWatermarks() {
    
    String _dataDir("C:\\Samples\\");

    // Open document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    // Iterate through and get sub-type, text and location of artifact
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        Console::WriteLine(u"{0} {1} {2}", artifact->get_Subtype(), 
            artifact->get_Text(), artifact->get_Rectangle());
    }

}
```

### Programming Samples: Counting Artifacts of a Particular Type

To calculate the total count of artifacts of a particular type (for example, the total number of watermarks), use the following code:

```cpp
void Artifacts::CountingArtifacts() {

    String _dataDir("C:\\Samples\\");

    // Open document
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    int count = 0;
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        // If artifact type is watermark, increate the counter
        if (artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) count++;
    }
    Console::WriteLine(u"Page contains {0} watermarks", count);
}
```