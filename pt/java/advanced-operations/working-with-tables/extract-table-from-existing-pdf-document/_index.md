---
title: Extrair tabelas de PDF em Java
linktitle: Extrair tabela
type: docs
weight: 20
url: /pt/java/extracting-table/
description: Saiba como extrair dados de tabela de documentos PDF existentes em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair dados de tabela de arquivos PDF com Java
Abstract: Este artigo explica como extrair tabelas de documentos PDF usando Aspose.PDF for Java. Ele mostra como usar TableAbsorber para detectar tabelas por página, iterar linhas e células, e coletar o texto das células para processamento subsequente.
aliases:
    - /pt/java/extract-table-from-existing-pdf-document/
---
Use `TableAbsorber` quando precisar detectar estruturas de tabela em um PDF existente e ler seu conteúdo.

## Extrair texto de tabelas detectadas

Use este exemplo quando precisar localizar tabelas em cada página e coletar o texto de suas células.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Visitar cada página com [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Itere através de tabelas absorvidas, linhas e células e, em seguida, gere o texto extraído.

```java
public static void extract(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);
            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table ----");
                for (AbsorbedRow row : table.getRowList()) {
                    System.out.println("Row:");
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
