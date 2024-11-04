---
title: Obtener, Actualizar y Expandir un Marcador
linktitle: Obtener, Actualizar y Expandir un Marcador
type: docs
weight: 20
url: /java/get-update-and-expand-bookmark/
description: Este artículo describe cómo usar marcadores en un archivo PDF. Con nuestra biblioteca Java, puedes obtener marcadores del archivo PDF, obtener el número de página de un marcador, actualizar marcadores en un Documento PDF y expandir marcadores al ver un documento.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Marcadores

La colección [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) contiene todos los marcadores de un archivo PDF. Este artículo explica cómo obtener marcadores de un archivo PDF y cómo obtener en qué página se encuentra un marcador en particular.

Para obtener los marcadores, recorre la colección [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) y obtén cada marcador en la OutlineItemCollection.
 El OutlineItemCollection proporciona acceso a todos los atributos del marcador. El siguiente fragmento de código te muestra cómo obtener marcadores del archivo PDF.

```java
    public static void GettingBookmarks() {
        // Abrir documento
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Bucle a través de todos los marcadores
        for (OutlineItemCollection outlineItem : (Iterable<OutlineItemCollection>) pdfDocument.getOutlines()) {
            System.out.println("Título :- " + outlineItem.getTitle());
            System.out.println("Es cursiva :- " + outlineItem.getItalic());
            System.out.println("Es negrita :- " + outlineItem.getBold());
            System.out.println("Color :- " + outlineItem.getColor());
        }
    }
```

## Obtener el número de página de un marcador

Una vez que has añadido un marcador, puedes averiguar en qué página se encuentra obteniendo el PageNumber de destino asociado con el objeto Bookmark.

```java
    public static void GettingBookmarksPageNumber() {
        // Crear PdfBookmarkEditor
        PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
        // Abrir archivo PDF
        bookmarkEditor.bindPdf(GetDataDir() + "UpdateBookmarks.pdf");
        // Extraer marcadores
        Bookmarks bookmarks = bookmarkEditor.extractBookmarks();
        for (Bookmark bookmark : (Iterable<Bookmark>) bookmarks) {
            String strLevelSeprator = "";
            for (int i = 1; i < bookmark.getLevel(); i++) {
                strLevelSeprator += "---- ";
            }
            System.out.println("Título :- " + strLevelSeprator + bookmark.getTitle());
            System.out.println("Número de página :- " + strLevelSeprator + bookmark.getPageNumber());
            System.out.println("Acción de página :- " + strLevelSeprator + bookmark.getAction());
        }
    }
```

## Actualizar Marcadores en un Documento PDF

Para actualizar un marcador en un archivo PDF, primero obtén el marcador particular de la colección OutlineColletion del objeto Document especificando el índice del marcador. Una vez que hayas recuperado el marcador en el objeto [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection), puedes actualizar sus propiedades y luego guardar el archivo PDF actualizado usando el método Save. Los siguientes fragmentos de código muestran cómo actualizar marcadores en un documento PDF.

```java
    public static void UpdateBookmarksInPDFDocument() {
        // Abrir documento
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Obtener un objeto de marcador
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);

        // Actualizar el objeto de marcador
        pdfOutline.setTitle("Updated Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        // Establecer la página de destino como 2
        pdfOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Guardar salida
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## Actualizar Marcadores Hijos en un Documento PDF

Para actualizar un marcador hijo:

1. Recupere el marcador hijo que desea actualizar del archivo PDF obteniendo primero el marcador principal y luego el marcador hijo utilizando los valores de índice apropiados.
1. Guarde el archivo PDF actualizado usando el método Save.

{{% alert color="primary" %}}

Obtenga un marcador de la colección OutlineCollection del objeto Document especificando el índice del marcador, y luego obtenga el marcador hijo especificando el índice de este marcador principal.

{{% /alert %}}

El siguiente fragmento de código le muestra cómo actualizar marcadores hijos en un documento PDF.

```java
    public static void UpdateChildBookmarksInPDFDocument() {
        // Abrir documento
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Obtener un objeto de marcador
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);
        // Obtener objeto de marcador hijo
        OutlineItemCollection childOutline = pdfOutline.get_Item(1);

        // Actualizar el objeto de marcador
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);
        // Establecer la página de destino como 2
        childOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Guardar salida
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## Marcadores expandidos al ver el documento

Los marcadores se mantienen en la colección [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) del objeto Document, que a su vez está en la colección [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). Sin embargo, podemos tener un requisito para que todos los marcadores estén expandidos al ver el archivo PDF.

Para cumplir con este requisito, podemos establecer el estado abierto para cada elemento de esquema/marcador como Abierto. El siguiente fragmento de código muestra cómo establecer el estado abierto para cada marcador como expandido en un documento PDF.

```java
    public static void ExpandedBookmarks() {    
        Document doc = new Document(GetDataDir()+"UpdateBookmarks.pdf");
        // establecer el modo de visualización de página, es decir, mostrar miniaturas, pantalla completa, mostrar panel de adjuntos
        doc.setPageMode(PageMode.UseOutlines);
        // imprimir el conteo total de marcadores en el archivo PDF
        System.out.println(doc.getOutlines().size());
        // recorrer cada elemento de esquema en la colección de esquemas del archivo PDF
        for (int counter = 1; counter <= doc.getOutlines().size(); counter++) {
            // establecer el estado abierto para el elemento de esquema
            doc.getOutlines().get_Item(counter).setOpen(true);
        }
        // guardar el archivo PDF
        doc.save(_dataDir+"Bookmarks_Expanded.pdf");
    }
```