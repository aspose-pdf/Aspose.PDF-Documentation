---
title: Manage PDF header and footer artifacts in C++
linktitle: Manage PDF Headers and Footers
type: docs
weight: 70
url: /cpp/artifacts-header-footer/
description: Add styled header and footer artifacts and delete matching pagination artifacts from a PDF page using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create and Remove PDF Header and Footer Artifacts in C++
Abstract: Add centered header and footer text with Aspose.PDF for C++ using Arial, navy text, and a 14-point font. A separate example removes header and footer pagination artifacts from the first page.
---

HeaderArtifact and FooterArtifact provide artifact-based page headers and footers. The following examples use the first page and style the text with Arial at 14 points in navy.

The input PDF must contain at least one page. Configure the Aspose.PDF for C++ SDK before using these functions; the text examples also require Arial to be available.

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

## Delete header and footer artifacts

Remove both header and footer pagination artifacts from the first page. Other artifact types and subtypes are left in the collection.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first page [Artifacts](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_artifacts/) collection.
1. Iterate backward from [ArtifactCollection::get_Count()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifactcollection/get_count/) to index 1.
1. Check [Artifact::get_Type()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_type/) for Pagination and [get_Subtype()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_subtype/) for Header or Footer.
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


void DeleteHeaderFooterArtifact(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto artifacts = document->get_Pages()->idx_get(1)->get_Artifacts();
    for (int i = artifacts->get_Count(); i >= 1; --i) {
        auto artifact = artifacts->idx_get(i);
        if (artifact->get_Type() == Artifact::ArtifactType::Pagination &&
            (artifact->get_Subtype() == Artifact::ArtifactSubtype::Header
                || artifact->get_Subtype() == Artifact::ArtifactSubtype::Footer)) {
            artifacts->Delete(artifact);
        }
    }
    document->Save(outputFile);
}
```
