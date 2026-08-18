---
title: Extraia tabelas de PDF em Java
linktitle: Extrair tabela
type: docs
weight: 20
url: /java/extracting-table/
description: Aprenda como extrair dados de tabelas de documentos PDF existentes em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraia dados de tabelas de arquivos PDF com Java
Abstract: Este artigo explica como extrair tabelas de documentos PDF usando Aspose.PDF para Java. Ele mostra como usar o TableAbsorber para detectar tabelas por página, iterar linhas e células e coletar texto de células para processamento downstream.
---
Use `TableAbsorber` quando precisar detectar estruturas de tabelas em um PDF existente e ler seu conteúdo.

## Extraia texto de tabelas detectadas

Use este exemplo quando precisar localizar tabelas em cada página e coletar o texto das células.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Visite cada página com [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Itere através de tabelas, linhas e células absorvidas e, em seguida, produza o texto extraído.

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
