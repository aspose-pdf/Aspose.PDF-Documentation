---
title: Manipular tabelas em documentos PDF existentes
linktitle: Manipular Tabelas
type: docs
weight: 40
url: /java/manipulating-tables/
description: Aprenda como inspecionar e modificar tabelas em documentos PDF existentes usando Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspecione e modifique tabelas PDF existentes com Java
Abstract: Este artigo explica como manipular tabelas já presentes em documentos PDF usando Aspose.PDF para Java. Ele cobre a localização de tabelas com TableAbsorber, atualização de texto dentro de uma célula e substituição de uma tabela detectada por um novo objeto Table.
---
Use `TableAbsorber` quando precisar localizar tabelas existentes e atualizar seu conteúdo.

## Substituir texto dentro de uma célula da tabela

Use este exemplo quando o texto em uma célula detectada precisar ser atualizado sem reconstruir a tabela inteira.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e visite a página com [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Valide se a tabela de destino e os fragmentos de texto da célula existem.
1. Substitua o texto da célula e salve o documento atualizado.

```java
public static void replaceCells(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }
        if (absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0).getTextFragments().size() == 0) {
            throw new IllegalStateException("The target cell has no text fragments.");
        }

        absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1).setText("New Value");
        document.save(outputFile.toString());
    }
}
```

## Substitua uma tabela detectada por uma nova tabela

Use este exemplo quando a tabela original precisar ser totalmente substituída por uma recém-construída.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e detecte tabelas na página.
1. Crie uma nova [Tabela](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) com a estrutura desejada.
1. Substitua a tabela absorvida e salve o PDF de saída.

```java
public static void replaceTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }

        AbsorbedTable oldTable = absorber.getTableList().get(0);
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1.0f));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");
        row = newTable.getRows().add();
        row.getCells().add("Col 12");
        row.getCells().add("Col 22");
        row.getCells().add("Col 32");

        absorber.replace(document.getPages().get_Item(1), oldTable, newTable);
        document.save(outputFile.toString());
    }
}
```
