---
title: Working with Table in Tagged PDFs 
linktitle: Working with Table in Tagged PDFs
type: docs
weight: 40
url: /java/working-with-table-in-tagged-pdfs/
description: This article explains how to works with table in Tagged PDF document with Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Manipulate Tables in Tagged PDFs using Aspose.PDF for Java
Abstract: The article provides a comprehensive guide on creating and styling tables in Tagged PDF documents using the Aspose.PDF for Java library, specifically from version 19.6 or greater. It outlines the use of various classes and methods such as `TableElement` and `createTableElement()` from the `ITaggedContent` interface to construct tables. The guide includes detailed code snippets demonstrating how to create table elements including headers, bodies, footers, rows, and cells with specific styling attributes. Key styling features are highlighted, such as background color, borders, alignment, and text state, along with capabilities for setting spans and verifying PDF/UA compliance. The document further details the application of these styles at the table, row, and cell levels, providing example code snippets for each. The article serves as a resource for developers looking to enhance their PDF documents programmatically with well-structured tables.
SoftwareApplication: java
---

{{% alert color="primary" %}}

This feature is supported by version 19.6 or greater.

{{% /alert %}}

## Create Table in Tagged PDF

Aspose.PDF for Java allows creating a table in Tagged PDF documents. For working with tables, the API provides [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement) class. In order to create a table, you can use [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) method of [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) interface. Furthermore, you can use [createTHead()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTHead--), [createTBody()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTBody--) and [createTFoot()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement#createTFoot--) methods of TableElement class for creating Table Head, Table Body, and Table Foot respectively. To create a table row, you can use [createTR()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableRowCollectionElement#createTR--) method of [TableRowCollectionElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableRowCollectionElement) class. The following code snippet shows, how to create a table in the Tagged PDF document: 

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Create document
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Example table");
taggedContent.setLanguage("en-US");

// Get root structure element
StructureElement rootElement = taggedContent.getRootElement();


TableElement tableElement = taggedContent.createTableElement();
rootElement.appendChild(tableElement);

tableElement.setBorder(new BorderInfo(BorderSide.All, 1.2F, Color.getDarkBlue()));

TableTHeadElement tableTHeadElement = tableElement.createTHead();
TableTBodyElement tableTBodyElement = tableElement.createTBody();
TableTFootElement tableTFootElement = tableElement.createTFoot();
int rowCount = 50;
int colCount = 4;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.createTR();
headTrElement.setAlternativeText("Head Row");

headTrElement.setBackgroundColor(Color.getLightGray());

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Head %s", colIndex));

    thElement.setBackgroundColor(Color.getGreenYellow());
    thElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getLightGray()));

    thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));

    thElement.setAlignment(HorizontalAlignment.Right);
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Row %s", rowIndex));

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

        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Cell [%s, %s]", rowIndex, colIndex));


        tdElement.setBackgroundColor(Color.getYellow());
        tdElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getGray()));


        tdElement.setMargin(new MarginInfo(8.0, 2.0, 8.0, 2.0));

        tdElement.setAlignment(HorizontalAlignment.Center);

        TextState cellTextState = new TextState();
        cellTextState.setForegroundColor(Color.getDarkBlue());
        cellTextState.setFontSize(7.5F);
        cellTextState.setFontStyle(FontStyles.Bold);
        cellTextState.setFont(FontRepository.findFont("Arial"));
        tdElement.setDefaultCellTextState(cellTextState);

        tdElement.isWordWrapped();
        tdElement.setVerticalAlignment(VerticalAlignment.Center);

        tdElement.setColSpan(colSpan);
        tdElement.setRowSpan(rowSpan);
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Foot Row");

footTrElement.setBackgroundColor(Color.getLightSeaGreen());

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Foot %s", colIndex));

    tdElement.setAlignment(HorizontalAlignment.Center);
    tdElement.getStructureTextState().setFontSize(7F);
    tdElement.getStructureTextState().setFontStyle(FontStyles.Bold);
}


StructureAttributes tableAttributes = tableElement.getAttributes().getAttributes(AttributeOwnerStandard.Table);
StructureAttribute summaryAttribute = new StructureAttribute(AttributeKey.Summary);
summaryAttribute.setStringValue("The summary text for table");
tableAttributes.setAttribute(summaryAttribute);


