---
title: العمل مع الجداول في ملفات PDF المعلّمة
linktitle: العمل مع الجداول في ملفات PDF المعلّمة
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/working-with-table-in-tagged-pdfs/
description: يشرح هذا المقال كيفية العمل مع الجداول في مستند PDF المعلّم مع Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Table in Tagged PDFs",
    "alternativeHeadline": "Streamlined Table Creation in Tagged PDFs",
    "abstract": "تتيح الوظيفة الجديدة في Aspose.PDF for .NET للمستخدمين إنشاء وتنسيق الجداول بسلاسة داخل مستندات PDF المعلّمة. تعزز هذه الميزة إمكانية الوصول إلى المستندات والامتثال، مما يسمح بإضافة رؤوس الجداول، والأجسام، والتذييلات مع الحفاظ على الامتثال لمعايير PDF/UA. مع مجموعة متنوعة من الخصائص القابلة للتخصيص، يمكن للمستخدمين بسهولة تعديل أنماط الجداول، بما في ذلك الحدود، والخلفيات، والمحاذاة، لتلبية متطلبات التنسيق المحددة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "table, Tagged PDF, Aspose.PDF for .NET, CreateTableElement, TableElement, style table, table row, table cell, PDF/UA compliance, manipulate tables",
    "wordcount": "2179",
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
    "url": "/net/working-with-table-in-tagged-pdfs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-table-in-tagged-pdfs/"
    },
    "dateModified": "2024-11-25",
    "description": "يشرح هذا المقال كيفية العمل مع الجداول في مستند PDF المعلّم مع Aspose.PDF for .NET."
}
</script>

## إنشاء جدول في PDF المعلّم

Aspose.PDF for .NET يتيح إنشاء جدول في مستندات PDF المعلّمة. للعمل مع الجداول، توفر واجهة برمجة التطبيقات [TableElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement) class. لإنشاء جدول، يمكنك استخدام [CreateTableElement()](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createtableelement) method of [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) interface. علاوة على ذلك، يمكنك استخدام [CreateTHead()](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/methods/createthead)، [CreateTBody()](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/methods/createtbody) و [CreateTFoot()](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/methods/createtfoot) methods of TableElement class لإنشاء رأس الجدول، جسم الجدول، وتذييل الجدول على التوالي. لإنشاء صف جدول، يمكنك استخدام [CreateTR()](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablerowcollectionelement/methods/createtr) method of [TableRowCollectionElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablerowcollectionelement) class. يمكنك أيضًا التحقق مما إذا كان مستند PDF الذي تم إنشاؤه يتوافق مع PDF/UA باستخدام Validate() method of Document class.

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

