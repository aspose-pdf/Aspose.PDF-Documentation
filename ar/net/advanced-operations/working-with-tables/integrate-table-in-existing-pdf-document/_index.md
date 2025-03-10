---
title: دمج الجدول مع مصادر البيانات PDF
linktitle: دمج الجدول
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/integrate-table/
description: يوضح هذا المقال كيفية دمج جداول PDF. دمج الجدول مع قاعدة البيانات وتحديد ما إذا كان الجدول سينقسم في الصفحة الحالية.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Integrate Table with Data Sources PDF",
    "alternativeHeadline": "Integrate PDF Tables with Data Sources Seamlessly",
    "abstract": "تتيح ميزة دمج الجدول مع مصادر البيانات PDF للمطورين استيراد البيانات بسلاسة من مصادر متنوعة، بما في ذلك قواعد البيانات وإطار الكيان، مباشرة إلى جداول PDF باستخدام Aspose.PDF for .NET. مع وظائف لتحديد ترقيم الصفحات ودعم للأعمدة المتكررة، تعزز هذه الميزة عرض البيانات مع الحفاظ على سلامة الوثيقة من خلال منع انقسام الجدول عبر الصفحات.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2201",
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
    "url": "/net/integrate-table/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/integrate-table/"
    },
    "dateModified": "2024-11-26",
    "description": "يظهر هذا المقال كيفية دمج جداول PDF. دمج الجدول مع قاعدة البيانات وتحديد ما إذا كان الجدول سينقسم في الصفحة الحالية."
}
</script>

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/) .

## دمج الجدول مع قاعدة البيانات

