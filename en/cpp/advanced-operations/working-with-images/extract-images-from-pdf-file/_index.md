---
title: Extract images from PDF in C++
linktitle: Extract Images
type: docs
weight: 30
url: /cpp/extract-images-from-pdf-file/
description: Save an embedded PDF image, extract images whose placements lie in a region, and read image alternative text using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export PDF Images and Read Alternative Text in C++
Abstract: Learn how to save an embedded PDF image and filter image placements by a page region with Aspose.PDF for C++. A separate example reads alternative text and prints the first returned item for each detected placement.
---

Save an embedded PDF image, extract images whose placements lie in a region, and read image alternative text using Aspose.PDF for C++.

## Save the first image

The input must contain at least one image resource on page 1. This exports an embedded image, not a rendered page.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create an output file stream.
1. Select the first [XImage](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximage/) resource on page 1.
1. Call [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximage/) on the image with the output stream.
1. Close the stream.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XImage.h>
#include <Aspose.PDF.Cpp/XImageCollection.h>
#include <Aspose.PDF.Cpp/ImagePlacement.h>
#include <Aspose.PDF.Cpp/ImagePlacementAbsorber.h>
#include <Aspose.PDF.Cpp/ImagePlacementCollection.h>

#include <system/io/file.h>

using namespace System;
using namespace Aspose::Pdf;

void ImageExamples::ExtractImage(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto output = System::IO::File::Create(outputFile);
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1)->Save(output);
    output->Close();
}
```

## Extract images placed inside a region

For example, image_index.jpg becomes image_1.jpg, image_2.jpg, and so on. The function filters placements by their rectangles and exports complete embedded images; it does not crop image pixels to the region.

1. Require an output filename containing the literal text index.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Visit page 1 with [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacementabsorber/).
1. Create a region [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/) from (0, 0) to (590, 590).
1. Check whether both lower-left and upper-right placement corners are contained in the region.
1. For each matching [ImagePlacement](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacement/), save its [XImage](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximage/) to a numbered output stream.
1. Close each output stream.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XImage.h>
#include <Aspose.PDF.Cpp/XImageCollection.h>
#include <Aspose.PDF.Cpp/ImagePlacement.h>
#include <Aspose.PDF.Cpp/ImagePlacementAbsorber.h>
#include <Aspose.PDF.Cpp/ImagePlacementCollection.h>

#include <system/io/file.h>

using namespace System;
using namespace Aspose::Pdf;

void ImageExamples::ExtractFromRegion(String inputFile, String outputFile)
{
    if (outputFile.Contains(u"index") == false)
    {
        std::cout << "Please provide a valid output filename containing 'index'." << std::endl;
        return;
    }
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    auto absorber = MakeObject<ImagePlacementAbsorber>();
    page->Accept(absorber);
    auto region = MakeObject<Rectangle>(0, 0, 590, 590);
    int index = 1;
    for (auto& placement : absorber->get_ImagePlacements())
    {
        auto rect = placement->get_Rectangle();
        auto lower = MakeObject<Point>(rect->get_LLX(), rect->get_LLY());
        auto upper = MakeObject<Point>(rect->get_URX(), rect->get_URY());
        if (!region->Contains(lower, true) || !region->Contains(upper, true))
            continue;
        auto output = System::IO::File::Create(outputFile.Replace(u"index", String::Format(u"{0}", index++)));
        placement->get_Image()->Save(output);
        output->Close();
    }
}
```

## Read image alternative text

The outputFile parameter is unused: this function writes to the console. It prints only the first returned alternative-text item for each placement. Use an SDK version that exposes GetAlternativeText().

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Visit page 1 with [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacementabsorber/).
1. Iterate through the detected [ImagePlacement](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacement/) objects.
1. Call [GetAlternativeText()](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximage/) on each [XImage](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximage/) with the page.
1. Print the first returned item, or an empty string if none is returned.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XImage.h>
#include <Aspose.PDF.Cpp/XImageCollection.h>
#include <Aspose.PDF.Cpp/ImagePlacement.h>
#include <Aspose.PDF.Cpp/ImagePlacementAbsorber.h>
#include <Aspose.PDF.Cpp/ImagePlacementCollection.h>

#include <system/io/file.h>

using namespace System;
using namespace Aspose::Pdf;


void ImageExamples::ExtractAltText(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    auto absorber = MakeObject<ImagePlacementAbsorber>();
    page->Accept(absorber);
    for (auto& placement : absorber->get_ImagePlacements())
    {
        auto lines = placement->get_Image()->GetAlternativeText(page);
        std::cout << "Alt Text: " << (lines->get_Count() ? lines->idx_get(0) : String::Empty) << std::endl;
    }
}
```
