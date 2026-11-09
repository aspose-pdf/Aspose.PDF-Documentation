---
title: Add images to PDF in C++
linktitle: Add Images
type: docs
weight: 10
url: /cpp/add-image-to-existing-pdf-file/
description: Create PDFs containing images using a page rectangle, drawing operators, Flate compression, or alternative text with Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insert Images into New PDF Pages with C++
Abstract: Learn how to create PDF pages containing images with Aspose.PDF for C++. The examples use page rectangles, drawing operators, Flate compression, and an attempt to assign alternative text.
---

Create PDFs containing images using a page rectangle, drawing operators, Flate compression, or alternative text with Aspose.PDF for C++.

## Add an image to a new page

In these four examples, inputFile is an image file and the output is a newly created PDF.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Define a [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/) with coordinates (20, 730, 120, 830).
1. Call [AddImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) on the [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) with the input image path and rectangle.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;

void ImageExamples::AddImage(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    page->AddImage(inputFile, MakeObject<Rectangle>(20, 730, 120, 830));
    document->Save(outputFile);
}
```

## Draw an image with PDF operators

The matrix scales the image to the page width and centers it vertically. A tall image can extend beyond the page bounds.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and open the input image stream.
1. Add a page and set its size to 842 by 595 points.
1. Add the stream to [XImageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximagecollection/) and retain the returned resource name.
1. Calculate a page-width image height from the [XImage](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximage/) pixel aspect ratio.
1. Add [GSave](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/gsave/), [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/concatenatematrix/), [Do](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/do/), and [GRestore](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/grestore/) operators to the page contents.
1. Close the image stream.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Operator.h>
#include <Aspose.PDF.Cpp/OperatorCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XImage.h>
#include <Aspose.PDF.Cpp/XImageCollection.h>

#include <system/io/file.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Operators;

void ImageExamples::AddUsingOperators(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto stream = System::IO::File::OpenRead(inputFile);
    auto page = document->get_Pages()->Add();
    page->SetPageSize(842, 595);
    auto images = page->get_Resources()->get_Images();
    auto name = images->Add(stream);
    auto image = images->idx_get(images->get_Count());
    double width = page->get_MediaBox()->get_Width();
    double height = width * image->get_Height() / image->get_Width();
    page->get_Contents()->Add(MakeObject<GSave>());
    page->get_Contents()->Add(MakeObject<ConcatenateMatrix>(
        width, 0, 0, height, 0, (page->get_MediaBox()->get_Height() - height) / 2));
    page->get_Contents()->Add(MakeObject<Do>(name));
    page->get_Contents()->Add(MakeObject<GRestore>());
    stream->Close();
    document->Save(outputFile);
}
```

## Add an image with Flate compression

The fixed square matrix can change the displayed aspect ratio of a nonsquare image.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/), open the image stream, and add a page.
1. Add the image to [XImageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximagecollection/) with [ImageFilterType](https://reference.aspose.com/pdf/cpp/aspose.pdf/imagefiltertype/) set to Flate.
1. Add [GSave](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/gsave/) and a [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/concatenatematrix/) scaling the image to 600 by 600 points.
1. Draw the named resource with [Do](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/do/) and restore the graphics state with [GRestore](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/grestore/).
1. Close the image stream.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/ImageFilterType.h>
#include <Aspose.PDF.Cpp/Operator.h>
#include <Aspose.PDF.Cpp/OperatorCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XImage.h>
#include <Aspose.PDF.Cpp/XImageCollection.h>

#include <system/io/file.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Operators;

void ImageExamples::AddWithFlateCompression(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto stream = System::IO::File::OpenRead(inputFile);
    auto page = document->get_Pages()->Add();
    auto name = page->get_Resources()->get_Images()->Add(stream, ImageFilterType::Flate);
    page->get_Contents()->Add(MakeObject<GSave>());
    page->get_Contents()->Add(MakeObject<ConcatenateMatrix>(600, 0, 0, 600, 0, 0));
    page->get_Contents()->Add(MakeObject<Do>(name));
    page->get_Contents()->Add(MakeObject<GRestore>());
    stream->Close();
    document->Save(outputFile);
}
```

## Add alternative text to an image

The example attempts to set alternative text and reports whether it succeeded. It does not validate PDF/UA compliance. Use an SDK version that exposes TrySetAlternativeText().

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page sized 842 by 595 points.
1. Call [AddImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) on the [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) using a rectangle that covers the page.
1. Select the first [XImage](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximage/) resource and call [TrySetAlternativeText()](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximage/) with the description and page.
1. Print the returned success flag.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XImage.h>
#include <Aspose.PDF.Cpp/XImageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void ImageExamples::AddWithAltText(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    page->SetPageSize(842, 595);
    page->AddImage(inputFile, MakeObject<Rectangle>(0, 0, 842, 595));
    bool added = page->get_Resources()->get_Images()->idx_get(1)->TrySetAlternativeText(
        u"Alternative text for image", page);
    std::cout << "Alternative text added: " << added << std::endl;
    document->Save(outputFile);
}
```
