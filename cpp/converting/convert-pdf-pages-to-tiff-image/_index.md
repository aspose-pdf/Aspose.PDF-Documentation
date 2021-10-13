---
title: Convert PDF to TIFF 
linktitle: Convert PDF to TIFF 
type: docs
weight: 30
url: /cpp/convert-pdf-to-tiff/
lastmod: "2021-06-05"
description: This article describes how to convert pages in PDF document into TIFF image. You will learn how to convert all or single pages to TIFF images with Aspose.PDF for C++.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** makes a possible to convert PDF Pages to TIFF  images.

## Live Example

Aspose.PDF for C++ presents you online free application ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), where you may try to investigate the functionality and quality it works.

[![PDF to TIFF](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

## Convert PDF Pages to One TIFF Image

Aspose.PDF for C++ explain how to convert all pages in a PDF file to a single TIFF image:

1. Create a [String Class](https://apireference.aspose.com/pdf/cpp/class/system.string) for path name and file name.

1. Open document with MakeObject.

1. Create Resolution object.

1. Create TIffSettings object.

1. Create TiFF device with specified attributes.

1. Convert a particular page and save the image to stream.

The following code snippet shows how to convert all the PDF pages to a single TIFF image.

```cpp
void ConvertPDFtoTIFF()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for file name
 String infilename("PageToTiff.pdf");
 String outfilename("PagesToTIFF_out.tif");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

 // Create Resolution object
 auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

 // Create TiffSettings object
 auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
 tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::None);
 tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Default);
 tiffSettings->set_Shape(Aspose::Pdf::Devices::ShapeType::Landscape);
 tiffSettings->set_SkipBlankPages(false);

 // Create TIFF device
 auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);

 // Convert pages and save the image to stream
 tiffDevice->Process(document, 1, 2, imageStream);
 std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convert One Page to TIFF Image

Aspose.PDF for C++ allows you to convert a particular page in a PDF file to a TIFF image, use an overloaded version of the Process(..) method which takes a page number as an argument for conversion. The following code snippet shows how to convert the first page of a PDF to TIFF format.

```cpp
void ConvertPDFtoTiffSinglePage()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for file name
 String infilename("PageToTiff.pdf");
 String outfilename("PageToTiff_out.tif");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

 // Create Resolution object
 auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

 // Create TIFF device
 auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution);

 // Convert a particular page and save the image to stream
 tiffDevice->Process(document, 1, 1, imageStream);
 std::clog << __func__ << ": Finish" << std::endl;
}
```

