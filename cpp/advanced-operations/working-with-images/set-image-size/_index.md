---
title: Set Image Size using C++
linktitle: Set Image Size
type: docs
weight: 80
url: /cpp/set-image-size/
description: This section describes how to set image size PDF file using C++ library.
lastmod: "2021-12-18"
---

It is possible to set the size of an image that's being added to a PDF file. In order to set size, you can use [FixWidth](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#a08f2f92b184632385eab19fb96c6d40e) and [FixHeight](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#aed67b52e058b97df6931c214d7092dfa) properties of [Aspose.Pdf.Image Class](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image).

The following code snippet demonstrates how to set the size of an image:

```cpp
void WorkingWithImages::ExampleSetImageSize()
{
    String _dataDir("C:\\Samples\\");
    // Instantiate Document object
    auto document = MakeObject<Document>();
    // add page to pages collection of PDF file
    auto page = document->get_Pages()->Add();
    // Create an image instance
    auto img = MakeObject<Image>();
    // Set Image Width and Height in Points
    img->set_FixWidth(100);
    img->set_FixHeight(100);
    // Set image type as SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Unknown);
    // Path for source file
    img->set_File(_dataDir + u"aspose-logo.jpg");
    page->get_Paragraphs()->Add(img);
    //Set page properties
    page->get_PageInfo()->set_Width(800);
    page->get_PageInfo()->set_Height(800);
    // save resultant PDF file
    document->Save(_dataDir + u"SetImageSize_out.pdf");
}
```
