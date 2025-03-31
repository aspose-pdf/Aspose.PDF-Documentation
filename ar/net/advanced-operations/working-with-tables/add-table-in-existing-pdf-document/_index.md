---
title: إنشاء أو إضافة جدول في PDF باستخدام C#
linktitle: إنشاء أو إضافة جدول
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/add-table-in-existing-pdf-document/
description: Aspose.PDF for .NET هي مكتبة تُستخدم لإنشاء وقراءة وتحرير جداول PDF. تحقق من الوظائف المتقدمة الأخرى في هذا الموضوع.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create or Add Table In PDF using C#",
    "alternativeHeadline": "Add Tables to PDFs Effortlessly with C#",
    "abstract": "تتيح الميزة الجديدة في Aspose.PDF for .NET للمطورين إنشاء وإضافة جداول بسلاسة إلى مستندات PDF الموجودة باستخدام C#. تتضمن هذه الوظيفة ميزات متقدمة مثل الحدود القابلة للتخصيص، وتعبئة الخلايا، ودعم دمج الخلايا باستخدام ColSpan وRowSpan، مما يعزز عرض البيانات في ملفات PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "3283",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET هي مكتبة تُستخدم لإنشاء وقراءة وتحرير جداول PDF. تحقق من الوظائف المتقدمة الأخرى في هذا الموضوع."
}
</script>

## إنشاء جدول باستخدام C\#

