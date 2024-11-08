---
title: 既存のPDFドキュメントからテーブルを抽出する
linktitle: テーブルを抽出
type: docs
weight: 25
url: /ja/java/extract-table-from-existing-pdf-document/
description: Aspose.PDF for Javaを使用すると、PDFドキュメント内に含まれるテーブルを様々に操作することが可能です。既存のPDFドキュメントにテーブルを追加および抽出したり、新しいページにテーブルをレンダリングしたりできます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFからテーブルを抽出する

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
        // ソースPDFドキュメントをロードする
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