---
title: Mover páginas PDF en Java
linktitle: Moviendo páginas PDF
type: docs
weight: 100
url: /es/java/move-pages/
description: Aprenda cómo mover páginas PDF dentro de un documento o entre documentos en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mover páginas PDF entre documentos en Java
Abstract: Este artículo explica cómo mover páginas en PDFs usando Aspose.PDF for Java. Cubre mover una sola página o varias páginas a otro documento, y reubicar una página dentro del mismo PDF.
---
Aspose.PDF for Java le permite mover páginas entre documentos o reubicar páginas dentro del mismo PDF.

## Mover una página a otro documento

Utilice este ejemplo cuando una sola página debe eliminarse del PDF de origen y guardarse en un documento separado.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y cree un documento de destino.
1. Agregue la página objetivo al destino y elimínela del origen.
1. Guarde ambos documentos.

```java
public static void movePageFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        anotherDocument.getPages().add(document.getPages().get_Item(2));
        document.getPages().delete(2);
        document.save(sourceOutputFile.toString());
        anotherDocument.save(outputFile.toString());
    }
}
```

## Mover varias páginas a otro documento

Utilice este ejemplo cuando varias páginas deben transferirse del PDF de origen a un nuevo documento.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y cree el documento de destino.
1. Copie las páginas seleccionadas en el documento de destino.
1. Elimine las páginas movidas del origen y guarde ambos archivos.

```java
public static void moveBunchPagesFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        Integer[] pages = {1, 2};
        for (Integer pageIndex : pages) {
            dstDocument.getPages().add(srcDocument.getPages().get_Item(pageIndex));
        }
        dstDocument.save(outputFile.toString());
        srcDocument.getPages().delete(pages);
        srcDocument.save(sourceOutputFile.toString());
    }
}
```

## Mover una página dentro del mismo documento

Utilice este ejemplo cuando una página deba reubicarse en una nueva ubicación dentro del mismo PDF.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Duplique la página objetivo en la nueva posición y elimine la entrada de la página original.
1. Guarde el documento reordenado.

```java
public static void movePageInNewLocationInSameDocument(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString())) {
        srcDocument.getPages().add(srcDocument.getPages().get_Item(2));
        srcDocument.getPages().delete(2);
        srcDocument.save(outputFile.toString());
    }
}
```
