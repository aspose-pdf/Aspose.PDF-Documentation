---
title: إنشاء أو إضافة جدول في PDF
linktitle: إنشاء أو إضافة جدول
type: docs
weight: 10
url: /ar/cpp/add-table-in-existing-pdf-document/
description: Aspose.PDF for C++ هي مكتبة تُستخدم لإنشاء وقراءة وتحرير الجداول في PDF. باستخدام هذه المكتبة، يمكنك تقسيم جدول على صفحة PDF باستخدام C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إنشاء جدول باستخدام C++

الجداول مهمة عند العمل مع مستندات PDF. فهي توفر ميزات رائعة لعرض المعلومات بطريقة منظمة.

الجداول في مستند PDF تنظم البيانات في صفوف وأعمدة بطريقة منظمة. يتيح لك Aspose.PDF for C++ API إضافة الجداول إلى مستند PDF، وإضافة الصفوف والأعمدة إليه في تطبيقات C++ الخاصة بك. تُستخدم فئة [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table/) لإضافة جدول إلى المستند. يمكن اتباع الخطوات التالية لإضافة جدول إلى مستند PDF باستخدام C++.

### إضافة جدول في مستند PDF موجود

لإضافة جدول إلى ملف PDF موجود باستخدام Aspose.PDF for C++، اتبع الخطوات التالية:


1. تحميل الملف المصدر.
1. تهيئة جدول وتعيين أعمدته وصفوفه.
1. ضبط إعدادات الجدول (قمنا بتعيين الحدود).
1. ملء الجدول.
1. إضافة الجدول إلى صفحة.
1. حفظ الملف.

توضح مقتطفات الشيفرة التالية كيفية إضافة نص في ملف PDF موجود.

>العناوين

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderCornerStyle.h>
#include <Aspose.PDF.Cpp/Generator/ColumnAdjustment.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/HtmlFragment.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
```
```

>عينة

```cpp
using namespace System;
using namespace Aspose::Pdf;

void AddingTableInExistingPDFDocument() {
    
    String _dataDir("C:\\Samples\\");
    
    // تحميل مستند PDF المصدر
    auto document = MakeObject<Document>(_dataDir + u"AddTable.pdf");
    
    // تهيئة مثيل جديد للجدول
    auto table = MakeObject<Table>();
    
    // تعيين لون حدود الجدول كـ LightGray
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));
    // تعيين الحدود لخلايا الجدول
    table->set_DefaultCellBorder (MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));

    // إنشاء حلقة لإضافة 10 صفوف
    for (int row_count = 1; row_count < 10; row_count++)
    {
        // إضافة صف إلى الجدول
        auto row = table->get_Rows()->Add();
        // إضافة خلايا الجدول
        row->get_Cells()->Add(String::Format(u"عمود ({0}, 1)", row_count));
        row->get_Cells()->Add(String::Format(u"عمود ({0}, 2)", row_count));
        row->get_Cells()->Add(String::Format(u"عمود ({0}, 3)", row_count));
    }

    // إضافة كائن الجدول إلى الصفحة الأولى من المستند المدخل
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    
    // حفظ المستند المحدث الذي يحتوي على كائن الجدول
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

### دمج الأعمدة والصفوف في الجداول

يقدم Aspose.PDF for C++ خاصية [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) لدمج الأعمدة في الجدول وخاصية [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) لدمج الصفوف.

نستخدم خاصية [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) أو [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) على كائن [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell) الذي ينشئ خلية الجدول. بعد تطبيق الخصائص المطلوبة يمكن إضافة الخلية التي تم إنشاؤها إلى الجدول.

```cpp
void AddTable_RowColSpan()
{
    String _dataDir("C:\\Samples\\");

    // Load source PDF document
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    // Initializes a new instance of the Table
    auto table = MakeObject<Table>();
    // Set the table border color as LightGray
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Color::get_Black()));
        // Set the border for table cells
    table->set_DefaultCellBorder(
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, .5f, 
            Color::get_Black()));
    

    // Add 1st row to table
    auto row1 = table->get_Rows()->Add();
    for (int cellCount = 1; cellCount < 5; cellCount++)
    {
        // Add table cells
        row1->get_Cells()->Add(String::Format(u"اختبار 1 {0}", cellCount));
    }

    // Add 2nd row to table
    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"اختبار 2 1");
    auto cell = row2->get_Cells()->Add(u"اختبار 2 2");
    cell->set_ColSpan(2);
    row2->get_Cells()->Add(u"اختبار 2 4");

    // Add 3rd row to table
    auto row3 = table->get_Rows()->Add();
    row3->get_Cells()->Add(u"اختبار 3 1");
    row3->get_Cells()->Add(u"اختبار 3 2");
    row3->get_Cells()->Add(u"اختبار 3 3");
    row3->get_Cells()->Add(u"اختبار 3 4");

    // Add 4th row to table
    auto row4 = table->get_Rows()->Add();
    row4->get_Cells()->Add(u"اختبار 4 1");
    cell = row4->get_Cells()->Add(u"اختبار 4 2");
    cell->set_RowSpan (2);
    row4->get_Cells()->Add(u"اختبار 4 3");
    row4->get_Cells()->Add(u"اختبار 4 4");


    // Add 5th row to table
    auto row5 = table->get_Rows()->Add();
    row5->get_Cells()->Add(u"اختبار 5 1");
    row5->get_Cells()->Add(u"اختبار 5 3");
    row5->get_Cells()->Add(u"اختبار 5 4");

    // Add table object to first page of input document
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);

    // Save updated document containing table object
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

