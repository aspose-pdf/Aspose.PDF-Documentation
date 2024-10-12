---
title: استخراج الصور من ملف PDF باستخدام C++
linktitle: استخراج الصور
type: docs
weight: 30
url: /cpp/extract-images-from-pdf-file/
description: يوضح هذا القسم كيفية استخراج الصور من ملف PDF باستخدام مكتبة C++.
lastmod: "2021-12-18"
---

يمكنك استخدام Aspose.PDF for C++ لاستخراج جميع الصور من مستندات PDF الخاصة بك إلى ملفات منفصلة يمكن إعادة استخدامها في برامج أخرى.

تُحفظ الصور في مجموعة Resources الخاصة بكل صفحة في مجموعة Images. لاستخراج صفحة معينة، ثم الحصول على الصورة من مجموعة Images باستخدام الفهرس الخاص بالصورة.

يعيد فهرس الصورة كائن [XImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image). يوفر هذا الكائن طريقة Save التي يمكن استخدامها لحفظ الصورة المستخرجة.

يوضح مقتطف الشيفرة التالي كيفية استخراج الصور من ملف PDF.

```cpp
void WorkingWithImages::ExtractImages()
{
    String _dataDir("C:\\Samples\\");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + u"ExtractImages.pdf");

    // استخراج صورة معينة
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + u"output.jpg");

    // حفظ الصورة المستخرجة
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    // حفظ ملف PDF المحدث
    document->Save(_dataDir + u"ExtractImages_out.pdf");
}
```