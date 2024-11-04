---
title: دمج الجدول مع مصادر البيانات PDF
linktitle: دمج الجدول
type: docs
weight: 30
url: /net/integrate-table/
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
    "headline": "دمج الجدول مع مصادر البيانات PDF",
    "alternativeHeadline": "كيفية دمج الجدول مع مصادر البيانات PDF",
    "author": {
        "@type": "Person",
        "name":"أنستاسيا هولوب",
        "givenName": "أنستاسيا",
        "familyName": "هولوب",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد وثيقة PDF",
    "keywords": "pdf, c#, دمج الجدول",
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
    "url": "/net/integrate-table/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/integrate-table/"
    },
    "dateModified": "2022-02-04",
    "description": "يوضح هذا المقال كيفية دمج جداول PDF. دمج الجدول مع قاعدة البيانات وتحديد ما إذا كان الجدول سينقسم في الصفحة الحالية."
}
</script>

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## دمج الجدول مع قاعدة البيانات

القواعد مصممة لتخزين وإدارة البيانات. من الممارسات الشائعة للمبرمجين ملء الكائنات المختلفة بالبيانات من القواعد. يناقش هذا المقال إضافة البيانات من قاعدة بيانات إلى جدول. من الممكن ملء كائن [الجدول](https://reference.aspose.com/pdf/net/aspose.pdf/table) بالبيانات من أي مصدر بيانات باستخدام Aspose.PDF لـ .NET. وليس ذلك فحسب، بل إنه سهل للغاية.

[Aspose.PDF لـ .NET](https://docs.aspose.com/pdf/net/) يتيح للمطورين استيراد البيانات من:

- مصفوفة الكائنات
- DataTable
- DataView

يوفر هذا الموضوع معلومات حول جلب البيانات من DataTable أو DataView.

يجب أن يكون جميع المطورين العاملين تحت منصة .NET مُلمين بمفاهيم ADO.NET الأساسية التي قدمها إطار .NET.
جميع المطورين العاملين تحت منصة .NET يجب أن يكونوا ملمين بالمفاهيم الأساسية لـ ADO.NET التي قدمها إطار .NET.

تُستخدم طرق ImportDataTable(..) و ImportDataView(..) للفئة Table لاستيراد البيانات من قواعد البيانات.

يُظهر المثال أدناه استخدام طريقة ImportDataTable. في هذا المثال، يتم إنشاء كائن DataTable من البداية ويتم إضافة السجلات برمجيًا بدلاً من ملء DataTable بالبيانات من قواعد البيانات. يمكن للمطورين أيضًا ملء DataTable من قاعدة البيانات حسب رغبتهم.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

DataTable dt = new DataTable("Employee");
dt.Columns.Add("Employee_ID", typeof(Int32));
dt.Columns.Add("Employee_Name", typeof(string));
dt.Columns.Add("Gender", typeof(string));
// إضافة صفين إلى كائن DataTable برمجياً
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
// إنشاء نموذج Document
Document doc = new Document();
doc.Pages.Add();
// تهيئة نموذج جديد للجدول
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
// تعيين عرض الأعمدة للجدول
table.ColumnWidths = "40 100 100 100";
// تعيين لون حدود الجدول باللون الرمادي الفاتح
table.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
// تعيين الحدود لخلايا الجدول
table.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, .5f, Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray));
table.ImportDataTable(dt, true, 0, 1, 3, 3);

