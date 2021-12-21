---
title: Add Header and Footer to PDF
linktitle: Add Header and Footer to PDF
type: docs
weight: 70
url: /cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for C++ allows you to add headers and footers to your PDF file using TextStamp class.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** allows you to add header and footer in your existing PDF file. You may add images or text to a PDF document. Also, try to add different headers in one PDF File with C++.

## Adding Text in Header of PDF File

You can use [TextStamp](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) class to add text in the header of a PDF file. TextStamp class provides properties necessary to create a text based stamp like font size, font style, and font color etc. In order to add text in the header, you need to create a Document object and a TextStamp object using required properties. After that, you can call AddStamp method of the Page to add the text in the header of the PDF.

You need to set the TopMargin property in such a way that it adjusts the text in the header area of your PDF. You also need to set HorizontalAlignment to Center and VerticalAlignment to Top.

The following code snippet shows you how to add text in the header of a PDF file with C++.

```cpp
void AddingTextInHeaderOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinHeader.pdf");
    String outputFileName("TextinHeader_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create header
    auto textStamp = MakeObject<TextStamp>(u"Header Text");

    // Set properties of the stamp
    textStamp->set_TopMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // Add header on all pages
    for(auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```

## Adding Text in Footer of PDF File

You can use TextStamp class to add text in the footer of a PDF file. TextStamp class provides properties necessary to create a text based stamp like font size, font style, and font color etc. In order to add text in the footer, you need to create a Document object and a TextStamp object using required properties. After that, you can call AddStamp method of the Page to add the text in the footer of the PDF.

{{% alert color="primary" %}}

You need to set the Bottom Margin property in such a way that it adjusts the text in the footer area of your PDF. You also need to set HorizontalAlignment to Center and VerticalAlignment to Bottom

{{% /alert %}}

The following code snippet shows you how to add text in the footer of a PDF file with C++.

```cpp
void AddingTextInFooterOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinFooter.pdf");
    String outputFileName("TextinFooter_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create footer
    auto textStamp = MakeObject<TextStamp>(u"Footer Text");

    // Set properties of the stamp
    textStamp->set_BottomMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Bottom);

    // Add footer on all pages
    for (auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```

## Adding Image in Header of PDF File

You can use [ImageStamp](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) class to add image in the header of a PDF file. Image Stamp class provides properties necessary to create image based stamp like font size, font style, and font color etc. In order to add image in the header, you need to create a Document object and a Image Stamp object using required properties. After that, you can call AddStamp method of the Page to add the image in the header of the PDF.

The following code snippet shows you how to add image in the header of a PDF file with C++.

```cpp
void AddingImageInHeaderOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinHeader.pdf");
    String outputFileName("ImageinHeader_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create header
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // Set properties of the stamp
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment (VerticalAlignment::Top);

    // Add header on all pages
    for(auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```

## Adding Image in Footer of PDF File

You can use Image Stamp class to add image in the footer of a PDF file. Image Stamp class provides properties necessary to create image based stamp like font size, font style, and font color etc. In order to add image in the footer, you need to create a Document object and an Image Stamp object using required properties. After that, you can call AddStamp method of the Page to add the image in the footer of the PDF.

You need to set the [BottomMargin](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.stamp#aeab91949cf3eb473018b31a74fed7173) property in such a way that it adjusts the image in the footer area of your PDF. You also need to set [HorizontalAlignment](https://apireference.aspose.com/pdf/cpp/namespace/aspose.pdf#aefec9c0bf30ee5e6fb2640e69aed6cd9) to `Center` and [VerticalAlignment](https://apireference.aspose.com/pdf/cpp/namespace/aspose.pdf#ad4956d03096fc515eaa34319a6bf636a) to `Bottom`.

The following code snippet shows you how to add image in the footer of a PDF file with C++.

```cpp
void AddingImageInFooterOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinFooter.pdf");
    String outputFileName("ImageinFooter_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create header
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // Set properties of the stamp
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // Add header on all pages
    for (auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```

## Adding different Headers in one PDF File

We know that we can add TextStamp in Header/Footer section of the document by using TopMargin or Bottom Margin properties, but sometimes we may have the requirement to add multiple header/footers in a single PDF document. **Aspose.PDF for C++** explains how to do this.

In order to accomplish this requirement, we will create individual TextStamp objects (number of objects depends upon the number of Header/Footers required)and will add them to PDF document. We may also specify different formatting information for individual stamp object. In following example, we have created Document object and three TextStamp objects and then we have used [AddStamp](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) method of the Page to add the text in the header section of the PDF. The following code snippet shows you how to add image in the footer of a PDF file with Aspose.PDF for C++.

```cpp
void AddingDifferentHeadersInOnePDFFile()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("multiheader.pdf");
    String outputFileName("multiheader_out.pdf");

    // Open source document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create three stamps
    auto stamp1 = MakeObject<TextStamp>("Header 1");
    auto stamp2 = MakeObject<TextStamp>("Header 2");
    auto stamp3 = MakeObject<TextStamp>("Header 3");

    // Set stamp alignment (place stamp on page top, centered horiznotally)
    stamp1->set_VerticalAlignment(VerticalAlignment::Top);
    stamp1->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Specify the font style as Bold
    stamp1->get_TextState()->set_FontStyle(FontStyles::Bold);
    // Set the text fore ground color information as red
    stamp1->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Specify the font size as 14
    stamp1->get_TextState()->set_FontSize(14);

    // Now we need to set the vertical alignment of 2nd stamp object as Top
    stamp2->set_VerticalAlignment(VerticalAlignment::Top);
    // Set Horizontal alignment information for stamp as Center aligned
    stamp2->set_HorizontalAlignment (HorizontalAlignment::Center);
    // Set the zooming factor for stamp object
    stamp2->set_Zoom(10);

    // Set the formatting of 3rd stamp object
    // Specify the Vertical alignment information for stamp object as TOP
    stamp3->set_VerticalAlignment(VerticalAlignment::Top);
    // Set the Horizontal alignment inforamtion for stamp object as Center aligned
    stamp3->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Set the rotation angle for stamp object
    stamp3->set_RotateAngle(35);
    // Set pink as background color for stamp
    stamp3->get_TextState()->set_BackgroundColor(Color::get_Pink());
    // Change the font face information for stamp to Verdana
    stamp3->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));

    // First stamp is added on first page;
    document->get_Pages()->idx_get(1)->AddStamp(stamp1);
    // Second stamp is added on second page;
    document->get_Pages()->idx_get(2)->AddStamp(stamp2);
    // Third stamp is added on third page.
    document->get_Pages()->idx_get(3)->AddStamp(stamp3);

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```