الجداول مهمة عند العمل مع مستندات PDF. إنها توفر ميزات رائعة لعرض المعلومات بطريقة منظمة. يحتوي مساحة أسماء Aspose.PDF على فئات تُسمى [Table](https://reference.aspose.com/pdf/ar/net/aspose.pdf/table)، [Cell](https://reference.aspose.com/pdf/ar/net/aspose.pdf/cell)، و[Row](https://reference.aspose.com/pdf/ar/net/aspose.pdf/row) التي توفر وظائف لإنشاء الجداول عند توليد مستندات PDF من الصفر.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

يمكن إنشاء جدول عن طريق إنشاء كائن من فئة Table.

```csharp
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### إضافة جدول في مستند PDF موجود

لإضافة جدول إلى ملف PDF موجود باستخدام Aspose.PDF for .NET، اتبع الخطوات التالية:

1. تحميل الملف المصدر.
1. تهيئة جدول وتعيين أعمدته وصفوفه.
1. تعيين إعدادات الجدول (لقد قمنا بتعيين الحدود).
1. ملء الجدول.
1. إضافة الجدول إلى صفحة.
1. حفظ الملف.

تظهر مقتطفات الكود التالية كيفية إضافة نص في ملف PDF موجود.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTable.pdf"))
    {
        // Initializes a new instance of the Table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        // Set the table border color as LightGray
        table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Set the border for table cells
        table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Create a loop to add 10 rows
        for (int row_count = 1; row_count < 10; row_count++)
        {
            // Add row to table
            Aspose.Pdf.Row row = table.Rows.Add();
            // Add table cells
            row.Cells.Add("Column (" + row_count + ", 1)");
            row.Cells.Add("Column (" + row_count + ", 2)");
            row.Cells.Add("Column (" + row_count + ", 3)");
        }
        // Add table object to first page of input document
        document.Pages[1].Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddTable_out.pdf");
    }
}
```

### ColSpan وRowSpan في الجداول

توفر Aspose.PDF for .NET خاصية [ColSpan](https://reference.aspose.com/pdf/ar/net/aspose.pdf/cell/properties/colspan) لدمج الأعمدة في جدول و[RowSpan](https://reference.aspose.com/pdf/ar/net/aspose.pdf/cell/properties/rowspan) لدمج الصفوف.

نستخدم خاصية `ColSpan` أو `RowSpan` على كائن `Cell` الذي ينشئ خلية الجدول. بعد تطبيق الخصائص المطلوبة، يمكن إضافة الخلية التي تم إنشاؤها إلى الجدول.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTableRowColSpan()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Initializes a new instance of the Table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table
        {
            // Set the table border color as LightGray
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black),
            // Set the border for table cells
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Color.Black)
        };

        // Add 1st row to table
        Aspose.Pdf.Row row1 = table.Rows.Add();
        for (int cellCount = 1; cellCount <5; cellCount++)
        {
            // Add table cells
            row1.Cells.Add($"Test 1 {cellCount}");
        }

        // Add 2nd row to table
        Aspose.Pdf.Row row2 = table.Rows.Add();
        row2.Cells.Add($"Test 2 1");
        var cell = row2.Cells.Add($"Test 2 2");
        cell.ColSpan = 2;
        row2.Cells.Add($"Test 2 4");

        // Add 3rd row to table
        Aspose.Pdf.Row row3 = table.Rows.Add();
        row4.Cells.Add("Test 3 1");
        row4.Cells.Add("Test 3 2");
        row4.Cells.Add("Test 3 3");
        row4.Cells.Add("Test 3 4");

        // Add 4th row to table
        Aspose.Pdf.Row row4 = table.Rows.Add();
        row3.Cells.Add("Test 4 1");
        cell = row3.Cells.Add("Test 4 2");
        cell.RowSpan = 2;
        row3.Cells.Add("Test 4 3");
        row3.Cells.Add("Test 4 4");

        // Add 5th row to table
        row4 = table.Rows.Add();
        row4.Cells.Add("Test 5 1");
        row4.Cells.Add("Test 5 3");
        row4.Cells.Add("Test 5 4");

        // Add table object to first page of input document
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddTableRowColSpan_out.pdf");
    }
}
```

نتيجة تنفيذ الكود أدناه هي الجدول الموضح في الصورة التالية:

![عرض ColSpan وRowSpan](colspan_rowspan.png)

## العمل مع الحدود، الهوامش والتعبئة

يرجى ملاحظة أنه يدعم أيضًا ميزة تعيين نمط الحدود، والهوامش وتعبئة الخلايا للجداول. قبل الخوض في مزيد من التفاصيل الفنية، من المهم فهم مفاهيم الحدود، الهوامش والتعبئة التي تم تقديمها أدناه في رسم بياني:

![الحدود، الهوامش والتعبئة](set-border-style-margins-and-padding-of-table_1.png)

في الشكل أعلاه، يمكنك أن ترى أن حدود الجدول، الصف والخلية تتداخل. باستخدام Aspose.PDF، يمكن أن يحتوي الجدول على هوامش ويمكن أن تحتوي الخلايا على تعبئة. لتعيين هوامش الخلايا، يجب علينا تعيين تعبئة الخلية.

### الحدود

لتعيين حدود الجدول، [Row](https://reference.aspose.com/pdf/ar/net/aspose.pdf/row) و[Cell](https://reference.aspose.com/pdf/ar/net/aspose.pdf/cell) الكائنات، استخدم خصائص Table.Border وRow.Border وCell.Border. يمكن أيضًا تعيين حدود الخلايا باستخدام خاصية DefaultCellBorder لفئة [Table](https://reference.aspose.com/pdf/ar/net/aspose.pdf/table) أو Row. جميع الخصائص المتعلقة بالحدود التي تم مناقشتها أعلاه يتم تعيينها على كائن من فئة Row، التي يتم إنشاؤها عن طريق استدعاء مُنشئها. تحتوي فئة Row على العديد من التحميلات الزائدة التي تأخذ تقريبًا جميع المعلمات المطلوبة لتخصيص الحدود.

### الهوامش أو التعبئة

يمكن إدارة تعبئة الخلايا باستخدام خاصية [DefaultCellPadding](https://reference.aspose.com/pdf/ar/net/aspose.pdf/table/properties/defaultcellpadding) لفئة Table. جميع الخصائص المتعلقة بالتعبئة يتم تعيينها على كائن من فئة [MarginInfo](https://reference.aspose.com/pdf/ar/net/aspose.pdf/margininfo) التي تأخذ معلومات حول معلمات `Left` و`Right` و`Top` و`Bottom` لإنشاء هوامش مخصصة.

في المثال التالي، يتم تعيين عرض حدود الخلية إلى 0.1 نقطة، وعرض حدود الجدول إلى 1 نقطة وتعيين تعبئة الخلية إلى 5 نقاط.

![الهامش والحدود في جدول PDF](margin-border.png)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddMarginsOrPadding()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page page = document.Pages.Add();
        // Instantiate a table object
        Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
        // Add the table in paragraphs collection of the desired section
        page.Paragraphs.Add(tab1);
        // Set with column widths of the table
        tab1.ColumnWidths = "50 50 50";
        // Set default cell border using BorderInfo object
        tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
        // Set table border using another customized BorderInfo object
        tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
        // Create MarginInfo object and set its left, bottom, right and top margins
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 5f;
        margin.Left = 5f;
        margin.Right = 5f;
        margin.Bottom = 5f;
        // Set the default cell padding to the MarginInfo object
        tab1.DefaultCellPadding = margin;
        // Create rows in the table and then cells in the rows
        Aspose.Pdf.Row row1 = tab1.Rows.Add();
        row1.Cells.Add("col1");
        row1.Cells.Add("col2");
        row1.Cells.Add();
        Aspose.Pdf.Text.TextFragment mytext = new Aspose.Pdf.Text.TextFragment("col3 with large text string");
        // Row1.Cells.Add("col3 with large text string to be placed inside cell");
        row1.Cells[2].Paragraphs.Add(mytext);
        row1.Cells[2].IsWordWrapped = false;
        // Row1.Cells[2].Paragraphs[0].FixedWidth= 80;
        Aspose.Pdf.Row row2 = tab1.Rows.Add();
        row2.Cells.Add("item1");
        row2.Cells.Add("item2");
        row2.Cells.Add("item3");
        // Save PDF document
        document.Save(dataDir + "MarginsOrPadding_out.pdf");
    }
}
```

