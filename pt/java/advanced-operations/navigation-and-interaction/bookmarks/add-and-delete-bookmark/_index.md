---
title: Adicionar e excluir marcadores de PDF em Java
linktitle: Adicionar e excluir um favorito
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: Aprenda como adicionar e excluir marcadores em documentos PDF usando Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicione ou remova marcadores em documentos PDF com Java
Abstract: Este artigo mostra como criar e excluir marcadores usando Aspose.PDF para Java. Os exemplos demonstram a adição de um marcador de nível superior, a criação de uma hierarquia de marcadores secundários, a exclusão de todos os marcadores e a remoção de um marcador específico por título.
---
Use a coleção de esboços de documentos para gerenciar marcadores de forma programática.

## Adicione um marcador de nível superior

Use este exemplo quando o documento incluir uma única entrada de resumo de nível superior.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) e configure seu título, estilo e ação.
1. Adicione o marcador aos contornos do documento e salve o arquivo.

```java
public static void addBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        pdfOutline.setAction(new GoToAction(document.getPages().get_Item(1)));

        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## Adicionar um marcador filho

Este exemplo cria um marcador pai e aninha um marcador filho nele.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie objetos pai e filho [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/).
1. Adicione o filho ao pai, adicione o pai à coleção de estrutura de tópicos e salve o documento.

```java
public static void addChildBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(document.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        pdfOutline.add(pdfChildOutline);
        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## Excluir todos os favoritos

Use esta abordagem quando toda a coleção de contornos precisar ser removida do documento.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Exclua a coleção completa de contornos.
1. Salve o arquivo de saída limpo.

```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## Excluir um favorito específico

Use este exemplo quando um marcador nomeado precisar ser removido sem limpar toda a árvore de contorno.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Exclua o marcador por título da coleção de contornos.
1. Salve o documento atualizado.

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
