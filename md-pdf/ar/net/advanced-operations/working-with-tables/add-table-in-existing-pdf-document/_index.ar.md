---
title: إنشاء أو إضافة جدول في ملف PDF باستخدام C#
linktitle: إنشاء أو إضافة جدول
type: docs
weight: 10
url: /net/add-table-in-existing-pdf-document/
description: Aspose.PDF لـ .NET هي مكتبة تُستخدم لإنشاء وقراءة وتعديل جداول PDF. تحقق من الوظائف المتقدمة الأخرى في هذا الموضوع.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-extract-a-table/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إنشاء أو إضافة جدول في ملف PDF باستخدام C#",
    "alternativeHeadline": "كيفية إضافة جدول في PDF مع .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستند PDF",
    "keywords": "pdf, c#, إنشاء جدول في pdf, إضافة جدول",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق وثائق Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF لـ .NET هي مكتبة تُستخدم لإنشاء وقراءة وتعديل جداول PDF. تحقق من الوظائف المتقدمة الأخرى في هذا الموضوع."
}
</script>
## إنشاء جدول باستخدام C\#

الجداول مهمة عند العمل مع مستندات PDF. إنها توفر ميزات رائعة لعرض المعلومات بطريقة منظمة. تحتوي الفضاء الاسمي Aspose.PDF على فئات تسمى [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table)، [Cell](https://reference.aspose.com/pdf/net/aspose.pdf/cell)، و [Row](https://reference.aspose.com/pdf/net/aspose.pdf/row) التي توفر وظائف لإنشاء جداول عند إنشاء مستندات PDF من البداية.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

يمكن إنشاء الجدول بإنشاء كائن من فئة Table.

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### إضافة جدول في مستند PDF موجود

لإضافة جدول إلى ملف PDF موجود باستخدام Aspose.PDF لـ .NET، اتبع الخطوات التالية:

1. تحميل الملف المصدر.
1. تهيئة جدول وتعيين أعمدته وصفوفه.
1. تعيين إعدادات الجدول (لقد قمنا بتعيين الحدود).
1. ملء الجدول.
1. إضافة الجدول إلى صفحة.
1.
1.

تظهر الأجزاء التالية من الكود كيفية إضافة نص في ملف PDF موجود.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى مجلد الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// تحميل مستند PDF المصدر
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddTable.pdf");
// يبدأ تهيئة نموذج جديد للجدول
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// تعيين لون حدود الجدول كرمادي فاتح
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// تعيين الحدود لخلايا الجدول
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// إنشاء حلقة لإضافة 10 صفوف
for (int row_count = 1; row_count < 10; row_count++)
{
    // إضافة صف إلى الجدول
    Aspose.Pdf.Row row = table.Rows.Add();
    // إضافة خلايا الجدول
    row.Cells.Add("عمود (" + row_count + ", 1)");
    row.Cells.Add("عمود (" + row_count + ", 2)");
    row.Cells.Add("عمود (" + row_count + ", 3)");
}
// إضافة كائن الجدول إلى الصفحة الأولى من المستند الأصلي
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "document_with_table_out.pdf";
// حفظ المستند المحدث الذي يحتوي على كائن الجدول
doc.Save(dataDir);
```
### ColSpan و RowSpan في الجداول

يوفر Aspose.PDF لـ .NET خاصية [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/colspan) لدمج الأعمدة في جدول وخاصية [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf/cell/properties/rowspan) لدمج الصفوف.

نستخدم خاصية `ColSpan` أو `RowSpan` على كائن `Cell` الذي ينشئ خلية الجدول. بعد تطبيق الخصائص المطلوبة، يمكن إضافة الخلية المنشأة إلى الجدول.

```csharp
public static void AddTable_RowColSpan()
{
    // تحميل وثيقة PDF المصدر
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document();
    pdfDocument.Pages.Add();

    // يبدأ إنشاء نموذج جديد للجدول
    Aspose.Pdf.Table table = new Aspose.Pdf.Table
    {
        // تعيين لون حد الجدول باللون الرمادي الفاتح
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black),
        // تعيين حدود لخلايا الجدول
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black)
    };

    // إضافة الصف الأول إلى الجدول
    Aspose.Pdf.Row row1 = table.Rows.Add();
    for (int cellCount = 1; cellCount <5; cellCount++)
    {
        // إضافة خلايا الجدول
        row1.Cells.Add($"Test 1 {cellCount}");
    }

    // إضافة الصف الثاني إلى الجدول
    Aspose.Pdf.Row row2 = table.Rows.Add();
    row2.Cells.Add($"Test 2 1");
    var cell = row2.Cells.Add($"Test 2 2");
    cell.ColSpan = 2;
    row2.Cells.Add($"Test 2 4");

    // إضافة الصف الثالث إلى الجدول
    Aspose.Pdf.Row row3 = table.Rows.Add();
    row3.Cells.Add("Test 3 1");
    row3.Cells.Add("Test 3 2");
    row3.Cells.Add("Test 3 3");
    row3.Cells.Add("Test 3 4");

    // إضافة الصف الرابع إلى الجدول
    Aspose.Pdf.Row row4 = table.Rows.Add();
    row4.Cells.Add("Test 4 1");
    cell = row4.Cells.Add("Test 4 2");
    cell.RowSpan = 2;
    row4.Cells.Add("Test 4 3");
    row4.Cells.Add("Test 4 4");

    // إضافة الصف الخامس إلى الجدول
    row4 = table.Rows.Add();
    row4.Cells.Add("Test 5 1");
    row4.Cells.Add("Test 5 3");
    row4.Cells.Add("Test 5 4");

    // إضافة كائن الجدول إلى الصفحة الأولى من الوثيقة المدخلة
    pdfDocument.Pages[1].Paragraphs.Add(table);

    // حفظ الوثيقة المحدثة التي تحتوي على كائن الجدول
    doc.Save(Path.Combine(_dataDir, "document_with_table_out.pdf"));
}
```
نتيجة تنفيذ الكود أدناه هي الجدول الموضح في الصورة التالية:

![عرض ColSpan و RowSpan](colspan_rowspan.png)

## العمل مع الحدود والهوامش والتبطين

يرجى ملاحظة أنه يدعم أيضًا ميزة تعيين نمط الحدود والهوامش وتبطين الخلايا للجداول. قبل الخوض في التفاصيل التقنية، من المهم فهم مفاهيم الحدود والهوامش والتبطين المقدمة أدناه في الرسم التوضيحي:

![الحدود والهوامش والتبطين](set-border-style-margins-and-padding-of-table_1.png)

في الشكل أعلاه، يمكنك أن ترى أن حدود الجدول والصف والخلية تتداخل. باستخدام Aspose.PDF، يمكن للجدول أن يحتوي على هوامش ويمكن للخلايا أن تحتوي على تبطين. لتعيين هوامش الخلايا، يجب أن نضع تبطين للخلايا.

### الحدود

لتعيين حدود الجدول، [الصف](https://reference.aspose.com/pdf/net/aspose.pdf/row) و [الخلية](https://reference.aspose.com/pdf/net/aspose.pdf/cell)، استخدم خصائص Table.Border، Row.Border و Cell.Border.
لتعيين حدود الجدول، [الصف](https://reference.aspose.com/pdf/net/aspose.pdf/row) و [الخلية](https://reference.aspose.com/pdf/net/aspose.pdf/cell)، استخدم خصائص Table.Border، Row.Border و Cell.Border.

### الهوامش أو الحشوة

يمكن التحكم في حشوة الخلية باستخدام خاصية [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) لفئة الجدول. تُعين جميع خصائص الحشوة لمثيل من فئة [MarginInfo](https://reference.aspose.com/pdf/net/aspose.pdf/margininfo) التي تأخذ معلومات حول المعاملات `Left`، `Right`، `Top` و `Bottom` لإنشاء هوامش مخصصة.

في المثال التالي، يتم ضبط عرض حد الخلية على 0.1 نقطة، وعرض حد الجدول على 1 نقطة وحشوة الخلية على 5 نقاط.

![الهامش والحدود في جدول PDF](margin-border.png)

```csharp
// لأمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// استدعاء كائن الوثيقة بواسطة الاستدعاء الخالي للمنشئ
Document doc = new Document();
Page page = doc.Pages.Add();
// استدعاء كائن الجدول
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// إضافة الجدول إلى مجموعة الفقرات من القسم المطلوب
page.Paragraphs.Add(tab1);
// تعيين عرض الأعمدة للجدول
tab1.ColumnWidths = "50 50 50";
// تعيين حد الخلية الافتراضي باستخدام كائن BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// تعيين حد الجدول باستخدام كائن BorderInfo مخصص آخر
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// إنشاء كائن MarginInfo وتعيين هوامشه اليسرى والسفلى واليمنى والعليا
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// تعيين حشوة الخلية الافتراضية لكائن MarginInfo
tab1.DefaultCellPadding = margin;
// إنشاء صفوف في الجدول ثم خلايا في الصفوف
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add();
TextFragment mytext = new TextFragment("col3 with large text string");
// Row1.Cells.Add("col3 with large text string to be placed inside cell");
row1.Cells[2].Paragraphs.Add(mytext);
row1.Cells[2].IsWordWrapped = false;
// Row1.Cells[2].Paragraphs[0].FixedWidth= 80;
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");
dataDir = dataDir + "MarginsOrPadding_out.pdf";
// حفظ ملف PDF
doc.Save(dataDir);
```
لإنشاء جدول بزوايا مدورة، استخدم قيمة `RoundedBorderRadius` لفئة BorderInfo واضبط نمط زاوية الجدول على الشكل الدائري.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

GraphInfo graph = new GraphInfo();
graph.Color = Aspose.Pdf.Color.Red;
// إنشاء كائن BorderInfo فارغ
BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
// ضبط الحدود لتكون مدورة حيث نصف قطر الدائرة هو 15
bInfo.RoundedBorderRadius = 15;
// ضبط نمط زاوية الجدول على الشكل الدائري.
tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
// تعيين معلومات حدود الجدول
tab1.Border = bInfo;
```

