---
title: Remove PDF watermark artifacts in C++
linktitle: Remove Watermarks
type: docs
weight: 90
url: /cpp/remove-watermarks/
description: Remove only watermark pagination artifacts from the first PDF page using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete PDF Watermark Pagination Artifacts in C++
Abstract: Filter the first page artifacts by the Pagination type and Watermark subtype, then delete matching entries. Watermarks represented by ordinary text, images, or annotations remain in the document.
---

The example deletes only artifacts with the Pagination type and Watermark subtype on the first page. Visible watermarks stored as regular page text, images, or annotations remain in the PDF. It does not scan or modify artifacts on other pages.

The input PDF must contain at least one page. Configure the Aspose.PDF for C++ SDK and use a writable output path for examples that save a PDF.

## Delete watermark artifacts

Check both Type and Subtype before deleting each matching first-page artifact. Reverse iteration avoids skipping entries after deletion.

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

## Related artifact topics

- [Add Watermarks](/pdf/cpp/add-watermarks/)
- [Extract Watermark Details](/pdf/cpp/extract-watermarks/)
- [Work with PDF Artifacts](/pdf/cpp/artifacts/)