// Save Tagged Pdf Document
document.save(path + "CreateTableElement.pdf");
```

## Style Table Element

Aspose.PDF for Java allows styling a table in Tagged PDF document. In order to style a table, you can create a table using [createTableElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createTableElement--) method of [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent) interface.  and set style table using properties of [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableElement) class. The following is the list properties you can use to style a table:

- BackgroundColor
- Border
- Alignment
- CornerStyle
- Broken
- ColumnAdjustment
- ColumnWidths
- DefaultCellBorder
- DefaultCellPadding
- DefaultCellTextState
- DefaultColumnWidth
- IsBroken
- IsBordersIncluded
- Left
- Top

The following code snippet shows how to style a table in Tagged PDF document:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Create document
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Example table style");
taggedContent.setLanguage("en-US");

// Get root structure element
StructureElement rootElement = taggedContent.getRootElement();


// Create table structure element
TableElement tableElement = taggedContent.createTableElement();
rootElement.appendChild(tableElement);


tableElement.setBackgroundColor(Color.getBeige());
tableElement.setBorder(new BorderInfo(BorderSide.All, 0.80F, Color.getGray()));
tableElement.setAlignment(HorizontalAlignment.Center);
tableElement.setBroken(TableBroken.Vertical);
tableElement.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);
tableElement.setColumnWidths("80 80 80 80 80");
tableElement.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.50F, Color.getDarkBlue()));
tableElement.setDefaultCellPadding(new MarginInfo(16.0, 2.0, 8.0, 2.0));
tableElement.getDefaultCellTextState().setForegroundColor(Color.getDarkCyan());
tableElement.getDefaultCellTextState().setFontSize(8F);
tableElement.setDefaultColumnWidth("70");

tableElement.setBroken(false);
tableElement.setBordersIncluded(true);

tableElement.setLeft(0F);
tableElement.setTop(40F);

tableElement.setRepeatingColumnsCount(2);
tableElement.setRepeatingRowsCount(3);
TextState rowStyle = new TextState();
rowStyle.setBackgroundColor(Color.getLightCoral());
tableElement.setRepeatingRowsStyle(rowStyle);




TableTHeadElement tableTHeadElement = tableElement.createTHead();
TableTBodyElement tableTBodyElement = tableElement.createTBody();
TableTFootElement tableTFootElement = tableElement.createTFoot();
int rowCount = 10;
int colCount = 5;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.createTR();
headTrElement.setAlternativeText("Head Row");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Head %s", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Row %s", rowIndex));

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Cell [%s, %s]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Foot Row");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Foot %s", colIndex));
}

// Save Tagged Pdf Document
document.save(path + "StyleTableElement.pdf");
```

## Style Table Row

Aspose.PDF for Java allows styling a table row in Tagged PDF document. In order to style a table row, you can use the properties of [TableTRElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableTRElement) class. The following is the list properties you can use to style a table row:

- BackgroundColor
- Border
- DefaultCellBorder
- MinRowHeight
- FixedRowHeight
- IsInNewPage
- IsRowBroken
- DefaultCellTextState
- DefaultCellPadding
- VerticalAlignment

The following code snippet shows how to style a table row in the Tagged PDF document:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Create document
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Example table row style");
taggedContent.setLanguage("en-US");

// Get root structure element
StructureElement rootElement = taggedContent.getRootElement();


// Create table structure element
TableElement tableElement = taggedContent.createTableElement();
rootElement.appendChild(tableElement);


