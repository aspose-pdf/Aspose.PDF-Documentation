---
title: العمل مع الجدول في ملفات PDF الموسومة
linktitle: العمل مع الجدول في ملفات PDF الموسومة
type: docs
weight: 40
url: ar/net/working-with-table-in-tagged-pdfs/
description: يشرح هذا المقال كيفية العمل مع الجدول في مستند PDF الموسوم باستخدام Aspose.PDF لـ .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع الجدول في ملفات PDF الموسومة",
    "alternativeHeadline": "التلاعب بالجداول في ملفات PDF الموسومة",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستندات PDF",
    "keywords": "table, pdf, style table element, create table",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
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
    "url": "/net/working-with-table-in-tagged-pdfs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-table-in-tagged-pdfs/"
    },
    "dateModified": "2022-02-04",
    "description": "يشرح هذا المقال كيفية العمل مع الجدول في مستند PDF الموسوم باستخدام Aspose.PDF لـ .NET."
}
</script>
## إنشاء جدول في مستند PDF الموسوم

يتيح Aspose.PDF لـ .NET إنشاء جدول في مستندات PDF الموسومة.
Aspose.PDF لـ .NET يسمح بإنشاء جدول في مستندات PDF الموسومة.

الشفرة البرمجية التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

الشفرة البرمجية التالية توضح كيفية إنشاء جدول في مستند PDF الموسوم:

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// إنشاء مستند
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("جدول مثال");
taggedContent.SetLanguage("en-US");

// الحصول على عنصر البنية الجذرية
StructureElement rootElement = taggedContent.RootElement;


TableElement tableElement = taggedContent.CreateTableElement();
rootElement.AppendChild(tableElement);

tableElement.Border = new BorderInfo(BorderSide.All, 1.2F, Color.DarkBlue);

TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
TableTFootElement tableTFootElement = tableElement.CreateTFoot();
int rowCount = 50;
int colCount = 4;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.CreateTR();
headTrElement.AlternativeText = "صف الرأس";

headTrElement.BackgroundColor = Color.LightGray;

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.CreateTH();
    thElement.SetText(String.Format("رأس {0}", colIndex));

    thElement.BackgroundColor = Color.GreenYellow;
    thElement.Border = new BorderInfo(BorderSide.All, 4.0F, Color.Gray);

    thElement.IsNoBorder = true;
    thElement.Margin = new MarginInfo(16.0, 2.0, 8.0, 2.0);

    thElement.Alignment = HorizontalAlignment.Right;
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.CreateTR();
    trElement.AlternativeText = String.Format("صف {0}", rowIndex);

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        int colSpan = 1;
        int rowSpan = 1;

        if (colIndex == 1 && rowIndex == 1)
        {
            colSpan = 2;
            rowSpan = 2;
        }
        else if (colIndex == 2 && (rowIndex == 1 || rowIndex == 2))
        {
            continue;
        }
        else if (rowIndex == 2 && (colIndex == 1 || colIndex == 2))
        {
            continue;
        }

        TableTDElement tdElement = trElement.CreateTD();
        tdElement.SetText(String.Format("خلية [{0}, {1}]", rowIndex, colIndex));


        tdElement.BackgroundColor = Color.Yellow;
        tdElement.Border = new BorderInfo(BorderSide.All, 4.0F, Color.Gray);

        tdElement.IsNoBorder = false;
        tdElement.Margin = new MarginInfo(8.0, 2.0, 8.0, 2.0);

        tdElement.Alignment = HorizontalAlignment.Center;

        TextState cellTextState = new TextState();
        cellTextState.ForegroundColor = Color.DarkBlue;
        cellTextState.FontSize = 7.5F;
        cellTextState.FontStyle = FontStyles.Bold;
        cellTextState.Font = FontRepository.FindFont("Arial");
        tdElement.DefaultCellTextState = cellTextState;

        tdElement.IsWordWrapped = true;
        tdElement.VerticalAlignment = VerticalAlignment.Center;

        tdElement.ColSpan = colSpan;
        tdElement.RowSpan = rowSpan;
    }
}

