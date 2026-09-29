---
title: Agregar y eliminar marcadores PDF en Java
linktitle: Agregar y eliminar un marcador
type: docs
weight: 10
url: /es/java/add-and-delete-bookmark/
description: Aprenda cómo agregar y eliminar marcadores en documentos PDF usando Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar o eliminar marcadores en documentos PDF con Java
Abstract: Este artículo muestra cómo crear y eliminar marcadores usando Aspose.PDF for Java. Los ejemplos demuestran cómo agregar un marcador de nivel superior, crear una jerarquía de marcadores secundarios, eliminar todos los marcadores y eliminar un marcador específico por título.
---
Utilice la colección del esquema del documento para gestionar los marcadores programáticamente.

## Agregar un marcador de nivel superior

Utilice este ejemplo cuando el documento debe incluir una única entrada de esquema de nivel superior.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`OutlineItemCollection`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) y configure su título, estilo y acción.
1. Agregue el marcador a los contornos del documento y guarde el archivo.

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

## Agregar un marcador hijo

Este ejemplo crea un marcador principal y anida un marcador hijo debajo de él.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree padre y hijo [`OutlineItemCollection`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) objetos.
1. Agregue el hijo al padre, agrega el padre a la colección de contorno y guarde el documento.

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

## Eliminar todos los marcadores

Utilice este enfoque cuando se deba eliminar toda la colección de marcadores del documento.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Elimine la colección completa de marcadores.
1. Guarde el archivo de salida limpio.

```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## Eliminar un marcador específico

Utilice este ejemplo cuando se deba eliminar un marcador con nombre sin eliminar todo el árbol de contornos.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Elimine el marcador por título de la colección de esquemas.
1. Guarde el documento actualizado.

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