## تطبيق إعدادات AutoFit المختلفة على جدول

عند إنشاء جدول باستخدام وكيل بصري مثل Microsoft Word، ستجد نفسك غالبًا تستخدم أحد خيارات AutoFit لتحجيم الجدول تلقائيًا إلى العرض المطلوب.
عند إنشاء جدول باستخدام وكيل بصري مثل Microsoft Word، ستجد نفسك غالبًا تستخدم أحد خيارات AutoFit لتحجيم الجدول تلقائيًا إلى العرض المطلوب.

بشكل افتراضي يقوم Aspose.Pdf بإدراج جدول جديد باستخدام `ColumnAdjustment` بقيمة `Customized`. سيتم تحجيم الجدول إلى العرض المتاح في الصفحة. لتغيير سلوك التحجيم لهذا الجدول أو جدول موجود يمكنك استدعاء طريقة Table.autoFit(int). تقبل هذه الطريقة تعداد AutoFitBehavior الذي يحدد نوع التحجيم التلقائي المطبق على الجدول.

كما في Microsoft Word، طريقة autofit هي في الواقع اختصار يطبق خصائص مختلفة على الجدول دفعة واحدة. هذه الخصائص هي في الواقع ما تعطي الجدول السلوك الملاحظ. سنناقش هذه الخصائص لكل خيار من خيارات التحجيم التلقائي. سنستخدم الجدول التالي ونطبق إعدادات التحجيم التلقائي المختلفة كعرض توضيحي:

