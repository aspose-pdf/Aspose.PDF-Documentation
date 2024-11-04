---
title: إضافة كائن خط إلى ملف PDF
linktitle: إضافة خط
type: docs
weight: 40
url: /cpp/add-line/
description: توضح هذه المقالة كيفية إنشاء كائن خط إلى ملف PDF باستخدام Aspose.PDF for C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة كائن خط

يدعم Aspose.PDF for C++ ميزة إضافة كائنات الرسوم (مثل الرسم، الخط، المستطيل إلخ.) إلى مستندات PDF. يمكنك أيضًا الاستفادة من إضافة كائن [Line](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.line/) حيث يمكنك أيضًا تحديد نمط الشرط، اللون وغيرها من التنسيقات لعنصر الخط.

اتبع الخطوات التالية:

1. إنشاء [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) PDF جديد

1. إضافة [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) إلى مجموعة الصفحات في ملف PDF

1. إنشاء مثيل [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/).

1. إضافة كائن Graph إلى مجموعة الفقرات في مثيل الصفحة.

1. Create [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) instance.

1. ضبط عرض الخط.

1. إضافة كائن [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) إلى مجموعة الأشكال لكائن Graph.

1. احفظ ملف PDF الخاص بك.

يوضح مقطع الشفرة التالي كيفية إضافة كائن [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) مملوء باللون.

```cpp

void AddLineObjectToPDF()
{

String _dataDir("C:\\Samples\\");

// Create Document instance

auto document = MakeObject<Document>();


// Add page to pages collection of PDF file

auto page = document->get_Pages()->Add();


// Create Graph instance

auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);


// Add graph object to paragraphs collection of page instance

page->get_Paragraphs()->Add(graph);


// Create Rectangle instance

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(new float[] { 100, 100, 200, 100 });



// Specify fill color for Graph object

line->get_GraphInfo()->set_DashArray (MakeArray<int>({ 0, 1, 0 }));

line->get_GraphInfo()->set_DashPhase (1);



// Add rectangle object to shapes collection of Graph object

graph->get_Shapes()->Add(line);



// Save PDF file

document->Save(_dataDir + u"AddLineObject_out.pdf");
}

```
![Add Line](add_line.png)

## كيفية إضافة خط متقطع إلى مستند PDF الخاص بك

```cpp
void DashLengthInBlackAndDashLengthInWhite()
{

String _dataDir("C:\\Samples\\");

// انشاء مثيل للمستند

auto document = MakeObject<Document>();


// إضافة صفحة إلى مجموعة صفحات ملف PDF

auto page = document->get_Pages()->Add();


// انشاء كائن الرسم بأبعاد معينة

auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

// إضافة كائن الرسم إلى مجموعة الفقرات في مثيل الصفحة

page->get_Paragraphs()->Add(canvas);



// انشاء كائن الخط

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<float>({ 100, 100, 200, 100 }));

// تعيين اللون لكائن الخط

line->get_GraphInfo()->set_Color (Aspose::Pdf::Color::get_Red());

// تحديد مصفوفة الشرطات لكائن الخط

line->get_GraphInfo()->set_DashArray(MakeArray<int>({ 0, 1, 0 }));

// تعيين المرحلة المتقطعة لمثيل الخط

line->get_GraphInfo()->set_DashPhase(1);

// إضافة الخط إلى مجموعة الأشكال في كائن الرسم

canvas->get_Shapes()->Add(line);


// حفظ ملف PDF

document->Save(_dataDir + u"DashLength_out.pdf");
}
```

دعونا نتحقق من النتيجة:

![Dashed Line](dash_line.png)

## رسم خط عبر الصفحة

يمكننا أيضًا استخدام كائن الخط لرسم تقاطع يبدأ من الزاوية اليسرى السفلية إلى الزاوية اليمنى العليا ومن الزاوية اليسرى العليا إلى الزاوية اليمنى السفلية.

يرجى الاطلاع على مقتطف الشفرة التالي لتحقيق هذا المتطلب.

```cpp
void ExampleLineAcrossPage() {

    // قم بإنشاء مثيل المستند
    String _dataDir("C:\\Samples\\");
    // قم بإنشاء مثيل المستند
    auto document = MakeObject<Document>();
   
    // أضف صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->Add();
    // ضبط هامش الصفحة على جميع الجوانب ليكون 0

    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);

    // قم بإنشاء كائن الرسم البياني مع العرض والارتفاع يساويان أبعاد الصفحة
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(
        page->get_PageInfo()->get_Width(), 
        page->get_PageInfo()->get_Height());

    // قم بإنشاء كائن الخط الأول الذي يبدأ من الزاوية اليسرى السفلية إلى الزاوية اليمنى العليا للصفحة
    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(
        MakeArray<double>({ 
                      page->get_Rect()->get_LLX(), 0, 
                      page->get_PageInfo()->get_Width(),
                      page->get_Rect()->get_URY() }));

    // أضف الخط إلى مجموعة الأشكال في كائن الرسم البياني
    graph->get_Shapes()->Add(line);
    // ارسم خطًا من الزاوية اليسرى العليا للصفحة إلى الزاوية اليمنى السفلية للصفحة
    auto line2 = MakeObject<Aspose::Pdf::Drawing::Line>( MakeArray<double>({0, 
        page->get_Rect()->get_URY(), page->get_PageInfo()->get_Width(), page->get_Rect()->get_LLX() }));

    // أضف الخط إلى مجموعة الأشكال في كائن الرسم البياني
    graph->get_Shapes()->Add(line2);
    // أضف كائن الرسم البياني إلى مجموعة الفقرات في الصفحة
    page->get_Paragraphs()->Add(graph);

    // احفظ ملف PDF
    document->Save(_dataDir + u"DrawingLine_out.pdf");
}
```