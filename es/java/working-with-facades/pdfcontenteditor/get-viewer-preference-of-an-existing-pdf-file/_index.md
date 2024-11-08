---
title: Obtener Preferencias del Visor de un Archivo PDF Existente
type: docs
weight: 70
url: /es/java/get-viewer-preference-of-an-existing-pdf-file/
description: Esta sección muestra cómo trabajar con Aspose.PDF Facades usando la Clase PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Obtener Preferencias del Visor de un Archivo PDF Existente

La clase [ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) representa los modos de visualización de archivos PDF; por ejemplo, posicionar la ventana del documento en el centro de la pantalla, ocultar la barra de menú de la aplicación del visor, etc.

Para leer las configuraciones utilizamos 'getViewerPreference'. Este método devuelve una variable donde se guardan todas las configuraciones.

```java
 public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Cambiar las Preferencias del Visor
            var preferences = editor.getViewerPreference();
            if ((preferences & ViewerPreference.CENTER_WINDOW) != 0)
                System.out.println("Ventana centrada");
            if ((preferences & ViewerPreference.HIDE_MENUBAR) != 0)
                System.out.println("Barra de menú oculta");
        }
```