توضح مقتطفات الشيفرة التالية كيفية إنشاء جدول في مستند PDF المعلّم:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        taggedContent.SetTitle("Example table");
        taggedContent.SetLanguage("en-US");

        // Get root structure element
        Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

        Aspose.Pdf.LogicalStructure.TableElement tableElement = taggedContent.CreateTableElement();
        rootElement.AppendChild(tableElement);

        tableElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1.2F, Aspose.Pdf.Color.DarkBlue);

        Aspose.Pdf.LogicalStructure.TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
        Aspose.Pdf.LogicalStructure.TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
        Aspose.Pdf.LogicalStructure.TableTFootElement tableTFootElement = tableElement.CreateTFoot();
        int rowCount = 50;
        int colCount = 4;
        int rowIndex;
        int colIndex;

        Aspose.Pdf.LogicalStructure.TableTRElement headTrElement = tableTHeadElement.CreateTR();
        headTrElement.AlternativeText = "Head Row";

        headTrElement.BackgroundColor = Aspose.Pdf.Color.LightGray;

        for (colIndex = 0; colIndex < colCount; colIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTHElement thElement = headTrElement.CreateTH();
            thElement.SetText(String.Format("Head {0}", colIndex));

            thElement.BackgroundColor = Aspose.Pdf.Color.GreenYellow;
            thElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 4.0F, Aspose.Pdf.Color.Gray);

            thElement.IsNoBorder = true;
            thElement.Margin = new Aspose.Pdf.MarginInfo(16.0, 2.0, 8.0, 2.0);

            thElement.Alignment = Aspose.Pdf.HorizontalAlignment.Right;
        }

        for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTRElement trElement = tableTBodyElement.CreateTR();
            trElement.AlternativeText = string.Format("Row {0}", rowIndex);

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

                Aspose.Pdf.LogicalStructure.TableTDElement tdElement = trElement.CreateTD();
                tdElement.SetText(String.Format("Cell [{0}, {1}]", rowIndex, colIndex));

                tdElement.BackgroundColor = Aspose.Pdf.Color.Yellow;
                tdElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 4.0F, Aspose.Pdf.Color.Gray);

                tdElement.IsNoBorder = false;
                tdElement.Margin = new Aspose.Pdf.MarginInfo(8.0, 2.0, 8.0, 2.0);

                tdElement.Alignment = Aspose.Pdf.HorizontalAlignment.Center;

                var cellTextState = new Aspose.Pdf.Text.TextState();
                cellTextState.ForegroundColor = Aspose.Pdf.Color.DarkBlue;
                cellTextState.FontSize = 7.5F;
                cellTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
                cellTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
                tdElement.DefaultCellTextState = cellTextState;

                tdElement.IsWordWrapped = true;
                tdElement.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;

                tdElement.ColSpan = colSpan;
                tdElement.RowSpan = rowSpan;
            }
        }

        Aspose.Pdf.LogicalStructure.TableTRElement footTrElement = tableTFootElement.CreateTR();
        footTrElement.AlternativeText = "Foot Row";

        footTrElement.BackgroundColor = Aspose.Pdf.Color.LightSeaGreen;

        for (colIndex = 0; colIndex < colCount; colIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTDElement tdElement = footTrElement.CreateTD();
            tdElement.SetText(String.Format("Foot {0}", colIndex));

            tdElement.Alignment = Aspose.Pdf.HorizontalAlignment.Center;
            tdElement.StructureTextState.FontSize = 7F;
            tdElement.StructureTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        }

        Aspose.Pdf.LogicalStructure.StructureAttributes tableAttributes = tableElement.Attributes.GetAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Table);
        var summaryAttribute = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.Summary);
        summaryAttribute.SetStringValue("The summary text for table");
        tableAttributes.SetAttribute(summaryAttribute);

        // Save Tagged PDF Document
        document.Save(dataDir + "CreateTableElement_out.pdf");
    }

    // Check PDF/UA compliance
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateTableElement_out.pdf"))
    {
        bool isPdfUaCompliance = document.Validate(dataDir + "CreateTableElement_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
        Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document1 = new Aspose.Pdf.Document();
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document1.TaggedContent;

    taggedContent.SetTitle("Example table");
    taggedContent.SetLanguage("en-US");

    // Get root structure element
    Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

    Aspose.Pdf.LogicalStructure.TableElement tableElement = taggedContent.CreateTableElement();
    rootElement.AppendChild(tableElement);

    tableElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1.2F, Aspose.Pdf.Color.DarkBlue);

    Aspose.Pdf.LogicalStructure.TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
    Aspose.Pdf.LogicalStructure.TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
    Aspose.Pdf.LogicalStructure.TableTFootElement tableTFootElement = tableElement.CreateTFoot();
    int rowCount = 50;
    int colCount = 4;
    int rowIndex;
    int colIndex;

    Aspose.Pdf.LogicalStructure.TableTRElement headTrElement = tableTHeadElement.CreateTR();
    headTrElement.AlternativeText = "Head Row";

    headTrElement.BackgroundColor = Aspose.Pdf.Color.LightGray;

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        Aspose.Pdf.LogicalStructure.TableTHElement thElement = headTrElement.CreateTH();
        thElement.SetText(String.Format("Head {0}", colIndex));

        thElement.BackgroundColor = Aspose.Pdf.Color.GreenYellow;
        thElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 4.0F, Aspose.Pdf.Color.Gray);

        thElement.IsNoBorder = true;
        thElement.Margin = new Aspose.Pdf.MarginInfo(16.0, 2.0, 8.0, 2.0);

        thElement.Alignment = Aspose.Pdf.HorizontalAlignment.Right;
    }

    for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
    {
        Aspose.Pdf.LogicalStructure.TableTRElement trElement = tableTBodyElement.CreateTR();
        trElement.AlternativeText = string.Format("Row {0}", rowIndex);

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

            Aspose.Pdf.LogicalStructure.TableTDElement tdElement = trElement.CreateTD();
            tdElement.SetText(String.Format("Cell [{0}, {1}]", rowIndex, colIndex));

            tdElement.BackgroundColor = Aspose.Pdf.Color.Yellow;
            tdElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 4.0F, Aspose.Pdf.Color.Gray);

            tdElement.IsNoBorder = false;
            tdElement.Margin = new Aspose.Pdf.MarginInfo(8.0, 2.0, 8.0, 2.0);

            tdElement.Alignment = Aspose.Pdf.HorizontalAlignment.Center;

            var cellTextState = new Aspose.Pdf.Text.TextState();
            cellTextState.ForegroundColor = Aspose.Pdf.Color.DarkBlue;
            cellTextState.FontSize = 7.5F;
            cellTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
            cellTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            tdElement.DefaultCellTextState = cellTextState;

            tdElement.IsWordWrapped = true;
            tdElement.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;

            tdElement.ColSpan = colSpan;
            tdElement.RowSpan = rowSpan;
        }
    }

    Aspose.Pdf.LogicalStructure.TableTRElement footTrElement = tableTFootElement.CreateTR();
    footTrElement.AlternativeText = "Foot Row";

    footTrElement.BackgroundColor = Aspose.Pdf.Color.LightSeaGreen;

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        Aspose.Pdf.LogicalStructure.TableTDElement tdElement = footTrElement.CreateTD();
        tdElement.SetText(String.Format("Foot {0}", colIndex));

        tdElement.Alignment = Aspose.Pdf.HorizontalAlignment.Center;
        tdElement.StructureTextState.FontSize = 7F;
        tdElement.StructureTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
    }

    Aspose.Pdf.LogicalStructure.StructureAttributes tableAttributes = tableElement.Attributes.GetAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Table);
    var summaryAttribute = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.Summary);
    summaryAttribute.SetStringValue("The summary text for table");
    tableAttributes.SetAttribute(summaryAttribute);

    // Save Tagged PDF Document
    document1.Save(dataDir + "CreateTableElement_out.pdf");

    // Check PDF/UA compliance
    using var document2 = new Aspose.Pdf.Document(dataDir + "CreateTableElement_out.pdf");
    bool isPdfUaCompliance = document2.Validate(dataDir + "CreateTableElement_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
    Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
}
```
{{< /tab >}}
{{< /tabs >}}

## تنسيق عنصر الجدول

Aspose.PDF for .NET يتيح تنسيق جدول في مستند PDF المعلّم. لتنسيق جدول، يمكنك إنشاء جدول باستخدام [CreateTableElement()](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createtableelement) method of [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) interface وتعيين تنسيق الجدول باستخدام خصائص [TableElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement) class. فيما يلي قائمة الخصائص التي يمكنك استخدامها لتنسيق جدول:

- [BackgroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/backgroundcolor).
- [Border](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/border).
- [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/alignment).
- [CornerStyle](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/cornerstyle).
- [Broken](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/broken).
- [ColumnAdjustment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/columnadjustment).
- [ColumnWidths](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/columnwidths).
- [DefaultCellBorder](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcellborder).
- [DefaultCellPadding](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcellpadding).
- [DefaultCellTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcelltextstate).
- [DefaultColumnWidth](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/defaultcolumnwidth).
- [IsBroken](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/isbroken).
- [IsBordersIncluded](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/isbordersincluded).
- [Left](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/left).
- [Top](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/properties/top).

توضح مقتطفات الشيفرة التالية كيفية تنسيق جدول في مستند PDF المعلّم:

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void StyleTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        taggedContent.SetTitle("Example table style");
        taggedContent.SetLanguage("en-US");

        // Get root structure element
        Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

        // Create table structure element
        Aspose.Pdf.LogicalStructure.TableElement tableElement = taggedContent.CreateTableElement();
        rootElement.AppendChild(tableElement);

        tableElement.BackgroundColor = Aspose.Pdf.Color.Beige;
        tableElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.80F, Aspose.Pdf.Color.Gray);
        tableElement.Alignment = Aspose.Pdf.HorizontalAlignment.Center;
        tableElement.Broken = Aspose.Pdf.TableBroken.Vertical;
        tableElement.ColumnAdjustment = Aspose.Pdf.ColumnAdjustment.AutoFitToWindow;
        tableElement.ColumnWidths = "80 80 80 80 80";
        tableElement.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.50F, Aspose.Pdf.Color.DarkBlue);
        tableElement.DefaultCellPadding = new Aspose.Pdf.MarginInfo(16.0, 2.0, 8.0, 2.0);
        tableElement.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.DarkCyan;
        tableElement.DefaultCellTextState.FontSize = 8F;
        tableElement.DefaultColumnWidth = "70";

        tableElement.IsBroken = false;
        tableElement.IsBordersIncluded = true;

        tableElement.Left = 0F;
        tableElement.Top = 40F;

        tableElement.RepeatingColumnsCount = 2;
        tableElement.RepeatingRowsCount = 3;
        var rowStyle = new Aspose.Pdf.Text.TextState();
        rowStyle.BackgroundColor = Aspose.Pdf.Color.LightCoral;
        tableElement.RepeatingRowsStyle = rowStyle;

        Aspose.Pdf.LogicalStructure.TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
        Aspose.Pdf.LogicalStructure.TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
        Aspose.Pdf.LogicalStructure.TableTFootElement tableTFootElement = tableElement.CreateTFoot();
        int rowCount = 10;
        int colCount = 5;
        int rowIndex;
        int colIndex;

        Aspose.Pdf.LogicalStructure.TableTRElement headTrElement = tableTHeadElement.CreateTR();
        headTrElement.AlternativeText = "Head Row";

        for (colIndex = 0; colIndex < colCount; colIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTHElement thElement = headTrElement.CreateTH();
            thElement.SetText(String.Format("Head {0}", colIndex));
        }

        for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTRElement trElement = tableTBodyElement.CreateTR();
            trElement.AlternativeText = String.Format("Row {0}", rowIndex);

            for (colIndex = 0; colIndex < colCount; colIndex++)
            {
                Aspose.Pdf.LogicalStructure.TableTDElement tdElement = trElement.CreateTD();
                tdElement.SetText(String.Format("Cell [{0}, {1}]", rowIndex, colIndex));
            }
        }

        Aspose.Pdf.LogicalStructure.TableTRElement footTrElement = tableTFootElement.CreateTR();
        footTrElement.AlternativeText = "Foot Row";

        for (colIndex = 0; colIndex < colCount; colIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTDElement tdElement = footTrElement.CreateTD();
            tdElement.SetText(String.Format("Foot {0}", colIndex));
        }

        // Save Tagged PDF Document
        document.Save(dataDir + "StyleTableElement_out.pdf");
    }

    // Check PDF/UA compliance
    using (var document = new Aspose.Pdf.Document(dataDir + "StyleTableElement_out.pdf"))
    {
        bool isPdfUaCompliance = document.Validate(dataDir + "StyleTableElement_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
        Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void StyleTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document1 = new Aspose.Pdf.Document();
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document1.TaggedContent;

    taggedContent.SetTitle("Example table style");
    taggedContent.SetLanguage("en-US");

    // Get root structure element
    Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

    // Create table structure element
    Aspose.Pdf.LogicalStructure.TableElement tableElement = taggedContent.CreateTableElement();
    rootElement.AppendChild(tableElement);

    tableElement.BackgroundColor = Aspose.Pdf.Color.Beige;
    tableElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.80F, Aspose.Pdf.Color.Gray);
    tableElement.Alignment = Aspose.Pdf.HorizontalAlignment.Center;
    tableElement.Broken = Aspose.Pdf.TableBroken.Vertical;
    tableElement.ColumnAdjustment = Aspose.Pdf.ColumnAdjustment.AutoFitToWindow;
    tableElement.ColumnWidths = "80 80 80 80 80";
    tableElement.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.50F, Aspose.Pdf.Color.DarkBlue);
    tableElement.DefaultCellPadding = new Aspose.Pdf.MarginInfo(16.0, 2.0, 8.0, 2.0);
    tableElement.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.DarkCyan;
    tableElement.DefaultCellTextState.FontSize = 8F;
    tableElement.DefaultColumnWidth = "70";

    tableElement.IsBroken = false;
    tableElement.IsBordersIncluded = true;

    tableElement.Left = 0F;
    tableElement.Top = 40F;

    tableElement.RepeatingColumnsCount = 2;
    tableElement.RepeatingRowsCount = 3;
    var rowStyle = new Aspose.Pdf.Text.TextState();
    rowStyle.BackgroundColor = Aspose.Pdf.Color.LightCoral;
    tableElement.RepeatingRowsStyle = rowStyle;

    Aspose.Pdf.LogicalStructure.TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
    Aspose.Pdf.LogicalStructure.TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
    Aspose.Pdf.LogicalStructure.TableTFootElement tableTFootElement = tableElement.CreateTFoot();
    int rowCount = 10;
    int colCount = 5;
    int rowIndex;
    int colIndex;

    Aspose.Pdf.LogicalStructure.TableTRElement headTrElement = tableTHeadElement.CreateTR();
    headTrElement.AlternativeText = "Head Row";

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        Aspose.Pdf.LogicalStructure.TableTHElement thElement = headTrElement.CreateTH();
        thElement.SetText(String.Format("Head {0}", colIndex));
    }

    for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
    {
        Aspose.Pdf.LogicalStructure.TableTRElement trElement = tableTBodyElement.CreateTR();
        trElement.AlternativeText = String.Format("Row {0}", rowIndex);

        for (colIndex = 0; colIndex < colCount; colIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTDElement tdElement = trElement.CreateTD();
            tdElement.SetText(String.Format("Cell [{0}, {1}]", rowIndex, colIndex));
        }
    }

    Aspose.Pdf.LogicalStructure.TableTRElement footTrElement = tableTFootElement.CreateTR();
    footTrElement.AlternativeText = "Foot Row";

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        Aspose.Pdf.LogicalStructure.TableTDElement tdElement = footTrElement.CreateTD();
        tdElement.SetText(String.Format("Foot {0}", colIndex));
    }

    // Save Tagged PDF Document
    document1.Save(dataDir + "StyleTableElement_out.pdf");

    // Check PDF/UA compliance
    using var document2 = new Aspose.Pdf.Document(dataDir + "StyleTableElement_out.pdf");
    bool isPdfUaCompliance = document2.Validate(dataDir + "StyleTableElement_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
    Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
}
```
{{< /tab >}}
{{< /tabs >}}