نتيجة تنفيذ الشيفرة أدناه هي الجدول الموضح في الصورة التالية:

![عرض توضيحي لـ ColSpan وRowSpan](colspan_rowspan.png)

## العمل مع الحدود والهوامش والحشوات

لاحظ أنه يدعم أيضًا وظيفة تعيين الحدود، الهوامش وحشوات الخلايا للجدول، دعونا نفهم أولاً مفهوم الحدود، الهوامش والحشوات، والتي يتم تقديمها في الرسم البياني أدناه:

![الحدود، الهوامش والحشوات](set-border-style-margins-and-padding-of-table_1.png)

تحقق من الرسم بالتفصيل. يظهر أن حدود الجدول، الصفوف، والخلايا تتداخل. باستخدام Aspose.PDF for C++ يمكن أن يحتوي الجدول على هوامش ويمكن تقليص الخلايا. لتعيين هوامش الخلية، يجب علينا تعيين حشوة الخلية.

## الحدود

لتعيين حدود كائنات [الجدول](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table)، [الصف](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.row) و[الخلية](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell)، استخدم خصائص Table.Border، Row.Border وCell.Border. حدود الخلايا يمكن تعيينها أيضًا باستخدام خاصية [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) أو خاصية DefaultCellBorder لفئة Row. جميع الخصائص المتعلقة بالحدود التي تم مناقشتها أعلاه يتم تعيينها على مثيل لفئة Row، والتي يتم إنشاؤها عن طريق استدعاء المُنشئ الخاص بها. تحتوي فئة Row على العديد من التحميلات الزائدة التي تأخذ تقريبًا جميع المعلمات المطلوبة لتخصيص الحدود.

## الهوامش أو الحشو

