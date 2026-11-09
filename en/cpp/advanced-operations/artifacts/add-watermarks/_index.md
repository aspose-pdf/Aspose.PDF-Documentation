---
title: Manage PDF watermark artifacts in C++
linktitle: Adding Watermark
type: docs
weight: 30
url: /cpp/add-watermarks/
description: Create a styled text watermark artifact, read watermark text and bounds, and delete watermark artifacts using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add, Inspect, and Delete PDF Watermark Artifacts in C++
Abstract: Create a centered text watermark with Aspose.PDF for C++ and configure its font, rotation, opacity, and background placement. Additional examples print watermark text and rectangles and remove watermark pagination artifacts from the first page.
---

WatermarkArtifact adds a watermark as a page artifact. These examples use the first page and operate on artifact-based watermarks.

The input PDF must contain at least one page. Configure the Aspose.PDF for C++ SDK before using these functions; the text examples also require Arial to be available.

## Add a text watermark

Create a centered WATERMARK in bold 72-point Arial with BlueViolet text, 60-degree rotation, and 0.2 opacity. IsBackground places it behind page content.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Configure a [TextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/) with Arial, size, color, and bold style.
1. Create a [WatermarkArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/watermarkartifact/) and set its text and state with [Artifact::SetTextAndState()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/settextandstate/).
1. Set horizontal and vertical alignment on the [Artifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/).
1. Set rotation, opacity, and IsBackground on the [Artifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/).
1. Add the artifact to the first page with [ArtifactCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifactcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>

using namespace System;
using namespace Aspose::Pdf;

#include <Aspose.PDF.Cpp/Artifacts/WatermarkArtifact.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/VerticalAlignment.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

void AddWatermarkArtifact(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto state = MakeObject<Aspose::Pdf::Text::TextState>();
    state->set_FontSize(72);
    state->set_ForegroundColor(Color::get_BlueViolet());
    state->set_FontStyle(Aspose::Pdf::Text::FontStyles::Bold);
    state->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Arial"));
    auto artifact = MakeObject<WatermarkArtifact>();
    artifact->SetTextAndState(u"WATERMARK", state);
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment(VerticalAlignment::Center);
    artifact->set_Rotation(60);
    artifact->set_Opacity(0.2);
    artifact->set_IsBackground(true);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(outputFile);
}
```

## Read watermark text and bounds

Print the text and rectangle of first-page artifacts with type Pagination and subtype Watermark. This function reads artifact properties; it does not export an image or create another PDF.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through [Page::get_Artifacts()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_artifacts/) on the first page.
1. Filter using [Artifact::get_Type()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_type/) and [get_Subtype()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_subtype/).
1. Print [Artifact::get_Text()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_text/) and [get_Rectangle()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_rectangle/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>

using namespace System;
using namespace Aspose::Pdf;

#include <iostream>
#include <Aspose.PDF.Cpp/Rectangle.h>

void ExtractWatermarkFromPdf(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto artifact : document->get_Pages()->idx_get(1)->get_Artifacts()) {
        if (artifact->get_Type() == Artifact::ArtifactType::Pagination &&
            artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) {
            std::cout << artifact->get_Text() << " " << artifact->get_Rectangle()->ToString() << std::endl;
        }
    }
}
```

## Delete watermark artifacts

Remove watermark pagination artifacts from the first page by iterating backward through the collection.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first page [Artifacts](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_artifacts/) collection.
1. Iterate backward from [ArtifactCollection::get_Count()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifactcollection/get_count/) to index 1.
1. Check [Artifact::get_Type()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_type/) for Pagination and [get_Subtype()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_subtype/) for Watermark.
1. Delete matches with [ArtifactCollection::Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifactcollection/delete/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>

using namespace System;
using namespace Aspose::Pdf;


void DeleteWatermarkArtifact(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto artifacts = document->get_Pages()->idx_get(1)->get_Artifacts();
    for (int i = artifacts->get_Count(); i >= 1; --i) {
        auto artifact = artifacts->idx_get(i);
        if (artifact->get_Type() == Artifact::ArtifactType::Pagination &&
            artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) {
            artifacts->Delete(artifact);
        }
    }
    document->Save(outputFile);
}
```