لإنشاء جدول بزاوية مستديرة، استخدم قيمة `RoundedBorderRadius` لفئة BorderInfo وقم بتعيين نمط الزاوية للجدول إلى مستدير.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTableWithRoundCorner()
{
    Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();

    Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
    graph.Color = Aspose.Pdf.Color.Red;
    // Create a blank BorderInfo object
    Aspose.Pdf.BorderInfo bInfo = new Aspose.Pdf.BorderInfo(BorderSide.All, graph);
    // Set the border a rounder border where radius of round is 15
    bInfo.RoundedBorderRadius = 15;
    // Set the table Corner style as Round.
    tab1.CornerStyle = Aspose.Pdf.BorderCornerStyle.Round;
    // Set the table border information
    tab1.Border = bInfo;
}
```

## تطبيق إعدادات AutoFit مختلفة على جدول

عند إنشاء جدول باستخدام وكيل بصري مثل Microsoft Word، ستجد غالبًا نفسك تستخدم أحد خيارات AutoFit لتغيير حجم الجدول تلقائيًا إلى العرض المطلوب. على سبيل المثال، يمكنك استخدام خيار AutoFit to Window لتناسب الجدول مع عرض الصفحة وخيار AutoFit to Contents للسماح لكل خلية بالنمو أو الانكماش لاستيعاب محتوياتها.

بشكل افتراضي، تقوم Aspose.PDF بإدراج جدول جديد باستخدام `ColumnAdjustment` مع قيمة `Customized`. سيقوم الجدول بالتكيف مع العرض المتاح على الصفحة. لتغيير سلوك الحجم على مثل هذا الجدول أو جدول موجود، يمكنك استدعاء طريقة Table.autoFit(int). تقبل هذه الطريقة تعداد AutoFitBehavior الذي يحدد نوع التكيف التلقائي المطبق على الجدول.

كما هو الحال في Microsoft Word، تعتبر طريقة التكيف التلقائي في الواقع اختصارًا يطبق خصائص مختلفة على الجدول دفعة واحدة. هذه الخصائص هي ما يمنح الجدول السلوك الملحوظ. سنناقش هذه الخصائص لكل خيار من خيارات التكيف التلقائي. سنستخدم الجدول التالي ونطبق إعدادات التكيف التلقائي المختلفة كعرض توضيحي:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAutoFitToWindow()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page sec1 = document.Pages.Add();

        // Instantiate a table object
        Aspose.Pdf.Table tab1 = new Aspose.Pdf.Table();
        // Add the table in paragraphs collection of the desired section
        sec1.Paragraphs.Add(tab1);

        // Set with column widths of the table
        tab1.ColumnWidths = "50 50 50";
        tab1.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;

        // Set default cell border using BorderInfo object
        tab1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);

        // Set table border using another customized BorderInfo object
        tab1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
        // Create MarginInfo object and set its left, bottom, right and top margins
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 5f;
        margin.Left = 5f;
        margin.Right = 5f;
        margin.Bottom = 5f;

        // Set the default cell padding to the MarginInfo object
        tab1.DefaultCellPadding = margin;

        // Create rows in the table and then cells in the rows
        Aspose.Pdf.Row row1 = tab1.Rows.Add();
        row1.Cells.Add("col1");
        row1.Cells.Add("col2");
        row1.Cells.Add("col3");
        Aspose.Pdf.Row row2 = tab1.Rows.Add();
        row2.Cells.Add("item1");
        row2.Cells.Add("item2");
        row2.Cells.Add("item3");

        // Save PDF document
        document.Save(dataDir + "AutoFitToWindow_out.pdf");
    }
}
```

### الحصول على عرض الجدول

