---
title: Add Image stamps in PDF programmatically 
linktitle: Image stamps in PDF File
type: docs
weight: 10
url: /cpp/image-stamps-in-pdf-page/
description: Add the Image Stamp in your PDF document using ImageStamp class with the Aspose.PDF for C++ library.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Image Stamp in PDF File

You can use the ImageStamp class to add an image stamp to a PDF file. The ImageStamp class provides the properties necessary for creating an image-based stamp, such as height, width, opacity and so on.

To add an image stamp:

1. Create a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object and an ImageStamp object using required properties.
1. Call the [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) class [AddStamp](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) method to add the stamp to the PDF.

The following code snippet shows how to add image stamp in the PDF file.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddImageStampToPDFFile()
{    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("AddImageStamp.pdf");

    String outputFileName("AddImageStamp_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create image stamp
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");
    imageStamp->set_Background(true);
    imageStamp->set_XIndent(100);
    imageStamp->set_YIndent(100);
    imageStamp->set_Height(48);
    imageStamp->set_Width(225);
    imageStamp->set_Rotate(Rotation::on270);
    imageStamp->set_Opacity(0.5);
   
    // Add stamp to particular page    
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);

    // Save output document
    document->Save(_dataDir + outputFileName);
}
```

## Control Image Quality when Adding Stamp

When adding an image as a stamp object, you can control the quality of the image. The Quality property of the [ImageStamp](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) class is used for this purpose. It indicates the quality of image in percents (valid values are 0..100).

```cpp
void ControlImageQualityWhenAddingStamp() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("ControlImageQuality_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create image stamp
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    imageStamp->set_Quality(10);
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);    
    document->Save(_dataDir + u"ControlImageQuality_out.pdf");
}
```

## Image Stamp as Background in Floating Box

Aspose.PDF API lets you add image stamp as background in a floating box. The BackgroundImage property of FloatingBox class can be used to set the background image stamp for a floating box as shown in following code sample.

```cpp
void ImageStampAsBackgroundInFloatingBox() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("AddImageStampAsBackgroundInFloatingBox_out.pdf");

    // Instantiate Document object
    auto document = MakeObject<Document>();

    // Add page to PDF document
    auto page = document->get_Pages()->Add();

    // Create FloatingBox object
    auto aBox = MakeObject<FloatingBox>(200, 100);

    // Set left position for FloatingBox
    aBox->set_Left(40);
    // Set Top position for FloatingBox
    aBox->set_Top(80);
    // Set the Horizontal alignment for FloatingBox
    aBox->set_HorizontalAlignment(HorizontalAlignment::Center);
    
    // Add text fragment to paragraphs collection of FloatingBox    
    aBox->get_Paragraphs()->Add(MakeObject<TextFragment>(u"main text"));

    // Set border for FloatingBox
    aBox->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));

    // Add background image
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.png");
    aBox->set_BackgroundImage(image);

    // Set background color for FloatingBox
    aBox->set_BackgroundColor(Color::get_Yellow());

    // Add FloatingBox to paragraphs collection of page object
    page->get_Paragraphs()->Add(aBox);
    // Save the PDF document
    document->Save(_dataDir + outputFileName);
}
```
