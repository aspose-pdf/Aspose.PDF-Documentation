---
title: Remove PDF Bates numbering in C++
linktitle: Remove Bates Numbering
type: docs
weight: 100
url: /cpp/remove-bates-numbering/
description: Remove Bates numbering from the document page collection using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Bates Identifiers from PDF Pages in C++
Abstract: Pass all document pages to PageCollectionExtensions::DeleteBatesNumbering and save the result. The operation targets Bates numbering rather than arbitrary page-number text.
---

Pass the entire document page collection to DeleteBatesNumbering(). Unlike the first-page artifact examples, this function processes Bates numbering across the document.

Configure the SDK and choose a writable output path.

## Delete Bates numbering

Remove Bates numbering through the page collection extension method.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Pass the document pages to [PageCollectionExtensions::DeleteBatesNumbering()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollectionextensions/deletebatesnumbering/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>

using namespace System;
using namespace Aspose::Pdf;

#include <Aspose.PDF.Cpp/Artifacts/Pagination/PageCollectionExtensions.h>

void DeleteBatesNumbering(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    PageCollectionExtensions::DeleteBatesNumbering(document->get_Pages());
    document->Save(outputFile);
}
```

## Related artifact topics

- [Add Bates Numbering](/pdf/cpp/add-bates-numbering/)
- [Work with PDF Artifacts](/pdf/cpp/artifacts/)
