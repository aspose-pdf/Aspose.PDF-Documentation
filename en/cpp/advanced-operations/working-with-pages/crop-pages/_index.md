---
title: Crop PDF pages in C++
linktitle: Crop Pages
type: docs
weight: 40
url: /cpp/crop-pages/
description: Change PDF page boxes or crop the first page to its first detected image placement using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Change PDF page boxes or crop the first page to its first detected image placement using Aspose.PDF for C++.

## Set page boxes to a rectangle

The example leaves MediaBox unchanged. Page-box changes affect the visible or production regions and do not remove content outside the boxes.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/) using the supplied coordinates.
1. Set CropBox, TrimBox, ArtBox, and BleedBox on the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of CropExamples.cropPage.
void CropPage(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    auto newBox = MakeObject<Rectangle>(200, 220, 2170, 1520, true);
    document->get_Pages()->idx_get(1)->set_CropBox(newBox);
    document->get_Pages()->idx_get(1)->set_TrimBox(newBox);
    document->get_Pages()->idx_get(1)->set_ArtBox(newBox);
    document->get_Pages()->idx_get(1)->set_BleedBox(newBox);
    document->Save(outputFile);
}
```

## Crop to the first image placement

This crops to the first image placement only; it does not calculate a bounding box for all text, images, or other content.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create an [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacementabsorber/) and process page 1.
1. If an image placement exists, assign its rectangle to the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) CropBox.
1. Otherwise, print that no images were found.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/ImagePlacement.h>
#include <Aspose.PDF.Cpp/ImagePlacementAbsorber.h>
#include <Aspose.PDF.Cpp/ImagePlacementCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of CropExamples.cropPageByContent.
void CropPageByContent(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    auto absorber = MakeObject<ImagePlacementAbsorber>();
    document->get_Pages()->idx_get(1)->Accept(absorber);
    if (absorber->get_ImagePlacements()->get_Count() > 0) {
        document->get_Pages()->idx_get(1)->set_CropBox(absorber->get_ImagePlacements()->idx_get(1)->get_Rectangle());
    } else {
        std::cout << "No images found on the first page" << std::endl;
    }
    document->Save(outputFile);
}
```
