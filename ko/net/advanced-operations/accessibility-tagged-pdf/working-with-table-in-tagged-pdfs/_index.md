---
title: 태그가 있는 PDF에서 테이블 작업하기
linktitle: 태그가 있는 PDF에서 테이블 작업하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/working-with-table-in-tagged-pdfs/
description: 이 문서에서는 Aspose.PDF for .NET을 사용하여 태그가 있는 PDF 문서에서 테이블 작업하는 방법을 설명합니다.
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
    "abstract": "Aspose.PDF for .NET의 새로운 기능은 사용자가 태그가 있는 PDF 문서 내에서 테이블을 원활하게 생성하고 스타일을 지정할 수 있도록 합니다. 이 기능은 문서 접근성과 준수를 향상시켜 테이블 헤더, 본문 및 바닥글을 추가하면서 PDF/UA 준수를 유지할 수 있게 합니다. 다양한 사용자 정의 가능한 속성을 통해 사용자는 특정 형식 요구 사항을 충족하기 위해 테이블 스타일(테두리, 배경 및 정렬 포함)을 쉽게 조작할 수 있습니다.",
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
    "description": "이 문서에서는 Aspose.PDF for .NET을 사용하여 태그가 있는 PDF 문서에서 테이블 작업하는 방법을 설명합니다."
}
</script>

## 태그가 있는 PDF에서 테이블 생성

Aspose.PDF for .NET은 태그가 있는 PDF 문서에서 테이블을 생성할 수 있게 합니다. 테이블 작업을 위해 API는 [TableElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement) 클래스를 제공합니다. 테이블을 생성하려면 [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) 인터페이스의 [CreateTableElement()](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createtableelement) 메서드를 사용할 수 있습니다. 또한, [TableElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement) 클래스의 [CreateTHead()](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/methods/createthead), [CreateTBody()](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/methods/createtbody) 및 [CreateTFoot()](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/methods/createtfoot) 메서드를 사용하여 각각 테이블 헤드, 테이블 본문 및 테이블 바닥글을 생성할 수 있습니다. 테이블 행을 생성하려면 [TableRowCollectionElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablerowcollectionelement) 클래스의 [CreateTR()](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablerowcollectionelement/methods/createtr) 메서드를 사용할 수 있습니다. 생성된 PDF 문서가 PDF/UA 준수인지 확인하려면 Document 클래스의 Validate() 메서드를 사용할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작업합니다.

다음 코드 스니펫은 태그가 있는 PDF 문서에서 테이블을 생성하는 방법을 보여줍니다:

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

## 테이블 요소 스타일 지정

Aspose.PDF for .NET은 태그가 있는 PDF 문서에서 테이블을 스타일링할 수 있게 합니다. 테이블을 스타일링하려면 [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) 인터페이스의 [CreateTableElement()](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createtableelement) 메서드를 사용하여 테이블을 생성하고 [TableElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement) 클래스의 속성을 사용하여 테이블 스타일을 설정할 수 있습니다. 다음은 테이블 스타일을 지정하는 데 사용할 수 있는 속성 목록입니다:

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

다음 코드 스니펫은 태그가 있는 PDF 문서에서 테이블을 스타일링하는 방법을 보여줍니다:

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

## 테이블 행 스타일 지정

Aspose.PDF for .NET은 태그가 있는 PDF 문서에서 테이블 행을 스타일링할 수 있게 합니다. 테이블 행을 스타일링하려면 [TableTRElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tabletrelement) 클래스의 속성을 사용할 수 있습니다. 다음은 테이블 행을 스타일링하는 데 사용할 수 있는 속성 목록입니다:

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

다음 코드 스니펫은 태그가 있는 PDF 문서에서 테이블 행을 스타일링하는 방법을 보여줍니다:

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

## 테이블 셀 스타일 지정

Aspose.PDF for .NET은 태그가 있는 PDF 문서에서 테이블 셀을 스타일링할 수 있게 합니다. 테이블 셀을 스타일링하려면 [TableCellElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement) 클래스의 속성을 사용할 수 있습니다. 다음은 테이블 셀을 스타일링하는 데 사용할 수 있는 속성 목록입니다:

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

다음 코드 스니펫은 태그가 있는 PDF 문서에서 테이블 셀을 스타일링하는 방법을 보여줍니다:

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