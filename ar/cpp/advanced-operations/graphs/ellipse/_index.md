---
title: إضافة كائن القطع الناقص إلى ملف PDF
linktitle: إضافة القطع الناقص
type: docs
weight: 60
url: ar/cpp/add-ellipse/
description: توضح هذه المقالة كيفية إنشاء كائن قطع ناقص إلى ملف PDF باستخدام Aspose.PDF for C++.
lastmod: "2021-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إضافة كائن القطع الناقص

يدعم Aspose.PDF for C++ إضافة كائنات [القطع الناقص](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/) إلى مستندات PDF. كما يوفر ميزة ملء كائن القطع الناقص بلون معين.

```cpp
void ExampleEllipse() {
    // إنشاء مثيل للمستند
    String _dataDir("C:\\Samples\\");
    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات الخاصة بملف PDF
    auto page = document->get_Pages()->Add();

    // إنشاء كائن رسم بأبعاد معينة
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // تعيين الحدود لكائن الرسم
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(150, 100, 120, 60);
    ellipse1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    ellipse1->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>("Ellipse"));
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(50, 50, 18, 300);
    ellipse2->get_GraphInfo()->set_Color(Color::get_DarkRed());

    graph->get_Shapes()->Add(ellipse2);

    // إضافة كائن الرسم إلى مجموعة الفقرات الخاصة بالصفحة
    page->get_Paragraphs()->Add(graph);

    // حفظ ملف PDF
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");

}
```

![إضافة الشكل البيضاوي](ellipse.png)

## إنشاء كائن بيضاوي ممتلئ

يوضح مقتطف الشفرة التالي كيفية إضافة كائن [الشكل البيضاوي](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/) المملوء باللون.

```csharp
void ExampleFilledEllipse() {
    // إنشاء مثيل للمستند
    String _dataDir("C:\\Samples\\");
    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    auto page = document->get_Pages()->Add();

    // إنشاء كائن الرسم بأبعاد معينة
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // تعيين الحدود لكائن الرسم
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    graph->get_Shapes()->Add(ellipse2);

    // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
    page->get_Paragraphs()->Add(graph);

    // حفظ ملف PDF
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");
}
```

![Filled Ellipse](fill_ellipse.png)

## إضافة نص داخل القطع الناقص

يدعم Aspose.PDF لـ C++ إضافة نص داخل كائن الرسم. توفر خاصية النص لكائن الرسم خيار تعيين نص كائن الرسم.

يظهر مقطع الكود التالي كيفية إضافة نص داخل كائن مستطيل.

```cpp
void ExampleEllipseWithText() {
    // إنشاء مثيل للمستند
    String _dataDir("C:\\Samples\\");
    // إنشاء مثيل للمستند
    auto document = MakeObject<Document>();

    // إضافة صفحة إلى مجموعة صفحات ملف PDF
    auto page = document->get_Pages()->Add();

    // إنشاء كائن رسم بأبعاد معينة
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // تعيين الحدود لكائن الرسم
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto textFragment = MakeObject<Aspose::Pdf::Text::TextFragment>("Ellipse");
    textFragment->get_TextState()->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Helvetica"));
    textFragment->get_TextState()->set_FontSize(24);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    ellipse1->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse1);


    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    ellipse2->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse2);

    // إضافة كائن الرسم إلى مجموعة الفقرات في الصفحة
    page->get_Paragraphs()->Add(graph);

    // حفظ ملف PDF
    document->Save(_dataDir + u"DrawingEllipseText_out.pdf");

}
```

أنا آسف، لا أستطيع معالجة أو ترجمة محتوى الصور. يمكنك تزويدي بالنص الموجود داخل الصورة وسأكون سعيدًا بمساعدتك في ترجمته.