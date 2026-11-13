---
title: Remove PDF header and footer artifacts in C++
linktitle: Remove Headers and Footers
type: docs
weight: 110
url: /cpp/remove-headers-footers/
description: Remove header and footer pagination artifacts from the first PDF page using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete PDF Header and Footer Pagination Artifacts in C++
Abstract: Remove first-page artifacts classified as Pagination with a Header or Footer subtype. The example preserves other artifact classifications and ordinary page content.
---

The example processes page 1 only and removes Pagination artifacts with the Header or Footer subtype. Text, images, or annotations that merely look like a header or footer are not selected by this filter.

The input PDF must contain at least one page. Configure the Aspose.PDF for C++ SDK and use a writable output path for examples that save a PDF.

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

## Related artifact topics

- [Add Headers and Footers](/pdf/cpp/artifacts-header-footer/)
- [Work with PDF Artifacts](/pdf/cpp/artifacts/)
