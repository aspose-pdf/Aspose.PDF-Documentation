---
title: Agregar páginas PDF en Java
linktitle: Agregar páginas
type: docs
weight: 10
url: /es/java/add-pages/
description: Aprenda cómo agregar o insertar páginas en documentos PDF con Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar o insertar páginas PDF con Java
Abstract: Este artículo explica cómo agregar páginas a archivos PDF usando Aspose.PDF for Java. Cubre la inserción de una página en blanco en una posición específica, añadir una página al final de un documento y importar una página de otro PDF.
---
Aspose.PDF for Java le permite insertar páginas en blanco o importar páginas de otro documento.

## Inserte una página vacía en una posición específica

Utilice este ejemplo cuando necesite agregar una página en blanco en medio de un PDF existente.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Inserte una página nueva en la posición objetivo en la colección de páginas.
1. Guarde el documento actualizado.

```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## Añadir una página vacía al final

Utilice este ejemplo cuando necesite ampliar el documento con una nueva página en blanco al final.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar una nueva página al final de la colección de páginas.
1. Guarde el PDF modificado.

```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## Agregar una página de otro documento

Utilice este ejemplo cuando quiera importar una página de un PDF a otro PDF.

1. Cree el destino [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y abra el documento de origen.
1. Agregue cualquier contenido de destino requerido e importe la página objetivo del PDF de origen.
1. Guarde el documento resultante.

```java
public static void addPageFromAnotherDocument(Path inputFile, Path outputFile) {
    try (Document document = new Document();
         Document anotherDocument = new Document(inputFile.toString())) {
        document.getPages().add().getParagraphs().add(new TextFragment("This is first page!"));
        document.getPages().add(anotherDocument.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```