```csharp
// لأمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// استدعاء كائن Pdf بواسطة استدعاء مُنشئه الفارغ
Document doc = new Document();
// إنشاء القسم في كائن Pdf
Page sec1 = doc.Pages.Add();

// توقيع كائن جدول
Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
// إضافة الجدول في مجموعة الفقرات للقسم المطلوب
sec1.Paragraphs.Add(tab1);

// تعيين عرض الأعمدة للجدول
tab1.ColumnWidths = "50 50 50";
tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

// تعيين حد الخلية الافتراضي باستخدام كائن BorderInfo
tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

// تعيين حد الجدول باستخدام كائن BorderInfo مخصص آخر
tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// إنشاء كائن MarginInfo وتعيين الهوامش اليسرى، السفلى، اليمنى والعليا
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;

// تعيين حشوة الخلية الافتراضية لكائن MarginInfo
tab1.DefaultCellPadding = margin;

// إنشاء صفوف في الجدول ثم خلايا في الصفوف
Aspose.Pdf.Row row1 = tab1.Rows.Add();
row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
Aspose.Pdf.Row row2 = tab1.Rows.Add();
row2.Cells.Add("item1");
row2.Cells.Add("item2");
row2.Cells.Add("item3");

dataDir = dataDir + "AutoFitToWindow_out.pdf";
// حفظ الوثيقة المحدثة التي تحتوي على كائن الجدول
doc.Save(dataDir);
```
### الحصول على عرض الجدول

