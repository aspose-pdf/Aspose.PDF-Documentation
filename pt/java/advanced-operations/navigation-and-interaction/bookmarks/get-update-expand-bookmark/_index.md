---
title: Obtenha, atualize e expanda marcadores de PDF em Java
linktitle: Obtenha, atualize e expanda um marcador
type: docs
weight: 20
url: /java/get-update-and-expand-bookmark/
description: Aprenda como recuperar, atualizar e expandir marcadores em documentos PDF usando Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspecione propriedades de marcadores e expanda contornos em arquivos PDF com Java
Abstract: Este artigo explica como ler, atualizar e expandir marcadores usando Aspose.PDF para Java. Ele cobre a iteração por meio de itens de estrutura de tópicos, a extração de números de páginas de marcadores com PdfBookmarkEditor, a leitura de marcadores filhos, a atualização de títulos e estilos de marcadores e a força de abertura de contornos quando o documento é exibido.
---
Aspose.PDF para Java expõe marcadores por meio do modelo de estrutura de tópicos do documento e da fachada `PdfBookmarkEditor`.

## Obtenha propriedades de favoritos

Use este exemplo quando precisar inspecionar as entradas de marcadores de nível superior no esboço do documento.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pela coleção de contornos.
1. Leia e imprima o título, o estilo e os valores de cor do marcador.

```java
public static void getBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
        }
    }
}
```

## Obtenha números de página de favoritos

Este exemplo usa `PdfBookmarkEditor` para extrair títulos, níveis, números de páginas e ações de marcadores.

1. Vincule o PDF de origem a [PdfBookmarkEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/).
1. Extraia a coleção de marcadores e repita-a.
1. Imprima o nível, o título, o número da página e as informações de ação de cada marcador.

```java
public static void getBookmarkPageNumber(Path inputFile) {
    PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
    try {
        bookmarkEditor.bindPdf(inputFile.toString());
        for (Bookmark bookmark : bookmarkEditor.extractBookmarks()) {
            String levelSeparator = "";
            for (int i = 0; i < bookmark.getLevel(); i++) {
                levelSeparator += "----";
            }

            System.out.println(levelSeparator + " Title: " + bookmark.getTitle());
            System.out.println(levelSeparator + " Page Number: " + bookmark.getPageNumber());
            System.out.println(levelSeparator + " Page Action: " + bookmark.getAction());
        }
    } finally {
        bookmarkEditor.close();
    }
}
```

## Obtenha marcadores infantis

Use este exemplo quando precisar inspecionar itens de estrutura de tópicos de nível superior e aninhados.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelos contornos de nível superior e imprima suas propriedades.
1. Detecte marcadores filhos, percorra-os e imprima suas propriedades.

```java
public static void getChildBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
            int count = outlineItem.size();
            if (count > 0) {
                System.out.println("Child Bookmarks");
                for (int j = 1; j <= outlineItem.size(); j++) {
                    OutlineItemCollection childOutlineItem = outlineItem.get_Item(j);
                    System.out.println(childOutlineItem.getTitle());
                    System.out.println(childOutlineItem.getItalic());
                    System.out.println(childOutlineItem.getBold());
                    System.out.println(childOutlineItem.getColor());
                }
            }
        }
    }
}
```

## Atualizar favoritos

Use este exemplo quando um título e estilo de marcador existente precisar ser modificado.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse o item de estrutura de destino e seu marcador filho.
1. Atualize as propriedades do marcador e salve o documento.

```java
public static void updateBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection outline = document.getOutlines().get_Item(1);
        OutlineItemCollection childOutline = outline.get_Item(1);
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);

        document.save(outputFile.toString());
    }
}
```

## Expanda os favoritos por padrão

Use este exemplo quando o painel de marcadores for aberto e mostrar itens de estrutura de tópicos expandidos quando o documento for exibido.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Defina o modo de página para usar contornos e marque cada item de contorno como aberto.
1. Salve o documento atualizado.

```java
public static void expandedBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setPageMode(PageMode.UseOutlines);
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection item = document.getOutlines().get_Item(i);
            item.setOpen(true);
        }
        document.save(outputFile.toString());
    }
}
```
