---
title: إنشاء ملف PDF معقد
linktitle: إنشاء ملف PDF معقد
type: docs
weight: 60
url: ar/cpp/complex-pdf-example/
description: يسمح لك Aspose.PDF for C++ بإنشاء مستندات أكثر تعقيدًا تحتوي على صور وقطع نصية وجداول في مستند واحد.
lastmod: "2021-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

أظهر مثال [Hello, World](/pdf/cpp/hello-world-example/) خطوات بسيطة لإنشاء مستند PDF باستخدام C++ وAspose.PDF. في هذه المقالة، سنلقي نظرة على إنشاء مستند أكثر تعقيدًا باستخدام C++ وAspose.PDF for C++. كمثال، سنأخذ مستندًا من شركة وهمية تعمل في خدمات عبّارات الركاب. سيحتوي مستندنا على صورة وقطعتين نصيتين (عنوان وفقرة) وجدول. لبناء مثل هذا المستند، سنستخدم نهجًا قائمًا على DOM. يمكنك قراءة المزيد في قسم [أساسيات واجهة برمجة تطبيقات DOM](/pdf/cpp/basics-of-dom-api/).

إذا أنشأنا مستندًا من البداية، نحتاج إلى اتباع خطوات معينة:

1. Create a [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) لاسم المسار واسم الملف.
1. إنشاء كائن [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). في هذه الخطوة، سنقوم بإنشاء مستند PDF فارغ مع بعض البيانات الوصفية ولكن بدون صفحات.
1. إضافة [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) إلى كائن المستند. الآن، سيكون لدى مستندنا صفحة واحدة.
1. إضافة [Image](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image) إلى الصفحة.
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) للرأس. للرأس، سنستخدم خط Arial بحجم 24pt ومحاذاة في الوسط.
1. إضافة الرأس إلى [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170) الصفحة.
1. 
إنشاء [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) للوصف. للوصف سنستخدم خط Arial بحجم خط 24 نقطة ومحاذاة مركزية.
1. أضف (الوصف) إلى فقرات الصفحة.
1. إنشاء جدول، إضافة خصائص الجدول.
1. أضف (الجدول) إلى [فقرات](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170) الصفحة.
1. احفظ المستند "Complex.pdf".

```cpp
void ExampleComplex()
{
    String outputFileName;

    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String filename("Complex.pdf");

    // Initialize document object
    auto document = MakeObject<Document>();
    // Add page
    auto page = document->get_Pages()->Add();

    // Add image
    String imageFileName = _dataDir + String(u"logo.png");

    // Add image to Images collection of Page Resources
    auto rectangle = MakeObject<Rectangle>(20, 730, 120, 830);
    page->AddImage(imageFileName, rectangle);

    // Add Header
    auto header = MakeObject<TextFragment>(u"مسارات العبّارات الجديدة في خريف 2020");
    auto textFragementState = header->get_TextState();
    textFragementState->set_Font(FontRepository::FindFont(u"Arial"));
    textFragementState->set_FontSize(24);
    header->set_HorizontalAlignment(HorizontalAlignment::Center);
    auto position = MakeObject<Aspose::Pdf::Text::Position>(130, 720);
    header->set_Position(position);
    page->get_Paragraphs()->Add(header);

    // Add description
    String descriptionText(u"يجب على الزوار شراء التذاكر عبر الإنترنت وتقتصر التذاكر على 5,000 يوميًا. تعمل خدمة العبّارات بنصف السعة وبجدول زمني مخفض. توقع الاصطفاف.");
    auto description = MakeObject<TextFragment>(descriptionText);
    description->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    description->get_TextState()->set_FontSize(14);
    description->set_HorizontalAlignment(HorizontalAlignment::Left);
    page->get_Paragraphs()->Add(description);

    // Add table
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"200");

    table->set_Border(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, 1.0f, Aspose::Pdf::Color::get_DarkSlateGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, .5f, Aspose::Pdf::Color::get_Black()));
    table->get_Margin()->set_Bottom(10);
    table->get_DefaultCellTextState()->set_Font(FontRepository::FindFont(u"Helvetica"));

    auto headerRow = table->get_Rows()->Add();
    headerRow->get_Cells()->Add(u"يغادر المدينة");
    headerRow->get_Cells()->Add(u"يغادر الجزيرة");

    for (auto headerRowCell : headerRow->get_Cells())
    {
        headerRowCell->set_BackgroundColor(Color::get_Gray());
        headerRowCell->get_DefaultCellTextState()->set_ForegroundColor(Color::get_WhiteSmoke());
    }

    String arrivals[10] = { u"6:00",u"6:45", u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45" };
    String departures[10] = { u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45", u"11:00", u"11:45" };

    for (int i = 0; i < 10; i++)
    {
        auto dataRow = table->get_Rows()->Add();
        dataRow->get_Cells()->Add(arrivals[i]);
        dataRow->get_Cells()->Add(departures[i]);
    }

    page->get_Paragraphs()->Add(table);

    // Save updated PDF
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```