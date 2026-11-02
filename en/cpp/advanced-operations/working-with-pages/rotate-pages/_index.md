---
title: Rotate PDF pages in C++
linktitle: Rotate Pages
type: docs
weight: 90
url: /cpp/rotate-pages/
description: Set the rotation of every PDF page to 90 degrees using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Set Every PDF Page to 90-Degree Rotation in C++
Abstract: Learn how to iterate through a PDF document and set each page's rotation with Aspose.PDF for C++. The example assigns 90-degree rotation to every page and saves the result.
---

Set the rotation of every PDF page to 90 degrees using Aspose.PDF for C++.

## Set all pages to 90-degree rotation

The example sets an absolute rotation value of 90 degrees rather than adding 90 degrees to the existing rotation.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through every [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Set Rotate to on90 from [Rotation](https://reference.aspose.com/pdf/cpp/aspose.pdf/rotation/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rotation.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of RotatePagesExamples.rotatePage.
void RotatePage(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    for (const auto& page : document->get_Pages()) {
        page->set_Rotate(Rotation::on90);
    }
    document->Save(outputFile);
}
```
