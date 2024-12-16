---
title: Establecer Preferencia de Visor de un Archivo PDF Existente
type: docs
weight: 60
url: /es/java/set-viewer-preference-of-an-existing-pdf-file/
description: Esta sección muestra cómo trabajar con Aspose.PDF Facades utilizando la Clase PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Establecer Preferencia de Visor de un Archivo PDF Existente

La clase [ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) representa modos de visualización de archivos PDF; por ejemplo, posicionar la ventana del documento en el centro de la pantalla, ocultar la barra de menú de la aplicación del visor, etc.

El método [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) en la clase [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) le permite cambiar la preferencia del visor.
 Para hacer eso, necesitas crear un objeto de la clase [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) y enlazar el archivo PDF de entrada utilizando el método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-).

Después de eso, puedes llamar al método [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) para establecer cualquier preferencia. Finalmente, tienes que guardar el archivo PDF actualizado usando el método Save. El siguiente fragmento de código te muestra cómo cambiar la preferencia del visor en un archivo PDF existente.

Por ejemplo, especificamos el parámetro [CENTER WINDOW](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#CENTER_WINDOW) con el cual centramos la ventana, después removemos la barra de herramientas superior con [HIDE MENUBAR](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#HIDE_MENUBAR) y con [PAGE MODE USE NONE](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#PAGE_MODE_USE_NONE) abrimos el modo de pantalla completa.
```java
public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Cambiar las preferencias del visor
            editor.changeViewerPreference(ViewerPreference.CENTER_WINDOW);
            editor.changeViewerPreference(ViewerPreference.HIDE_MENUBAR);
            editor.changeViewerPreference(ViewerPreference.PAGE_MODE_USE_NONE);
            
            editor.save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```