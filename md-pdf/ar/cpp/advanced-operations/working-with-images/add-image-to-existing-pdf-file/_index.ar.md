---
title: Add Image to PDF using C++
linktitle: Add Image
type: docs
weight: 10
url: /cpp/add-image-to-existing-pdf-file/
description: يصف هذا القسم كيفية إضافة صورة إلى ملف PDF موجود باستخدام مكتبة C++.
lastmod: "2021-12-18"
---

## إضافة صورة في ملف PDF موجود

تحتوي كل صفحة PDF على خصائص الموارد والمحتويات. يمكن أن تكون الموارد صورًا ونماذج على سبيل المثال، بينما يتم تمثيل المحتوى بمجموعة من العمليات PDF. كل عملية لها اسمها وحجتها. يستخدم هذا المثال العمليات لإضافة صورة إلى ملف PDF.

لإضافة صورة إلى ملف PDF موجود:

- قم بإنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) وافتح مستند PDF المدخل.
- احصل على الصفحة التي تريد إضافة صورة إليها.
- أضف الصورة إلى مجموعة الموارد الخاصة بالصفحة.
- استخدم العمليات لوضع الصورة على الصفحة:
- استخدم [GSave operator](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) لحفظ الحالة الرسومية الحالية.

- استخدم [ConcatenateMatrix operator](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix#a40ca09b1fa45560d57a1fd042d3fbe96) لتحديد مكان وضع الصورة.
- استخدم [المشغل Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do/) لرسم الصورة على الصفحة.
- أخيرًا، استخدم [المشغل GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/) لحفظ الحالة الرسومية المحدثة.
- احفظ الملف.
يوضح المقتطف البرمجي التالي كيفية إضافة الصورة في مستند PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImages::AddImageToExistingPDF()
{
    String _dataDir("C:\\Samples\\");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + u"AddImage.pdf");

    // تعيين الإحداثيات
    int lowerLeftX = 50;
    int lowerLeftY = 750;
    int upperRightX = 100;
    int upperRightY = 800;

    // احصل على الصفحة التي تريد إضافة الصورة إليها
    auto page = document->get_Pages()->idx_get(1);

    // تحميل الصورة في التدفق
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"logo.png");

    // أضف صورة إلى مجموعة الصور لموارد الصفحة
    page->get_Resources()->get_Images()->Add(imageStream);

    // استخدام المشغل GSave: هذا المشغل يحفظ حالة الرسوميات الحالية
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // إنشاء كائنات مستطيل ومصفوفة
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

    auto matrix = MakeObject<Matrix>(
        MakeArray<double>({
            rectangle->get_URX() - rectangle->get_LLX(),
            0,                  0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(), rectangle->get_LLY() }));

    // استخدام مشغل ConcatenateMatrix (دمج المصفوفة):
    // يحدد كيفية وضع الصورة
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

    // استخدام المشغل Do: هذا المشغل يرسم الصورة
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));

    // استخدام المشغل GRestore: هذا المشغل يستعيد حالة الرسوميات
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // احفظ ملف PDF الجديد
    document->Save(_dataDir + u"updated_document.pdf");

    // إغلاق تدفق الصورة
    imageStream->Close();
}
```

## إضافة مرجع لصورة واحدة عدة مرات في مستند PDF

في بعض الأحيان، لدينا متطلبات لاستخدام نفس الصورة عدة مرات في مستند PDF. يؤدي إضافة نسخة جديدة إلى زيادة حجم مستند PDF الناتج. تتيح لك طريقة [XImageCollection.Add(XImage)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image/) إضافة مرجع لنفس كائن PDF كالصورة الأصلية التي تحسن حجم مستند PDF.

```cpp
void WorkingWithImages::AddReferenceOfaSingleImageMultipleTimes() {

    String _dataDir("C:\\Samples\\");
    auto imageRectangle = MakeObject<Rectangle>(0, 0, 30, 15);

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    document->get_Pages()->Add();
    document->get_Pages()->Add();

    auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.png");

    SharedPtr<Aspose::Pdf::XImage> image;

    for (auto page : document->get_Pages()) {
        auto annotation = MakeObject<Aspose::Pdf::Annotations::WatermarkAnnotation>(page, page->get_Rect());
        auto form = annotation->get_Appearance()->idx_get(u"N");
        form->set_BBox(page->get_Rect());
        String name;
        if (image != nullptr) {
            name = form->get_Resources()->get_Images()->Add(imageStream);
            image = form->get_Resources()->get_Images()->idx_get(name);
        }
        else {
            form->get_Resources()->get_Images()->AddWithName(image);
        }
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
        form->get_Contents()->Add(
            MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(
                MakeObject<Matrix>(imageRectangle->get_Width(), 0, 0, imageRectangle->get_Height(), 0, 0)));

        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(name));
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
        page->get_Annotations()->Add(annotation, false);
        imageRectangle = MakeObject<Rectangle>(0, 0, imageRectangle->get_Width() * 1.01, imageRectangle->get_Height() * 1.01);
    }
    document->Save(_dataDir + u"AddReferenceOfaSingleImageMultipleTimes_out.pdf");
}
```

## وضع الصورة على الصفحة والحفاظ على نسبة العرض إلى الارتفاع

إذا لم نكن نعرف أبعاد الصورة، فهناك فرصة كبيرة للحصول على صورة مشوهة على الصفحة. المثال التالي يوضح إحدى الطرق لتجنب هذا.

```cpp
void WorkingWithImages::AddingImageAndPreserveAspectRatioIntoPDF() {

    String _dataDir("C:\\Samples\\");

    auto bitmap = System::Drawing::Image::FromFile(_dataDir + u"3410492.jpg");

    int width;
    int height;

    width = bitmap->get_Width();
    height = bitmap->get_Height();

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page->AddImage(_dataDir + u"3410492.jpg", new Rectangle(10, 10, scaledWidth, scaledHeight));
    document->Save(_dataDir + u"sample_image.pdf");
}
```

## التعرف على ما إذا كانت الصورة داخل PDF ملونة أو بالأبيض والأسود

لتقليل حجم الصورة، تحتاج إلى ضغطها. قبل أن تتمكن من تحديد نوع الضغط لصورة ما، تحتاج إلى معرفة ما إذا كانت ملونة أم بالأبيض والأسود.

يعتمد نوع الضغط المطبق على الصورة على ColorSpace للصورة الأصلية، أي إذا كانت الصورة ملونة (RGB) فاستخدم ضغط JPEG2000، وإذا كانت بالأبيض والأسود فاستخدم ضغط JBIG2 / JBIG2000.

قد يحتوي ملف PDF على عناصر مثل النص، الصورة، الرسم، المرفق، التعليق التوضيحي وغيرها، وإذا كان ملف PDF المصدر يحتوي على صور، يمكننا تحديد مساحة اللون للصورة وتطبيق الضغط المناسب للصورة لتقليل حجم ملف PDF.

يوضح مقتطف الشيفرة التالي الخطوات لتحديد ما إذا كانت الصورة داخل PDF ملونة أم بالأبيض والأسود.

```cpp
void WorkingWithImages::CheckColors() {

    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"test4.pdf");
    try {
        // iterate through all pages of PDF file
        for (auto page : document->get_Pages()) {
            // create Image Placement Absorber instance
            auto abs = MakeObject<ImagePlacementAbsorber>();
            page->Accept(abs);

            for (auto ia : abs->get_ImagePlacements()) {
                /* ColorType */
                auto colorType = ia->get_Image()->GetColorType();
                switch (colorType) {
                case ColorType::Grayscale:
                    Console::WriteLine(u"صورة بالأبيض والأسود");
                    break;
                case ColorType::Rgb:
                    Console::WriteLine(u"صورة ملونة");
                    break;
                }
            }
        }
    }
    catch (Exception ex) {
        Console::WriteLine(u"خطأ في قراءة الملف = {0}", document->get_FileName());
    }
}
```
## التحكم في جودة الصورة

من الممكن التحكم في جودة الصورة التي تتم إضافتها إلى ملف PDF. استخدم طريقة [Replace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection#a698b65051b073f0f4b84b1235889bd72) في فئة [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection).

يوضح مقطع الشيفرة التالي كيفية تحويل جميع صور المستند إلى صيغة JPEG باستخدام جودة 80% للضغط.

```cpp
void WorkingWithImages::ControlImageQuality() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample_with_images.pdf");

    for (auto page : document->get_Pages())
    {
        int idx = 1;
        for (auto image : page->get_Resources()->get_Images())
        {
            auto imageStream = MakeObject<System::IO::MemoryStream>();
            image->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Jpeg());
            page->get_Resources()->get_Images()->Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }

    document->Save(_dataDir + u"sample_with_images_out.pdf");
}
```