---
title: Extraer páginas PDF en Java
linktitle: Extrayendo páginas PDF
type: docs
weight: 80
url: /es/java/extract-pages/
description: Aprenda cómo extraer una o varias páginas PDF en archivos nuevos en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga páginas PDF en documentos nuevos con Java
Abstract: Este artículo explica cómo extraer páginas de archivos PDF usando Aspose.PDF for Java. Cubre la copia de una sola página y la extracción de varias páginas en un documento de destino separado utilizando indexación de páginas basada en 1.
---
Aspose.PDF for Java le permite copiar páginas seleccionadas en un nuevo documento de destino.

## Extraer una sola página

Utilice este ejemplo cuando necesite guardar una página del PDF de origen en un documento separado.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y crear un documento de destino.
1. Copiar la página objetivo en la colección de páginas de destino.
1. Guarda el nuevo PDF.

```java
public static void extractPage(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        dstDocument.getPages().add(srcDocument.getPages().get_Item(2));
        dstDocument.save(outputFile.toString());
    }
}
```

## Extraer varias páginas

Utilice este ejemplo cuando necesite copiar varias páginas en un PDF separado.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y crear un documento de destino.
1. Itere a través de los índices de página seleccionados y añádalos al destino.
1. Guarde el documento de páginas extraídas.

```java
public static void extractBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        Integer[] pages = {2, 3};
        for (Integer pageIndex : pages) {
            anotherDocument.getPages().add(document.getPages().get_Item(pageIndex));
        }
        anotherDocument.save(outputFile.toString());
    }
}
```
