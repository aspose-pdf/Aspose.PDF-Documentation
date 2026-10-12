---
title: Convert image formats to PDF in C++
linktitle: Convert Images to PDF
type: docs
weight: 60
url: /cpp/convert-images-format-to-pdf/
description: Convert BMP, JPEG, PNG, EMF, DICOM, TIFF, CGM, and SVG images to PDF in C++ using Aspose.PDF.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create PDFs from Raster and Vector Images in C++
Abstract: Learn how to convert BMP, JPEG, PNG, EMF, DICOM, TIFF, CGM, and SVG images to PDF with Aspose.PDF for C++. The examples use image placement or format-specific load options and demonstrate page sizing from a JPEG and SVG page size adjustment.
---

Convert image files into PDF documents with Aspose.PDF for C++. These examples place images on PDF pages or load vector formats with dedicated options. They also cover SVG page size adjustment and page dimensions derived from a JPEG bitmap.

## Convert BMP to PDF

Place a BMP image on a page in a new PDF document.

1. Create an empty [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page with [Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create an [Image](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/) and set its File property to the input image path.
1. Add the image to the page's [Paragraphs](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

//Convert BMP to PDF
void ConvertBMPtoPDF(String path_infile, String path_outfile) {
    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(path_infile);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(path_outfile);
}
```

## Convert JPEG to PDF

Place a JPEG image on a page in a new PDF document.

1. Create an empty [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page with [Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create an [Image](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/) and set its File property to the input image path.
1. Add the image to the page's [Paragraphs](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertJPEGtoPDF(String path_infile, String path_outfile)
{
    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(path_infile);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(path_outfile);
}
```

## Set PDF page dimensions from a JPEG

Use a bitmap to obtain the JPEG dimensions and configure the PDF page size and margins.

The source adds the same image object twice; it is retained below rather than silently corrected. Review the output if you need a single image placement. Bitmap pixel dimensions are assigned directly to PDF page dimensions; the example does not calculate the page size from image DPI.

1. Create an empty [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page with [Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Open the image file and create a System::Drawing::Bitmap.
1. Create an [Image](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/) and add it to the page's [Paragraphs](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection.
1. Set the [PageInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/pageinfo/) height and width from the bitmap dimensions.
1. Set all page margins to zero.
1. Add the image to the paragraphs collection again, as shown in the supplied source.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertJPGtoPDF_fitsize(String path_infile, String path_outfile)
{
    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto fileStream = System::IO::File::OpenRead(path_infile);
    auto bitMap = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(path_infile);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Set page dimensions and margins
    page->get_PageInfo()->set_Height(bitMap->get_Height());
    page->get_PageInfo()->set_Width(bitMap->get_Width());
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(path_outfile);
}
```

## Convert PNG to PDF

Place a PNG image on a page in a new PDF document.

1. Create an empty [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page with [Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create an [Image](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/) and set its File property to the input image path.
1. Add the image to the page's [Paragraphs](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertPNGtoPDF(String path_infile, String path_outfile)
{    
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(path_infile);
    page->get_Paragraphs()->Add(image);
    document->Save(path_outfile);
}
```

## Convert EMF to PDF

Place a EMF image on a page in a new PDF document.

1. Create an empty [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page with [Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create an [Image](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/) and set its File property to the input image path.
1. Add the image to the page's [Paragraphs](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertEMFtoPDF(String path_infile, String path_outfile)
{
    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(path_infile);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(path_outfile);
}
```

## Convert DICOM to PDF

Place a DICOM image on a page in a new PDF document.

1. Create an empty [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page with [Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create an [Image](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/) and set its File property to the DICOM path.
1. Set FileType to ImageFileType::Dicom.
1. Add the image to the page's [Paragraphs](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

using namespace System;
using namespace Aspose::Pdf;

void ConvertDICOMtoPDF(String path_infile, String path_outfile)
{
    // Instantiate Document Object
    auto document = MakeObject<Document>();

    // Add a page to pages collection of document
    auto page = document->get_Pages()->Add();

    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(path_infile);
    image->set_FileType(Aspose::Pdf::ImageFileType::Dicom);

    page->get_Paragraphs()->Add(image);

    // Save output as PDF format
    document->Save(path_outfile);
}
```

## Convert TIFF to PDF through a stream

Load a TIFF bitmap and pass its image data to a PDF image through a memory stream.

This example creates one PDF page and does not iterate over TIFF frames. It is not an example of exporting every frame of a multipage TIFF.

1. Create an empty [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page with [Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Open the input TIFF as a readable stream and construct a System::Drawing::Bitmap.
1. Create an [Image](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/) and a System::IO::MemoryStream.
1. Save the bitmap to the memory stream using TIFF encoding.
1. Set the image's ImageStream and add it to the page's [Paragraphs](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertTIFFtoPDF(String path_infile, String path_outfile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto fileStream = System::IO::File::OpenRead(path_infile);
    auto pdfImage = MakeObject<Aspose::Pdf::Image>();
    auto bitmap = MakeObject<System::Drawing::Bitmap>(fileStream);
    auto imgStream = MakeObject<System::IO::MemoryStream>();
    auto imageStream = System::DynamicCast<System::IO::Stream>(imgStream);
    bitmap->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Tiff());
    pdfImage->set_ImageStream(imageStream);
    page->get_Paragraphs()->Add(pdfImage);
    document->Save(path_outfile);
}
```

## Convert CGM to PDF

Load the CGM source with format-specific options and save it as PDF.

1. Create [CgmLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/cgmloadoptions/).
1. Construct a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with the input file path and the load options.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

#include <Aspose.PDF.Cpp/CgmLoadOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertCGMtoPDF(String path_infile, String path_outfile)
{
    auto options = MakeObject<CgmLoadOptions>();
    auto document = MakeObject<Document>(path_infile, options);
    document->Save(path_outfile);
}
```

## Convert SVG to PDF

Load the SVG source with format-specific options and save it as PDF.

1. Create [SvgLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/svgloadoptions/).
1. Construct a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with the input file path and the load options.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/SvgLoadOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertSVGtoPDF(String path_infile, String path_outfile)
{
    auto options = MakeObject<SvgLoadOptions>();
    auto document = MakeObject<Document>(path_infile, options);
    document->Save(path_outfile);
}
```

## Convert SVG with page size adjustment

Enable automatic page size adjustment and select the SVG conversion engine used by the supplied example.

1. Create [SvgLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/svgloadoptions/).
1. Set AdjustPageSize to true.
1. Set ConversionEngine to SvgLoadOptions::ConversionEngines::NewEngine.
1. Construct a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) from the SVG path and options.
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/SvgLoadOptions.h>

using namespace System;
using namespace Aspose::Pdf;

void ConvertSVGtoPDF_Advanced(String path_infile, String path_outfile)
{
    auto options = MakeObject<SvgLoadOptions>();
    options->set_AdjustPageSize(true);
    options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;
    auto document = MakeObject<Document>(path_infile, options);
    document->Save(path_outfile);
}
```