TableTRElement footTrElement = tableTFootElement.CreateTR();
footTrElement.AlternativeText = "صف القدم";

footTrElement.BackgroundColor = Color.LightSeaGreen;

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.CreateTD();
    tdElement.SetText(String.Format("قدم {0}", colIndex));

    tdElement.Alignment = HorizontalAlignment.Center;
    tdElement.StructureTextState.FontSize = 7F;
    tdElement.StructureTextState.FontStyle = FontStyles.Bold;
}


StructureAttributes tableAttributes = tableElement.Attributes.GetAttributes(AttributeOwnerStandard.Table);
StructureAttribute summaryAttribute = new StructureAttribute(AttributeKey.Summary);
summaryAttribute.SetStringValue("نص الملخص للجدول");
tableAttributes.SetAttribute(summaryAttribute);


// حفظ مستند PDF الموسوم
document.Save(dataDir + "CreateTableElement.pdf");

// التحقق من الامتثال لـ PDF/UA
document = new Document(dataDir + "CreateTableElement.pdf");
bool isPdfUaCompliance = document.Validate(dataDir + "table.xml", PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("الامتثال لـ PDF/UA: {0}", isPdfUaCompliance));
```
## تنسيق عنصر الجدول

يسمح Aspose.PDF لـ .NET بتنسيق جدول في مستند PDF الموسوم. من أجل تنسيق جدول، يمكنك إنشاء جدول باستخدام طريقة [CreateTableElement()](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createtableelement) لواجهة [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) وضبط تنسيق الجدول باستخدام خصائص فئة [TableElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement). فيما يلي قائمة الخصائص التي يمكنك استخدامها لتنسيق الجدول:

- [BackgroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/backgroundcolor)
- [Border](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/border)
- [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/alignment)
- [CornerStyle](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/cornerstyle)
- [نمط الزاوية](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/cornerstyle)
- [مكسور](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/broken)
- [تعديل العمود](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/columnadjustment)
- [عرض الأعمدة](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/columnwidths)
- [حد الخلية الافتراضي](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcellborder)
- [حشوة الخلية الافتراضية](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcellpadding)
- [حالة نص الخلية الافتراضية](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcelltextstate)
- [عرض العمود الافتراضي](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcolumnwidth)
- [هل هو مكسور](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/isbroken)

- [IsBroken](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/isbroken)
- [IsBordersIncluded](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/isbordersincluded)
- [Left](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/left)
- [Top](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/top)

الكود التالي يوضح كيفية تنسيق الجدول في مستند PDF الموسوم:

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// إنشاء المستند
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("مثال على تنسيق الجدول");
taggedContent.SetLanguage("en-US");

// الحصول على عنصر البنية الجذرية
StructureElement rootElement = taggedContent.RootElement;

// إنشاء عنصر بنية الجدول
TableElement tableElement = taggedContent.CreateTableElement();
rootElement.AppendChild(tableElement);

tableElement.BackgroundColor = Color.Beige;
tableElement.Border = new BorderInfo(BorderSide.All, 0.80F, Color.Gray);
tableElement.Alignment = HorizontalAlignment.Center;
tableElement.Broken = TableBroken.Vertical;
tableElement.ColumnAdjustment = ColumnAdjustment.AutoFitToWindow;
tableElement.ColumnWidths = "80 80 80 80 80";
tableElement.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.50F, Color.DarkBlue);
tableElement.DefaultCellPadding = new MarginInfo(16.0, 2.0, 8.0, 2.0);
tableElement.DefaultCellTextState.ForegroundColor = Color.DarkCyan;
tableElement.DefaultCellTextState.FontSize = 8F;
tableElement.DefaultColumnWidth = "70";

tableElement.IsBroken = false;
tableElement.IsBordersIncluded = true;

tableElement.Left = 0F;
tableElement.Top = 40F;

tableElement.RepeatingColumnsCount = 2;
tableElement.RepeatingRowsCount = 3;
TextState rowStyle = new TextState();
rowStyle.BackgroundColor = Color.LightCoral;
tableElement.RepeatingRowsStyle = rowStyle;

TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
TableTFootElement tableTFootElement = tableElement.CreateTFoot();
int rowCount = 10;
int colCount = 5;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.CreateTR();
headTrElement.AlternativeText = "صف الرأس";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.CreateTH();
    thElement.SetText(String.Format("رأس {0}", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.CreateTR();
    trElement.AlternativeText = String.Format("صف {0}", rowIndex);

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.CreateTD();
        tdElement.SetText(String.Format("خلية [{0}, {1}]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.CreateTR();
footTrElement.AlternativeText = "صف القدم";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.CreateTD();
    tdElement.SetText(String.Format("قدم {0}", colIndex));
}

// حفظ مستند PDF الموسوم
document.Save(dataDir + "StyleTableElement.pdf");

// التحقق من التوافق مع PDF/UA
document = new Document(dataDir + "StyleTableElement.pdf");
bool isPdfUaCompliance = document.Validate(dataDir + "StyleTableElement.xml", PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("التوافق مع PDF/UA: {0}", isPdfUaCompliance));
```
## جدول أنماط الصفوف

