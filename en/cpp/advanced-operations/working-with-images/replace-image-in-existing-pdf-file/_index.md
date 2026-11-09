---
title: Replace images in PDF in C++
linktitle: Replace Images
type: docs
weight: 40
url: /cpp/replace-image-in-existing-pdf-file/
description: Replace an image resource or the first detected image placement on the first PDF page using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Update PDF Image Resources and Placements in C++
Abstract: Learn how to replace the first image resource or the first detected image placement on a PDF page with Aspose.PDF for C++. Both examples load a replacement JPEG from the input PDF directory and save the updated document.
---

Replace an image resource or the first detected image placement on the first PDF page using Aspose.PDF for C++.

## Replace an image resource

The input must contain an image resource at index 1 on page 1. Replacing a resource can affect every placement that uses that resource.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Open sample_new.jpg from the input PDF directory.
1. Select the first page [XImageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximagecollection/) and call [Replace(1, stream)](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximagecollection/).
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Close the replacement-image stream.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
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

void ImageExamples::ReplaceImage(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto stream = System::IO::File::OpenRead(
        System::IO::Path::Combine(System::IO::Path::GetDirectoryName(inputFile), u"sample_new.jpg"));
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Replace(1, stream);
    document->Save(outputFile);
    stream->Close();
}
```

## Replace the first detected image placement

If no placement is found, the PDF is saved without replacement. The sample opens the replacement file before checking for placements.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Open sample_new.jpg from the input PDF directory.
1. Visit page 1 with [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacementabsorber/).
1. If a placement exists, call [Replace()](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacement/) on the first [ImagePlacement](https://reference.aspose.com/pdf/cpp/aspose.pdf/imageplacement/) with the stream.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Close the replacement-image stream.

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
#include <Aspose.PDF.Cpp/ImagePlacement.h>
#include <Aspose.PDF.Cpp/ImagePlacementAbsorber.h>
#include <Aspose.PDF.Cpp/ImagePlacementCollection.h>

#include <system/io/file.h>

using namespace System;
using namespace Aspose::Pdf;


void ImageExamples::ReplaceWithAbsorber(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto stream = System::IO::File::OpenRead(
        System::IO::Path::Combine(System::IO::Path::GetDirectoryName(inputFile), u"sample_new.jpg"));
    auto absorber = MakeObject<ImagePlacementAbsorber>();
    document->get_Pages()->idx_get(1)->Accept(absorber);
    if (absorber->get_ImagePlacements()->get_Count() > 0)
        absorber->get_ImagePlacements()->idx_get(1)->Replace(stream);
    document->Save(outputFile);
    stream->Close();
}
```
