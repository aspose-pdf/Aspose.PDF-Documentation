---
title: Merge PDF files in C++
linktitle: Merge PDF files
type: docs
weight: 50
url: /cpp/merge-pdf/
description: Combine two PDF files into one document in C++ by appending pages with Aspose.PDF.
lastmod: "2026-10-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Combine related PDF files into one document by appending their page collections.

## Merge two PDF documents

1. Open both input files as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) objects.
1. Append the pages of the second document to the first with [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void MergeDocuments(String inputFile1, String inputFile2, String outputFile) {
    auto document1 = MakeObject<Document>(inputFile1);
    auto document2 = MakeObject<Document>(inputFile2);
    document1->get_Pages()->Add(document2->get_Pages());
    document1->Save(outputFile);
}
```
