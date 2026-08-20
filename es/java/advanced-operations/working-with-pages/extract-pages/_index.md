---
title: Extraer páginas PDF en Java
linktitle: Extraer páginas PDF
type: docs
weight: 80
url: /java/extract-pages/
description: Aprenda a extraer una o varias páginas PDF en nuevos archivos en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga páginas PDF en nuevos documentos con Java
Abstract: Este artículo explica cómo extraer páginas de archivos PDF usando Aspose.PDF para Java. Cubre la copia de una sola página y la extracción de varias páginas en un documento de destino separado mediante la indexación basada en 1 página.
---
Aspose.PDF para Java le permite copiar páginas seleccionadas en un nuevo documento de destino.


## 
Extraer una sola página



Utilice este ejemplo cuando necesite guardar una página del PDF de origen en un documento separado.


1. 
Abra el [Documento] PDF de origen (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y cree un documento de destino.

1. 
Copie la página de destino en la colección de páginas de destino.
1. Guarde el nuevo PDF.


```java
public static void extractPage(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        dstDocument.getPages().add(srcDocument.getPages().get_Item(2));
        dstDocument.save(outputFile.toString());
    }
}
```

## 
Extraer varias páginas



Utilice este ejemplo cuando necesite copiar varias páginas en un PDF independiente.


1. 
Abra el [Documento] PDF de origen (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y cree un documento de destino.

1. 
Itere a través de los índices de páginas seleccionadas y agréguelos al destino.
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
