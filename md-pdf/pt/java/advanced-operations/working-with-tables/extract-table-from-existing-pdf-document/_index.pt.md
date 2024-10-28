---
title: Extrair Tabela de Documento PDF Existente
linktitle: Extrair Tabela
type: docs
weight: 25
url: /java/extract-table-from-existing-pdf-document/
description: Aspose.PDF para Java torna possível realizar várias manipulações com as tabelas contidas no seu documento pdf. Você pode adicionar e extrair uma tabela no documento PDF existente, renderizar a tabela em uma nova página, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair Tabela do PDF

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
        // Carregar documento PDF de origem
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