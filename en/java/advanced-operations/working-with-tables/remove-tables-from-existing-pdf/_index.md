---
title: Remove Tables from existing PDF
linktitle: Remove Tables
type: docs
weight: 40
url: /java/remove-tables-from-existing-pdf/
description: Aspose.PDF for Java allows you to remove table and multiple tables from your PDF document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: 
Abstract: This article discusses the functionality of the Aspose.PDF for Java library, specifically focusing on the ability to manipulate tables within PDF documents. It highlights the use of the `TableAbsorber` class to locate and remove tables from existing PDF files. The article provides detailed code examples demonstrating how to remove a single table from a PDF document using the `Remove` method of the `TableAbsorber` class. Additionally, it explains how to remove multiple tables from a PDF by iterating through the collection of tables identified by `TableAbsorber`. These functionalities simplify the process of editing PDF documents by allowing developers to efficiently manage table structures within them.
---

{{% alert color="primary" %}}

Aspose.PDF for Java offers the capabilities to insert/create Table inside PDF document while its being generated from scratch or you can also add the table object in any existing PDF document. However you may have a requirement to [Manipulate Tables in existing PDF](https://docs.aspose.com/pdf/java/manipulate-tables-in-existing-pdf/) where you can update the contents in existing table cells. However you may come across a requirement to remove table objects from existing PDF document.

{{% /alert %}}

In order to remove the tables, we need to use [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) class to get hold of tables in existing PDF and then call [Remove](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#remove-com.aspose.pdf.AbsorbedTable-) method.

## Remove Table from PDF document

We have added new function i.e. Remove() to the existing [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) Class in order to remove table from PDF document. Once the absorber successfully finds tables on the page, it becomes capable to remove them. Please check following code snippet showing how to remove a table from PDF document:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRemoveTable {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RemoveTable() {
        // Load existing PDF document
        Document pdfDocument = new Document(_dataDir + "Table_input.pdf");

        // Create TableAbsorber object to find tables
        TableAbsorber absorber = new TableAbsorber();

        // Visit first page with absorber
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // Get first table on the page
        AbsorbedTable table = absorber.getTableList().get(0);

        // Remove the table
        absorber.remove(table);

        // Save PDF
        pdfDocument.save(_dataDir + "Table_out.pdf");
    }  
```

## Remove Multiple Tables from PDF document

Sometimes a PDF document may contain more than one table and you may come up with a requirement to remove multiple tables from it. In order to remove multiple tables from PDF document, please use the following code snippet:

```java
    public static void RemoveMultipleTable() {
        // Load existing PDF document
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // Create TableAbsorber object to find tables
        TableAbsorber absorber = new TableAbsorber();

        // Visit second page with absorber
        absorber.visit(pdfDocument.getPages().get_Item(2));

        // Loop through the copy of collection and removing tables
        for (AbsorbedTable table : absorber.getTableList())
            absorber.remove(table);

        // Save document
        pdfDocument.save(_dataDir + "Table2_out.pdf");
    }
}
```

