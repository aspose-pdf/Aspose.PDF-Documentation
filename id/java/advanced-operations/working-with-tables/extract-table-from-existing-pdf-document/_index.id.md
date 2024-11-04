---
title: Ekstrak Tabel dari Dokumen PDF yang Ada
linktitle: Ekstrak Tabel
type: docs
weight: 25
url: /java/extract-table-from-existing-pdf-document/
description: Aspose.PDF untuk Java memungkinkan untuk melakukan berbagai manipulasi dengan tabel yang terdapat dalam dokumen pdf Anda. Anda dapat menambahkan dan mengekstrak tabel dalam dokumen PDF yang ada, merender tabel pada halaman baru, dan lain-lain.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak Tabel dari PDF

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
        // Muat dokumen PDF sumber
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