في بعض الأحيان، يتطلب الأمر الحصول على عرض الجدول بشكل ديناميكي. تحتوي فئة Aspose.PDF.Table على طريقة [GetWidth](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/getwidth) لهذا الغرض. على سبيل المثال، لم تقم بتعيين عرض أعمدة الجدول بشكل صريح وقمت بتعيين [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnadjustment) إلى AutoFitToContent. في هذه الحالة، يمكنك الحصول على عرض الجدول كما يلي.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// إنشاء مستند جديد
Document doc = new Document();
// إضافة صفحة إلى المستند
Page page = doc.Pages.Add();
// تهيئة جدول جديد
Table table = new Table
{
    ColumnAdjustment = ColumnAdjustment.AutoFitToContent
};
// إضافة صف في الجدول
Row row = table.Rows.Add();
// إضافة خلية في الجدول
Cell cell = row.Cells.Add("نص الخلية 1");
cell = row.Cells.Add("نص الخلية 2");
// الحصول على عرض الجدول
Console.WriteLine(table.GetWidth());
```

## إضافة صورة SVG إلى خلية الجدول
## إضافة صورة SVG إلى خلية جدول

يدعم Aspose.PDF لـ .NET الميزة لإضافة خلية جدول إلى ملف PDF. عند إنشاء جدول، من الممكن إضافة نص أو صور إلى الخلايا. بالإضافة إلى ذلك، تقدم الواجهة البرمجية أيضًا ميزة تحويل ملفات SVG إلى تنسيق PDF. باستخدام مزيج من هذه الميزات، من الممكن تحميل صورة SVG وإضافتها إلى خلية جدول.

يوضح المقتطف التالي من الشفرة الخطوات لإنشاء مثيل جدول وإضافة صورة SVG داخل خلية جدول.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// توثيق مثيل الكائن
Document doc = new Document();
// إنشاء مثيل صورة
Aspose.Pdf.Image img = new Aspose.Pdf.Image();
// تحديد نوع الصورة كـ SVG
img.FileType = Aspose.Pdf.ImageFileType.Svg;
// مسار لملف المصدر
img.File = dataDir + "SVGToPDF.svg";
// تعيين عرض لمثيل الصورة
img.FixWidth = 50;
// تعيين ارتفاع لمثيل الصورة
img.FixHeight = 50;
// إنشاء مثيل الجدول
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// تعيين عرض لخلايا الجدول
table.ColumnWidths = "100 100";
// إنشاء كائن صف وإضافته إلى مثيل الجدول
Aspose.Pdf.Row row = table.Rows.Add();
// إنشاء كائن خلية وإضافته إلى مثيل الصف
Aspose.Pdf.Cell cell = row.Cells.Add();
// إضافة textfragment إلى مجموعة فقرات كائن الخلية
cell.Paragraphs.Add(new TextFragment("First cell"));
// إضافة خلية أخرى إلى كائن الصف
cell = row.Cells.Add();
// إضافة صورة SVG إلى مجموعة فقرات كائن الخلية المضافة حديثًا
cell.Paragraphs.Add(img);
// إنشاء كائن صفحة وإضافته إلى مجموعة صفحات الكائن المستند
Page page = doc.Pages.Add();
// إضافة الجدول إلى مجموعة فقرات كائن الصفحة
page.Paragraphs.Add(table);

dataDir = dataDir + "AddSVGObject_out.pdf";
// حفظ ملف PDF
doc.Save(dataDir);
```
## استخدام علامات HTML داخل الجدول

أحيانًا قد تحتاج إلى استيراد محتويات قاعدة البيانات التي تحتوي على بعض علامات HTML ثم استيراد المحتوى إلى كائن الجدول. عند استيراد المحتوى، يجب أن يتم تقديم علامات HTML بشكل مناسب داخل مستند PDF. لقد قمنا بتحسين طريقة ImprotDataTable()، من أجل تحقيق مثل هذا الطلب على النحو التالي:

{{% alert color="primary" %}}

يرجى أخذ في الاعتبار أن استخدام علامات HTML داخل عنصر الجدول يزيد من وقت توليد المستند، حيث يحتاج API إلى معالجة علامات HTML بشكل مناسب وتقديمها في مستند PDF الناتج.

{{% /alert %}}

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("data", System.Type.GetType("System.String"));

DataRow dr = dt.NewRow();
dr[0] = "<li>قسم الطب الطارئ: 3400 شارع سبروس الطابق الأرضي مبنى سيلفرستين فيلادلفيا PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>خدمة طب المراقبة في بن: 3400 شارع سبروس الطابق الأرضي دونر فيلادلفيا PA 19104-4206</li>";
dt.Rows.Add(dr);
dr = dt.NewRow();
dr[0] = "<li>UPHS/Presbyterian - قسم الطب الطارئ: 51 شارع 39 شمالاً. فيلادلفيا PA 19104-2640</li>";
dt.Rows.Add(dr);