يتيح Aspose.PDF لـ .NET تصميم صف جدول في مستند PDF الموسوم. لتصميم صف جدول، يمكنك استخدام خصائص فئة [TableTRElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tabletrelement). فيما يلي قائمة بالخصائص التي يمكنك استخدامها لتصميم صف جدول:

- لون الخلفية
- الحدود
- حدود الخلية الافتراضية
- الارتفاع الأدنى للصف
- الارتفاع الثابت للصف
- هل في صفحة جديدة
- هل الصف مكسور
- حالة نص الخلية الافتراضية
- تبطين الخلية الافتراضي
- محاذاة عمودية

يوضح الجزء التالي من الكود كيفية تصميم صف جدول في مستند PDF الموسوم:

```csharp
// للحصول على الأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى مجلد المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// إنشاء مستند
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("مثال على تصميم صف الجدول");
taggedContent.SetLanguage("en-US");

// الحصول على عنصر الهيكل الجذر
StructureElement rootElement = taggedContent.RootElement;

// إنشاء عنصر هيكل الجدول
TableElement tableElement = taggedContent.CreateTableElement();
rootElement.AppendChild(tableElement);

TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
TableTFootElement tableTFootElement = tableElement.CreateTFoot();
int rowCount = 7;
int colCount = 3;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.CreateTR();
headTrElement.AlternativeText = "صف الرأس";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.CreateTH();
    thElement.SetText(String.Format("رأس {0}", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.CreateTR();
    trElement.AlternativeText = String.Format("صف {0}", rowIndex);

    trElement.BackgroundColor = Color.LightGoldenrodYellow;
    trElement.Border = new BorderInfo(BorderSide.All, 0.75F, Color.DarkGray);

    trElement.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.50F, Color.Blue);
    trElement.MinRowHeight = 100.0;
    trElement.FixedRowHeight = 120.0;
    trElement.IsInNewPage = (rowIndex % 3 == 1);
    trElement.IsRowBroken = true;

    TextState cellTextState = new TextState();
    cellTextState.ForegroundColor = Color.Red;
    trElement.DefaultCellTextState = cellTextState;

    trElement.DefaultCellPadding = new MarginInfo(16.0, 2.0, 8.0, 2.0);
    trElement.VerticalAlignment = VerticalAlignment.Bottom;

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.CreateTD();
        tdElement.SetText(String.Format("خلية [{0}, {1}]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.CreateTR();
footTrElement.AlternativeText = "صف القدم";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.CreateTD();
    tdElement.SetText(String.Format("قدم {0}", colIndex));
}

// حفظ مستند PDF الموسوم
document.Save(dataDir + "StyleTableRow.pdf");

// التحقق من الامتثال لـ PDF/UA
document = new Document(dataDir + "StyleTableRow.pdf");
bool isPdfUaCompliance = document.Validate(dataDir + "StyleTableRow.xml", PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("الامتثال لـ PDF/UA: {0}", isPdfUaCompliance));
```
## تنسيق خلية الجدول

