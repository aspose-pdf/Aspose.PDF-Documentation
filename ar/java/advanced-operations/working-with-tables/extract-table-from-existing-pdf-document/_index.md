---
title: استخراج جدول من مستند PDF موجود
linktitle: استخراج جدول
type: docs
weight: 25
url: /ar/java/extract-table-from-existing-pdf-document/
description: تجعل Aspose.PDF for Java من الممكن تنفيذ عمليات مختلفة مع الجداول الموجودة في مستند PDF الخاص بك. يمكنك إضافة واستخراج جدول في مستند PDF موجود، وعرض الجدول في صفحة جديدة وغيرها.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج جدول من PDF

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
        // تحميل مستند PDF المصدر
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