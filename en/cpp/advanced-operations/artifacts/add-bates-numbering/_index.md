---
title: Add Bates numbering to PDF in C++
linktitle: Add Bates Numbering
type: docs
weight: 10
url: /cpp/add-bates-numbering/
description: Apply six-digit Bates numbering through direct or pagination APIs using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Apply Sequential Bates Identifiers to PDF Pages in C++
Abstract: Configure a shared BatesNArtifact and apply it with AddBatesNumbering or AddPagination. Both supplied C++ examples append two blank pages before numbering all document pages.
---

Bates numbering assigns sequential identifiers to pages. Both C++ addition examples append two blank pages to the input document before numbering the entire page collection. This behavior differs from the Python examples, which number the existing pages.

The shared helper sets six digits starting at `000001`, no prefix or suffix, and bottom-right placement. Save it as `bates-artifact.h` beside either addition example. Configure the SDK and choose a writable output path.

## Configure the shared Bates artifact

Save the following helper as bates-artifact.h beside the addition examples. It configures six digits starting at 1, all pages through the end of the document, no prefix or suffix, bottom-right alignment, and explicit margins.

1. Create a [BatesNArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/batesnartifact/).
1. Set its page range and subset using [PaginationArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/paginationartifact/) properties.
1. Set the number of digits, start number, prefix, and suffix on the [BatesNArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/batesnartifact/).
1. Configure alignment and margins through [Artifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/) properties.

```cpp
#pragma once
#include <Aspose.PDF.Cpp/Artifacts/BatesNArtifact.h>
#include <Aspose.PDF.Cpp/Artifacts/Pagination/Subset.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/VerticalAlignment.h>

inline System::SharedPtr<Aspose::Pdf::BatesNArtifact> CreateBatesArtifact()
{
    using namespace Aspose::Pdf;
    auto artifact = System::MakeObject<BatesNArtifact>();
    artifact->set_StartPage(1);
    artifact->set_EndPage(0);
    artifact->set_Subset(Subset::All);
    artifact->set_NumberOfDigits(6);
    artifact->set_StartNumber(1);
    artifact->set_Prefix(u"");
    artifact->set_Suffix(u"");
    artifact->set_ArtifactVerticalAlignment(VerticalAlignment::Bottom);
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Right);
    artifact->set_RightMargin(72);
    artifact->set_LeftMargin(72);
    artifact->set_TopMargin(36);
    artifact->set_BottomMargin(36);
    return artifact;
}
```

## Add Bates numbering directly

Append two blank pages and apply the shared Bates artifact to the document pages.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Append two pages with [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Call CreateBatesArtifact() to obtain the configured [BatesNArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/batesnartifact/).
1. Apply it with [PageCollectionExtensions::AddBatesNumbering()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollectionextensions/addbatesnumbering/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>

using namespace System;
using namespace Aspose::Pdf;

#include "bates-artifact.h"
#include <Aspose.PDF.Cpp/Artifacts/Pagination/PageCollectionExtensions.h>

void AddBatesNArtifact(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (int i = 0; i < 2; ++i) {
        document->get_Pages()->Add();
    }
    auto artifact = CreateBatesArtifact();
    PageCollectionExtensions::AddBatesNumbering(document->get_Pages(), artifact);
    document->Save(outputFile);
}
```

## Add Bates numbering through pagination

Use the same helper, but pass the Bates artifact in a collection of PaginationArtifact objects to AddPagination().

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Append two pages with [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Call CreateBatesArtifact() and add the result to a list of [PaginationArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/paginationartifact/) objects.
1. Call [PageCollectionExtensions::AddPagination()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollectionextensions/addpagination/) for the document page collection.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>

using namespace System;
using namespace Aspose::Pdf;

#include "bates-artifact.h"
#include <Aspose.PDF.Cpp/Artifacts/Pagination/PageCollectionExtensions.h>
#include <Aspose.PDF.Cpp/Artifacts/PaginationArtifact.h>
#include <system/collections/list.h>

void AddBatesNArtifactPagination(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (int i = 0; i < 2; ++i) {
        document->get_Pages()->Add();
    }
    auto artifact = CreateBatesArtifact();
    auto artifacts = MakeObject<System::Collections::Generic::List<SharedPtr<PaginationArtifact>>>();
    artifacts->Add(artifact);
    PageCollectionExtensions::AddPagination(document->get_Pages(), artifacts);
    document->Save(outputFile);
}
```

## Moved inspection and removal guides

<a id="delete-bates-numbering"></a>

See [Remove Bates Numbering](/pdf/cpp/remove-bates-numbering/) for this operation.

## Related artifact topics

- [Remove Bates Numbering](/pdf/cpp/remove-bates-numbering/)
- [Work with PDF Artifacts](/pdf/cpp/artifacts/)
