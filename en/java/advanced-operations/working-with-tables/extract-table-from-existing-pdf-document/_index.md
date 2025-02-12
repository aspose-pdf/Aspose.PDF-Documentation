---
title: Extract Table from Existing PDF Document
linktitle: Extract Table
type: docs
weight: 25
url: /java/extract-table-from-existing-pdf-document/
description: Aspose.PDF for Java makes it possible to carry out various manipulations with the tables contained in your pdf document. You may add and extract a table in the existing PDF document, render table on a new page and etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Extract Table from PDF using Aspose.PDF for Java
Abstract: The article presents a Java program that extracts tables from a PDF document using the Aspose.PDF library. The program, part of the `com.aspose.pdf.examples` package, defines a class `ExampleExtractTable` that includes a method `Extract_Table()`. This method loads a specified PDF file, iterates through its pages, and employs the `TableAbsorber` class to identify and extract tables. Within each table, it navigates through rows and cells to gather text fragments, ultimately printing the extracted text to the console. The example illustrates how to programmatically access and retrieve tabular data from PDF documents using Aspose.PDF in Java.
SoftwareApplication: java  
---

## Extract Table from PDF

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

import jdk.jshell.spi.ExecutionControl.NotImplementedException;

import java.io.*;
import java.util.*;

public class ExampleExtractTable {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Extract_Table()
    {
        // Load source PDF document
        Document pdfDocument = new Document(_dataDir + "the_worlds_cities_in_2018_data_booklet 7.pdf");
        for(Page page : pdfDocument.getPages())
        {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);
            for (AbsorbedTable table : absorber.getTableList())
            {
                for (AbsorbedRow row : table.getRowList())
                {
                    for (AbsorbedCell cell : row.getCellList())
                    {
                        TextFragmentCollection textFragmentCollection = cell.getTextFragments();
                        for (TextFragment fragment : textFragmentCollection)
                        {
                            String txt = "";
                            for (TextSegment seg : fragment.getSegments())
                                txt += seg.getText();
                            System.out.println(txt);
                        }
                    }
                }
            }
        }
    }
```
