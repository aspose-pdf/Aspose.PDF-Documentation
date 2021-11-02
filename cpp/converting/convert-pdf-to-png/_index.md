---
title: Convert PDF to PNG 
linktitle: Convert PDF to PNG
type: docs
weight: 20
url: /cpp/convert-pdf-to-png/
lastmod: "2021-06-05"
description: This page describes how to convert PDF Pages to PNG image, convert all and single pages to PNG images with Aspose.PDF for C++.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Use the Aspose.PDF for C++ library for converting PDF Pages to <abbr title="Portable Network Graphics">PNG</abbr> Images in an accessible and convenient way.

## Convert PDF Pages to PNG Images

## Live Example

Aspose.PDF for C++ presents you online free application ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), where you may try to investigate the functionality and quality it works.

[![How to convert PDF to PNG](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)

Aspose.PDF for C++ show you how to convert PDf to PNG Single Page:

1. Create a [String Class](https://apireference.aspose.com/pdf/cpp/class/system.string) for path name and file name.

1. Open document with MakeObject.

1. Create Resolution object.

1. Create PNG device with specified attributes Width, Height, Resolution.

1. Convert a particular page and save the image to stream.

1. Close stream using imageStream.

```cpp
void ConvertPDFtoPngSinglePage()
{
 std::clog << __func__ << ": Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for file name
 String infilename("PageToPng.pdf");
 String outfilename("PageToPng_out.png");

 // Open document
 auto document = MakeObject<Document>(_dataDir + infilename);

 auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

 // Create Resolution object
 auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

 // Create PNG device with specified attributes Width, Height, Resolution
 auto PngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice >(500, 700, resolution);

 // Convert a particular page and save the image to stream
 PngDevice->Process(document->get_Pages()->idx_get(1), imageStream);

 // Close stream
 imageStream->Close();
 std::clog << __func__ << ": Finish" << std::endl;
}
```
