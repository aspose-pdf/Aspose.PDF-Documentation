---
title: Añadir acciones de Marcadores a un archivo PDF existente
type: docs
weight: 20
url: es/java/adding-bookmark-actions/
description: Esta sección explica cómo añadir acciones de Marcadores a un archivo PDF existente con Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La clase [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) presente en el paquete com.aspose.pdf.facades proporciona la flexibilidad para añadir acciones de Marcadores a un archivo PDF. Puedes crear un enlace con las acciones en serie correspondientes para ejecutar un elemento de menú en el visor de PDF. Esta clase también proporciona la característica de crear acciones adicionales para eventos de documentos.

El siguiente ejemplo de código demuestra cómo añadir una acción de Marcador a un documento PDF.

```java
// Crear una instancia de PdfContentEditor
PdfContentEditor pdfContentEditor = new PdfContentEditor();

// Cargar el archivo PDF existente
pdfContentEditor.bindPdf("input.pdf");

// Añadir una acción de Marcador al documento PDF
pdfContentEditor.createBookmarkAction("Page 1", 1);

// Guardar el archivo PDF actualizado
pdfContentEditor.save("output.pdf");

 Si haces clic en esta pestaña, se realiza la acción deseada. Con la ayuda de un marcador, al hacer clic en él, realizamos la acción deseada. Luego crea un [CreateBookmarkAction](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createBookmarksAction-java.lang.String-java.awt.Color-boolean-boolean-java.lang.String-java.lang.String-java.lang.String-), establece los parámetros del texto, colores, indica el nombre del marcador, y también indica el número de página. La última acción se realiza con "GoTo", permite ir desde cualquier lugar a la página que necesitamos.

```java
public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.createBookmarksAction("Bookmark 1", java.awt.Color.GREEN, true, false, "", "GoTo", "2");

            // Guarda el resultado en un archivo PDF
            editor.save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```