---
title: Excluir páginas PDF em Java
linktitle: Excluindo páginas PDF
type: docs
weight: 80
url: /java/delete-pages/
description: Aprenda como excluir páginas de arquivos PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exclua uma ou mais páginas PDF em Java
Abstract: Este artigo explica como remover páginas de arquivos PDF usando Aspose.PDF para Java. Abrange a exclusão de uma única página e a exclusão de várias páginas de uma vez por meio da API de coleção de páginas.
---
Use a coleção de páginas do documento quando precisar remover uma ou mais páginas de um PDF.

## Excluir uma única página

Use este exemplo quando precisar remover uma página pelo seu índice.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Exclua a página de destino da coleção de páginas.
1. Salve o documento atualizado.

```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## Excluir várias páginas

Use este exemplo quando várias páginas precisarem ser removidas em uma operação.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Passe os índices de páginas a serem excluídos da coleção de páginas.
1. Salve o PDF modificado.

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```
