---
title: إضافة رأس وتذييل إلى PDF
linktitle: إضافة رأس وتذييل إلى PDF
type: docs
weight: 70
url: /cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for C++ يسمح لك بإضافة رؤوس وتذييلات إلى ملف PDF الخاص بك باستخدام فئة TextStamp.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** يسمح لك بإضافة رأس وتذييل في ملف PDF الموجود لديك. يمكنك إضافة صور أو نص إلى مستند PDF. حاول أيضًا إضافة رؤوس مختلفة في ملف PDF واحد باستخدام C++.

## إضافة نص في رأس ملف PDF

يمكنك استخدام فئة [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) لإضافة نص في رأس ملف PDF. 
توفر فئة TextStamp الخصائص اللازمة لإنشاء ختم نصي مثل حجم الخط ونمط الخط ولون الخط وما إلى ذلك. لإضافة نص في الرأس، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة النص في رأس ملف PDF.

تحتاج إلى تعيين خاصية TopMargin بطريقة تجعلها تضبط النص في منطقة الرأس من ملف PDF الخاص بك. تحتاج أيضًا إلى تعيين HorizontalAlignment إلى Center و VerticalAlignment إلى Top.

يوضح لك مقتطف الشيفرة التالي كيفية إضافة نص في رأس ملف PDF باستخدام C++.

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
## إضافة نص في تذييل ملف PDF

يمكنك استخدام فئة TextStamp لإضافة نص في تذييل ملف PDF. توفر فئة TextStamp الخصائص اللازمة لإنشاء ختم يعتمد على النص مثل حجم الخط، نمط الخط، ولون الخط إلخ. لإضافة نص في التذييل، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة النص في تذييل ملف الـ PDF.

{{% alert color="primary" %}}

تحتاج إلى ضبط خاصية الحافة السفلية بحيث تضبط النص في منطقة التذييل لملف PDF الخاص بك. كما تحتاج إلى ضبط المحاذاة الأفقية إلى الوسط والمحاذاة الرأسية إلى الأسفل

{{% /alert %}}

يظهر لك المثال التالي كيفية إضافة نص في تذييل ملف PDF باستخدام C++.

```cpp
void AddingTextInFooterOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinFooter.pdf");
    String outputFileName("TextinFooter_out.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // إنشاء تذييل
    auto textStamp = MakeObject<TextStamp>(u"Footer Text");

    // ضبط خصائص الختم
    textStamp->set_BottomMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Bottom);

    // إضافة التذييل على جميع الصفحات
    for (auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // حفظ المستند المحدث
    document->Save(_dataDir + outputFileName);
}
```

## إضافة صورة في رأس ملف PDF

يمكنك استخدام فئة [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) لإضافة صورة في رأس ملف PDF. توفر فئة ختم الصورة الخصائص اللازمة لإنشاء ختم يعتمد على الصورة مثل حجم الخط، نمط الخط، ولون الخط إلخ. لإضافة صورة في الرأس، تحتاج إلى إنشاء كائن Document وكائن Image Stamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة الصورة في رأس ملف PDF.

يوضح لك مقتطف الشفرة التالي كيفية إضافة صورة في رأس ملف PDF باستخدام C++.

```cpp
void AddingImageInHeaderOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinHeader.pdf");
    String outputFileName("ImageinHeader_out.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // إنشاء الرأس
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // تعيين خصائص الختم
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment (VerticalAlignment::Top);

    // إضافة الرأس في جميع الصفحات
    for(auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // حفظ المستند المحدث
    document->Save(_dataDir + outputFileName);
}
```

## إضافة صورة في تذييل ملف PDF

يمكنك استخدام فئة Image Stamp لإضافة صورة في تذييل ملف PDF. توفر فئة Image Stamp الخصائص اللازمة لإنشاء ختم يعتمد على الصورة مثل حجم الخط، نمط الخط، ولون الخط وغيرها. لإضافة صورة في التذييل، تحتاج إلى إنشاء كائن Document وكائن Image Stamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة الصورة في تذييل ملف PDF.

تحتاج إلى تعيين خاصية [BottomMargin](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.stamp#aeab91949cf3eb473018b31a74fed7173) بطريقة تضبط الصورة في منطقة التذييل لملف PDF. كما تحتاج إلى تعيين [HorizontalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#aefec9c0bf30ee5e6fb2640e69aed6cd9) إلى `Center` و [VerticalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ad4956d03096fc515eaa34319a6bf636a) إلى `Bottom`.

يُظهر لك مقتطف الشيفرة التالي كيفية إضافة صورة في تذييل ملف PDF باستخدام C++.

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

## إضافة رؤوس مختلفة في ملف PDF واحد

نعلم أنه يمكننا إضافة نص في قسم الترويسة/الذيل للوثيقة باستخدام خصائص الهامش العلوي أو الهامش السفلي، ولكن في بعض الأحيان قد يكون لدينا متطلبات لإضافة ترويسات/ذيول متعددة في وثيقة PDF واحدة. **Aspose.PDF for C++** يشرح كيفية القيام بذلك.

من أجل تحقيق هذا المتطلب، سنقوم بإنشاء كائنات TextStamp فردية (عدد الكائنات يعتمد على عدد الرؤوس/التذييلات المطلوبة) وسنضيفها إلى مستند PDF. يمكننا أيضًا تحديد معلومات تنسيق مختلفة لكل كائن ختم فردي. في المثال التالي، قمنا بإنشاء كائن Document وثلاثة كائنات TextStamp ثم استخدمنا طريقة [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) من الصفحة لإضافة النص في قسم الرأس من PDF. يوضح لك مقطع الكود التالي كيفية إضافة صورة في تذييل ملف PDF باستخدام Aspose.PDF لـ C++.

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