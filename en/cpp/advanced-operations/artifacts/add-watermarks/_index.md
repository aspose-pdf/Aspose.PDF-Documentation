---
title: Add PDF watermark artifacts in C++
linktitle: Add Watermarks
type: docs
weight: 30
url: /cpp/add-watermarks/
description: Add a styled text watermark artifact to the first PDF page using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Place a Styled Text Watermark Artifact in C++
Abstract: Create a centered WatermarkArtifact with bold Arial text, a 60-degree rotation, and 0.2 opacity. The C++ example places it behind the first page content.
---

Use `WatermarkArtifact` to add a text watermark to page 1. The example uses Arial, so make that font available to the application.

The input PDF must contain at least one page. Configure the Aspose.PDF for C++ SDK and use a writable output path for examples that save a PDF.

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

## Moved inspection and removal guides

<a id="read-watermark-text-and-bounds"></a>

See [Extract Watermark Details](/pdf/cpp/extract-watermarks/) for this operation.

<a id="delete-watermark-artifacts"></a>

See [Remove Watermarks](/pdf/cpp/remove-watermarks/) for this operation.

## Related artifact topics

- [Extract Watermark Details](/pdf/cpp/extract-watermarks/)
- [Remove Watermarks](/pdf/cpp/remove-watermarks/)
- [Work with PDF Artifacts](/pdf/cpp/artifacts/)
