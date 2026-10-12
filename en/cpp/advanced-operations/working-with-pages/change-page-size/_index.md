---
title: Read and change PDF page size in C++
linktitle: Change Page Size
type: docs
weight: 30
url: /cpp/change-page-size/
description: Read PDF page dimensions, compare rectangles with and without rotation, and set a page size using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Read PDF page dimensions, compare rectangles with and without rotation, and set a page size using Aspose.PDF for C++.

## Read the first page size

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select page 1 and call [GetPageRect()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/getpagerect/) with true.
1. Print the [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/) width and height.

Source example: `get-page-size.cpp`.

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of ChangeSizeExamples.getPageSize.
void GetPageSize(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);

    auto rectangle = document->get_Pages()->idx_get(1)->GetPageRect(true);
    std::cout << rectangle->get_Width() << " : " << rectangle->get_Height() << std::endl;
}
```

## Compare page size with rotation

The rotation change is made in memory only; this function does not save a PDF.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Set page 1 rotation to on90 using [Rotation](https://reference.aspose.com/pdf/cpp/aspose.pdf/rotation/).
1. Call [GetPageRect()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/getpagerect/) with false and print the dimensions.
1. Call [GetPageRect()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/getpagerect/) with true and print the dimensions.

Source example: `get-page-size-rotation.cpp`.

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rotation.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of ChangeSizeExamples.getPageSizeRotation.
void GetPageSizeRotation(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);

    auto page = document->get_Pages()->idx_get(1);
    page->set_Rotate(Rotation::on90);
    auto rectangle = page->GetPageRect(false);
    std::cout << rectangle->get_Width() << " : " << rectangle->get_Height() << std::endl;
    rectangle = page->GetPageRect(true);
    std::cout << rectangle->get_Width() << " : " << rectangle->get_Height() << std::endl;
}
```

## Set the first page size

The dimensions are in PDF points. This changes the page geometry; it does not explicitly scale the existing page content.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and print its page-box dimensions.
1. Call [SetPageSize()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/setpagesize/) with width 597.6 and height 842.4.
1. Print the resulting page-box dimensions.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `set-page-size.cpp`.

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of ChangeSizeExamples.setPageSize.
void SetPageSize(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    auto page = document->get_Pages()->idx_get(1);
    std::cout << "Before set" << std::endl;
    std::cout << "CropBox: " << page->get_CropBox()->get_Width() << " x " << page->get_CropBox()->get_Height() << std::endl;
    std::cout << "TrimBox: " << page->get_TrimBox()->get_Width() << " x " << page->get_TrimBox()->get_Height() << std::endl;
    std::cout << "ArtBox: " << page->get_ArtBox()->get_Width() << " x " << page->get_ArtBox()->get_Height() << std::endl;
    std::cout << "BleedBox: " << page->get_BleedBox()->get_Width() << " x " << page->get_BleedBox()->get_Height() << std::endl;
    std::cout << "MediaBox: " << page->get_MediaBox()->get_Width() << " x " << page->get_MediaBox()->get_Height() << std::endl;
    page->SetPageSize(597.6, 842.4);
    std::cout << "After set" << std::endl;
    std::cout << "CropBox: " << page->get_CropBox()->get_Width() << " x " << page->get_CropBox()->get_Height() << std::endl;
    std::cout << "TrimBox: " << page->get_TrimBox()->get_Width() << " x " << page->get_TrimBox()->get_Height() << std::endl;
    std::cout << "ArtBox: " << page->get_ArtBox()->get_Width() << " x " << page->get_ArtBox()->get_Height() << std::endl;
    std::cout << "BleedBox: " << page->get_BleedBox()->get_Width() << " x " << page->get_BleedBox()->get_Height() << std::endl;
    std::cout << "MediaBox: " << page->get_MediaBox()->get_Width() << " x " << page->get_MediaBox()->get_Height() << std::endl;
    document->Save(outputFile);
}
```
