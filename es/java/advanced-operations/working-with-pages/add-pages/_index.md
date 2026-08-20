---
title: Agregar páginas PDF en Java
linktitle: Agregar páginas
type: docs
weight: 10
url: /java/add-pages/
description: Aprenda a agregar o insertar páginas en documentos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar o insertar páginas PDF con Java
Abstract: Este artículo explica cómo agregar páginas a archivos PDF usando Aspose.PDF para Java. Cubre insertar una página en blanco en una posición específica, agregar una página al final de un documento e importar una página desde otro PDF.
---
Aspose.PDF para Java le permite insertar páginas en blanco o importar páginas desde otro documento.


## 
Insertar una página vacía en una posición específica



Utilice este ejemplo cuando necesite agregar una página en blanco en medio de un PDF existente.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Inserte una nueva página en la posición de destino en la colección de páginas.
1. Guarde el documento actualizado.


```java
public static void insertEmptyPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().insert(2);
        document.save(outputFile.toString());
    }
}
```

## 
Agregar una página vacía al final



Utilice este ejemplo cuando necesite ampliar el documento con una nueva última página en blanco.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue una nueva página al final de la colección de páginas.
1. Guarde el PDF modificado.


```java
public static void addEmptyPageToEnd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();
        document.save(outputFile.toString());
    }
}
```

## 
Agregar una página de otro documento



Utilice este ejemplo cuando desee importar una página de un PDF a otro PDF.


1. 
Cree el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) de destino y abra el documento de origen.

1. 
Agregue cualquier contenido de destino requerido e importe la página de destino desde el PDF de origen.
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
