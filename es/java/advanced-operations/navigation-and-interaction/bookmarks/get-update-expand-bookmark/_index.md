---
title: Obtenga, actualice y expanda marcadores de PDF en Java
linktitle: Obtener, actualizar y ampliar un marcador
type: docs
weight: 20
url: /java/get-update-and-expand-bookmark/
description: Aprenda a recuperar, actualizar y expandir marcadores en documentos PDF usando Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspeccione las propiedades de los marcadores y expanda los esquemas en archivos PDF con Java
Abstract: Este artículo explica cómo leer, actualizar y expandir marcadores usando Aspose.PDF para Java. Cubre la iteración a través de elementos de esquema, la extracción de números de páginas de marcadores con PdfBookmarkEditor, la lectura de marcadores secundarios, la actualización de títulos y estilos de marcadores y la fuerza para abrir los esquemas cuando se muestra el documento.
---
Aspose.PDF para Java expone marcadores tanto a través del modelo de esquema del documento como de la fachada `PdfBookmarkEditor`.


## 
Obtener propiedades de marcador



Utilice este ejemplo cuando necesite inspeccionar las entradas de marcadores de nivel superior en el esquema del documento.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Iterar a través de la colección de contornos.
1. Lea e imprima el título, el estilo y los valores de color del marcador.


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

## 
Obtener números de páginas de favoritos



Este ejemplo utiliza `PdfBookmarkEditor` para extraer títulos de marcadores, niveles, números de página y acciones.


1. 
Vincule el PDF de origen a [PdfBookmarkEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/).

1. 
Extraiga la colección de marcadores y repítala.
1. Imprima el nivel, título, número de página e información de acción para cada marcador.


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

## 
Obtener marcadores infantiles



Utilice este ejemplo cuando necesite inspeccionar elementos de esquema anidados y de nivel superior.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Repita los esquemas de nivel superior e imprima sus propiedades.
1. Detecte marcadores secundarios, luego revíselos e imprima sus propiedades.


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

## 
Actualizar marcadores



Utilice este ejemplo cuando deba modificar el título y el estilo de un marcador existente.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Acceda al elemento del esquema de destino y a su marcador secundario.
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

## 
Expandir marcadores de forma predeterminada



Utilice este ejemplo cuando el panel de marcadores debería abrirse y mostrar elementos de esquema ampliados cuando se muestra el documento.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Configure el modo de página para usar esquemas y marque cada elemento del esquema como abierto.
1. Guarde el documento actualizado.

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
