---
title: Delete images from PDF in C++
linktitle: Delete Images
type: docs
weight: 20
url: /cpp/delete-images-from-pdf-file/
description: Delete the first image resource from the first PDF page using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove an Embedded Image Resource from a PDF in C++
Abstract: Learn how to delete an image resource from a PDF page with Aspose.PDF for C++. The example removes the first image from the first page and saves the modified document.
---

Delete the first image resource from the first PDF page using Aspose.PDF for C++.

## Delete the first image resource

The PDF must contain page 1 and at least one image resource on that page. This example does not iterate through every page or image.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select page 1 and retrieve its [XImageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximagecollection/).
1. Call [Delete(1)](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximagecollection/) on the image collection.
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

void ImageExamples::DeleteImage(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Delete(1);
    document->Save(outputFile);
}
```