## تنسيق صف الجدول

Aspose.PDF for .NET يتيح تنسيق صف جدول في مستند PDF المعلّم. لتنسيق صف جدول، يمكنك استخدام خصائص [TableTRElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tabletrelement) class. فيما يلي قائمة الخصائص التي يمكنك استخدامها لتنسيق صف جدول:

- BackgroundColor.
- Border.
- DefaultCellBorder.
- MinRowHeight.
- FixedRowHeight.
- IsInNewPage.
- IsRowBroken.
- DefaultCellTextState.
- DefaultCellPadding.
- VerticalAlignment.

توضح مقتطفات الشيفرة التالية كيفية تنسيق صف جدول في مستند PDF المعلّم:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void StyleTableRow()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        taggedContent.SetTitle("Example table row style");
        taggedContent.SetLanguage("en-US");

        // Get root structure element
        Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

        // Create table structure element
        Aspose.Pdf.LogicalStructure.TableElement tableElement = taggedContent.CreateTableElement();
        rootElement.AppendChild(tableElement);

        Aspose.Pdf.LogicalStructure.TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
        Aspose.Pdf.LogicalStructure.TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
        Aspose.Pdf.LogicalStructure.TableTFootElement tableTFootElement = tableElement.CreateTFoot();
        int rowCount = 7;
        int colCount = 3;
        int rowIndex;
        int colIndex;

        Aspose.Pdf.LogicalStructure.TableTRElement headTrElement = tableTHeadElement.CreateTR();
        headTrElement.AlternativeText = "Head Row";

        for (colIndex = 0; colIndex < colCount; colIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTHElement thElement = headTrElement.CreateTH();
            thElement.SetText(string.Format("Head {0}", colIndex));
        }

        for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTRElement trElement = tableTBodyElement.CreateTR();
            trElement.AlternativeText = string.Format("Row {0}", rowIndex);

            trElement.BackgroundColor = Aspose.Pdf.Color.LightGoldenrodYellow;
            trElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.75F, Aspose.Pdf.Color.DarkGray);

            trElement.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.50F, Aspose.Pdf.Color.Blue);
            trElement.MinRowHeight = 100.0;
            trElement.FixedRowHeight = 120.0;
            trElement.IsInNewPage = (rowIndex % 3 == 1);
            trElement.IsRowBroken = true;

            var cellTextState = new Aspose.Pdf.Text.TextState();
            cellTextState.ForegroundColor = Aspose.Pdf.Color.Red;
            trElement.DefaultCellTextState = cellTextState;

            trElement.DefaultCellPadding = new Aspose.Pdf.MarginInfo(16.0, 2.0, 8.0, 2.0);
            trElement.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom;

            for (colIndex = 0; colIndex < colCount; colIndex++)
            {
                Aspose.Pdf.LogicalStructure.TableTDElement tdElement = trElement.CreateTD();
                tdElement.SetText(string.Format("Cell [{0}, {1}]", rowIndex, colIndex));
            }
        }

        Aspose.Pdf.LogicalStructure.TableTRElement footTrElement = tableTFootElement.CreateTR();
        footTrElement.AlternativeText = "Foot Row";

        for (colIndex = 0; colIndex < colCount; colIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTDElement tdElement = footTrElement.CreateTD();
            tdElement.SetText(string.Format("Foot {0}", colIndex));
        }

        // Save Tagged PDF Document
        document.Save(dataDir + "StyleTableRow_out.pdf");
    }

    // Check PDF/UA compliance
    using (var document = new Aspose.Pdf.Document(dataDir + "StyleTableRow_out.pdf"))
    {
        bool isPdfUaCompliance = document.Validate(dataDir + "StyleTableRow_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
        Console.WriteLine(string.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void StyleTableRow()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document1 = new Aspose.Pdf.Document();
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document1.TaggedContent;

    taggedContent.SetTitle("Example table row style");
    taggedContent.SetLanguage("en-US");

    // Get root structure element
    Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

    // Create table structure element
    Aspose.Pdf.LogicalStructure.TableElement tableElement = taggedContent.CreateTableElement();
    rootElement.AppendChild(tableElement);

    Aspose.Pdf.LogicalStructure.TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
    Aspose.Pdf.LogicalStructure.TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
    Aspose.Pdf.LogicalStructure.TableTFootElement tableTFootElement = tableElement.CreateTFoot();
    int rowCount = 7;
    int colCount = 3;
    int rowIndex;
    int colIndex;

    Aspose.Pdf.LogicalStructure.TableTRElement headTrElement = tableTHeadElement.CreateTR();
    headTrElement.AlternativeText = "Head Row";

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        Aspose.Pdf.LogicalStructure.TableTHElement thElement = headTrElement.CreateTH();
        thElement.SetText(string.Format("Head {0}", colIndex));
    }

    for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
    {
        Aspose.Pdf.LogicalStructure.TableTRElement trElement = tableTBodyElement.CreateTR();
        trElement.AlternativeText = string.Format("Row {0}", rowIndex);

        trElement.BackgroundColor = Aspose.Pdf.Color.LightGoldenrodYellow;
        trElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.75F, Aspose.Pdf.Color.DarkGray);

        trElement.DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.50F, Aspose.Pdf.Color.Blue);
        trElement.MinRowHeight = 100.0;
        trElement.FixedRowHeight = 120.0;
        trElement.IsInNewPage = (rowIndex % 3 == 1);
        trElement.IsRowBroken = true;

        var cellTextState = new Aspose.Pdf.Text.TextState();
        cellTextState.ForegroundColor = Aspose.Pdf.Color.Red;
        trElement.DefaultCellTextState = cellTextState;

        trElement.DefaultCellPadding = new Aspose.Pdf.MarginInfo(16.0, 2.0, 8.0, 2.0);
        trElement.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom;

        for (colIndex = 0; colIndex < colCount; colIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTDElement tdElement = trElement.CreateTD();
            tdElement.SetText(string.Format("Cell [{0}, {1}]", rowIndex, colIndex));
        }
    }

    Aspose.Pdf.LogicalStructure.TableTRElement footTrElement = tableTFootElement.CreateTR();
    footTrElement.AlternativeText = "Foot Row";

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        Aspose.Pdf.LogicalStructure.TableTDElement tdElement = footTrElement.CreateTD();
        tdElement.SetText(string.Format("Foot {0}", colIndex));
    }

    // Save Tagged PDF Document
    document1.Save(dataDir + "StyleTableRow_out.pdf");

    // Check PDF/UA compliance
    using var document2 = new Aspose.Pdf.Document(dataDir + "StyleTableRow_out.pdf");
    bool isPdfUaCompliance = document2.Validate(dataDir + "StyleTableRow_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
    Console.WriteLine(string.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
}
```
{{< /tab >}}
{{< /tabs >}}

## تنسيق خلية الجدول

Aspose.PDF for .NET يتيح تنسيق خلية جدول في مستند PDF المعلّم. لتنسيق خلية جدول، يمكنك استخدام خصائص [TableCellElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement) class. فيما يلي قائمة الخصائص التي يمكنك استخدامها لتنسيق خلية جدول:

- [BackgroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/backgroundcolor).
- [Border](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/border).
- [IsNoBorder](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/isnoborder).
- [Margin](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/margin).
- [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/alignment).
- [DefaultCellTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/defaultcelltextstate).
- [IsWordWrapped](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/iswordwrapped).
- [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/verticalalignment).
- [ColSpan](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/colspan).
- [RowSpan](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement/properties/rowspan).

توضح مقتطفات الشيفرة التالية كيفية تنسيق خلية جدول في مستند PDF المعلّم:

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void StyleTableCell()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        taggedContent.SetTitle("Example table cell style");
        taggedContent.SetLanguage("en-US");

        // Get root structure element
        Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

        // Create table structure element
        Aspose.Pdf.LogicalStructure.TableElement tableElement = taggedContent.CreateTableElement();
        rootElement.AppendChild(tableElement);

        Aspose.Pdf.LogicalStructure.TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
        Aspose.Pdf.LogicalStructure.TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
        Aspose.Pdf.LogicalStructure.TableTFootElement tableTFootElement = tableElement.CreateTFoot();
        int rowCount = 4;
        int colCount = 4;
        int rowIndex;
        int colIndex;

        Aspose.Pdf.LogicalStructure.TableTRElement headTrElement = tableTHeadElement.CreateTR();
        headTrElement.AlternativeText = "Head Row";

        for (colIndex = 0; colIndex < colCount; colIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTHElement thElement = headTrElement.CreateTH();
            thElement.SetText(string.Format("Head {0}", colIndex));

            thElement.BackgroundColor = Aspose.Pdf.Color.GreenYellow;
            thElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 4.0F, Aspose.Pdf.Color.Gray);

            thElement.IsNoBorder = true;
            thElement.Margin = new Aspose.Pdf.MarginInfo(16.0, 2.0, 8.0, 2.0);

            thElement.Alignment = Aspose.Pdf.HorizontalAlignment.Right;
        }

        for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTRElement trElement = tableTBodyElement.CreateTR();
            trElement.AlternativeText = string.Format("Row {0}", rowIndex);

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

                Aspose.Pdf.LogicalStructure.TableTDElement tdElement = trElement.CreateTD();
                tdElement.SetText(string.Format("Cell [{0}, {1}]", rowIndex, colIndex));

                tdElement.BackgroundColor = Aspose.Pdf.Color.Yellow;
                tdElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 4.0F, Aspose.Pdf.Color.Gray);

                tdElement.IsNoBorder = false;
                tdElement.Margin = new Aspose.Pdf.MarginInfo(8.0, 2.0, 8.0, 2.0);

                tdElement.Alignment = Aspose.Pdf.HorizontalAlignment.Center;

                var cellTextState = new Aspose.Pdf.Text.TextState();
                cellTextState.ForegroundColor = Aspose.Pdf.Color.DarkBlue;
                cellTextState.FontSize = 7.5F;
                cellTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
                cellTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
                tdElement.DefaultCellTextState = cellTextState;

                tdElement.IsWordWrapped = true;
                tdElement.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;

                tdElement.ColSpan = colSpan;
                tdElement.RowSpan = rowSpan;
            }
        }

        Aspose.Pdf.LogicalStructure.TableTRElement footTrElement = tableTFootElement.CreateTR();
        footTrElement.AlternativeText = "Foot Row";

        for (colIndex = 0; colIndex < colCount; colIndex++)
        {
            Aspose.Pdf.LogicalStructure.TableTDElement tdElement = footTrElement.CreateTD();
            tdElement.SetText(string.Format("Foot {0}", colIndex));
        }

        // Save Tagged PDF Document
        document.Save(dataDir + "StyleTableCell_out.pdf");
    }

    // Check PDF/UA compliance
    using (var document = new Aspose.Pdf.Document(dataDir + "StyleTableCell_out.pdf"))
    {
        bool isPdfUaCompliance = document.Validate(dataDir + "StyleTableCell_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
        Console.WriteLine(string.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void StyleTableCell()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document1 = new Aspose.Pdf.Document();
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document1.TaggedContent;

    taggedContent.SetTitle("Example table cell style");
    taggedContent.SetLanguage("en-US");

    // Get root structure element
    Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

    // Create table structure element
    Aspose.Pdf.LogicalStructure.TableElement tableElement = taggedContent.CreateTableElement();
    rootElement.AppendChild(tableElement);

    Aspose.Pdf.LogicalStructure.TableTHeadElement tableTHeadElement = tableElement.CreateTHead();
    Aspose.Pdf.LogicalStructure.TableTBodyElement tableTBodyElement = tableElement.CreateTBody();
    Aspose.Pdf.LogicalStructure.TableTFootElement tableTFootElement = tableElement.CreateTFoot();
    int rowCount = 4;
    int colCount = 4;
    int rowIndex;
    int colIndex;

    Aspose.Pdf.LogicalStructure.TableTRElement headTrElement = tableTHeadElement.CreateTR();
    headTrElement.AlternativeText = "Head Row";

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        Aspose.Pdf.LogicalStructure.TableTHElement thElement = headTrElement.CreateTH();
        thElement.SetText(string.Format("Head {0}", colIndex));

        thElement.BackgroundColor = Aspose.Pdf.Color.GreenYellow;
        thElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 4.0F, Aspose.Pdf.Color.Gray);

        thElement.IsNoBorder = true;
        thElement.Margin = new Aspose.Pdf.MarginInfo(16.0, 2.0, 8.0, 2.0);

        thElement.Alignment = Aspose.Pdf.HorizontalAlignment.Right;
    }

    for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
    {
        Aspose.Pdf.LogicalStructure.TableTRElement trElement = tableTBodyElement.CreateTR();
        trElement.AlternativeText = string.Format("Row {0}", rowIndex);

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

            Aspose.Pdf.LogicalStructure.TableTDElement tdElement = trElement.CreateTD();
            tdElement.SetText(string.Format("Cell [{0}, {1}]", rowIndex, colIndex));

            tdElement.BackgroundColor = Aspose.Pdf.Color.Yellow;
            tdElement.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 4.0F, Aspose.Pdf.Color.Gray);

            tdElement.IsNoBorder = false;
            tdElement.Margin = new Aspose.Pdf.MarginInfo(8.0, 2.0, 8.0, 2.0);

            tdElement.Alignment = Aspose.Pdf.HorizontalAlignment.Center;

            var cellTextState = new Aspose.Pdf.Text.TextState();
            cellTextState.ForegroundColor = Aspose.Pdf.Color.DarkBlue;
            cellTextState.FontSize = 7.5F;
            cellTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
            cellTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            tdElement.DefaultCellTextState = cellTextState;

            tdElement.IsWordWrapped = true;
            tdElement.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;

            tdElement.ColSpan = colSpan;
            tdElement.RowSpan = rowSpan;
        }
    }

    Aspose.Pdf.LogicalStructure.TableTRElement footTrElement = tableTFootElement.CreateTR();
    footTrElement.AlternativeText = "Foot Row";

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        Aspose.Pdf.LogicalStructure.TableTDElement tdElement = footTrElement.CreateTD();
        tdElement.SetText(string.Format("Foot {0}", colIndex));
    }

    // Save Tagged PDF Document
    document1.Save(dataDir + "StyleTableCell_out.pdf");

    // Check PDF/UA compliance
    using var document2 = new Aspose.Pdf.Document(dataDir + "StyleTableCell_out.pdf");
    bool isPdfUaCompliance = document2.Validate(dataDir + "StyleTableCell_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
    Console.WriteLine(string.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
}
```
{{< /tab >}}
{{< /tabs >}}

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