---
title: Obtener, actualizar y expandir marcadores PDF en Java
linktitle: Obtener, actualizar y expandir un marcador
type: docs
weight: 20
url: /es/java/get-update-and-expand-bookmark/
description: Aprenda a recuperar, actualizar y expandir marcadores en documentos PDF usando Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspeccione las propiedades de los marcadores y expanda los esquemas en archivos PDF con Java
Abstract: Este artículo explica cómo leer, actualizar y expandir marcadores usando Aspose.PDF for Java. Cubre la iteración a través de los elementos del esquema del documento, la extracción de los números de página de los marcadores con PdfBookmarkEditor, la lectura de marcadores hijos, la actualización de los títulos y el estilo de los marcadores, y forzar que los esquemas se abran cuando el documento se muestra.
---
Aspose.PDF for Java expone marcadores a través tanto del modelo de esquema del documento como del `PdfBookmarkEditor` fachada.

## Obtener propiedades de los marcadores

Utilice este ejemplo cuando necesite inspeccionar las entradas de marcadores de nivel superior en el esquema del documento.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de la colección de contornos.
1. Leer e imprimir el título del marcador, el estilo y los valores de color.

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

## Obtener números de página de los marcadores

Este ejemplo usa `PdfBookmarkEditor` para extraer los títulos de los marcadores, niveles, números de página y acciones.

1. Vincular el PDF de origen a [PdfBookmarkEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/).
1. Extraiga la colección de marcadores y recorrala.
1. Imprima el nivel, el título, el número de página y la información de acción para cada marcador.

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

## Obtener marcadores secundarios

Utilice este ejemplo cuando necesite inspeccionar tanto los elementos de esquema de nivel superior como los anidados.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere a través de los esquemas de nivel superior y muestre sus propiedades.
1. Detecte los marcadores secundarios, luego itere a través de ellos y muestre sus propiedades.

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

## Actualizar marcadores

Utilice este ejemplo cuando se deba modificar el título y el estilo de un marcador existente.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceda al elemento de esquema objetivo y a su marcador hijo.
1. Actualice las propiedades del marcador y guarde el documento.

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

## Expandir marcadores de forma predeterminada

Utilice este ejemplo cuando el panel de marcadores debe abrirse y mostrar los elementos del esquema ampliados al visualizar el documento.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Establezca el modo de página para usar marcadores y marque cada elemento de marcador como abierto.
1. Guarda el documento actualizado.

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
