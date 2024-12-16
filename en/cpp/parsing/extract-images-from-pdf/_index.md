---
title: Extract Images from PDF 
linktitle: Extract Images from PDF
type: docs
weight: 20
url: /cpp/extract-images-from-the-pdf-file/
description: How to extract a part of the image from PDF using Aspose.PDF for C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Also, a demanded task when working with PDF documents is to extract images from a PDF file. For example, you received a PDF email with a lot of great images that you would like to extract as separate files.

Aspose.PDF library allows you to extract images from PDF with еру  next code snippet:

```cpp
void ExtractImage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-image.pdf");
    String outfilename("extracted_image.jpeg");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Extract a particular image
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Save output image
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    std::clog << __func__ << ": Finish" << std::endl;
}
```
