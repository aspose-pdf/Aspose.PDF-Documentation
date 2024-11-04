---
title: تقديم الجدول من مصدر البيانات
linktitle: تقديم الجدول من مصدر البيانات
type: docs
weight: 30
url: /net/render-table-from-the-data-source/
description: تشرح هذه الصفحة كيفية تقديم الجدول من مصدر البيانات باستخدام مكتبة Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تتيح لك Aspose.PDF إنشاء الجدول باستخدام DataSource من DataSet، Data Table، المصفوفات والكائنات IEnumerable باستخدام فئة PdfLightTable

فئة [Table class](https://reference.aspose.com/pdf/net/aspose.pdf/table) تستخدم لمعالجة الجداول. تمنحنا هذه الفئة القدرة على إنشاء الجداول ووضعها في الوثيقة، باستخدام [Rows](https://reference.aspose.com/pdf/net/aspose.pdf/rows) و [Cells](https://reference.aspose.com/pdf/net/aspose.pdf/cell). لذا، لإنشاء الجدول، تحتاج إلى إضافة العدد المطلوب من الصفوف وملئها بالعدد المناسب من الخلايا.

المثال التالي ينشئ جدول 4x10.

```csharp
var table = new Table
    {
        // تعيين عرض الأعمدة الأوتوماتيكي للجدول
        ColumnWidths = "25% 25% 25% 25%",
        // تعيين تبطين الخلية
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // اليسار الأسفل اليمين الأعلى
        // تعيين لون حد الجدول باللون الأخضر
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // تعيين حد لخلايا الجدول باللون الأسود
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // إضافة صف إلى الجدول
        var row = table.Rows.Add();
        // إضافة خلايا الجدول
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i+1}, {rowCount +1})");
        }
    }
    // إضافة كائن الجدول إلى الصفحة الأولى من الوثيقة
    document.Pages[1].Paragraphs.Add(table);
```
عند تهيئة كائن الجدول، تم استخدام إعدادات الواجهة البسيطة:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - عرض الأعمدة (افتراضيًا);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - الحقول الافتراضية لخلية الجدول؛
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - خصائص إطار الجدول (النمط، السماكة، اللون)؛
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - خصائص إطار الخلية (النمط، السماكة، اللون).

## تصدير البيانات من مصفوفة الكائنات

توفر فئة الجدول طرقًا للتفاعل مع مصادر بيانات ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) و [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).

نظرًا لأن هذه الكائنات ليست مناسبة جدًا للعمل في نموذج MVC، سنقتصر على مثال موجز. في هذا المثال (السطر 50)، يتم استدعاء طريقة ImportDataTable ويتم تلقي كمتغيرات مثيل DataTable وإعدادات إضافية مثل علامة الرأس والموضع الأولي (الصفوف/الأعمدة) لإخراج البيانات.

```csharp
// إنشاء مستند PDF جديد
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// يبدأ تهيئة مثيل جديد للنص لعنوان التقرير
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // تعيين عرض الأعمدة للطاولة
    ColumnWidths = "25% 25% 25% 25%",
    // تعيين حشوة الخلية
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // اليسار الأسفل اليمين الأعلى
    // تعيين لون حد الطاولة كأخضر
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // تعيين الحد لخلايا الطاولة كأسود
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("لا توجد سلسلة اتصال في config.json");

var resultTable = new DataTable();

using (var conn = new SqlConnection(connectionString))
{
    const string sql = "SELECT * FROM Tennats";
    using (var cmd = new SqlCommand(sql, conn))
    {
        using (var adapter = new SqlDataAdapter(cmd))
        {
            adapter.Fill(resultTable);
        }
    }
}

table.ImportDataTable(resultTable,true,1,1);

// إضافة كائن الجدول إلى الصفحة الأولى من المستند المدخل
document.Pages[1].Paragraphs.Add(table);
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "demotable2.pdf"
    };
}
```

