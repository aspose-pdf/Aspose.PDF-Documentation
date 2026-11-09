---
title: Import and export annotations in C++
linktitle: Import and Export Annotations
type: docs
weight: 80
url: /cpp/import-export-annotations/
description: Copy annotations from the first page of a source PDF to a new PDF document using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transfer PDF Annotations Between Documents in C++
Abstract: Learn how to copy annotations from the first page of an existing PDF into a new PDF document with Aspose.PDF for C++. The example creates a destination page, adds each source annotation with AnnotationCollection::Add, and saves the result.
---

Aspose.PDF for C++ lets you transfer annotations between PDF documents through the page Annotations collection. The following example copies annotations from the first page of an existing PDF to a page in a new document.

## Copy annotations from one PDF to another

The ImportExport function accepts the source PDF path and the output PDF path. It creates a blank destination page and copies the source annotations using Add(annot, true). The true argument requests that the annotation be copied rather than moved.

This example transfers annotations only. The source page text, images, and other page content are not copied. The input PDF must contain at least one page.

1. Open the source PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a destination [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Add a [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) to the destination document with [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Get the first source page through [PageCollection::idx_get()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/idx_get/).
1. Iterate through the source page [Annotations](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_annotations/) collection.
1. Copy each annotation to the destination page with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/), passing true as the isCopy argument.
1. Save the destination PDF with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

void ImportExport(System::String inputFile, System::String outputFile)
{
    auto sourceDocument = MakeObject<Document>(inputFile);
    auto destinationDocument = MakeObject<Document>();
    auto page = destinationDocument->get_Pages()->Add();
    for (auto& annot : sourceDocument->get_Pages()->idx_get(1)->get_Annotations()) {
        page->get_Annotations()->Add(annot, true);
    }
    destinationDocument->Save(outputFile);
}
```
