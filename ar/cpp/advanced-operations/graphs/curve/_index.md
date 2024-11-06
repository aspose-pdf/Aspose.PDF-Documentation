---
title: إضافة كائن منحنى إلى ملف PDF
linktitle: إضافة منحنى
type: docs
weight: 30
url: ar/cpp/add-curve/
description: تشرح هذه المقالة كيفية إنشاء كائن منحنى إلى ملف PDF الخاص بك باستخدام Aspose.PDF for C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة كائن منحنى

المنحنى [Curve](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.curve/) هو اتحاد متصل لخطوط إسقاطية، كل خط يلتقي بثلاثة خطوط أخرى في نقاط مزدوجة عادية.

تستخدم منحنيات بيزير على نطاق واسع في الرسومات الحاسوبية لنمذجة المنحنيات الناعمة. يتم احتواء المنحنى بالكامل داخل الهيكل المحدب لنقاط التحكم الخاصة به، ويمكن عرض النقاط بيانياً واستخدامها للتلاعب بالمنحنى بشكل بديهي.
يتم احتواء المنحنى بالكامل داخل الرباعي الذي تكون زواياه هي النقاط الأربع المعطاة (هيكلها المحدب).

في هذه المقالة، سنستعرض ببساطة منحنيات الرسوم البيانية، والمنحنيات المملوءة، التي يمكنك إنشاؤها في مستند PDF الخاص بك.

اتبع الخطوات التالية:

1. إنشاء مثيل [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. إنشاء [Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) بأبعاد معينة

1. تعيين [Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) لكائن الرسم

1. إضافة كائن [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) إلى مجموعة الفقرات في الصفحة

1. حفظ ملف PDF الخاص بنا

```cpp
void ExampleCurve() {

    // إنشاء مثيل Document
    String _dataDir("C:\\Samples\\");
    // إنشاء مثيل Document
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->Add();

    // إنشاء كائن رسم بأبعاد معينة
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // تعيين الحدود لكائن الرسم
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double> ({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // إضافة كائن الرسم البياني إلى مجموعة الفقرات في الصفحة
    page->get_Paragraphs()->Add(graph);

    // حفظ ملف PDF
    document->Save(_dataDir + u"DrawingCurve1_out.pdf");
}
```
الصورة التالية توضح النتيجة التي تم تنفيذها باستخدام مقطع الكود الخاص بنا:

![رسم منحنى](drawing_curve.png)

## إنشاء كائن منحنى مملوء

هذا المثال يوضح كيفية إضافة كائن منحنى مملوء بلون.

```cpp
void ExampleFilledCurve() {

    // إنشاء مثيل للمستند
    String _dataDir("C:\\Samples\\");
    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->Add();

    // إنشاء كائن رسم بأبعاد معينة
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // تعيين حدود لكائن الرسم
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double>({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
    page->get_Paragraphs()->Add(graph);

    // حفظ ملف PDF
    document->Save(_dataDir + u"DrawingCurve2_out.pdf");
}
```

انظر إلى نتيجة إضافة منحنى مملوء:

![منحنى مملوء](filled_curve.png)