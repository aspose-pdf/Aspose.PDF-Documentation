---
title: تدوير صفحات PDF باستخدام C++
linktitle: تدوير صفحات PDF
type: docs
weight: 50
url: /cpp/rotate-pages/
description: يصف هذا الموضوع كيفية تدوير اتجاه الصفحة في ملف PDF موجود برمجياً باستخدام C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

يصف هذا الموضوع كيفية تحديث أو تغيير اتجاه الصفحات في ملف PDF موجود برمجياً باستخدام C++.

## تغيير اتجاه الصفحة

يسمح لك Aspose.PDF for C++ بتغيير اتجاه الصفحة من أفقي إلى عمودي والعكس صحيح. لتغيير اتجاه الصفحة، قم بتعيين MediaBox للصفحة باستخدام مقطع الكود التالي. يمكنك أيضًا تغيير اتجاه الصفحة عن طريق تعيين زاوية الدوران باستخدام طريقة Rotate().

```cpp
void ChangePageOrientation() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {

        auto r = page->get_MediaBox();
        double newHeight = r->get_Width();
        double newWidth = r->get_Height();
        double newLLX = r->get_LLX();

        // يجب علينا تحريك الصفحة للأعلى لتعويض تغيير حجم الصفحة
        // (حافة الصفحة السفلية هي 0,0 والمعلومات عادة ما توضع من
        // أعلى الصفحة. لهذا السبب نحرك الحافة السفلية للأعلى على الفرق بين
        // الطول القديم والجديد.

        double newLLY = r->get_LLY() + (r->get_Height() - newHeight);
        page->set_MediaBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
        // في بعض الأحيان نحتاج أيضًا إلى تعيين CropBox (إذا تم تعيينه في الملف الأصلي)
        page->set_CropBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

        // تعيين زاوية دوران الصفحة
        page->set_Rotate(Rotation::on90);
    }

    // حفظ الملف الناتج
    document->Save(_dataDir + outputFileName);
}
```

## ملاءمة محتوى الصفحة لتوجه الصفحة الجديد

يرجى ملاحظة أنه عند استخدام جزء الكود أعلاه، قد يتم قطع بعض محتويات المستند لأن ارتفاع الصفحة قد تم تخفيضه. لتجنب ذلك، قم بزيادة العرض بشكل متناسب واترك الارتفاع كما هو. مثال على الحسابات:

```cpp
void FittingPageContentToNewPageOrientation()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {
        auto r = page->get_MediaBox();
        // New height the same
        double newHeight = r->get_Height();
        // New width is expanded proportionally to make orientation landscape
        // (we assume that previous orientation is portrait)
        double newWidth = r->get_Height() * r->get_Height() / r->get_Width();

        // ...

    }
}
```

بجانب النهج أعلاه، فكر في استخدام واجهة PdfPageEditor التي يمكنها تطبيق تكبير على محتويات الصفحة.

```cpp
void ZoomPageContent()
{

    String _dataDir("C:\\Samples\\");
    String inputFileName("ZoomToPageContents.pdf");
    String outputFileName("ZoomToPageContents_out.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // الحصول على المنطقة المستطيلة للصفحة الأولى من ملف PDF
    auto rect = document->get_Pages()->idx_get(1)->get_Rect();

    // إنشاء مثيل PdfPageEditor
    auto ppe = MakeObject<Aspose::Pdf::Facades::PdfPageEditor>();
    // ربط ملف PDF المصدر
    ppe->BindPdf(_dataDir + inputFileName);
    // تعيين معامل التكبير
    ppe->set_Zoom ((float)(rect->get_Width() / rect->get_Height()));
    // تحديث حجم الصفحة
    ppe->set_PageSize(MakeObject<PageSize>((float)rect->get_Height(), (float)rect->get_Width()));

    // حفظ الملف الناتج
    document->Save(_dataDir + outputFileName);
}
```