---
title: Add image stamps to PDF in C++
linktitle: Image Stamps
type: docs
weight: 100
url: /cpp/image-stamps-in-pdf-page/
description: Add image stamps with position, size, rotation, opacity, or quality settings and add a floating-box background image using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Position and Style PDF Image Stamps in C++
Abstract: Learn how to configure image stamp position, dimensions, rotation, opacity, and quality with Aspose.PDF for C++. The examples also add a background image through a floating box.
---

Add image stamps with position, size, rotation, opacity, or quality settings and add a floating-box background image using Aspose.PDF for C++.

## Add a positioned image stamp

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create an [ImageStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf/imagestamp/) from imageFile.
1. Set background mode, position, dimensions, rotation, and opacity.
1. Call [AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/addstamp/) on page 1.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/ImageStamp.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rotation.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of StampingExamples.addImageStamp.
void AddImageStamp(System::String inputFile, System::String imageFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    auto imageStamp = MakeObject<ImageStamp>(imageFile);
    imageStamp->set_Background(true);
    imageStamp->set_XIndent(100);
    imageStamp->set_YIndent(100);
    imageStamp->set_Height(300);
    imageStamp->set_Width(300);
    imageStamp->set_Rotate(Rotation::on270);
    imageStamp->set_Opacity(0.5);

    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);
    document->Save(outputFile);
}
```

## Set image stamp quality

The low quality setting can affect image appearance. Review the saved output.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create an [ImageStamp](https://reference.aspose.com/pdf/cpp/aspose.pdf/imagestamp/) from imageFile.
1. Set Quality to 10.
1. Call [AddStamp()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/addstamp/) on page 1.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/ImageStamp.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of StampingExamples.addImageStampWithQualityControl.
void AddImageStampWithQualityControl(System::String inputFile, System::String imageFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    auto imageStamp = MakeObject<ImageStamp>(imageFile);
    imageStamp->set_Quality(10);
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);
    document->Save(outputFile);
}
```

## Add a floating-box background image

This adds a paragraph-based floating box rather than calling AddStamp().

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select page 1 and create a [FloatingBox](https://reference.aspose.com/pdf/cpp/aspose.pdf/floatingbox/) sized 200 by 100.
1. Configure position, alignment, text, and border.
1. Create an [Image](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/) and assign it as BackgroundImage.
1. Set the background color and add the box to the page paragraphs.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/FloatingBox.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

// Port of StampingExamples.addImageAsBackgroundInFloatingBox.
void AddImageAsBackgroundInFloatingBox(System::String inputFile, System::String imageFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    auto page = document->get_Pages()->idx_get(1);
    auto box = MakeObject<FloatingBox>(200.0f, 100.0f);
    box->set_Left(40);
    box->set_Top(80);
    box->set_HorizontalAlignment(HorizontalAlignment::Center);
    box->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Text in Floating Box"));
    box->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));

    auto image = MakeObject<Image>();
    image->set_File(imageFile);
    box->set_BackgroundImage(image);
    box->set_BackgroundColor(Color::get_Yellow());
    page->get_Paragraphs()->Add(box);

    document->Save(outputFile);
}
```
