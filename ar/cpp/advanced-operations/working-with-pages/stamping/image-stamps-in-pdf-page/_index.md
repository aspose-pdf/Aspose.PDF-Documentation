---
title: إضافة الطوابع الصورية في ملف PDF برمجياً 
linktitle: الطوابع الصورية في ملف PDF
type: docs
weight: 10
url: ar/cpp/image-stamps-in-pdf-page/
description: أضف الطابع الصوري في وثيقة PDF باستخدام فئة ImageStamp مع مكتبة Aspose.PDF for C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة طابع صوري في ملف PDF

يمكنك استخدام فئة ImageStamp لإضافة طابع صوري إلى ملف PDF. توفر فئة ImageStamp الخصائص اللازمة لإنشاء طابع مستند إلى الصورة، مثل الارتفاع، العرض، الشفافية وهكذا.

لإضافة طابع صوري:

1. قم بإنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) وكائن ImageStamp باستخدام الخصائص المطلوبة.
1. قم باستدعاء طريقة [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) لإضافة الطابع إلى PDF.

يوضح مقتطف الكود التالي كيفية إضافة طابع صوري في ملف PDF.

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

## التحكم في جودة الصورة عند إضافة ختم

عند إضافة صورة ككائن ختم، يمكنك التحكم في جودة الصورة. خاصية الجودة في فئة [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) تُستخدم لهذا الغرض. تشير إلى جودة الصورة بالنسبة المئوية (القيم الصالحة هي 0..100).

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

## ختم الصورة كخلفية في صندوق عائم

تسمح لك Aspose.PDF API بإضافة ختم صورة كخلفية في صندوق عائم. خاصية BackgroundImage لفئة FloatingBox يمكن استخدامها لتعيين ختم صورة الخلفية لصندوق عائم كما هو موضح في نموذج الكود التالي.

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