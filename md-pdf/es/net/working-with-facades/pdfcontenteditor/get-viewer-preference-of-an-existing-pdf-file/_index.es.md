---
title: Obtener Preferencia de Visualización de un Archivo PDF
type: docs
weight: 70
url: /net/get-viewer-preference-of-an-existing-pdf-file/
description: Esta sección muestra cómo obtener la preferencia de visualización de un archivo PDF existente utilizando la clase PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Obtener Preferencia de Visualización de un Archivo PDF Existente

La clase [ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) representa los modos de visualización de archivos PDF; por ejemplo, posicionar la ventana del documento en el centro de la pantalla, ocultar la barra de menús de la aplicación del visor, etc.

Para leer la configuración utilizamos la clase [GetViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference). Este método devuelve una variable donde se guardan todas las configuraciones.

```csharp
      public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Cambiar Preferencias de Visualización
            var preferences = editor.GetViewerPreference();
            if ((preferences & ViewerPreference.CenterWindow) != 0)
                Console.WriteLine("Ventana Centrarse");
            if ((preferences & ViewerPreference.HideMenubar) != 0)
                Console.WriteLine("Barra de menús oculta");
            if ((preferences & ViewerPreference.PageModeFullScreen) != 0)
                Console.WriteLine("Modo de Página Pantalla Completa");
        }
```