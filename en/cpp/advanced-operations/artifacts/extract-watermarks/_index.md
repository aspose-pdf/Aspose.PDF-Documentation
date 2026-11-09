---
title: Extract PDF watermark details in C++
linktitle: Extract Watermark Details
type: docs
weight: 50
url: /cpp/extract-watermarks/
description: Read the text and rectangle of watermark pagination artifacts on the first PDF page using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspect PDF Watermark Text and Bounds in C++
Abstract: Read watermark artifact properties on the first PDF page. The example prints text and bounding rectangles for Pagination artifacts with the Watermark subtype.
---

This example inspects page 1 only. It prints properties of matching watermark artifacts rather than exporting watermark images or creating a separate PDF.

The input PDF must contain at least one page. Configure the Aspose.PDF for C++ SDK and use a writable output path for examples that save a PDF.

## Read watermark text and bounds

Print text and bounds for matching first-page pagination artifacts. The filter selects only the Watermark subtype.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through [Page::get_Artifacts()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_artifacts/) on the first page.
1. Filter using [Artifact::get_Type()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_type/) and [get_Subtype()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_subtype/).
1. Print [Artifact::get_Text()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_text/) and [get_Rectangle()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_rectangle/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>

using namespace System;
using namespace Aspose::Pdf;

#include <iostream>
#include <Aspose.PDF.Cpp/Rectangle.h>

void ExtractWatermarkFromPdf(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto artifact : document->get_Pages()->idx_get(1)->get_Artifacts()) {
        if (artifact->get_Type() == Artifact::ArtifactType::Pagination &&
            artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) {
            std::cout << artifact->get_Text() << " " << artifact->get_Rectangle()->ToString() << std::endl;
        }
    }
}
```

## Related artifact topics

- [Add Watermarks](/pdf/cpp/add-watermarks/)
- [Remove Watermarks](/pdf/cpp/remove-watermarks/)
- [Work with PDF Artifacts](/pdf/cpp/artifacts/)