// إضافة كائن الجدول إلى الصفحة الأولى من المستند الداخلي
doc.Pages[1].Paragraphs.Add(table);
dataDir = dataDir + "DataIntegrated_out.pdf";
// حفظ المستند المحدث الذي يحتوي على كائن الجدول
doc.Save(dataDir);
```
## كيفية تحديد ما إذا كانت الجدول ستنقسم في الصفحة الحالية

الجداول بشكل افتراضي تُضاف من الزاوية العلوية اليسرى وإذا وصلت الجدول إلى نهاية الصفحة، فإنها تنقسم تلقائيًا. يمكنك برمجيًا الحصول على المعلومات التي تفيد بأن الجدول سيتم استيعابه في الصفحة الحالية أو سينكسر في أسفل الصفحة. لهذا السبب، أولاً، تحتاج إلى الحصول على معلومات حجم الوثيقة، ثم تحتاج إلى الحصول على معلومات هامش الصفحة العلوي وهامش الصفحة السفلي، معلومات هامش الجدول العلوي وارتفاع الجدول. إذا أضفت هامش الصفحة العلوي + هامش الصفحة السفلي + هامش الجدول العلوي + ارتفاع الجدول وخصمته من ارتفاع الوثيقة، يمكنك الحصول على كمية المساحة المتبقية فوق الوثيقة. اعتمادًا على ارتفاع الصف المحدد (الذي حددته)، يمكنك حساب ما إذا كان يمكن استيعاب جميع صفوف الجدول ضمن المساحة المتبقية فوق صفحة أم لا. الرجاء إلقاء نظرة على مقتطف الكود التالي. في الكود التالي، يكون متوسط ارتفاع الصف 23.002 نقطة.

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// توثيق فئة PDF
Document pdf = new Document();
// إضافة القسم إلى أقسام مستند PDF
Aspose.Pdf.Page page = pdf.Pages.Add();
// توثيق كائن الجدول
Aspose.Pdf.Table table1 = new Aspose.Pdf.Table();
table1.Margin.Top = 300;
// إضافة الجدول في مجموعة فقرات القسم المطلوب
page.Paragraphs.Add(table1);
// تعيين عرض الأعمدة للجدول
table1.ColumnWidths = "100 100 100";
// تعيين حد الخلية الافتراضي باستخدام كائن BorderInfo
table1.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F);
// تعيين حد الجدول باستخدام كائن BorderInfo مخصص آخر
table1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1F);
// إنشاء كائن MarginInfo وتعيين هوامشه اليسرى والسفلية واليمنى والعليا
Aspose.Pdf.MarginInfo margin = new Aspose.Pdf.MarginInfo();
margin.Top = 5f;
margin.Left = 5f;
margin.Right = 5f;
margin.Bottom = 5f;
// تعيين التبطين الافتراضي للخلية إلى كائن MarginInfo
table1.DefaultCellPadding = margin;
// إذا زاد العداد إلى 17، ستنقسم الجدول
// لأنه لا يمكن استيعابه بعد الآن على هذه الصفحة
for (int RowCounter = 0; RowCounter <= 16; RowCounter++)
{
    // إنشاء صفوف في الجدول ثم خلايا في الصفوف
    Aspose.Pdf.Row row1 = table1.Rows.Add();
    row1.Cells.Add("col " + RowCounter.ToString() + ", 1");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 2");
    row1.Cells.Add("col " + RowCounter.ToString() + ", 3");
}
// الحصول على معلومات ارتفاع الصفحة
float PageHeight = (float)pdf.PageInfo.Height;
// الحصول على معلومات الارتفاع الكلي لهامش الصفحة العلوي والسفلي،
// هامش الجدول العلوي وارتفاع الجدول.
float TotalObjectsHeight = (float)page.PageInfo.Margin.Top + (float)page.PageInfo.Margin.Bottom + (float)table1.Margin.Top + (float)table1.GetHeight();

// عرض معلومات ارتفاع الوثيقة PDF، ارتفاع الجدول، هامش الجدول العلوي وهامش الصفحة العلوي
// وهامش السفلي
Console.WriteLine("ارتفاع مستند PDF = " + pdf.PageInfo.Height.ToString() + "\nمعلومات هامش العلوي = " + page.PageInfo.Margin.Top.ToString() + "\nمعلومات هامش السفلي = " + page.PageInfo.Margin.Bottom.ToString() + "\n\nمعلومات هامش أعلى الجدول = " + table1.Margin.Top.ToString() + "\nمتوسط ارتفاع الصف = " + table1.Rows[0].MinRowHeight.ToString() + " \nارتفاع الجدول " + table1.GetHeight().ToString() + "\n ----------------------------------------" + "\nارتفاع الصفحة الإجمالي =" + PageHeight.ToString() + "\nالارتفاع التراكمي بما في ذلك الجدول =" + TotalObjectsHeight.ToString());

// تحقق إذا خصمنا مجموع هامش الصفحة العلوي + هامش الصفحة السفلي
// + هامش أعلى الجدول وارتفاع الجدول من ارتفاع الصفحة وهو أقل
// من 10 (يمكن أن يكون متوسط ارتفاع الصف أكبر من 10)
if ((PageHeight - TotalObjectsHeight) <= 10)
    // إذا كانت القيمة أقل من 10، فعرض الرسالة.
    // التي تظهر أنه لا يمكن وضع صف آخر وإذا أضفنا جديد
    // صف، ستنقسم الجدول. وهذا يعتمد على قيمة ارتفاع الصف.
    Console.WriteLine("ارتفاع الصفحة - ارتفاع الكائنات < 10، لذا ستنقسم الجدول");

dataDir = dataDir + "DetermineTableBreak_out.pdf";
// حفظ مستند PDF
pdf.Save(dataDir);
```
## إضافة عمود متكرر في الجدول

