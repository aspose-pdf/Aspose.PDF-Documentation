---
title: Manipulate Tables in existing PDF
linktitle: Manipulate Tables
type: docs
weight: 30
url: /java/manipulate-tables-in-existing-pdf/
description: Manipulate tables in existing PDF file and replace old table with a new one in PDF document with Aspose.PDF for Java.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Manipulate Tables in PDF using Aspose.PDF for Java
Abstract: The article discusses the enhanced capabilities of Aspose.PDF for Java in manipulating tables within PDF documents. Initially, the library supported adding tables to new or existing PDFs, including integration with databases to create dynamic tables. The latest release introduces a feature for searching and parsing existing tables in a PDF using the new `Aspose.PDF.Text.TableAbsorber` class, which is similar to the existing `TextFragmentAbsorber`. A code example demonstrates updating the content of a specific table cell using this class. Additionally, the article explains how to replace an old table with a new one in a PDF document using the `TableAbsorber` class's `Replace()` method. A detailed code snippet illustrates this process, showing how to find a table, create a new table, and replace the old one within the PDF.
SoftwareApplication: java  
---

## Manipulate tables in existing PDF

One of the earliest features supported by Aspose.PDF for Java is its capabilities of Working with Tables and it provides great support for adding tables in PDF files being generated from scratch or any existing PDF files. You also get the capability to Integrate Table with Database (DOM) to create dynamic tables based on database contents. In this new release, we have implemented new feature of searching and parsing simple tables that already exist on page of PDF document. A new class named **Aspose.PDF.Text.TableAbsorber** provides these capabilities. The usage of TableAbsorber is very much similar to existing TextFragmentAbsorber class. 

The following code snippet shows the steps to update contents in particular table cell.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleManipulate {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ManipulateTables() {

        // Load existing PDF file
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Create TableAbsorber object to find tables
        TableAbsorber absorber = new TableAbsorber();

        // Visit first page with absorber
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // Get access to first table on page, their first cell and text fragments in it
        TextFragment fragment = absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1);

        // Change text of the first text fragment in the cell
        fragment.setText("hi world");

        pdfDocument.save(_dataDir + "ManipulateTable_out.pdf");
    }
```

## Replace old Table with a new one in PDF document

In case you need to find a particular table and replace it with the desired one, you can use Replace() the method of [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) Class in order to do that. 

Following example demonstrate the functionality to replace the table inside PDF document:

```java
public static void ReplaceOldTableWithNew() {

        // Load existing PDF document
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // Create TableAbsorber object to find tables
        TableAbsorber absorber = new TableAbsorber();

        Page page = pdfDocument.getPages().get_Item(1);

        // Visit first page with absorber
        absorber.visit(page);

        // Get first table on the page
        AbsorbedTable table = absorber.getTableList().get(0);

        // Create new table
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder (new BorderInfo(BorderSide.All, 1F));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");

        // Replace the table with new one
        absorber.replace(page, table, newTable);

        // Save document
        pdfDocument.save(_dataDir + "TableReplaced_out.pdf");
        
    }

}
```
