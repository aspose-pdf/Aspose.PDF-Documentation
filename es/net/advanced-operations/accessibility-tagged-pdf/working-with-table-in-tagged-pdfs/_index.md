---
title: Trabajando con Tablas en PDFs Etiquetados
linktitle: Trabajando con Tablas en PDFs Etiquetados
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/working-with-table-in-tagged-pdfs/
description: Este artículo explica cómo trabajar con tablas en documentos PDF etiquetados con Aspose.PDF for .NET.
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
    "abstract": "La nueva funcionalidad en Aspose.PDF for .NET permite a los usuarios crear y dar estilo a tablas dentro de documentos PDF etiquetados de manera fluida. Esta característica mejora la accesibilidad y el cumplimiento del documento, permitiendo la adición de encabezados, cuerpos y pies de tabla mientras se mantiene el cumplimiento de PDF/UA. Con una variedad de propiedades personalizables, los usuarios pueden manipular fácilmente los estilos de las tablas, incluidos bordes, fondos y alineaciones, para cumplir con requisitos de formato específicos.",
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
    "description": "Este artículo explica cómo trabajar con tablas en documentos PDF etiquetados con Aspose.PDF for .NET."
}
</script>

## Crear Tabla en PDF Etiquetado

Aspose.PDF for .NET permite crear una tabla en documentos PDF etiquetados. Para trabajar con tablas, la API proporciona la clase [TableElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement). Para crear una tabla, puedes usar el método [CreateTableElement()](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createtableelement) de la interfaz [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent). Además, puedes usar los métodos [CreateTHead()](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/methods/createthead), [CreateTBody()](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/methods/createtbody) y [CreateTFoot()](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement/methods/createtfoot) de la clase TableElement para crear el Encabezado de la Tabla, el Cuerpo de la Tabla y el Pie de la Tabla respectivamente. Para crear una fila de tabla, puedes usar el método [CreateTR()](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablerowcollectionelement/methods/createtr) de la clase [TableRowCollectionElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablerowcollectionelement). También puedes verificar si el documento PDF creado cumple con PDF/UA usando el método Validate() de la clase Document.

El siguiente fragmento de código también trabaja con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

El siguiente fragmento de código muestra cómo crear una tabla en el documento PDF etiquetado:

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

## Estilo del Elemento de Tabla

Aspose.PDF for .NET permite dar estilo a una tabla en el documento PDF etiquetado. Para dar estilo a una tabla, puedes crear una tabla usando el método [CreateTableElement()](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createtableelement) de la interfaz [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) y establecer el estilo de la tabla usando las propiedades de la clase [TableElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tableelement). La siguiente es la lista de propiedades que puedes usar para dar estilo a una tabla:

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

El siguiente fragmento de código muestra cómo dar estilo a una tabla en el documento PDF etiquetado:

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

## Estilo de la Fila de Tabla

Aspose.PDF for .NET permite dar estilo a una fila de tabla en el documento PDF etiquetado. Para dar estilo a una fila de tabla, puedes usar las propiedades de la clase [TableTRElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tabletrelement). La siguiente es la lista de propiedades que puedes usar para dar estilo a una fila de tabla:

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

El siguiente fragmento de código muestra cómo dar estilo a una fila de tabla en el documento PDF etiquetado:

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

## Estilo de la Celda de Tabla

Aspose.PDF for .NET permite dar estilo a una celda de tabla en el documento PDF etiquetado. Para dar estilo a una celda de tabla, puedes usar las propiedades de la clase [TableCellElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/tablecellelement). La siguiente es la lista de propiedades que puedes usar para dar estilo a una celda de tabla:

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

El siguiente fragmento de código muestra cómo dar estilo a una celda de tabla en el documento PDF etiquetado:

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