في الفئة Aspose.Pdf.Table، يمكنك ضبط خاصية RepeatingRowsCount التي ستكرر الصفوف إذا كان الجدول طويلاً بشكل عمودي وتجاوز إلى الصفحة التالية. ومع ذلك، في بعض الحالات، تكون الجداول عريضة جدًا بحيث لا تتسع في صفحة واحدة وتحتاج إلى الاستمرار إلى الصفحة التالية. لتحقيق هذا الغرض، قمنا بتنفيذ خاصية RepeatingColumnsCount في فئة Aspose.Pdf.Table. إعداد هذه الخاصية سيتسبب في انقسام الجدول إلى الصفحة التالية بطريقة عمودية وتكرار عدد الأعمدة المحدد في بداية الصفحة التالية. يوضح الجزء التالي من الشفرة استخدام خاصية RepeatingColumnsCount:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

string outFile = dataDir + "AddRepeatingColumn_out.pdf";
// إنشاء وثيقة جديدة
Document doc = new Document();
Aspose.Pdf.Page page = doc.Pages.Add();

// توضيح جدول خارجي يشغل الصفحة بأكملها
Aspose.Pdf.Table outerTable = new Aspose.Pdf.Table();
outerTable.ColumnWidths = "100%";
outerTable.HorizontalAlignment = HorizontalAlignment.Left;

// استدعاء كائن جدول سيتم تضمينه داخل الجدول الخارجي وسينقسم داخل الصفحة نفسها
Aspose.Pdf.Table mytable = new Aspose.Pdf.Table();
mytable.Broken = TableBroken.VerticalInSamePage;
mytable.ColumnAdjustment = ColumnAdjustment.AutoFitToContent;

// إضافة الجدول الخارجي إلى فقرات الصفحة
// إضافة mytable إلى outerTable
page.Paragraphs.Add(outerTable);
var bodyRow = outerTable.Rows.Add();
var bodyCell = bodyRow.Cells.Add();
bodyCell.Paragraphs.Add(mytable);
mytable.RepeatingColumnsCount = 5;
page.Paragraphs.Add(mytable);

// إضافة صف الرأس
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
    // إنشاء صفوف في الجدول ثم الخلايا في الصفوف
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
doc.Save(outFile);
```
## دمج الجدول مع مصدر إطار عمل الكيانات

الأكثر أهمية لـ .NET الحديث هو استيراد البيانات من إطارات عمل ORM. في هذه الحالة، من الجيد توسيع فئة الجدول بطرق مساعدة لاستيراد البيانات من قائمة بسيطة أو من البيانات المجمعة. دعونا نعطي مثالاً عن واحد من أشهر إطارات ORM - إطار عمل الكيان.

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
                            dataRow.Cells.Add(dataItem.toString());
                        }
                    }
                }
            }
        }
    }
```
سُمِحت سمات التوصيف بالبيانات بوصف النماذج ومساعدتنا في إنشاء الجدول. لذا، تم اختيار الخوارزمية التالية لتوليد الجدول لـ ImportEntityList:

- الأسطر 12-18: بناء صف العنوان وإضافة خلايا العنوان وفقاً للقاعدة "إذا كانت سمة العرض موجودة، فخذ قيمتها وإلا خذ اسم الخاصية"
- الأسطر 50-53: بناء صفوف البيانات وإضافة خلايا الصف وفقاً للقاعدة "إذا تم تعريف سمة DataTypeAttribute، فإننا نتحقق مما إذا كنا بحاجة إلى إجراء إعدادات تصميم إضافية لها، وإلا فقط نحول البيانات إلى نص ونضيفها إلى الخلية؛"

في هذا المثال، تم إجراء تخصيصات إضافية لـ DataType.Currency (الأسطر 32-34) و DataType.Date (الأسطر 35-43)، ولكن يمكنك إضافة غيرها إذا لزم الأمر.
خوارزمية طريقة ImportGroupedData شبه مماثلة للطريقة السابقة. يُستخدم فئة GroupViewModel الإضافية، لتخزين البيانات المجمعة.

```csharp
using System.Collections.Generic;
    public class GroupViewModel<K,T>
    {
        public K Key;
        public IEnumerable<T> Values;
    }
```
بما أننا نعالج المجموعات، أولاً نولد سطرًا للقيمة الرئيسية (السطور 66-71)، وبعدها - سطور هذه المجموعة.

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
                "contactType": "مبيعات",
                "areaServed": "US",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "الإنجليزية"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "AU",
                "availableLanguage": "الإنجليزية"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة تعديل ملفات PDF لـ .NET",
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

