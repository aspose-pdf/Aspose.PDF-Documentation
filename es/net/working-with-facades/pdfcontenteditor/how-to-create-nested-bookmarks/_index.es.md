---
title: Adding Bookmarks to PDF file
type: docs
weight: 20
url: /net/how-to-create-nested-bookmarks/
description: Esta sección explica cómo crear Marcadores Anidados con la Clase PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

Los marcadores le ofrecen la opción de realizar un seguimiento/enlace a una página específica dentro del documento PDF. La clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) en el [namespace Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) proporciona una característica que le permite crear su propio marcador de una manera sofisticada pero intuitiva dentro de un archivo PDF existente, en una página dada o en todas las páginas.

## Detalles de implementación

Además de la creación de marcadores simples, a veces tiene el requisito de crear un marcador en forma de capítulos donde anida los marcadores individuales dentro de los marcadores de capítulo para que cuando haga clic en el signo + de un capítulo pueda ver las páginas dentro cuando se expanden los marcadores, como se muestra en la imagen a continuación.
```csharp
   public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.CreateBookmarksAction("Marcador 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

            // Guarda el PDF resultante en un archivo
            editor.Save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```