Document doc = new Document();
doc.Pages.Add();
// يبدأ تهيئة نموذج جديد للجدول
Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
//تعيين عرض الأعمدة للجدول
tableProvider.ColumnWidths = "400 50 ";
// تعيين لون حد الجدول كرمادي فاتح
tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// تعيين الحدود لخلايا الجدول
tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 2.5F;
margin.Left = 2.5F;
margin.Bottom = 1.0F;
tableProvider.DefaultCellPadding = margin;

tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

doc.Pages[1].Paragraphs.Add(tableProvider);
doc.Save(dataDir + "HTMLInsideTableCell_out.pdf");
```
## إدراج فاصل صفحات بين صفوف الجدول

كسلوك افتراضي، عند إنشاء جدول داخل ملف PDF، يتدفق الجدول إلى الصفحات التالية عندما يصل إلى هامش أسفل الجدول. ومع ذلك، قد يكون لدينا متطلب لإدراج فاصل صفحات بالقوة عند إضافة عدد معين من الصفوف للجدول. يوضح الكود التالي الخطوات لإدراج فاصل صفحات عند إضافة 10 صفوف للجدول.

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// توثيق مثال المستند
Document doc = new Document();
// إضافة صفحة إلى مجموعة الصفحات في ملف PDF
doc.Pages.Add();
// إنشاء مثال الجدول
Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
// تعيين نمط الحدود للجدول
tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// تعيين نمط الحدود الافتراضي للجدول مع لون الحدود كأحمر
tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
// تحديد عرض أعمدة الجدول
tab.ColumnWidths = "100 100";
// إنشاء حلقة لإضافة 200 صف للجدول
for (int counter = 0; counter <= 200; counter++)
{
    Aspose.Pdf.Row row = new Aspose.Pdf.Row();
    tab.Rows.Add(row);
    Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
    cell1.Paragraphs.Add(new TextFragment("Cell " + counter + ", 0"));
    row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
    cell2.Paragraphs.Add(new TextFragment("Cell " + counter + ", 1"));
    row.Cells.Add(cell2);
    // عند إضافة 10 صفوف، قم بتقديم صف جديد في صفحة جديدة
    if (counter % 10 == 0 && counter != 0) row.IsInNewPage = true;
}
// إضافة الجدول إلى مجموعة الفقرات في ملف PDF
doc.Pages[1].Paragraphs.Add(tab);

dataDir = dataDir + "InsertPageBreak_out.pdf";
// حفظ مستند PDF
doc.Save(dataDir);
```
## عرض جدول في صفحة جديدة

بشكل افتراضي، يتم إضافة الفقرات إلى مجموعة الفقرات الخاصة بكائن الصفحة. ومع ذلك، من الممكن عرض جدول في صفحة جديدة بدلاً من مباشرة بعد كائن مستوى الفقرة الذي تم إضافته مسبقًا في الصفحة.

### مثال: كيفية عرض جدول في صفحة جديدة باستخدام C\#

لعرض جدول في صفحة جديدة، استخدم خاصية [IsInNewPage](https://reference.aspose.com/pdf/net/aspose.pdf/baseparagraph/properties/isinnewpage) في فئة BaseParagraph. يوضح الكود التالي كيفية القيام بذلك.

```csharp
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

Document doc = new Document();
PageInfo pageInfo = doc.PageInfo;
Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

marginInfo.Left = 37;
marginInfo.Right = 37;
marginInfo.Top = 37;
marginInfo.Bottom = 37;

pageInfo.IsLandscape = true;

Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "50 100";
// تم إضافة صفحة.
Page curPage = doc.Pages.Add();
for (int i = 1; i <= 120; i++)
{
    Aspose.Pdf.Row row = table.Rows.Add();
    row.FixedRowHeight = 15;
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("Content 1"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("HHHHH"));
}
Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
paragraphs.Add(table);
/********************************************/
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table.ColumnWidths = "100 100";
for (int i = 1; i <= 10; i++)
{
    Aspose.Pdf.Row row = table1.Rows.Add();
    Aspose.Pdf.Cell cell1 = row.Cells.Add();
    cell1.Paragraphs.Add(new TextFragment("LAAAAAAA"));
    Aspose.Pdf.Cell cell2 = row.Cells.Add();
    cell2.Paragraphs.Add(new TextFragment("LAAGGGGGG"));
}
table1.IsInNewPage = true;
// أريد الاحتفاظ بالجدول 1 في الصفحة التالية من فضلك...
paragraphs.Add(table1);
dataDir = dataDir + "IsNewPageProperty_Test_out.pdf";
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "مكتبة Aspose.PDF لـ .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "المبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "الإنجليزية"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "دولار أمريكي"
    },
    "applicationCategory": "مكتبة تعديل ملفات PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "ويندوز، ماك أو إس، لينكس",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