TableTHeadElement tableTHeadElement = tableElement.createTHead();
TableTBodyElement tableTBodyElement = tableElement.createTBody();
TableTFootElement tableTFootElement = tableElement.createTFoot();
int rowCount = 7;
int colCount = 3;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.createTR();
headTrElement.setAlternativeText("Head Row");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Head %s", colIndex));
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Row %s", rowIndex));

    trElement.setBackgroundColor(Color.getLightSeaGreen());
    trElement.setBorder(new BorderInfo(BorderSide.All, 0.75F, Color.getDarkGray()));

    trElement.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.50F, Color.getBlue()));
    trElement.setMinRowHeight(100.0);
    trElement.setFixedRowHeight(120.0);
    trElement.setRowBroken(true);

    TextState cellTextState = new TextState();
    cellTextState.setForegroundColor(Color.getRed());
    trElement.setDefaultCellTextState(cellTextState);

    trElement.setDefaultCellPadding(new MarginInfo(16.0, 2.0, 8.0, 2.0));
    trElement.setVerticalAlignment(VerticalAlignment.Bottom);

    for (colIndex = 0; colIndex < colCount; colIndex++)
    {
        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Cell [{0}, {1}]", rowIndex, colIndex));
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Foot Row");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Foot %s", colIndex));
}



// Save Tagged Pdf Document
document.save(path + "StyleTableRow.pdf");
```

## Style Table Cell

Aspose.PDF for Java allows styling a table cell in Tagged PDF document. In order to style a table cell, you can use the properties of [TableCellElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/TableCellElement) class. The following is the list properties you can use to style a table cell:

- BackgroundColor
- Border
- IsNoBorder
- Margin
- Alignment
- DefaultCellTextState
- IsWordWrapped
- VerticalAlignment
- ColSpan
- RowSpan

The following code snippet shows how to style a table cell in the Tagged PDF document. You can also verify **PDF/UA** compliance of the created document. Code snippet below show how to use this functionality.

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = Utils.getDataDir() + "TaggedPDFs\\";

// Create document
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Example table cell style");
taggedContent.setLanguage("en-US");

// Get root structure element
StructureElement rootElement = taggedContent.getRootElement();


// Create table structure element
TableElement tableElement = taggedContent.createTableElement();
rootElement.appendChild(tableElement);


TableTHeadElement tableTHeadElement = tableElement.createTHead();
TableTBodyElement tableTBodyElement = tableElement.createTBody();
TableTFootElement tableTFootElement = tableElement.createTFoot();
int rowCount = 4;
int colCount = 4;
int rowIndex;
int colIndex;

TableTRElement headTrElement = tableTHeadElement.createTR();
headTrElement.setAlternativeText("Head Row");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTHElement thElement = headTrElement.createTH();
    thElement.setText(String.format("Head %s", colIndex));

    thElement.setBackgroundColor(Color.getGreenYellow());
    thElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getGray()));

    thElement.setNoBorder(false);
    thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));

    thElement.setAlignment(HorizontalAlignment.Right);
}

for (rowIndex = 0; rowIndex < rowCount; rowIndex++)
{
    TableTRElement trElement = tableTBodyElement.createTR();
    trElement.setAlternativeText(String.format("Row %s", rowIndex));

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

        TableTDElement tdElement = trElement.createTD();
        tdElement.setText(String.format("Cell [%s, %s]", rowIndex, colIndex));


        tdElement.setBackgroundColor(Color.getYellow());
        tdElement.setBorder(new BorderInfo(BorderSide.All, 4.0F, Color.getGray()));

        tdElement.setNoBorder(false);
        tdElement.setMargin(new MarginInfo(8.0, 2.0, 8.0, 2.0));

        tdElement.setAlignment(HorizontalAlignment.Center);

        TextState cellTextState = new TextState();
        cellTextState.setForegroundColor(Color.getDarkBlue());
        cellTextState.setFontSize(7.5F);
        cellTextState.setFontStyle(FontStyles.Bold);
        cellTextState.setFont(FontRepository.findFont("Arial"));
        tdElement.setDefaultCellTextState(cellTextState);

        tdElement.setWordWrapped(false);
        tdElement.setVerticalAlignment(VerticalAlignment.Center);

        tdElement.setColSpan(colSpan);
        tdElement.setRowSpan(rowSpan);
    }
}

TableTRElement footTrElement = tableTFootElement.createTR();
footTrElement.setAlternativeText("Foot Row");

for (colIndex = 0; colIndex < colCount; colIndex++)
{
    TableTDElement tdElement = footTrElement.createTD();
    tdElement.setText(String.format("Foot %s", colIndex));
}


// Save Tagged Pdf Document
document.save(path + "StyleTableCell.pdf");
```
