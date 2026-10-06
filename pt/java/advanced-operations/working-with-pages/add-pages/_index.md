---
title: Adicionar páginas PDF em Java
linktitle: Adicionar páginas
type: docs
weight: 10
url: /pt/java/add-pages/
description: Aprenda como adicionar ou inserir páginas em documentos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar ou inserir páginas PDF com Java
Abstract: Este artigo explica como adicionar páginas a arquivos PDF usando Aspose.PDF for Java. Ele cobre a inserção de uma página em branco em uma posição específica, a adição de uma página ao final de um documento e a importação de uma página de outro PDF.
---
Aspose.PDF for Java permite inserir páginas em branco ou importar páginas de outro documento.

## Inserir uma página vazia em uma posição específica

Use este exemplo quando precisar adicionar uma página em branco no meio de um PDF existente.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Insira uma nova página na posição de destino na coleção de páginas.
1. Salve o documento atualizado.

```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## Anexar uma página vazia ao final

Use este exemplo quando precisar estender o documento com uma nova página em branco ao final.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicionar uma nova página ao final da coleção de páginas.
1. Salve o PDF modificado.

```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## Adicionar uma página de outro documento

Use este exemplo quando quiser importar uma página de um PDF para outro PDF.

1. Crie o destino [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e abra o documento de origem.
1. Adicione qualquer conteúdo necessário ao destino e importe a página alvo do PDF de origem.
1. Salve o documento resultante.

```java
public static void addPageFromAnotherDocument(Path inputFile, Path outputFile) {
    try (Document document = new Document();
         Document anotherDocument = new Document(inputFile.toString())) {
        document.getPages().add().getParagraphs().add(new TextFragment("This is first page!"));
        document.getPages().add(anotherDocument.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```
