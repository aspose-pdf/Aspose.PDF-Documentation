---
title: Remover tabelas de documentos PDF existentes
linktitle: Remover tabelas
description: Aprenda como remover uma ou mais tabelas de documentos PDF existentes em Java.
lastmod: "2026-06-09"
type: docs
weight: 50
url: /java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exclua uma ou várias tabelas de arquivos PDF com Java
Abstract: Este artigo explica como remover tabelas de documentos PDF existentes usando Aspose.PDF para Java. Ele apresenta o TableAbsorber para localizar tabelas e demonstra como excluir uma única tabela ou remover todas as tabelas detectadas de uma página.
---
Use `TableAbsorber` quando precisar excluir uma ou mais tabelas detectadas de um PDF existente.

## Remover uma tabela detectada

Use este exemplo quando apenas a primeira tabela correspondente em uma página precisar ser excluída.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Visite a página de destino com [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. Remova a primeira tabela detectada e salve o documento.

```java
public static void removeOneTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        absorber.remove(absorber.getTableList().get(0));
        document.save(outputFile.toString());
    }
}
```

## Remover todas as tabelas detectadas de uma página

Use este exemplo quando todas as tabelas correspondentes na página precisarem ser removidas.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Visite a página de destino com [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) e copie as tabelas detectadas para uma lista.
1. Remova cada tabela detectada e salve o PDF atualizado.

```java
public static void removeAllTables(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        List<AbsorbedTable> tables = new ArrayList<>(absorber.getTableList());
        for (AbsorbedTable table : tables) {
            absorber.remove(table);
        }
        document.save(outputFile.toString());
    }
}
```
