---
title: Extract images from PDF in C++
linktitle: Extract Images from PDF
type: docs
weight: 20
url: /cpp/extract-images-from-the-pdf-file/
description: Save an embedded image resource from a PDF page as JPEG using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Save an embedded image resource from a PDF page as JPEG using Aspose.PDF for C++.

## Extract the first image from page 1

Export one image from the first page resource collection.

The input must have page 1 and at least one image resource on it. The example does not iterate over all images.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select page 1 and retrieve its first [XImage](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximage/) resource.
1. Open a writable output stream.
1. Save the image using JPEG encoding.
1. Close the stream.

Source example: `images.cpp`.

```cpp
#include <system/io/file.h>
#include <drawing/imaging/image_format.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XImage.h>
#include <Aspose.PDF.Cpp/XImageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractImage(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(outputFile);

    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();
}
```
