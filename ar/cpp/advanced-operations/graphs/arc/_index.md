---
title: إضافة كائن قوس إلى ملف PDF
linktitle: إضافة قوس
type: docs
weight: 10
url: /ar/cpp/add-arc/
description: تشرح هذه المقالة كيفية إنشاء كائن قوس إلى ملف PDF باستخدام Aspose.PDF لـ C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة كائن قوس

يدعم Aspose.PDF لـ C++ ميزة إضافة كائنات الرسم (مثل الرسم، الخط، المستطيل إلخ) إلى مستندات PDF. كما يقدم ميزة تعبئة كائن [قوس](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc) بلون معين.

اتبع الخطوات التالية:

1. إنشاء مثيل [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. إنشاء [كائن رسم](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) بأبعاد معينة

1. تعيين [حدود](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) لكائن الرسم

1. أضف كائن [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) إلى مجموعة الفقرات في الصفحة

1. احفظ ملف PDF الخاص بنا

يُظهر مقطع الشيفرة التالي كيفية إضافة كائن [Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc/).

```cpp
void ExampleArc() {
    // إنشاء مثيل لوثيقة
    String _dataDir("C:\\Samples\\");
    // إنشاء مثيل لوثيقة
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->Add();

    // إنشاء كائن رسم بأبعاد معينة
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // تعيين حدود لكائن الرسم
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc1 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc1);

    auto arc2 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 90, 70, 180);
    arc2->get_GraphInfo()->set_Color(Color::get_DarkBlue());
    graph->get_Shapes()->Add(arc2);

    auto arc3 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 85, 120, 210);
    arc3->get_GraphInfo()->set_Color(Color::get_Red());
    graph->get_Shapes()->Add(arc3);

    // إضافة كائن Graph إلى مجموعة الفقرات في الصفحة
    page->get_Paragraphs()->Add(graph);

    // حفظ ملف PDF
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```
## إنشاء كائن قوس مملوء

المثال التالي يوضح كيفية إضافة كائن قوس مملوء باللون وأبعاد معينة.

```cpp
void ExampleFilledArc() {

    // إنشاء مثيل للمستند
    String _dataDir("C:\\Samples\\");
    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->Add();

    // إنشاء كائن رسم بأبعاد معينة
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // تعيين حدود لكائن الرسم
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc);

    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<double>({ 195, 100, 100, 100, 100, 195 }));
    line->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(line);

    // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
    page->get_Paragraphs()->Add(graph);

    // حفظ ملف PDF
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```

Let's see the result of adding a filled Arс:

![قوس ممتلئ](filled_arc.png)