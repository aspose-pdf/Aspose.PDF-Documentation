---
title: Inspect images in PDF in C++
linktitle: Get and Search Images
type: docs
weight: 50
url: /cpp/search-and-get-images-from-pdf-document/
description: Inspect image placement dimensions, coordinates, resolution, color types, and drawing transformations on the first PDF page with Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Read PDF Image Geometry, Resolution, and Color Types in C++
Abstract: Learn how to inspect image placement coordinates, dimensions, resolution, and color types with Aspose.PDF for C++. The examples also track drawing matrices to calculate displayed image sizes and effective resolution on the first page.
---

Inspect image placement dimensions, coordinates, resolution, color types, and drawing transformations on the first PDF page with Aspose.PDF for C++.

## Read image placement parameters

Placement dimensions and coordinates are in PDF points rather than source-image pixels. The outputFile parameter is unused; results are written to the console.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Visit page 1 with [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacementabsorber/).
1. Iterate through each [ImagePlacement](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacement/).
1. Read the placement [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/) width, height, and lower-left coordinates.
1. Read horizontal and vertical resolution and print the results.

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DOM/Matrix.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XImage.h>
#include <Aspose.PDF.Cpp/XImageCollection.h>
#include <Aspose.PDF.Cpp/ImagePlacement.h>
#include <Aspose.PDF.Cpp/ImagePlacementAbsorber.h>
#include <Aspose.PDF.Cpp/ImagePlacementCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void ImageExamples::ExtractParams(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    auto absorber = MakeObject<ImagePlacementAbsorber>();
    page->Accept(absorber);
    for (auto& placement : absorber->get_ImagePlacements())
    {
        auto rect = placement->get_Rectangle();
        std::cout << "image width: " << rect->get_Width() << "\nimage height: " << rect->get_Height()
                  << "\nimage LLX: " << rect->get_LLX() << "\nimage LLY: " << rect->get_LLY()
                  << "\nimage horizontal resolution: " << placement->get_Resolution()->get_X()
                  << "\nimage vertical resolution: " << placement->get_Resolution()->get_Y() << std::endl;
    }
}
```

## Count image placement color types

This counts detected placements, so one image resource can be counted more than once. BlackAndWhite and Undefined results are included in the total but not in either category counter. The outputFile parameter is unused.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Visit page 1 with [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacementabsorber/).
1. Read [GetColorType()](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximage/) from each placement [XImage](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximage/).
1. Count [ColorType](https://reference.aspose.com/pdf/cpp/aspose.pdf/colortype/) values Grayscale and Rgb.
1. Print the total placement count and the two category counts.

```cpp
#include <Aspose.PDF.Cpp/ColorType.h>
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

void ImageExamples::ExtractTypes(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    auto absorber = MakeObject<ImagePlacementAbsorber>();
    page->Accept(absorber);
    int gray = 0, rgb = 0;
    for (auto& placement : absorber->get_ImagePlacements())
    {
        auto type = placement->get_Image()->GetColorType();
        if (type == ColorType::Grayscale)
            ++gray;
        if (type == ColorType::Rgb)
            ++rgb;
    }
    std::cout << "Total Images = " << absorber->get_ImagePlacements()->get_Count()
              << "\nGrayscale Images = " << gray << "\nRGB Images = " << rgb << std::endl;
}
```

## Inspect drawing matrices and effective resolution

This example inspects direct image calls in the first page content stream. It does not recursively traverse Form XObjects or report inline images. The outputFile parameter is unused.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select page 1 and retrieve its [XImageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximagecollection/).
1. Initialize a stack with an identity [Matrix](https://reference.aspose.com/pdf/cpp/aspose.pdf/matrix/).
1. Track [GSave](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/gsave/) and [GRestore](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/grestore/) operators and apply [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/concatenatematrix/) transformations.
1. For each [Do](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/do/) operator naming an image resource, calculate the displayed width and height from the matrix.
1. Skip zero-sized results and calculate resolution as pixel size multiplied by 72 and divided by displayed size.
1. Print the resource name, displayed size, and effective resolution.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DOM/Matrix.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XImage.h>
#include <Aspose.PDF.Cpp/XImageCollection.h>
#include <Aspose.PDF.Cpp/ImagePlacement.h>
#include <Aspose.PDF.Cpp/ImagePlacementAbsorber.h>
#include <Aspose.PDF.Cpp/ImagePlacementCollection.h>
#include <Aspose.PDF.Cpp/Operator.h>
#include <Aspose.PDF.Cpp/OperatorCollection.h>


#include <system/io/file.h>
#include <vector>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Operators;

void ImageExamples::ExtractInformation(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    auto images = page->get_Resources()->get_Images();
    std::vector<SharedPtr<Matrix>> states{MakeObject<Matrix>(1, 0, 0, 1, 0, 0)};
    for (auto& op : page->get_Contents())
    {
        if (op.dynamic_pointer_cast<GSave>())
            states.push_back(MakeObject<Matrix>(states.back()));
        else if (op.dynamic_pointer_cast<GRestore>())
        {
            if (states.size() > 1)
                states.pop_back();
        }
        else if (auto concatenate = op.dynamic_pointer_cast<ConcatenateMatrix>())
        {
            states.back() = states.back()->Multiply(concatenate->get_Matrix());
        }
        else if (auto draw = op.dynamic_pointer_cast<Do>())
        {
            const auto name = draw->get_Name();
            if (images->get_Names()->Contains(name))
            {
                auto image = images->idx_get(name);
                auto& matrix = states.back();
                double width = std::hypot(matrix->get_A(), matrix->get_B());
                double height = std::hypot(matrix->get_C(), matrix->get_D());
                if (width == 0 || height == 0)
                    continue;
                std::cout << name << " image (" << width << ":" << height << "): res "
                          << image->get_Width() * 72 / width << " x " << image->get_Height() * 72 / height
                          << std::endl;
            }
        }
    }
}
```
