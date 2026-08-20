---
title: Eliminar páginas PDF en Java
linktitle: Eliminar páginas PDF
type: docs
weight: 80
url: /java/delete-pages/
description: Aprenda a eliminar páginas de archivos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar una o más páginas PDF en Java
Abstract: Este artículo explica cómo eliminar páginas de archivos PDF usando Aspose.PDF para Java. Cubre la eliminación de una sola página y la eliminación de varias páginas a la vez a través de la API de colección de páginas.
---
Utilice la colección de páginas del documento cuando necesite eliminar una o más páginas de un PDF.


## 
Eliminar una sola página



Utilice este ejemplo cuando necesite eliminar una página por su índice.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Elimine la página de destino de la colección de páginas.
1. Guarde el documento actualizado.


```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## 
Eliminar varias páginas



Utilice este ejemplo cuando deban eliminarse varias páginas en una sola operación.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Pase los índices de las páginas para eliminar de la colección de páginas.
1. Guarde el PDF modificado.

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```
