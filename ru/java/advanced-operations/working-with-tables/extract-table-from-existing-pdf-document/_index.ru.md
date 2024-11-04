---
title: Извлечение таблицы из существующего PDF-документа
linktitle: Извлечение таблицы
type: docs
weight: 25
url: /java/extract-table-from-existing-pdf-document/
description: Aspose.PDF для Java позволяет выполнять различные манипуляции с таблицами, содержащимися в вашем PDF-документе. Вы можете добавить и извлечь таблицу в существующем PDF-документе, отобразить таблицу на новой странице и т.д.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Извлечение таблицы из PDF

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
        // Загрузить исходный PDF-документ
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