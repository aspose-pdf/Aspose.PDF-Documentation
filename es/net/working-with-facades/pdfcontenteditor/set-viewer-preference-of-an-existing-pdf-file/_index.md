---
title: Establecer Preferencia de Visualización del PDF
type: docs
weight: 60
url: es/net/set-viewer-preference-of-an-existing-pdf-file/
description: Esta sección muestra cómo establecer la preferencia de visualización de un archivo PDF existente utilizando la clase PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Establecer Preferencia de Visualización de un Archivo PDF Existente

La clase [ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) representa modos de visualización de archivos PDF; por ejemplo, posicionar la ventana del documento en el centro de la pantalla, ocultar la barra de menú de la aplicación del visor, etc.

El método [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) en la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) te permite cambiar la preferencia de visualización. En orden de hacer eso, necesitas crear un objeto de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) y enlazar el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index).

Después de eso, puedes llamar al método [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) para establecer cualquier preferencia. Finalmente, tienes que guardar el archivo PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index). El siguiente fragmento de código te muestra cómo cambiar la preferencia del visor en un archivo PDF existente.

Por ejemplo, especificamos el parámetro [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) con el cual centramos la ventana, después removemos la barra de herramientas superior con [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) y con [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) abrimos el modo de pantalla completa.
```csharp
 public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Cambiar las preferencias del visor
            editor.ChangeViewerPreference(ViewerPreference.CenterWindow);
            editor.ChangeViewerPreference(ViewerPreference.HideMenubar);
            editor.ChangeViewerPreference(ViewerPreference.PageModeFullScreen);
            // Guarda el PDF resultante en un archivo
            editor.Save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```