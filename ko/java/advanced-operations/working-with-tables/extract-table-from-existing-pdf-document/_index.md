---
title: 기존 PDF 문서에서 테이블 추출
linktitle: 테이블 추출
type: docs
weight: 25
url: ko/java/extract-table-from-existing-pdf-document/
description: Aspose.PDF for Java를 사용하면 PDF 문서에 포함된 테이블에 대한 다양한 조작을 수행할 수 있습니다. 기존 PDF 문서에서 테이블을 추가 및 추출하고, 새 페이지에 테이블을 렌더링하는 등의 작업을 할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF에서 테이블 추출

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
        // 소스 PDF 문서 로드
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