تم بناء قواعد البيانات لتخزين وإدارة البيانات. من الممارسات الشائعة للمبرمجين ملء كائنات مختلفة بالبيانات من قواعد البيانات. يناقش هذا المقال إضافة بيانات من قاعدة بيانات إلى جدول. من الممكن ملء كائن [Table](https://reference.aspose.com/pdf/net/aspose.pdf/table) بالبيانات من أي مصدر بيانات باستخدام Aspose.PDF for .NET. وليس فقط ممكنًا، بل إنه سهل جدًا.

يسمح [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) للمطورين باستيراد البيانات من:

- مصفوفة الكائنات
- DataTable
- DataView

يوفر هذا الموضوع معلومات حول جلب البيانات من DataTable أو DataView.

يجب أن يكون جميع المطورين الذين يعملون تحت منصة .NET على دراية بمفاهيم ADO.NET الأساسية التي قدمها إطار عمل .NET. من الممكن الاتصال بجميع أنواع مصادر البيانات تقريبًا باستخدام ADO.NET. يمكننا استرداد البيانات من قواعد البيانات وحفظها في DataSet أو DataTable أو DataView. يوفر Aspose.PDF for .NET دعمًا لاستيراد البيانات من هذه أيضًا. وهذا يمنح المطورين مزيدًا من الحرية لملء الجداول في مستندات PDF من أي مصدر بيانات.

تستخدم طرق ImportDataTable(..) و ImportDataView(..) من فئة Table لاستيراد البيانات من قواعد البيانات.

يوضح المثال أدناه استخدام طريقة ImportDataTable. في هذا المثال، يتم إنشاء كائن DataTable من الصفر ويتم إضافة السجلات برمجيًا بدلاً من ملء DataTable بالبيانات من قواعد البيانات. يمكن للمطورين أيضًا ملء DataTable من قاعدة البيانات وفقًا لرغبتهم.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFromDataTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    DataTable dt = new DataTable("Employee");
    dt.Columns.Add("Employee_ID", typeof(Int32));
    dt.Columns.Add("Employee_Name", typeof(string));
    dt.Columns.Add("Gender", typeof(string));
    // Add 2 rows into the DataTable object programmatically
    DataRow dr = dt.NewRow();
    dr[0] = 1;
    dr[1] = "John Smith";
    dr[2] = "Male";
    dt.Rows.Add(dr);
    dr = dt.NewRow();
    dr[0] = 2;
    dr[1] = "Mary Miller";
    dr[2] = "Female";
    dt.Rows.Add(dr);
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Initializes a new instance of the Table
        Aspose.Pdf.Table table = new Aspose.Pdf.Table();
        // Set column widths of the table
        table.ColumnWidths = "40 100 100 100";
        // Set the table border color as LightGray
        table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        // Set the border for table cells
        table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
        table.ImportDataTable(dt, true, 0, 1, 3, 3);

        // Add table object to first page of input document
        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "ImportFromDataTable_out.pdf");
    }
}
```

## كيفية تحديد ما إذا كان الجدول سينكسر في الصفحة الحالية

تتم إضافة الجداول افتراضيًا من الزاوية العلوية اليسرى وإذا وصل الجدول إلى نهاية الصفحة، فإنه ينكسر تلقائيًا. يمكنك برمجيًا الحصول على المعلومات حول ما إذا كان سيتم استيعاب الجدول في الصفحة الحالية أو سينكسر في أسفل الصفحة. لهذا السبب، تحتاج أولاً إلى الحصول على معلومات حجم الوثيقة، ثم تحتاج إلى الحصول على معلومات هوامش الصفحة العلوية والسفلية، ومعلومات هوامش الجدول العلوية وارتفاع الجدول. إذا أضفت هامش الصفحة العلوي + هامش الصفحة السفلي + هامش الجدول العلوي + ارتفاع الجدول وطرحتها من ارتفاع الوثيقة، يمكنك الحصول على مقدار المساحة المتبقية فوق الوثيقة. اعتمادًا على الارتفاع المحدد للصف (الذي حددته)، يمكنك حساب ما إذا كان يمكن استيعاب جميع صفوف الجدول ضمن المساحة المتبقية فوق الصفحة أم لا. يرجى إلقاء نظرة على مقتطف الشيفرة التالي. في الشيفرة التالية، متوسط ارتفاع الصف هو 23.002 نقطة.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineTableBreak()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = pdf.Pages.Add();
        // Instantiate a table object
        Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
        table1.Margin.Top = 300;
        // Add the table in paragraphs collection of the desired section
        page.Paragraphs.Add(table1);
        // Set with column widths of the table
        table1.ColumnWidths = "100 100 100";
        // Set default cell border using BorderInfo object
        table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
        // Set table border using another customized BorderInfo object
        table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
        // Create MarginInfo object and set its left, bottom, right and top margins
        Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
        margin.Top = 5f;
        margin.Left = 5f;
        margin.Right = 5f;
        margin.Bottom = 5f;
        // Set the default cell padding to the MarginInfo object
        table1.DefaultCellPadding = margin;
        // If you increase the counter to 17, table will break
        // Because it cannot be accommodated any more over this page
        for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
        {
            // Create rows in the table and then cells in the rows
            Aspose.Pdf.Row row1 = table1.Rows.Add();
            row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
        }
        // Get the Page Height information
        float PageHeight = (float)pdf.PageInfo.Height;
        // Get the total height information of Page Top & Bottom margin,
        // Table Top margin and table height.
        float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

        // Display Page Height, Table Height, table Top margin and Page Top
        // And Bottom margin information
        Console.WriteLine("PDF document Height = " + pdf.PageInfo.Height.ToString() + "\nTop Margin Info = " + page.PageInfo.Margin.Top.ToString() + "\nBottom Margin Info = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nTable-Top Margin Info = " + table1.Margin.Top.ToString() + "\nAverage Row Height = " + table1.Rows[0].MinRowHeight.ToString() + " \nTable height " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nTotal Page Height =" + PageHeight.ToString() + "\nCummulative height including Table =" + TotalObjectsHeight.ToString());

        // Check if we deduct the sume of Page top margin + Page Bottom margin
        // + Table Top margin and table height from Page height and its less
        // Than 10 (an average row can be greater than 10)
        if ((PageHeight - TotalObjectsHeight) <= 10)
        {
            // If the value is less than 10, then display the message.
            // Which shows that another row can not be placed and if we add new
            // Row, table will break. It depends upon the row height value.
            Console.WriteLine("Page Height - Objects Height < 10, so table will break");
        }

        // Save PDF document
        document.Save(dataDir + "DetermineTableBreak_out.pdf");
    }
}
```

## إضافة عمود متكرر في الجدول

