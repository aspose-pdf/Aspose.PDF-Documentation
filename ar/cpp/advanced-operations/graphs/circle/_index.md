---
title: إضافة كائن دائرة إلى ملف PDF
linktitle: إضافة دائرة
type: docs
weight: 20
url: /ar/cpp/add-circle/
description: تشرح هذه المقالة كيفية إنشاء كائن دائرة إلى ملف PDF باستخدام Aspose.PDF لـ C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة كائن دائرة

مثل الرسوم البيانية الشريطية، يمكن استخدام الرسوم البيانية الدائرية لعرض البيانات في عدد من الفئات المنفصلة. ومع ذلك، بخلاف الرسوم البيانية الشريطية، يمكن استخدام الرسوم البيانية الدائرية فقط عندما يكون لديك بيانات لجميع الفئات التي تشكل الكل. لذا دعونا نلقي نظرة على إضافة كائن [دائرة](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.circle/) باستخدام Aspose.PDF لـ C++.

اتبع الخطوات أدناه:

1. إنشاء مثيل [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. إنشاء [كائن رسم](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) بأبعاد معينة

1. تعيين [حدود](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) لكائن الرسم

1. إضافة كائن [الرسم](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) إلى مجموعة الفقرات في الصفحة

1. حفظ ملف PDF الخاص بنا

```cpp
void ExampleCircle() {

    // إنشاء مثيل للمستند
    String _dataDir("C:\\Samples\\");
    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات لملف PDF
    auto page = document->get_Pages()->Add();

    // إنشاء كائن رسم بأبعاد معينة
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    // تعيين حدود لكائن الرسم
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);

    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(circle);

    // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
    page->get_Paragraphs()->Add(graph);

    // حفظ ملف PDF
    document->Save(_dataDir + u"DrawingCircle1_out.pdf");
}
```
دائرتنا المرسومة ستبدو هكذا:

![رسم دائرة](drawing_circle.png)

## إنشاء كائن دائرة ممتلئة

يوضح هذا المثال كيفية إضافة كائن دائرة ممتلئ باللون.

```cpp
void ExampleFilledCircle() {
    // إنشاء مثيل للمستند
    String _dataDir("C:\\Samples\\");
    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->Add();

    // إنشاء كائن رسم بأبعاد معينة
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // تعيين الحدود لكائن الرسم
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);
    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    circle->get_GraphInfo()->set_FillColor(Color::get_Green());

    circle->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>(u"دائرة"));

    graph->get_Shapes()->Add(circle);

    // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
    page->get_Paragraphs()->Add(graph);

    // حفظ ملف PDF
    document->Save(_dataDir + u"DrawingCircle2_out.pdf");
}
```

Let's see the result of adding a filled Circle:

![الدائرة المملوءة](filled_circle.png)