أحيانًا، يكون من الضروري الحصول على عرض الجدول ديناميكيًا. تحتوي فئة Aspose.PDF.Table على طريقة [GetWidth](https://reference.aspose.com/pdf/ar/net/aspose.pdf/table/methods/getwidth) لهذا الغرض. على سبيل المثال، إذا لم تقم بتعيين عرض أعمدة الجدول بشكل صريح وقمت بتعيين [ColumnAdjustment](https://reference.aspose.com/pdf/ar/net/aspose.pdf/table/properties/columnadjustment) إلى AutoFitToContent. في هذه الحالة، يمكنك الحصول على عرض الجدول كما يلي.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTableWidth()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page page = document.Pages.Add();
        // Initialize new table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table
        {
            ColumnAdjustment = ColumnAdjustment.AutoFitToContent
        };
        // Add row in table
        Aspose.Pdf.Row row = table.Rows.Add();
        // Add cell in table
        Aspose.Pdf.Cell cell = row.Cells.Add("Cell 1 text");
        cell = row.Cells.Add("Cell 2 text");
        // Get table width
        Console.WriteLine(table.GetWidth());
    }
}
```

## إضافة صورة SVG إلى خلية الجدول

تدعم Aspose.PDF for .NET ميزة إضافة خلية جدول إلى ملف PDF. أثناء إنشاء جدول، من الممكن إضافة نص أو صور إلى الخلايا. علاوة على ذلك، تقدم واجهة برمجة التطبيقات أيضًا ميزة تحويل ملفات SVG إلى تنسيق PDF. باستخدام مجموعة من هذه الميزات، من الممكن تحميل صورة SVG وإضافتها إلى خلية جدول.

تظهر مقتطفات الكود التالية خطوات إنشاء مثيل جدول وإضافة صورة SVG داخل خلية جدول.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddSvgObjectToTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create an image instance
        Aspose.Pdf.Image img = new Aspose.Pdf.Image();
        // Set image type as SVG
        img.FileType = Aspose.Pdf.ImageFileType.Svg;
        // Path for source file
        img.File = dataDir + "SVGToPDF.svg";
        // Set width for image instance
        img.FixWidth = 50;
        // Set height for image instance
        img.FixHeight = 50;
        // Create table instance
        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        // Set width for table cells
        table.ColumnWidths = "100 100";
        // Create row object and add it to table instance
        Aspose.Pdf.Row row = table.Rows.Add();
        // Create cell object and add it to row instance
        Aspose.Pdf.Cell cell = row.Cells.Add();
        // Add textfragment to paragraphs collection of cell object
        cell.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("First cell"));
        // Add another cell to row object
        cell = row.Cells.Add();
        // Add SVG image to paragraphs collection of recently added cell instance
        cell.Paragraphs.Add(img);
        // Create page object and add it to pages collection of document instance
        Aspose.Pdf.Page page = document.Pages.Add();
        // Add table to paragraphs collection of page object
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddSVGObjectToTable_out.pdf");
    }
}
```

## استخدام علامات HTML داخل الجدول

أحيانًا قد تواجه متطلبات لاستيراد محتويات قاعدة بيانات تحتوي على بعض علامات HTML ثم استيراد المحتوى إلى كائن الجدول. عند استيراد المحتوى، يجب أن يتم عرض علامات HTML وفقًا لذلك داخل مستند PDF. لقد قمنا بتحسين طريقة ImprotDataTable() لتحقيق مثل هذه المتطلبات كما يلي:

{{% alert color="primary" %}}

