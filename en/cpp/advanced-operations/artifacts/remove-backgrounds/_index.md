---
title: Remove PDF background artifacts in C++
linktitle: Remove Backgrounds
type: docs
weight: 80
url: /cpp/remove-backgrounds/
description: Remove background pagination artifacts from the first PDF page using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete Background Pagination Artifacts in C++
Abstract: Remove artifacts classified as Pagination and Background from page 1. The example iterates backward through the artifact collection before saving the document.
---

The example processes only the first page and deletes artifacts whose Type is Pagination and Subtype is Background. Background-like content stored as ordinary page text, images, or annotations is outside this filter.

The input PDF must contain at least one page. Configure the Aspose.PDF for C++ SDK and use a writable output path for examples that save a PDF.

## Remove background artifacts

Delete Pagination artifacts with the Background subtype from page 1. Reverse iteration avoids skipping items when the collection shrinks.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first page [Artifacts](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_artifacts/) collection.
1. Iterate backward from [ArtifactCollection::get_Count()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifactcollection/get_count/) to index 1.
1. Check [Artifact::get_Type()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_type/) for Pagination and [get_Subtype()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_subtype/) for Background.
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


void RemoveBackground(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto artifacts = document->get_Pages()->idx_get(1)->get_Artifacts();
    for (int i = artifacts->get_Count(); i >= 1; --i) {
        auto artifact = artifacts->idx_get(i);
        if (artifact->get_Type() == Artifact::ArtifactType::Pagination &&
            artifact->get_Subtype() == Artifact::ArtifactSubtype::Background) {
            artifacts->Delete(artifact);
        }
    }
    document->Save(outputFile);
}
```

## Related artifact topics

- [Add Backgrounds](/pdf/cpp/add-backgrounds/)
- [Work with PDF Artifacts](/pdf/cpp/artifacts/)
