---
title: تصيير الجدول باستخدام Entity Framework
linktitle: تصيير الجدول باستخدام Entity Framework
type: docs
weight: 40
url: /ar/net/render-table-using-entity-framework-model-as-data-source/
description: هذا المقال سيوضح لك كيفية تصيير جدول باستخدام نموذج Entity Framework كمصدر بيانات باستخدام Aspose.PDF لـ .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

هناك عدد من المهام التي لسبب ما قد يكون من الأسهل تصدير البيانات من قواعد البيانات إلى مستند PDF دون استخدام نظام تحويل HTML إلى PDF الذي أصبح مؤخراً شائعاً.

هذا المقال سيوضح لك كيفية توليد مستند PDF باستخدام Aspose.PDF لـ .NET.

## أساسيات توليد PDF مع Aspose.PDF

واحدة من أهم الفئات في Aspose.PDF هي [فئة المستند](https://reference.aspose.com/pdf/net/aspose.pdf/document). تعتبر هذه الفئة محرك تقديم PDF. لعرض بنية PDF، تستخدم مكتبة Aspose.PDF نموذج الوثيقة-الصفحة، حيث:

* Document - يحتوي على خصائص مستند PDF بما في ذلك مجموعة الصفحات;

* المستند - يحتوي على خصائص مستند PDF بما في ذلك مجموعة الصفحات؛
* الصفحة - تحتوي على خصائص صفحة معينة ومجموعات متنوعة من العناصر المرتبطة بهذه الصفحة.

لذلك، لإنشاء مستند PDF باستخدام Aspose.PDF، يجب اتباع الخطوات التالية:

1. إنشاء كائن المستند؛
1. إضافة الصفحة (كائن الصفحة) لكائن المستند؛
1. إنشاء الكائنات التي يتم وضعها على الصفحة (مثلاً قطعة نص، جدول، إلخ)
1. إضافة العناصر المُنشأة إلى المجموعة المقابلة على الصفحة (في حالتنا ستكون مجموعة الفقرات)؛
1. حفظ المستند كملف PDF.

```csharp
// الخطوة 1
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

// الخطوة 2
var pdfPage = document.Pages.Add();

// الخطوة 3
var textFragment = new TextFragment(reportTitle);
// ..........................................

var table = new Table
{
    // .................................
};

// الخطوة 4
pdfPage.Paragraphs.Add(textFragment);
pdfPage.Paragraphs.Add(table);

// الخطوة 5
using (var streamOut = new MemoryStream())
{
    document.Save(streamOut);
    return new FileContentResult(streamOut.ToArray(), "application/pdf")
    {
        FileDownloadName = "tenants.pdf"
    };
}
```
المشكلة الأكثر شيوعًا هي إخراج البيانات في شكل جدول. يُستخدم [فئة الجدول](https://reference.aspose.com/pdf/net/aspose.pdf/table) لمعالجة الجداول. تمنحنا هذه الفئة القدرة على إنشاء الجداول ووضعها في المستند، باستخدام [الصفوف](https://reference.aspose.com/pdf/net/aspose.pdf/rows) و[الخلايا](https://reference.aspose.com/pdf/net/aspose.pdf/cell). لذا، لإنشاء الجدول، تحتاج إلى إضافة عدد مطلوب من الصفوف وملؤها بالعدد المناسب من الخلايا.

المثال التالي ينشئ جدول 4x10.

```csharp
var table = new Table
    {
        // تعيين عرض الأعمدة التلقائي للجدول
        ColumnWidths = "25% 25% 25% 25%",
        // تعيين تبطين الخلية
        DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // اليسار الأسفل اليمين الأعلى
        // تعيين لون حدود الجدول باللون الأخضر
        Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
        // تعيين الحدود لخلايا الجدول باللون الأسود
        DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
    };
    for (var rowCount = 0; rowCount < 10; rowCount++)
    {
        // إضافة صف إلى الجدول
        var row = table.Rows.Add();
        // إضافة خلايا إلى الجدول
        for (int i = 0; i < 4; i++)
        {
            row.Cells.Add($"Cell ({i+1}, {rowCount +1})");
        }
    }
    // إضافة كائن الجدول إلى الصفحة الأولى من المستند
    document.Pages[1].Paragraphs.Add(table);
```
عند تهيئة كائن الجدول، تم استخدام إعدادات الواجهة البسيطة:

* [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/columnwidths) - عرض الأعمدة (افتراضيًا);
* [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellpadding) - الحقول الافتراضية لخلية الجدول;
* [Border](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/border) - خصائص إطار الجدول (النمط، السُمك، اللون);
* [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf/table/properties/defaultcellborder) - خصائص إطار الخلية (النمط، السُمك، اللون).

نتيجة لذلك، نحصل على جدول بمقاس 4x10 مع أعمدة ذات عرض متساوي.

![جدول 4x10](http://aspose-html-doc.azurewebsites.net/docs/images/img001.jpg)

## تصدير البيانات من كائنات ADO.NET

يوفر فئة الجدول طرقًا للتفاعل مع مصادر بيانات ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) و [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
توفر فئة الجدول طرقًا للتفاعل مع مصادر بيانات ADO.NET - [ImportDataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) و [ImportDataView](https://reference.aspose.com/pdf/net/aspose.pdf/table/methods/importdataview).
بالنظر إلى أن هذه الكائنات ليست ملائمة جدًا للعمل في قالب MVC، سنقتصر على مثال موجز. في هذا المثال (السطر 50)، يتم استدعاء طريقة ImportDataTable ويتم تلقي مثيل DataTable وإعدادات إضافية مثل علامة الرأس والموضع الأولي (الصفوف/الأعمدة) لإخراج البيانات.

```csharp
// إنشاء مستند PDF جديد
var document = new Document
{
    PageInfo = new PageInfo { Margin = new MarginInfo(28, 28, 28, 42) }
};

var pdfPage = document.Pages.Add();

// تهيئة مثيل جديد من TextFragment لعنوان التقرير
var textFragment = new TextFragment(reportTitle1);
Table table = new Table
{
    // تعيين عرض الأعمدة للجدول
    ColumnWidths = "25% 25% 25% 25%",
    // تعيين تبطين الخلية
    DefaultCellPadding = new MarginInfo(10, 5, 10, 5), // اليسار الأسفل اليمين الأعلى
    // تعيين لون حد الجدول باللون الأخضر
    Border = new BorderInfo(BorderSide.All, .5f, Color.Green),
    // تعيين الحد لخلايا الجدول باللون الأسود
    DefaultCellBorder = new BorderInfo(BorderSide.All, .2f, Color.Green),
};

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("config.json", false)
    .Build();

var connectionString = configuration.GetSection("connectionString").Value;

if (string.IsNullOrEmpty(connectionString))
    throw new ArgumentException("لا يوجد سلسلة اتصال في config.json");

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

// إضافة كائن الجدول إلى الصفحة الأولى من مستند الإدخال
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

## تصدير البيانات من إطار العمل Entity

من الأكثر أهمية بالنسبة لـ .NET الحديث هو استيراد البيانات من أطر عمل ORM. في هذه الحالة، من الجيد توسيع فئة الجدول بطرق تمديد لاستيراد البيانات من قائمة بسيطة أو من البيانات المجمعة. دعونا نقدم مثالاً على أحد أشهر أطر العمل ORM - إطار العمل Entity.

```csharp
public static class PdfHelper
    {
        public static void ImportEntityList<TSource>(this Pdf.Table table, IList<TSource> data)
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
        public static void ImportGroupedData<TKey,TValue>(this Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
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
                cell.BackgroundColor = Pdf.Color.DarkGray;
                cell.DefaultCellTextState.ForegroundColor = Pdf.Color.White;

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
سُميت خصائص توثيق البيانات بشكل متكرر لوصف النماذج ومساعدتنا في إنشاء الجدول. لذلك، تم اختيار خوارزمية توليد الجدول التالية لـ ImportEntityList:

* الأسطر 12-18: بناء صف العنوان وإضافة خلايا العنوان وفقًا للقاعدة "إذا كان السمة DisplayAttribute موجودة، فخذ قيمتها وإلا خذ اسم الخاصية"
* الأسطر 50-53: بناء صفوف البيانات وإضافة خلايا الصفوف وفقًا للقاعدة "إذا تم تعريف السمة DataTypeAttribute، فإننا نتحقق مما إذا كنا بحاجة إلى إجراء إعدادات تصميم إضافية لها، وإلا فقط تحويل البيانات إلى نص وإضافتها إلى الخلية؛"

في هذا المثال، تم إجراء تخصيصات إضافية لـ DataType.Currency (الأسطر 32-34) و DataType.Date (الأسطر 35-43)، ولكن يمكنك إضافة غيرها إذا لزم الأمر.
خوارزمية طريقة ImportGroupedData مشابهة تقريبًا للسابقة. يُستخدم فئة GroupViewModel إضافية، لتخزين البيانات المجمعة.

```csharp
.using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```

بما أننا نعالج المجموعات، نولد أولاً سطرًا لقيمة المفتاح (الأسطر 66-71)، وبعدها - سطور هذه المجموعة.