Aspose.PDF لـ .NET يسمح بتنسيق خلية جدول في مستند PDF الموسوم. من أجل تنسيق خلية جدول، يمكنك استخدام خصائص فئة [TableCellElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement). فيما يلي قائمة الخصائص التي يمكنك استخدامها لتنسيق خلية جدول:

- [BackgroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/backgroundcolor)
- [Border](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/border)
- [IsNoBorder](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/isnoborder)
- [Margin](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/margin)
- [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/alignment)
- [DefaultCellTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/defaultcelltextstate)
- [DefaultCellTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/defaultcelltextstate)
- [IsWordWrapped](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/iswordwrapped)
- [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/verticalalignment)
- [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/colspan)
- [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/rowspan)

الكود التالي يوضح كيفية تنسيق خلية الجدول في مستند PDF الموسوم:

```csharp
// للحصول على الأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// إنشاء مستند
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("أسلوب خلية الجدول المثال");
taggedContent.SetLanguage("en-US");

// الحصول على عنصر الهيكل الجذر
StructureElement rootElement = taggedContent.RootElement;

// إنشاء عنصر هيكل الجدول
TableElement tableElement = taggedContent.CreateTableElement();
rootElement.AppendChild(tableElement);

TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
TableTFootElement tableTFootElement = tableElement.CreateTFoot();
int rowCount = 4;
int colCount = 4;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.CreateTR();
headTrElement.AlternativeText = "صف الرأس";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.CreateTH();
    thElement.SetText(String.Format("رأس {0}", colIndex));

    thElement.BackgroundColor = Color.GreenYellow;
    thElement.Border = new BorderInfo(BorderSide.All, 4.0F, Color.Gray);

    thElement.IsNoBorder = true;
    thElement.Margin = new MarginInfo(16.0, 2.0, 8.0, 2.0);

    thElement.Alignment = HorizontalAlignment.Right;
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.CreateTR();
    trElement.AlternativeText = String.Format("الصف {0}", rowIndex);

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        int colSpan = 1;
        int rowSpan = 1;

        if (colIndex == 1 && rowIndex == 1)
        {
            colSpan = 2;
            rowSpan = 2;
        }
        else if (colIndex == 2 && (rowIndex == 1 || rowIndex == 2))
        {
            continue;
        }
        else if (rowIndex == 2 && (colIndex == 1 || colIndex == 2))
        {
            continue;
        }

        TableTDElement tdElement = trElement.CreateTD();
        tdElement.SetText(String.Format("خلية [{0}, {1}]", rowIndex, colIndex));


        tdElement.BackgroundColor = Color.Yellow;
        tdElement.Border = new BorderInfo(BorderSide.All, 4.0F, Color.Gray);

        tdElement.IsNoBorder = false;
        tdElement.Margin = new MarginInfo(8.0, 2.0, 8.0, 2.0);

        tdElement.Alignment = HorizontalAlignment.Center;

        TextState cellTextState = new TextState();
        cellTextState.ForegroundColor = Color.DarkBlue;
        cellTextState.FontSize = 7.5F;
        cellTextState.FontStyle = FontStyles.Bold;
        cellTextState.Font = FontRepository.FindFont("Arial");
        tdElement.DefaultCellTextState = cellTextState;

        tdElement.IsWordWrapped = true;
        tdElement.VerticalAlignment = VerticalAlignment.Center;

        tdElement.ColSpan = colSpan;
        tdElement.RowSpan = rowSpan;
    }
}

TableTRElement footTrElement = tableTFootElement.CreateTR();
footTrElement.AlternativeText = "صف القدم";

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.CreateTD();
    tdElement.SetText(String.Format("قدم {0}", colIndex));
}

// حفظ مستند PDF الموسوم
document.Save(dataDir + "StyleTableCell.pdf");

// التحقق من مطابقة PDF/UA
document = new Document(dataDir + "StyleTableCell.pdf");
bool isPdfUaCompliance = document.Validate(dataDir + "StyleTableCell.xml", PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("مطابقة PDF/UA: {0}", isPdfUaCompliance));
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
                "contactType": "مبيعات",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
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
    "applicationCategory": "مكتبة التعامل مع ملفات PDF لـ .NET",
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
```