في فئة Aspose.Pdf.Table، يمكنك تعيين RepeatingRowsCount الذي سيكرر الصفوف إذا كان الجدول طويلًا جدًا عموديًا ويتجاوز إلى الصفحة التالية. ومع ذلك، في بعض الحالات، تكون الجداول واسعة جدًا بحيث لا تتناسب مع صفحة واحدة وتحتاج إلى الاستمرار إلى الصفحة التالية. من أجل تحقيق هذا الغرض، قمنا بتنفيذ خاصية RepeatingColumnsCount في فئة Aspose.Pdf.Table. ستؤدي تعيين هذه الخاصية إلى كسر الجدول إلى الصفحة التالية عمودياً وتكرار عدد الأعمدة المعطاة في بداية الصفحة التالية. يوضح مقتطف الشيفرة التالي استخدام خاصية RepeatingColumnsCount:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRepeatingColumn()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Instantiate an outer table that takes up the entire page
        Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
        outerTable.ColumnWidths = "100%";
        outerTable.HorizontalAlignment = HorizontalAlignment.Left;

        // Instantiate a table object that will be nested inside outerTable that will break inside the same page
        Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
        mytable.Broken = TableBroken.VerticalInSamePage;
        mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

        // Add the outerTable to the page paragraphs
        // Add mytable to outerTable
        page.Paragraphs.Add(outerTable);
        var bodyRow = outerTable.Rows.Add();
        var bodyCell = bodyRow.Cells.Add();
        bodyCell.Paragraphs.Add(mytable);
        mytable.RepeatingColumnsCount = 5;
        page.Paragraphs.Add(mytable);

        // Add header Row
        Aspose.Pdf.Row row = mytable.Rows.Add();
        row.Cells.Add("header 1");
        row.Cells.Add("header 2");
        row.Cells.Add("header 3");
        row.Cells.Add("header 4");
        row.Cells.Add("header 5");
        row.Cells.Add("header 6");
        row.Cells.Add("header 7");
        row.Cells.Add("header 11");
        row.Cells.Add("header 12");
        row.Cells.Add("header 13");
        row.Cells.Add("header 14");
        row.Cells.Add("header 15");
        row.Cells.Add("header 16");
        row.Cells.Add("header 17");

        for (int RowCounter = 0; RowCounter <= 5; RowCounter++)
        {
            // Create rows in the table and then cells in the rows
            Aspose.Pdf.Row row1 = mytable.Rows.Add();
            row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 4");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 5");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 6");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 7");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 11");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 12");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 13");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 14");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 15");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 16");
            row1.Cells.Add("col " + RowCounter.ToString() + ", 17");
        }

        // Save PDF document
        document.Save(dataDir + "AddRepeatingColumn_out.pdf");
    }
}
```

## دمج الجدول مع مصدر إطار الكيان

أكثر صلة بـ .NET الحديثة هو استيراد البيانات من أطر ORM. في هذه الحالة، من الجيد توسيع فئة Table بأساليب توسيع لاستيراد البيانات من قائمة بسيطة أو من البيانات المجمعة. دعنا نقدم مثالًا لأحد أشهر أطر ORM - إطار الكيان.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public static class PdfHelper
{
    private static void ImportEntityList<TSource>(this Pdf.Table table, IList<TSource> data)
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
    
    private static void ImportGroupedData<TKey,TValue>(this Pdf.Table table, IEnumerable<Models.GroupViewModel<TKey, TValue>> groupedData)
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

تستخدم سمات Data Annotations غالبًا لوصف النماذج وتساعدنا في إنشاء الجدول. لذلك، تم اختيار خوارزمية توليد الجدول التالية لـ ImportEntityList:

- الأسطر 12-18: بناء صف رأس وإضافة خلايا الرأس وفقًا للقانون "إذا كانت DisplayAttribute موجودة، فخذ قيمتها وإلا خذ اسم الخاصية"
- الأسطر 50-53: بناء صفوف البيانات وإضافة خلايا الصف وفقًا للقانون "إذا كانت السمة DataTypeAttribute محددة، فإننا نتحقق مما إذا كنا بحاجة إلى إجراء إعدادات تصميم إضافية لها، وإلا فقط نقوم بتحويل البيانات إلى سلسلة وإضافتها إلى الخلية؛"

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

نظرًا لأننا نعالج المجموعات، أولاً نقوم بإنشاء سطر لقيمة المفتاح (الأسطر 66-71)، وبعد ذلك - الأسطر الخاصة بهذه المجموعة.

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