يرجى أخذ في الاعتبار أن استخدام علامات HTML داخل عنصر الجدول يزيد من وقت توليد المستند، حيث تحتاج واجهة برمجة التطبيقات إلى معالجة علامات HTML وفقًا لذلك وعرضها في مستند PDF الناتج.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHtmlInsideTableCell()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    DataTable dt = new DataTable("Employee");
    dt.Columns.Add("data", System.Type.GetType("System.String"));

    DataRow dr = dt.NewRow();
    dr[0] = "<li>Department of Emergency Medicine: 3400 Spruce Street Ground Silverstein Bldg Philadelphia PA 19104-4206</li>";
    dt.Rows.Add(dr);
    dr = dt.NewRow();
    dr[0] = "<li>Penn Observation Medicine Service: 3400 Spruce Street Ground Floor Donner Philadelphia PA 19104-4206</li>";
    dt.Rows.Add(dr);
    dr = dt.NewRow();
    dr[0] = "<li>UPHS/Presbyterian - Dept. of Emergency Medicine: 51 N. 39th Street . Philadelphia PA 19104-2640</li>";
    dt.Rows.Add(dr);

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Initializes a new instance of the Table
        Aspose.Pdf.Table tableProvider = new Aspose.Pdf.Table();
        //Set column widths of the table
        tableProvider.ColumnWidths = "400 50 ";
        // Set the table border color as LightGray
        tableProvider.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Set the border for table cells
        tableProvider.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.5F, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 2.5F;
        margin.Left = 2.5F;
        margin.Bottom = 1.0F;
        tableProvider.DefaultCellPadding = margin;

        tableProvider.ImportDataTable(dt, false, 0, 0, 3, 1, true);

        page.Paragraphs.Add(tableProvider);

        // Save PDF document
        document.Save(dataDir + "HTMLInsideTableCell_out.pdf");
    }
}
```

## إدراج فاصل صفحة بين صفوف الجدول

كسلوك افتراضي، عند إنشاء جدول داخل ملف PDF، يتدفق الجدول إلى الصفحات التالية عندما يصل إلى هامش أسفل الجدول. ومع ذلك، قد تكون لدينا متطلبات لإدراج فاصل صفحة بشكل قسري عندما يتم إضافة عدد معين من الصفوف للجدول. تظهر مقتطفات الكود التالية الخطوات لإدراج فاصل صفحة عند إضافة 10 صفوف للجدول.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPageBreak()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create table instance
        Aspose.Pdf.Table tab = new Aspose.Pdf.Table();
        // Set border style for table
        tab.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
        // Set default border style for table with border color as Red
        tab.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Red);
        // Specify table columsn widht
        tab.ColumnWidths = "100 100";
        // Create a loop to add 200 rows for table
        for (int counter = 0; counter <= 200; counter++)
        {
            Aspose.Pdf.Row row = new Aspose.Pdf.Row();
            tab.Rows.Add(row);
            Aspose.Pdf.Cell cell1 = new Aspose.Pdf.Cell();
            cell1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Cell " + counter + ", 0"));
            row.Cells.Add(cell1); Aspose.Pdf.Cell cell2 = new Aspose.Pdf.Cell();
            cell2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Cell " + counter + ", 1"));
            row.Cells.Add(cell2);
            // When 10 rows are added, render new row in new page
            if (counter % 10 == 0 && counter != 0)
            {
                row.IsInNewPage = true;
            }
        }
        // Add table to paragraphs collection of PDF file
        page.Paragraphs.Add(tab);

        // Save PDF document
        document.Save(dataDir + "InsertPageBreak_out.pdf");
    }
}
```

## عرض جدول في صفحة جديدة

بشكل افتراضي، تتم إضافة الفقرات إلى مجموعة الفقرات في كائن الصفحة. ومع ذلك، من الممكن عرض جدول في صفحة جديدة بدلاً من مباشرة بعد كائن فقرة المستوى المضاف سابقًا على الصفحة.

### عينة: كيفية عرض جدول في صفحة جديدة باستخدام C\#

لعرض الجدول في صفحة جديدة، استخدم خاصية [IsInNewPage](https://reference.aspose.com/pdf/ar/net/aspose.pdf/baseparagraph/properties/isinnewpage) في فئة BaseParagraph. تظهر مقتطفات الكود التالية كيفية القيام بذلك.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTableOnNewPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.PageInfo pageInfo = document.PageInfo;
        Aspose.Pdf.MarginInfo marginInfo = pageInfo.Margin;

        marginInfo.Left = 37;
        marginInfo.Right = 37;
        marginInfo.Top = 37;
        marginInfo.Bottom = 37;

        pageInfo.IsLandscape = true;

        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        table.ColumnWidths = "50 100";
        // Add page
        Page curPage = document.Pages.Add();
        for (int i = 1; i <= 120; i++)
        {
            Aspose.Pdf.Row row = table.Rows.Add();
            row.FixedRowHeight = 15;
            Aspose.Pdf.Cell cell1 = row.Cells.Add();
            cell1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Content 1"));
            Aspose.Pdf.Cell cell2 = row.Cells.Add();
            cell2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("HHHHH"));
        }
        Aspose.Pdf.Paragraphs paragraphs = curPage.Paragraphs;
        paragraphs.Add(table);

        Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
        table.ColumnWidths = "100 100";
        for (int i = 1; i <= 10; i++)
        {
            Aspose.Pdf.Row row = table1.Rows.Add();
            Aspose.Pdf.Cell cell1 = row.Cells.Add();
            cell1.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("LAAAAAAA"));
            Aspose.Pdf.Cell cell2 = row.Cells.Add();
            cell2.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("LAAGGGGGG"));
        }
        table1.IsInNewPage = true;
        // Keep table 1 to next page
        paragraphs.Add(table1);
        // Save PDF document
        document.Save(dataDir + "AddTableOnNewPage_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>