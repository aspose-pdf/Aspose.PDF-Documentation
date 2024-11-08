---
title: التعليقات اللاصقة في PDF باستخدام ++C
linktitle: التعليق اللاصق
type: docs
weight: 50
url: /ar/cpp/sticky-annotations/
description: هذا الموضوع عن التعليقات اللاصقة، كمثال نعرض تعليق العلامة المائية في النص. يُستخدم لتمثيل الرسوم البيانية على الصفحة. تحقق من مقتطف الكود لحل هذه المهمة.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة تعليق العلامة المائية

يجب استخدام تعليق العلامة المائية لتمثيل الرسوم البيانية التي ستتم طباعتها بحجم وموقع ثابتين على الصفحة، بغض النظر عن أبعاد الصفحة المطبوعة.

يمكنك إضافة نص العلامة المائية باستخدام [WatermarkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.watermark_annotation/) في موضع محدد من صفحة PDF. يمكن أيضًا التحكم في شفافية العلامة المائية باستخدام خاصية الشفافية.

يرجى التحقق من مقتطف الكود التالي لإضافة WatermarkAnnotation.

```cpp
 using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void ExampleWatermarkAnnotation::AddWaterMarkAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    //إنشاء تعليق
    auto wa = MakeObject<WatermarkAnnotation>(page, MakeObject<Rectangle>(100, 500, 400, 600));

    //إضافة التعليق إلى مجموعة التعليقات في الصفحة
    page->get_Annotations()->Add(wa);

    //إنشاء TextState لإعدادات الخط
    auto ts = MakeObject<TextState>();

    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Times New Roman"));
    ts->set_FontSize(32);

    //تعيين مستوى شفافية نص التعليق
    wa->set_Opacity(0.5);

    //إضافة نص إلى التعليق
    wa->SetTextAndState(MakeArray<String>({ u"Aspose.PDF", u"Watermark", u"Demo" }), ts);

    //حفظ المستند
    document->Save(_dataDir + u"sample_watermark.pdf");
}
```

## احصل على تعليق العلامة المائية

يرجى محاولة استخدام مقتطف الشيفرة التالي للحصول على تعليق العلامة المائية من مستند PDF.

```cpp
void ExampleWatermarkAnnotation::GetWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // تصفية التعليقات باستخدام AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // طباعة النتائج
    for (auto wa : watermarkAnnotations) {
        Console::WriteLine(wa->get_Rect());
    }
}
```

## حذف تعليق العلامة المائية

يرجى محاولة استخدام مقتطف الشيفرة التالي لحذف تعليق العلامة المائية من مستند PDF.

```cpp
void ExampleWatermarkAnnotation::DeleteWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // تصفية التعليقات باستخدام AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // حذف التعليقات
    for (auto wa : watermarkAnnotations) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_watermark_del.pdf");
}
```