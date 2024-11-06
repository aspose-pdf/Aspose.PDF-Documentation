---
title: Adding Javascript actions PDF 
type: docs
weight: 10
url: es/net/adding-javascript-actions/
description: Esta sección explica cómo agregar acciones de Javascript a un archivo PDF existente con Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) presente en el paquete Aspose.Pdf.Facades proporciona la flexibilidad para agregar acciones de Javascript a un archivo PDF. Puedes crear un enlace con las acciones en serie correspondientes para ejecutar un elemento de menú en el visor de PDF. Esta clase también ofrece la característica de crear acciones adicionales para eventos de documentos. 

En primer lugar, se dibuja un objeto en el [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), en nuestro ejemplo un [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle). Y establece la acción [createJavaScriptLink](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) en el Rectángulo. Después puedes guardar tu documento.

```csharp
  public static void AddingJavascriptActions()
        {
            PdfContentEditor editor = new PdfContentEditor();
            editor.BindPdf(_dataDir + "sample.pdf");
            // crear enlace de Javascript
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(50, 750, 50, 50);
            String code = "app.alert('¡Bienvenido a Aspose!');";
            editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);
            // guardar el archivo de salida
            editor.Save(_dataDir + "JavaScriptAdded_output.pdf");
        }
```