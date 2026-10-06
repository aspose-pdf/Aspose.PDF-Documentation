---
title: Obter, Atualizar e Expandir Marcadores PDF em Java
linktitle: Obter, Atualizar e Expandir um Marcador
type: docs
weight: 20
url: /pt/java/get-update-and-expand-bookmark/
description: Aprenda como recuperar, atualizar e expandir marcadores em documentos PDF usando Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspecione as propriedades dos marcadores e expanda contornos em arquivos PDF com Java
Abstract: Este artigo explica como ler, atualizar e expandir marcadores usando Aspose.PDF for Java. Ele cobre a iteração pelos itens de contorno, a extração dos números de página dos marcadores com PdfBookmarkEditor, a leitura de marcadores filhos, a atualização dos títulos e do estilo dos marcadores e a forçar a abertura dos contornos quando o documento é exibido.
---
Aspose.PDF for Java expõe marcadores tanto através do modelo de contorno do documento quanto `PdfBookmarkEditor` fachada.

## Obter propriedades do marcador

Use este exemplo quando precisar inspecionar as entradas de marcadores de nível superior no contorno do documento.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pela coleção de contornos.
1. Leia e imprima os valores de título, estilo e cor do marcador.

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

## Obter números de página dos marcadores

Este exemplo usa `PdfBookmarkEditor` para extrair títulos de marcadores, níveis, números de página e ações.

1. Vincular o PDF de origem a [PdfBookmarkEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/).
1. Extrair a coleção de marcadores e iterar sobre ela.
1. Imprimir o nível, título, número da página e informações de ação para cada marcador.

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

## Obter marcadores filhos

Use este exemplo quando precisar inspecionar itens de contorno de nível superior e aninhados.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelos contornos de nível superior e imprima suas propriedades.
1. Detecte marcadores filhos, depois itere por eles e imprima suas propriedades.

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

## Atualizar marcadores

Use este exemplo quando o título e o estilo de um marcador existente devem ser modificados.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse o item de contorno alvo e seu marcador filho.
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

## Expandir marcadores por padrão

Use este exemplo quando o painel de marcadores deve abrir e mostrar itens de contorno expandido quando o documento for exibido.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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