يمكن إدارة حشو الخلايا باستخدام خاصية [DefaultCellPadding](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#ac64196de6dfed7550c3278892ed9dbe0) لفئة Table. جميع الخصائص المتعلقة بالحشو يتم تعيينها إلى مثيل لفئة [MarginInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.margin_info/) التي تأخذ معلومات حول المعلمات `Left`، `Right`، `Top` و `Bottom` لإنشاء هوامش مخصصة.

![الهامش والحدود في جدول PDF](margin-border.png)

```cpp
void AddTable_MergingPadding() {

    String _dataDir("C:\\Samples\\");

    // إنشاء كائن الوثيقة عن طريق استدعاء منشئها الفارغ
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // إنشاء كائن الجدول
    auto tab1 = MakeObject<Table>();
    // إضافة الجدول في مجموعة الفقرات للقسم المطلوب
    page->get_Paragraphs()->Add(tab1);
    // تعيين عرض الأعمدة للجدول
    tab1->set_ColumnWidths (u"50 50 50");
    // تعيين الحدود الافتراضية للخلية باستخدام كائن BorderInfo
    tab1->set_DefaultCellBorder (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 0.1F));
    // تعيين حدود الجدول باستخدام كائن BorderInfo مخصص آخر
    tab1->set_Border (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 1.0F));

    // إنشاء كائن MarginInfo وتعيين الهوامش اليسرى، السفلى، اليمنى والعليا له
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top (5.0f);
    margin->set_Left (5.0f);
    margin->set_Right (5.0f);
    margin->set_Bottom (5.0f);

    // تعيين الحشو الافتراضي للخلية إلى كائن MarginInfo
    tab1->set_DefaultCellPadding (margin);
    // إنشاء الصفوف في الجدول ثم الخلايا في الصفوف
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add();

    auto mytext = MakeObject<Aspose::Pdf::Text::TextFragment>(u"col3 with large text string");
        
    row1->get_Cells()->idx_get(2)->get_Paragraphs()->Add(mytext);
    row1->get_Cells()->idx_get(2)->set_IsWordWrapped(false);
    

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // حفظ ملف Pdf
    document->Save(_dataDir + u"MarginsOrPadding_out.pdf");
}
```
لإنشاء جدول بزوايا مستديرة، استخدم فئة [BorderInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info) القيمة [RoundedBorderRadius](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info#a6a2bed69dd034fba9ce439dcbe1fd3de) وقم بتعيين نمط زاوية الجدول إلى مستدير.

```cpp
void AddTable_RoundedBorderRadius()
{
    // مسار دليل المستندات.
    String _dataDir("C:\\Samples\\");

    auto tab1 = MakeObject<Aspose::Pdf::Table>();

    auto graph = MakeObject<GraphInfo>();
    graph->set_Color(Color::get_Red());
    // إنشاء كائن BorderInfo فارغ
    auto bInfo = MakeObject<BorderInfo>(BorderSide::All, graph);

    // تعيين الحدود كحد مستدير حيث نصف القطر المستدير هو 15
    bInfo->set_RoundedBorderRadius(15);
    // تعيين نمط زاوية الجدول كمستدير.
    tab1->set_CornerStyle (Aspose::Pdf::BorderCornerStyle::Round);
    // تعيين معلومات حدود الجدول
    tab1->set_Border(bInfo);
}
```

### خاصية AutoFitToWindow في تعداد ColumnAdjustmentType

```cpp
void AddTable_AutoFitToWindow() {
    
    // المسار إلى دليل المستندات.
    String _dataDir("C:\\Samples\\");

    // إنشاء كائن Pdf عن طريق استدعاء المنشئ الفارغ
    auto document = MakeObject<Document>();

    // إنشاء القسم في كائن Pdf
    auto sec1 = document->get_Pages()->Add();

    // إنشاء كائن الجدول
    auto tab1 = MakeObject<Aspose::Pdf::Table>();
    // إضافة الجدول في مجموعة الفقرات للقسم المطلوب
    sec1->get_Paragraphs()->Add(tab1);

    // تعيين عرض الأعمدة في الجدول
    tab1->set_ColumnWidths (u"50 50 50");
    tab1->set_ColumnAdjustment (ColumnAdjustment::AutoFitToWindow);

    // تعيين حدود الخلية الافتراضية باستخدام كائن BorderInfo
    tab1->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 0.1F));

    // تعيين حدود الجدول باستخدام كائن BorderInfo مخصص آخر
    tab1->set_Border (MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 1.0F));

    // إنشاء كائن MarginInfo وتعيين الهوامش اليسرى والسفلية واليمنى والعلوية
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top(5.0f);
    margin->set_Left(5.0f);
    margin->set_Right(5.0f);
    margin->set_Bottom(5.0f);

    // تعيين حشو الخلية الافتراضي إلى كائن MarginInfo
    tab1->set_DefaultCellPadding(margin);

    // إنشاء صفوف في الجدول ثم خلايا في الصفوف
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // حفظ المستند المحدث الذي يحتوي على كائن الجدول
    document->Save(_dataDir + u"AutoFitToWindow_out.pdf");
}
```

### الحصول على عرض الجدول

هناك مهام تحتاج فيها إلى الحصول ديناميكيًا على عرض الجدول. تحتوي فئة [Aspose.PDF.Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) على طريقة [GetWidth] (https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#a3361cc8d4af87eec2e3da616c474ac1c) لهذا الغرض. على سبيل المثال، لم تقم بتعيين عرض أعمدة الجدول بشكل صريح، ولم تقم بتعيين [ColumnAdjustment] (https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#afc01382935026dd569c96d77d09dc3a4) إلى AutoFitToContent. في هذه الحالة، يمكنك الحصول على عرض الجدول التالي.

```cpp
void GetTableWidth() {
    // إنشاء مستند جديد
    auto document = MakeObject<Document>();
    
    // إضافة صفحة في المستند
    auto page = document->get_Pages()->Add();

    // تهيئة جدول جديد
    auto table = MakeObject<Table>();
    table->set_ColumnAdjustment(ColumnAdjustment::AutoFitToContent);
    
    // إضافة صف في الجدول
    auto row = table->get_Rows()->Add();

    // إضافة خلية في الجدول
    auto cell = row->get_Cells()->Add(u"Cell 1 text");
    cell = row->get_Cells()->Add(u"Cell 2 text");
    // الحصول على عرض الجدول
    Console::WriteLine(table->GetWidth());
}
```

## إضافة صورة SVG إلى خلية جدول

يسمح Aspose.PDF لـ C++ بإضافة خلايا الجدول إلى ملف PDF. عند إنشاء جدول، يمكنك إضافة نص أو صور إلى الخلايا. بالإضافة إلى ذلك، يوفر الـ API ميزة لتحويل ملفات SVG إلى PDF. باستخدام مزيج من هذه الوظائف، من الممكن تحميل صورة SVG وإضافتها إلى خلية جدول.

يُظهر المقتطف البرمجي التالي الخطوات اللازمة لإنشاء جدول وإضافة صورة SVG إلى خلية جدول.

```cpp
void InsertSVGObject() 
{
    String _dataDir("C:\\Samples\\");

    // Instantiate Document object
    auto document = MakeObject<Document>();
    // Create an image instance
    auto img = MakeObject<Aspose::Pdf::Image>();

    // Set image type as SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Svg);
    // Path for source file
    img->set_File (_dataDir + u"SVGToPDF.svg");
    // Set width for image instance
    img->set_FixWidth (50);
    // Set height for image instance
    img->set_FixHeight(50);
    // Create table instance
    auto table = MakeObject<Aspose::Pdf::Table>();
    // Set width for table cells
    table->set_ColumnWidths (u"100 100");
    // Create row object and add it to table instance
    auto row = table->get_Rows()->Add();
    // Create cell object and add it to row instance
    auto cell = row->get_Cells()->Add();
    // Add textfragment to paragraphs collection of cell object
    cell->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"First cell"));
    // Add another cell to row object
    cell = row->get_Cells()->Add();
    // Add SVG image to paragraphs collection of recently added cell instance
    cell->get_Paragraphs()->Add(img);
    // Create page object and add it to pages collection of document instance
    auto page = document->get_Pages()->Add();
    // Add table to paragraphs collection of page object
    page->get_Paragraphs()->Add(table);    
    // Save PDF file
    document->Save(_dataDir + u"AddSVGObject_out.pdf");
}
```

## استخدام علامات HTML داخل الجدول

بالنسبة لبعض المهام، ستحتاج إلى استيراد محتوى قاعدة البيانات مع بعض علامات HTML ثم استيراد المحتوى إلى كائن الجدول. عند استيراد المحتوى، يجب عرض علامات HTML داخل مستند PDF.

في مقتطف الشيفرة التالي، يمكنك تعيين لون حدود الجدول، وتعيين الحدود لخلايا الجدول. بعد ذلك، ستقوم بإنشاء حلقة لإضافة 10 صفوف. أضف كائن الجدول إلى الصفحة الأولى من مستند الإدخال واحفظ المستند المحدث.

```cpp
void AddHTMLFragmentToTableCell() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");    
    // Initializes a new instance of the Table
    auto table = MakeObject<Table>();
    // Set the table border color as LightGray
    table->set_Border(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // set the border for table cells
    table->set_DefaultCellBorder(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // create a loop to add 10 rows       
    for (int row_count = 1; row_count < 10; row_count++) {
        SmartPtr<Cell> cell;
        // add row to table
        auto row = table->get_Rows()->Add();
        // add table cells
        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Column <strong>({0}, 1)</strong>", row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Column <span style='color:red'>({0}, 2)</span>",row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Column <span style='text-decoration: underline'>([0}, 3)</span>", row_count)));
    }
    // Add table object to first page of input document
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    // Save updated document containing table object
    document->Save(_dataDir + u"AddHTMLObject_out.pdf");
}
```

## إدراج فاصل صفحة بين صفوف الجدول

عادةً، عند إنشاء جدول داخل ملف PDF، يمتد الجدول إلى الصفحات التالية عندما يصل إلى هامش الجدول السفلي. ولكن قد يكون لدينا متطلب لإجبار إدراج فاصل صفحة عندما يتم إضافة عدد معين من الصفوف إلى الجدول. يُظهر المقتطف البرمجي التالي الخطوات لإدراج فاصل صفحة أثناء إضافة 10 صفوف إلى الجدول.

يُظهر المقتطف البرمجي التالي الخطوات لإدراج فاصل صفحة عندما يتم إضافة 10 صفوف إلى الجدول.

```cpp
void InsertPageBreak() {
    String _dataDir("C:\\Samples\\");

    // Instantiate Document instance
    auto document = MakeObject<Document>();
    
    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    // Create table instance
    auto tab = MakeObject<Table>();

    // Set border style for table
    tab->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // Set default border style for table with border color as Red
    tab->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // Specify table columsn widht
    tab->set_ColumnWidths(u"100 100");

    // Create a loop to add 200 rows for table
    for (int counter = 0; counter <= 200; counter++) {
        auto row = MakeObject<Row>();
        tab->get_Rows()->Add(row);
        auto cell1 = MakeObject<Cell>();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 0", counter)));
        row->get_Cells()->Add(cell1);

        auto cell2 = new Cell();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 1", counter)));
        row->get_Cells()->Add(cell2);
        // When 10 rows are added, render new row in new page
        if (counter % 10 == 0 && counter != 0)
            row->set_IsInNewPage(true);
    }
    // Add table to paragraphs collection of PDF file
    page->get_Paragraphs()->Add(tab);

    // Save the PDF document
    document->Save(_dataDir + u"InsertPageBreak_out.pdf");
}
```

## عرض جدول في صفحة جديدة

افتراضيًا، يتم إضافة الفقرات إلى مجموعة الفقرات في كائن الصفحة. ومع ذلك، من الممكن عرض جدول في صفحة جديدة بدلاً من العرض مباشرة بعد الكائن على مستوى الفقرة المضاف سابقًا في الصفحة.

### مثال: كيفية عرض جدول في صفحة جديدة باستخدام C++

لعرض الجدول في صفحة جديدة، استخدم خاصية [IsInNewPage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph#a614946048d22afb9dce4cd42346c7561) في فئة [BaseParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph).
يظهر مقطع الكود التالي كيفية ذلك.

```cpp
void RenderTableOnNewPage()
{
    auto document = MakeObject<Document>();
    auto pageInfo = document->get_PageInfo();
    auto marginInfo = pageInfo->get_Margin();

    marginInfo->set_Left (37);
    marginInfo->set_Right (37);
    marginInfo->set_Top (37);
    marginInfo->set_Bottom (37);

    pageInfo->set_IsLandscape(true);

    auto table = MakeObject<Aspose::Pdf::Table>();
    table->set_ColumnWidths(u"50 100");
    // Added page.
    auto curPage = document->get_Pages()->Add();
    for (int i = 1; i <= 120; i++)
    {
        auto row = table->get_Rows()->Add();
        row->set_FixedRowHeight(15);
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Content 1"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"HHHHH"));
    }
    auto paragraphs = curPage->get_Paragraphs();
    paragraphs->Add(table);

    //-------------------------------------

    auto document = MakeObject<Document>();
    auto table1 = MakeObject<Aspose::Pdf::Table>();
    table1->set_ColumnWidths(u"100 100");

    String _dataDir("C:\\Samples\\");

    for (int i = 1; i <= 10; i++)
    {
        auto row = table1->get_Rows()->Add();
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAAAAAA"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAGGGGGG"));
    }
    
    table1->set_IsInNewPage (true);
    // I want to keep table 1 to next page please...
    paragraphs->Add(table1);
    
    document->Save(_dataDir + u"IsNewPageProperty_Test_out.pdf");
}
```