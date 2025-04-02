---
title: عرض جدول باستخدام Entity Framework
linktitle: عرض جدول باستخدام Entity Framework
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/render-table-using-entity-framework-model-as-data-source/
description: ستوضح لك هذه المقالة كيفية عرض جدول باستخدام نموذج Entity Framework كمصدر بيانات باستخدام Aspose.PDF for .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Render table with Entity Framework",
    "alternativeHeadline": "Render PDF from Entity Framework Data Easily",
    "abstract": "تقديم ميزة جديدة تسمح بعرض الجداول بسلاسة مباشرة من نماذج Entity Framework إلى مستندات PDF باستخدام Aspose.PDF for .NET. تبسط هذه الوظيفة تصور البيانات من خلال تمكين المستخدمين من استيراد البيانات من أطر ORM بكفاءة، مما يخلق جداول منظمة جيدًا مع سمات وخيارات تنسيق قابلة للتخصيص. عزز قدرات التقارير الخاصة بك مع هذا التكامل القوي، مما يوفر مخرجات PDF نظيفة واحترافية دون الحاجة إلى تحويلات قائمة على HTML.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1540",
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
    "url": "/net/render-table-using-entity-framework-model-as-data-source/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/render-table-using-entity-framework-model-as-data-source/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

هناك عدد من المهام عندما يكون من الأكثر ملاءمة تصدير البيانات من قواعد البيانات إلى مستند PDF دون استخدام مخطط تحويل HTML إلى PDF الشائع مؤخرًا.

ستوضح لك هذه المقالة كيفية إنشاء مستند PDF باستخدام Aspose.PDF for .NET.

## أساسيات توليد PDF باستخدام Aspose.PDF

واحدة من أهم الفئات في Aspose.PDF هي [فئة Document](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document). هذه الفئة هي محرك عرض PDF. لعرض هيكل PDF، تستخدم مكتبة Aspose.PDF نموذج Document-Page، حيث:

* Document - يحتوي على خصائص مستند PDF بما في ذلك مجموعة الصفحات.
* Page - يحتوي على خصائص صفحة معينة ومجموعات متنوعة من العناصر المرتبطة بهذه الصفحة.

لذلك، لإنشاء مستند PDF باستخدام Aspose.PDF، يجب عليك اتباع هذه الخطوات:

1. إنشاء كائن Document.
1. إضافة الصفحة (كائن Page) لكائن Document.
1. إنشاء كائنات توضع على الصفحة (مثل جزء نص، جدول، إلخ).
1. إضافة العناصر التي تم إنشاؤها إلى المجموعة المقابلة على الصفحة (في حالتنا ستكون مجموعة الفقرات).
1. حفظ المستند كملف PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document
           {
               PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
           })
    {
        // Add page
        var page = document.Pages.Add();

        var textFragment = new Aspose.Pdf.Text.TextFragment(reportTitle);

        var table = new Aspose.Pdf.Table
        {
            // .................................
        };

        page.Paragraphs.Add(textFragment);
        page.Paragraphs.Add(table);

        using (var streamOut = new MemoryStream())
        {
            // Save PDF document
            document.Save(streamOut);

            return new FileContentResult(streamOut.ToArray(), "application/pdf")
            {
                FileDownloadName = "tenants.pdf"
            };
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using var document = new Aspose.Pdf.Document
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    };

    // Add page
    var page = document.Pages.Add();

    var textFragment = new Aspose.Pdf.Text.TextFragment(reportTitle);

    var table = new Aspose.Pdf.Table
    {
        // .................................
    };

    page.Paragraphs.Add(textFragment);
    page.Paragraphs.Add(table);

    using var streamOut = new MemoryStream();

    // Save PDF document
    document.Save(streamOut);

    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
{{< /tab >}}
{{< /tabs >}}

المشكلة الأكثر شيوعًا هي إخراج البيانات في تنسيق جدول. تُستخدم [فئة Table](https://reference.aspose.com/pdf/ar/net/aspose.pdf/table) لمعالجة الجداول. تمنحنا هذه الفئة القدرة على إنشاء جداول ووضعها في المستند، باستخدام [Rows](https://reference.aspose.com/pdf/ar/net/aspose.pdf/rows) و [Cells](https://reference.aspose.com/pdf/ar/net/aspose.pdf/cell). لذا، لإنشاء الجدول، تحتاج إلى إضافة العدد المطلوب من الصفوف وملئها بالعدد المناسب من الخلايا.

المثال التالي ينشئ الجدول 4x10.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        var table = new Aspose.Pdf.Table
        {
            // Set column auto widths of the table
            ColumnWidths = "25% 25% 25% 25%",

            // Set cell padding
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top

            // Set the table border color as Green
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),

            // Set the border for table cells as Black
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
        };

        for (var rowCount = 0; rowCount < 10; rowCount++)
        {
            // Add row to table
            var row = table.Rows.Add();

            // Add table cells
            for (int i = 0; i < 4; i++)
            {
                row.Cells.Add($"Cell ({i + 1}, {rowCount + 1})");
            }
        }

        // Add table object to first page of input document
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddTable_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page
    var page = document.Pages.Add();

    var table = new Aspose.Pdf.Table
    {
        // Set column auto widths of the table
        ColumnWidths = "25% 25% 25% 25%",

        // Set cell padding
        DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top

        // Set the table border color as Green
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),

        // Set the border for table cells as Black
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
    };

    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // Add row to table
        var row = table.Rows.Add();

        // Add table cells
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i + 1}, {rowCount + 1})");
        }
    }

    // Add table object to first page of input document
    page.Paragraphs.Add(table);

    // Save PDF document
    document.Save(dataDir + "AddTable_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

عند تهيئة كائن Table، تم استخدام إعدادات الحد الأدنى للواجهة:

* [ColumnWidths](https://reference.aspose.com/pdf/ar/net/aspose.pdf/table/properties/columnwidths) - عرض الأعمدة (بشكل افتراضي).
* [DefaultCellPadding](https://reference.aspose.com/pdf/ar/net/aspose.pdf/table/properties/defaultcellpadding) - الحقول الافتراضية لخلايا الجدول.
* [Border](https://reference.aspose.com/pdf/ar/net/aspose.pdf/table/properties/border) - سمات إطار الجدول (النمط، السماكة، اللون).
* [DefaultCellBorder](https://reference.aspose.com/pdf/ar/net/aspose.pdf/table/properties/defaultcellborder) - سمات إطار الخلية (النمط، السماكة، اللون).

نتيجة لذلك، نحصل على الجدول 4x10 مع أعمدة ذات عرض متساوي.

![جدول 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## تصدير البيانات من كائنات ADO.NET

توفر فئة Table طرقًا للتفاعل مع مصادر بيانات ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/ar/net/aspose.pdf.table/importdatatable/methods/1) و [ImportDataView](https://reference.aspose.com/pdf/ar/net/aspose.pdf/table/methods/importdataview). تستورد الطريقة الأولى البيانات من DataTable، والثانية من DataView.
مفترضين أن هذه الكائنات ليست مريحة جدًا للعمل في قالب MVC، سنقتصر على مثال موجز. في هذا المثال (السطر 50)، يتم استدعاء طريقة ImportDataTable وتستقبل كمعلمات مثيل DataTable وإعدادات إضافية مثل علامة الرأس والموقع الأولي (صفوف/أعمدة) لإخراج البيانات.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    })
    {
        var table = new Aspose.Pdf.Table
        {
            // Set column widths of the table
            ColumnWidths = "25% 25% 25% 25%",
            // Set cell padding
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top
            // Set the table border color as Green
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),
            // Set the border for table cells as Black
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
        };

        var configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("config.json", false)
            .Build();

        var connectionString = configuration.GetSection("connectionString").Value;

        if (string.IsNullOrEmpty(connectionString))
        {
            throw new ArgumentException("No connection string in config.json");
        }

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

        table.ImportDataTable(resultTable, true, 1, 1);

        // Add table object to first page of input document
        document.Pages[1].Paragraphs.Add(table);

        using (var streamOut = new MemoryStream())
        {
            // Save PDF document
            document.Save(streamOut);

            return new FileContentResult(streamOut.ToArray(), "application/pdf")
            {
                FileDownloadName = "demotable2.pdf"
            };
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTable()
{
    // Create PDF document
    using var document = new Aspose.Pdf.Document
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    };

    var table = new Aspose.Pdf.Table
    {
        // Set column widths of the table
        ColumnWidths = "25% 25% 25% 25%",
        // Set cell padding
        DefaultCellPadding = new Aspose.Pdf.MarginInfo(10, 5, 10, 5), // Left Bottom Right Top
        // Set the table border color as Green
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.Green),
        // Set the border for table cells as Black
        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .2f, Aspose.Pdf.Color.Green),
    };

    var configuration = new ConfigurationBuilder()
        .SetBasePath(Directory.GetCurrentDirectory())
        .AddJsonFile("config.json", false)
        .Build();

    var connectionString = configuration.GetSection("connectionString").Value;

    if (string.IsNullOrEmpty(connectionString))
    {
        throw new ArgumentException("No connection string in config.json");
    }

    var resultTable = new DataTable();

    using var conn = new SqlConnection(connectionString);

    const string sql = "SELECT * FROM Tennats";

    using var cmd = new SqlCommand(sql, conn);

    using var adapter = new SqlDataAdapter(cmd);
    
    adapter.Fill(resultTable);

    table.ImportDataTable(resultTable, true, 1, 1);

    // Add table object to first page of input document
    document.Pages[1].Paragraphs.Add(table);

    using var streamOut = new MemoryStream();
    
    // Save PDF document
    document.Save(streamOut);

    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        PageInfo = new Aspose.Pdf.PageInfo { Margin = new Aspose.Pdf.MarginInfo(28, 28, 28, 42) }
    };
}
```
{{< /tab >}}
{{< /tabs >}}

## تصدير البيانات من Entity Framework

الأكثر صلة بـ .NET الحديثة هو استيراد البيانات من أطر ORM. في هذه الحالة، من الجيد توسيع فئة Table مع طرق إضافية لاستيراد البيانات من قائمة بسيطة أو من البيانات المجمعة. دعونا نقدم مثالاً لأحد أشهر أطر ORM - Entity Framework.

```csharp
public static class PdfHelper
{
    private static void ImportEntityList<TSource>(this Aspose.Pdf.Table table, IList<TSource> data)
    {
        var headRow = table.Rows.Add();

        var props = typeof(TSource).GetProperties(BindingFlags.Public | BindingFlags.Instance);
        foreach (var prop in props)
        {
            headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);
        }

        foreach (var item in data)
        {
            // Add row to table
            var row = table.Rows.Add();
            // Add table cells
            foreach (var t in props)
            {
                var dataItem = t.GetValue(item, null);
                if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                    switch (dataType.DataType)
                    {

                        case DataType.Currency:
                            row.Cells.Add(string.Format("{0:C}", dataItem));
                            break;
                        case DataType.Date:
                            var dateTime = (DateTime)dataItem;
                            if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                            {
                                row.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                    ? dateTime.ToShortDateString()
                                    : string.Format(df.DataFormatString, dateTime));
                            }
                            break;
                        default:
                            row.Cells.Add(dataItem.ToString());
                            break;
                    }
                else
                {
                    row.Cells.Add(dataItem.ToString());
                }
            }
        }
    }

    private static void ImportGroupedData<TKey, TValue>(this Aspose.Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
    {
        var headRow = table.Rows.Add();
        var props = typeof(TValue).GetProperties(BindingFlags.Public | BindingFlags.Instance);
        foreach (var prop in props)
        {
            headRow.Cells.Add(prop.GetCustomAttribute(typeof(DisplayAttribute)) is DisplayAttribute dd ? dd.Name : prop.Name);
        }

        foreach (var group in groupedData)
        {
            // Add group row to table
            var row = table.Rows.Add();
            var cell = row.Cells.Add(group.Key.ToString());
            cell.ColSpan = props.Length;
            cell.BackgroundColor = Aspose.Pdf.Color.DarkGray;
            cell.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.White;

            foreach (var item in group.Values)
            {
                // Add data row to table
                var dataRow = table.Rows.Add();
                // Add cells
                foreach (var t in props)
                {
                    var dataItem = t.GetValue(item, null);

                    if (t.GetCustomAttribute(typeof(DataTypeAttribute)) is DataTypeAttribute dataType)
                        switch (dataType.DataType)
                        {
                            case DataType.Currency:
                                dataRow.Cells.Add(string.Format("{0:C}", dataItem));
                                break;
                            case DataType.Date:
                                var dateTime = (DateTime)dataItem;
                                if (t.GetCustomAttribute(typeof(DisplayFormatAttribute)) is DisplayFormatAttribute df)
                                {
                                    dataRow.Cells.Add(string.IsNullOrEmpty(df.DataFormatString)
                                        ? dateTime.ToShortDateString()
                                        : string.Format(df.DataFormatString, dateTime));
                                }
                                break;
                            default:
                                dataRow.Cells.Add(dataItem.ToString());
                                break;
                        }
                    else
                    {
                        dataRow.Cells.Add(dataItem.ToString());
                    }
                }
            }
        }
    }
}
```

تُستخدم سمات Data Annotations غالبًا لوصف النماذج وتساعدنا في إنشاء الجدول. لذلك، تم اختيار خوارزمية توليد الجدول التالية لـ ImportEntityList:

* الأسطر 12-18: بناء صف رأس وإضافة خلايا رأس وفقًا للقانون "إذا كانت DisplayAttribute موجودة، فخذ قيمتها وإلا خذ اسم الخاصية".
* الأسطر 50-53: بناء صفوف البيانات وإضافة خلايا الصف وفقًا للقانون "إذا كانت السمة DataTypeAttribute محددة، فإننا نتحقق مما إذا كنا بحاجة إلى إجراء إعدادات تصميم إضافية لها، وإلا فقط نقوم بتحويل البيانات إلى سلسلة وإضافتها إلى الخلية؛".

في هذا المثال، تم إجراء تخصيصات إضافية لـ DataType.Currency (الأسطر 32-34) و DataType.Date (الأسطر 35-43)، ولكن يمكنك إضافة أخرى إذا لزم الأمر.
خوارزمية طريقة ImportGroupedData مشابهة تقريبًا للأخرى السابقة. يتم استخدام فئة GroupViewModel الإضافية، لتخزين البيانات المجمعة.

```csharp
using System.Collections.Generic;
public class GroupViewModel<K,T>
{
    public K Key;
    public IEnumerable<T> Values;
}
```

نظرًا لأننا نعالج المجموعات، نقوم أولاً بإنشاء سطر لقيمة المفتاح (الأسطر 66-71)، وبعد ذلك - الأسطر الخاصة بهذه المجموعة.