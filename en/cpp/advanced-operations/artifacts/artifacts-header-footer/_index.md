---
title: Add PDF header and footer artifacts in C++
linktitle: Add Headers and Footers
type: docs
weight: 70
url: /cpp/artifacts-header-footer/
description: Add styled header and footer artifacts to the first PDF page using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Centered PDF Header and Footer Text in C++
Abstract: Use HeaderArtifact and FooterArtifact to add centered text to page 1. Both examples use 14-point Arial and navy text.
---

Use `HeaderArtifact` and `FooterArtifact` to add running text as page artifacts. Each example modifies only the first page and requires Arial to be available.

The input PDF must contain at least one page. Configure the Aspose.PDF for C++ SDK and use a writable output path for examples that save a PDF.

## Add a header artifact

Add the centered text Sample Header to the first page.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [HeaderArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/headerartifact/) and set its text.
1. Configure its [TextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/) with Arial, size 14, and navy text.
1. Set the [Artifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/) horizontal alignment to Center.
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

#include <Aspose.PDF.Cpp/Artifacts/HeaderArtifact.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

void AddHeaderArtifact(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto artifact = MakeObject<HeaderArtifact>();
    artifact->set_Text(u"Sample Header");
    artifact->get_TextState()->set_FontSize(14);
    artifact->get_TextState()->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Arial"));
    artifact->get_TextState()->set_ForegroundColor(Color::get_Navy());
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Center);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(outputFile);
}
```

## Add a footer artifact

Add the centered text Sample Footer to the first page.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [FooterArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/footerartifact/) and set its text.
1. Configure its [TextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/) with Arial, size 14, and navy text.
1. Set the [Artifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/) horizontal alignment to Center.
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

#include <Aspose.PDF.Cpp/Artifacts/FooterArtifact.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

void AddFooterArtifact(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto artifact = MakeObject<FooterArtifact>();
    artifact->set_Text(u"Sample Footer");
    artifact->get_TextState()->set_FontSize(14);
    artifact->get_TextState()->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Arial"));
    artifact->get_TextState()->set_ForegroundColor(Color::get_Navy());
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Center);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(outputFile);
}
```

## Moved inspection and removal guides

<a id="delete-header-and-footer-artifacts"></a>

See [Remove Headers and Footers](/pdf/cpp/remove-headers-footers/) for this operation.

## Related artifact topics

- [Remove Headers and Footers](/pdf/cpp/remove-headers-footers/)
- [Work with PDF Artifacts](/pdf/cpp/artifacts/)
