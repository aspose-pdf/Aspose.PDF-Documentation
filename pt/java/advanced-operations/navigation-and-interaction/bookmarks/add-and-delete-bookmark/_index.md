---
title: Adicionar e Excluir Marcadores de PDF em Java
linktitle: Adicionar e Excluir um Marcador
type: docs
weight: 10
url: /pt/java/add-and-delete-bookmark/
description: Aprenda como adicionar e excluir marcadores em documentos PDF usando Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar ou remover marcadores em documentos PDF com Java
Abstract: Este artigo mostra como criar e excluir marcadores usando Aspose.PDF for Java. Os exemplos demonstram a adição de um marcador de nível superior, a criação de uma hierarquia de marcadores filhos, a exclusão de todos os marcadores e a remoção de um marcador específico pelo título.
---
Use a coleção de contorno de documento para gerenciar marcadores programaticamente.

## Adicionar um marcador de nível superior

Use este exemplo quando o documento deve incluir uma única entrada de contorno de nível superior.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

Este exemplo cria um marcador pai e aninha um marcador filho sob ele.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Criar pai e filho [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) objetos.
1. Adicione o filho ao pai, adicione o pai à coleção de contornos e salve o documento.

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

## Excluir todos os marcadores

Use esta abordagem quando toda a coleção de marcadores deve ser removida do documento.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Excluir a coleção completa de marcadores.
1. Salvar o arquivo de saída limpo.

```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## Excluir um marcador específico

Use este exemplo quando um marcador nomeado deve ser removido sem limpar toda a árvore de marcadores.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Exclua o marcador pelo título da coleção de outlines.
1. Salve o documento atualizado.

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
