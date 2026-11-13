---
title: Count PDF pagination artifacts in C++
linktitle: Counting Artifacts
type: docs
weight: 40
url: /cpp/counting-artifacts/
description: Count watermark, background, header, and footer pagination artifacts on the first PDF page using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Count PDF Pagination Artifacts by Subtype in C++
Abstract: Filter the first page artifact collection to Pagination entries and count four standard subtypes. The function prints zero for absent subtypes and does not modify or save the PDF.
---

Inspect the first page artifact collection and count Watermark, Background, Header, and Footer subtypes. Other artifact types and subtypes are skipped.

The input PDF must contain at least one page. Configure the Aspose.PDF for C++ SDK and use a writable output path for examples that save a PDF.

## Count pagination artifacts by subtype

Initialize four counters, skip artifacts whose type is not Pagination, and increment the counter for each recognized subtype. Print the counts without saving a modified PDF.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through the first page [Artifacts](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_artifacts/) collection.
1. Check [Artifact::get_Type()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_type/) and skip non-Pagination artifacts.
1. Switch on [Artifact::get_Subtype()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_subtype/) to count Watermark, Background, Header, and Footer.
1. Print the four counters.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>

using namespace System;
using namespace Aspose::Pdf;

#include <iostream>

void CountPdfArtifacts(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    int watermarks = 0, backgrounds = 0, headers = 0, footers = 0;
    for (auto& artifact : document->get_Pages()->idx_get(1)->get_Artifacts()) {
        if (artifact->get_Type() != Artifact::ArtifactType::Pagination) continue;
        switch (artifact->get_Subtype()) {
        case Artifact::ArtifactSubtype::Watermark: ++watermarks; break;
        case Artifact::ArtifactSubtype::Background: ++backgrounds; break;
        case Artifact::ArtifactSubtype::Header: ++headers; break;
        case Artifact::ArtifactSubtype::Footer: ++footers; break;
        default: break;
        }
    }
    std::cout << "Watermarks: " << watermarks << "\nBackgrounds: " << backgrounds
              << "\nHeaders: " << headers << "\nFooters: " << footers << std::endl;
}
```

## Related artifact topics

- [Extract Watermark Details](/pdf/cpp/extract-watermarks/)
- [Remove Watermarks](/pdf/cpp/remove-watermarks/)
- [Remove Backgrounds](/pdf/cpp/remove-backgrounds/)
- [Remove Headers and Footers](/pdf/cpp/remove-headers-footers/)
- [Work with PDF Artifacts](/pdf/cpp/artifacts/)
