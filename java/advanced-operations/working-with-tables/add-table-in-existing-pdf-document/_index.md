---
title: Create or Add Table In PDF using Aspose.PDF for Java
linktitle: Create or Add Table
type: docs
weight: 10
url: /java/add-table-in-existing-pdf-document/
description: Aspose.PDF for Java makes it possible to carry out various manipulations with the tables contained in your pdf document. You may add and extract a table in the existing PDF document, render table on a new page and etc.
lastmod: "2021-03-23"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Creating Table

 The Aspose.PDF namespace contains classes named [Table](http://www.aspose.com/api/java/pdf/com.aspose.pdf/classes/Table), [Cell](https://apireference.aspose.com/pdf/java/com.aspose.pdf/cell), and [Row](https://apireference.aspose.com/pdf/java/com.aspose.pdf/row) which provides functionality for creating tables when generating PDF documents from scratch.

Table can be created by creating object of Table Class.

```java
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Adding Table in Existing PDF Document

To add a table to an existing PDF file with Aspose.PDF for Java, take the following steps:

1. Load the source file.
1. Initialize a table and set its columns and rows.
1. Set table setting (we've set the borders).
1. Populate table.
1. Add the table to a page.
1. Save the file.

The following code snippets show how to add text in an existing PDF file.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddTable {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void CreateTable() {
        Document doc = new Document(_dataDir + "input.pdf");
        // Initializes a new instance of the Table
        Table table = new Table();
        // Set the table border color as LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // set the border for table cells
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // create a loop to add 10 rows
        for (int row_count = 1; row_count < 10; row_count++) {
            // add row to table
            Row row = table.getRows().add();
            // add table cells
            row.getCells().add("Column (" + row_count + ", 1)");
            row.getCells().add("Column (" + row_count + ", 2)");
            row.getCells().add("Column (" + row_count + ", 3)");
        }
        // Add table object to first page of input document
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // Save updated document containing table object
        doc.save(_dataDir + "document_with_table.pdf");
    }
```

### ColSpan and RowSpan in Aspose.PDF Tables using Java

Aspose.PDF for Java provides [setColSpan](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) method to merge the columns in a table and [setRowSpan](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) method to merge the rows.

We use [setColSpan](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) or [setRowSpan](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) methods on the [Cell](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Cell) object which creates the table cell. After applying the required properties the created cell can be added to the table.

```java
public static void AddTable_RowColSpan() {
        // Load source PDF document
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Initializes a new instance of the Table
        Table table = new Table();
        // Set the table border color as LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // Set the border for table cells
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // Add 1st row to table
        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            // Add table cells
            row1.getCells().add("Test 1 " + cellCount);
        }

        // Add 2nd row to table
        Row row2 = table.getRows().add();
        row2.getCells().add("Test 2 1");
        Cell cell = row2.getCells().add("Test 2 2");
        cell.setColSpan(2);
        row2.getCells().add("Test 2 4");

        // Add 3rd row to table
        Row row3 = table.getRows().add();
        row3.getCells().add("Test 3 1");
        row3.getCells().add("Test 3 2");
        row3.getCells().add("Test 3 3");
        row3.getCells().add("Test 3 4");

        // Add 4th row to table
        Row row4 = table.getRows().add();
        row3.getCells().add("Test 4 1");
        cell = row3.getCells().add("Test 4 2");
        cell.setRowSpan(2);
        row3.getCells().add("Test 4 3");
        row3.getCells().add("Test 4 4");

        // Add 5th row to table
        row4 = table.getRows().add();
        row4.getCells().add("Test 5 1");
        row4.getCells().add("Test 5 3");
        row4.getCells().add("Test 5 4");

        // Add table object to first page of input document
        page.getParagraphs().add(table);

        // Save updated document containing table object
        pdfDocument.save(_dataDir + "document_with_table_out.pdf");
    }
```

The result of the execution code below is the table depicted on the following image:

![ColSpan and RowSpan demo](colspan_rowspan.png)

## Working with Borders, Margins and Padding

Please note that it also supports the feature to set border style, margins and cell padding for tables. Before going into more technical details, it's important to understand the concepts of border, margins and padding which are presented below in a diagram:

![Borders, margins and padding](set-border-style-margins-and-padding-of-table_1.png)

In the above figure, you can see that the borders of table, row and cell overlap. Using Aspose.PDF, a table can have margins and cells can have paddings. To set cell margins, we have to set cell padding.

## Borders

To set the borders of Table, [Row](https://apireference.aspose.com/pdf/java/com.aspose.pdf/row)  and [Cell](https://apireference.aspose.com/pdf/java/com.aspose.pdf/cell) objects, use the [Table.setBorder](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Table#setBorder-com.aspose.pdf.BorderInfo-), [Row.setBorder](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Row#setBorder-com.aspose.pdf.BorderInfo-) and [Cell.setBorder](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Cell#setBorder-com.aspose.pdf.BorderInfo-) methods. Cell borders can also be set using the [Table](https://apireference.aspose.com/pdf/java/com.aspose.pdf/table) or [Row](https://apireference.aspose.com/pdf/java/com.aspose.pdf/row) class [DefaultCellBorder](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Row#setDefaultCellBorder-com.aspose.pdf.BorderInfo-) method. All border related properties discussed above are assigned an instance of the Row class, which is created by calling its constructor. The Row class has many overloads that take almost all the parameters required to customize the border.

## Margins or Padding

Cell padding can be managed using the Table class [DefaultCellPadding](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Table#setDefaultCellPadding-com.aspose.pdf.MarginInfo-) method. All padding related properties are assigned an instance of the [MarginInfo](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/MarginInfo) class that takes information about the `Left`, `Right`, `Top` and `Bottom` parameters to create custom margins.

In the following example, the width of the cell border is set to 0.1 point, the width of the table border is set to 1 point and cell padding is set to 5 points.

![Margin and Border in PDF Table](margin-border.png)

```java
public static void MargingPadding() {
        // Instntiate the Document object by calling its empty constructor
        Document doc = new Document();
        Page page = doc.getPages().add();
        // Instantiate a table object
        Table tab1 = new Table();
        // Add the table in paragraphs collection of the desired section
        page.getParagraphs().add(tab1);
        // Set with column widths of the table
        tab1.setColumnWidths ("50 50 50");
        // Set default cell border using BorderInfo object
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));
        // Set table border using another customized BorderInfo object
        tab1.setBorder (new BorderInfo(BorderSide.All, 1F));
        
        // Create MarginInfo object and set its left, bottom, right and top margins
        MarginInfo margin = new MarginInfo();
        margin.setTop (5f);
        margin.setLeft (5f);
        margin.setRight (5f);
        margin.setBottom (5f);
        
        // Set the default cell padding to the MarginInfo object
        tab1.setDefaultCellPadding(margin);
        
        // Create rows in the table and then cells in the rows
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 with large text string");
        
        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);
        
        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");
        
        // Save the PDF
        doc.save(_dataDir + "MarginsOrPadding_out.pdf");
    }
}
```

To create table with rounded corner, use the [BorderInfo](https://apireference.aspose.com/pdf/java/com.aspose.pdf/BorderInfo) class' `RoundedBorderRadius` value and set the table corner style to round.

```java
    public static void RoundedBorderRadius() {
        Document doc = new Document();
        Page page = doc.getPages().add();

        // Instantiate a table object
        Table tab1 = new Table();

        // Add the table in paragraphs collection of the desired section
        page.getParagraphs().add(tab1);

        GraphInfo graph = new GraphInfo();
        graph.setColor(Color.getRed());
        // Create a blank BorderInfo object
        BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
        // Set the border a rounder border where radius of round is 15
        bInfo.setRoundedBorderRadius(15);
        // Set the table Corner style as Round.
        tab1.setCornerStyle(BorderCornerStyle.Round);
        // Set the table border information
        tab1.setBorder(bInfo);
        // Create rows in the table and then cells in the rows
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 with large text string");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Save the PDF
        doc.save(_dataDir + "BorderRadius_out.pdf");
    }
```

### AutoFitToWindow property in ColumnAdjustmentType enumeration

```java
 public static void AutoFitToWindowProperty() {
        // Instntiate the Pdf object by calling its empty constructor
        Document doc = new Document();
        // Create the section in the Pdf object
        Page sec1 = doc.getPages().add();

        // Instantiate a table object
        Table tab1 = new Table();
        // Add the table in paragraphs collection of the desired section
        sec1.getParagraphs().add(tab1);

        // Set with column widths of the table
        tab1.setColumnWidths("50 50 50");
        tab1.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);

        // Set default cell border using BorderInfo object
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));

        // Set table border using another customized BorderInfo object
        tab1.setBorder(new BorderInfo(BorderSide.All, 1F));

        // Create MarginInfo object and set its left, bottom, right and top margins
        MarginInfo margin = new MarginInfo();
        margin.setTop(5f);
        margin.setLeft(5f);
        margin.setRight(5f);
        margin.setBottom(5f);

        // Set the default cell padding to the MarginInfo object
        tab1.setDefaultCellPadding(margin);

        // Create rows in the table and then cells in the rows
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Save updated document containing table object
        doc.save(_dataDir + "AutoFitToWindow_out.pdf");
    }
```

### Get Table Width

Sometimes, it is required to get table width dynamically. Aspose.PDF.Table class has a method [GetWidth](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Table#getWidth--) for the purpose. For example, you have not set table columns width explicitly and set [ColumnAdjustment](https://apireference.aspose.com/pdf/java/com.aspose.pdf/ColumnAdjustment) to AutoFitToContent. In this case you can get table width as following.

```java
public static void GetTableWidth() {
        // Create a new document
        Document doc = new Document();
        // Add page in document
        Page page = doc.getPages().add();

        // Initialize new table
        Table table = new Table();

        // Add the table in paragraphs collection of the desired section
        page.getParagraphs().add(table);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);

        // Add row in table
        Row row = table.getRows().add();
        // Add cell in table
        row.getCells().add("Cell 1 text");
        row.getCells().add("Cell 2 text");
        // Get table width
        System.out.println(table.getWidth());
    }
```

## Add SVG Object to Table Cell

Aspose.PDF for Java supports the feature to add a table cell into a PDF file. While creating a table, it is possible to add text or images into the cells. Furthermore, the API also offers the feature to convert SVG files to PDF format. Using a combination of these features, it is possible to load an SVG image and add it into a table cell.

The following code snippet shows the steps for creating a table instance and adding an SVG image inside a table cell.

```java
 public static void AddSVGObjectToTableCell() {
        // Instantiate Document object
        Document doc = new Document();
        // Create an image instance
        com.aspose.pdf.Image img = new com.aspose.pdf.Image();
        // Set image type as SVG
        img.setFileType (com.aspose.pdf.ImageFileType.Svg);
        // Path for source file
        img.setFile (_dataDir + "SVGToPDF.svg");
        // Set width for image instance
        img.setFixWidth (50);
        // Set height for image instance
        img.setFixHeight (50);        
        // Create table instance
        com.aspose.pdf.Table table = new com.aspose.pdf.Table();
        // Set width for table cells
        table.setColumnWidths ("100 100");
        // Create row object and add it to table instance
        com.aspose.pdf.Row row = table.getRows().add();
        // Create cell object and add it to row instance
        com.aspose.pdf.Cell cell = row.getCells().add();
        // Add textfragment to paragraphs collection of cell object
        cell.getParagraphs().add(new TextFragment("First cell"));
        // Add another cell to row object
        cell = row.getCells().add();
        // Add SVG image to paragraphs collection of recently added cell instance
        cell.getParagraphs().add(img);
        // Create page object and add it to pages collection of document instance
        Page page = doc.getPages().add();
        // Add table to paragraphs collection of page object
        page.getParagraphs().add(table);
        // Save PDF file
        doc.save(_dataDir + "AddSVGObject_out.pdf");
    }
```

## Add HTML Tags inside Table

Aspose.PDF for Java allows adding a new HTML Fragment into a Paragraph of your PDF file.

{{% alert color="primary" %}}

Please take into account that using of HTML Tags inside table element increases document generation time, as API needs to process HTML Tags accordingly and render them in the output PDF document.

{{% /alert %}}

```java
  public static void AddHTMLFragmentToTableCell() {
        Document doc = new Document(_dataDir + "input.pdf");
        // Initializes a new instance of the Table
        Table table = new Table();
        // Set the table border color as LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // set the border for table cells
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // create a loop to add 10 rows       
        for (int row_count = 1; row_count < 10; row_count++) {
            Cell cell;
            // add row to table
            Row row = table.getRows().add();
            // add table cells
            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Column <strong>(" + row_count + ", 1)</strong>"));
            
            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Column <span style='color:red'>(" + row_count + ", 2)</span>"));
            
            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Column <span style='text-decoration: underline'>(" + row_count + ", 3)</span>"));
        }
        // Add table object to first page of input document
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // Save updated document containing table object
        doc.save(_dataDir + "AddHTMLObject_out.pdf");
    }
    
}
```

## Insert a Page Break between rows of table

As a default behavior, when creating a table inside a PDF file, the table flows to subsequent pages when it reaches tables Bottom margin. However, we may have a requirement to forcefully insert page break when a certain number of rows are added for table. The following code snippet shows the steps to insert page break when 10 rows are added for the table.

```java
    public static void InsertPageBreak() {
        // Instantiate Document instance
        Document doc = new Document();
        // Add page to pages collection of PDF file
        Page page = doc.getPages().add();
        // Create table instance
        Table tab = new Table();
        // Set border style for table
        tab.setBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // Set default border style for table with border color as Red
        tab.setDefaultCellBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // Specify table columsn widht
        tab.setColumnWidths ("100 100");
        // Create a loop to add 200 rows for table
        for (int counter = 0; counter <= 200; counter++) {
            Row row = new Row();
            tab.getRows().add(row);
            Cell cell1 = new Cell();
            cell1.getParagraphs().add(new TextFragment("Cell " + counter + ", 0"));
            row.getCells().add(cell1);
            Cell cell2 = new Cell();
            cell2.getParagraphs().add(new TextFragment("Cell " + counter + ", 1"));
            row.getCells().add(cell2);
            // When 10 rows are added, render new row in new page
            if (counter % 10 == 0 && counter != 0)
                row.setInNewPage(true);
        }
        // Add table to paragraphs collection of PDF file
        page.getParagraphs().add(tab);

        // Save the PDF document
        doc.save(_dataDir + "InsertPageBreak_out.pdf");
    }
```

## Render Table on New Page

By default, paragraphs are added to a Page object's Paragraphs collection. However, it is possible to render a table on a new page instead of directly after the previously added paragraph level object on the page.

### Adding a Table

To render table on a new page, use the [IsInNewPage](https://apireference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) method in the [BaseParagraph](https://apireference.aspose.com/pdf/java/com.aspose.pdf/baseparagraph) class. The following code snippet shows how.

```java
public static void RenderTableOnNewPage(){
        Document doc = new Document();
        PageInfo pageInfo = doc.getPageInfo();
        MarginInfo marginInfo = pageInfo.getMargin();

        marginInfo.setLeft (37);
        marginInfo.setRight (37);
        marginInfo.setTop (37);
        marginInfo.setBottom (37);

        pageInfo.setLandscape(true);

        Table table = new Table();
        table.setColumnWidths ("50 100");
        // Added page.
        Page curPage = doc.getPages().add();
        for (int i = 1; i <= 120; i++)
        {
            Row row = table.getRows().add();
            row.setFixedRowHeight (15);
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("Content 1"));
            Cell cell2 = row.getCells().add();
            cell2.getParagraphs().add(new TextFragment("HHHHH"));
        }
        Paragraphs paragraphs = curPage.getParagraphs();
        paragraphs.add(table);
        /********************************************/
        Table table1 = new Table();
        table.setColumnWidths ("100 100");
        for (int i = 1; i <= 10; i++)
        {
            Row row = table1.getRows().add();
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("LAAAAAAA"));
            Cell cell2 = row.getCells().add();
            cell2.getParagraphs().add(new TextFragment("LAAGGGGGG"));
        }
        table1.setInNewPage (true);
        // I want to keep table 1 to next page please...
        paragraphs.add(table1);
        
        doc.save(_dataDir + "IsNewPageProperty_Test_out.pdf");
    }
}
```
