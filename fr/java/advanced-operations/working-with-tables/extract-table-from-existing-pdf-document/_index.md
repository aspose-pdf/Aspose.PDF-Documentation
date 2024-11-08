---
title: Extraire un tableau d'un document PDF existant
linktitle: Extraire un tableau
type: docs
weight: 25
url: /fr/java/extract-table-from-existing-pdf-document/
description: Aspose.PDF pour Java permet d'effectuer diverses manipulations avec les tableaux contenus dans votre document PDF. Vous pouvez ajouter et extraire un tableau dans le document PDF existant, rendre le tableau sur une nouvelle page, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire un tableau du PDF

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
        // Charger le document PDF source
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