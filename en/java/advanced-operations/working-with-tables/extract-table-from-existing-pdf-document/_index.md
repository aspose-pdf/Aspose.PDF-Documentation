---
title: Extract Tables from PDF in Java
linktitle: Extract Table
type: docs
weight: 20
url: /java/extracting-table/
description: Learn how to extract table data from existing PDF documents in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract table data from PDF files with Java
Abstract: This article explains how to extract tables from PDF documents using Aspose.PDF for Java. It shows how to use TableAbsorber to detect tables by page, iterate rows and cells, and collect cell text for downstream processing.
---
Use `TableAbsorber` when you need to detect table structures in an existing PDF and read their content.

## Extract table data from an existing PDF

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [TableAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/tableabsorber/) and visit each target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Iterate through each detected [AbsorbedTable](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/absorbedrow/), and [AbsorbedCell](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/absorbedcell/).
1. Read the extracted [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) values and output the collected table content.

```java
public static void extract(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);
            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table ----");
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            for (TextSegment segment : fragment.getSegments()) {
                                cellText.append(segment.getText());
                            }
                        }
                        rowText.append(" | ").append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```
