---
title: Agregar y eliminar marcadores de PDF en Java
linktitle: Agregar y eliminar un marcador
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: Aprenda a agregar y eliminar marcadores en documentos PDF usando Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar o eliminar marcadores en documentos PDF con Java
Abstract: Este artículo muestra cómo crear y eliminar marcadores usando Aspose.PDF para Java. Los ejemplos demuestran cómo agregar un marcador de nivel superior, crear una jerarquía de marcadores secundarios, eliminar todos los marcadores y eliminar un marcador específico por título.
---
Utilice la colección de esquemas de documentos para administrar marcadores mediante programación.


## 
Agregar un marcador de nivel superior



Utilice este ejemplo cuando el documento deba incluir una única entrada de esquema de nivel superior.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree una [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) y configure su título, estilo y acción.
1. Agregue el marcador a los esquemas del documento y guarde el archivo.


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

## 
Agregar un marcador infantil



Este ejemplo crea un marcador principal y anida un marcador secundario debajo de él.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree objetos primarios y secundarios [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/).
1. Agregue el hijo al padre, agregue el padre a la colección de esquemas y guarde el documento.


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

## 
Eliminar todos los marcadores



Utilice este enfoque cuando toda la colección de esquemas deba eliminarse del documento.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Elimina la colección de esquemas completos.
1. Guarde el archivo de salida limpio.


```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## 
Eliminar un marcador específico



Utilice este ejemplo cuando deba eliminarse un marcador con nombre sin borrar todo el árbol de contorno.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Elimina el marcador por título de la colección de esquemas.
1. Guarde el documento actualizado.

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
