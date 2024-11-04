---
title: Añadiendo acciones de Javascript a un archivo PDF existente
type: docs
weight: 10
url: /java/adding-javascript-actions/
description: Esta sección explica cómo añadir acciones de Javascript a un archivo PDF existente con Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La clase [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) presente en el paquete com.aspose.pdf.facades proporciona la flexibilidad para añadir acciones de Javascript a un archivo PDF. Puedes crear un enlace con las acciones en serie correspondientes para ejecutar un elemento de menú en el visor de PDF. Esta clase también ofrece la característica de crear acciones adicionales para eventos de documentos.

En primer lugar, se dibuja un objeto en el [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), en nuestro ejemplo un [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
 Y establezca la acción [createJavaScriptLink](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createJavaScriptLink-java.lang.String-java.awt.Rectangle-int-java.awt.Color-) en el Rectángulo. Después, puede guardar su documento.

```java
 public static void AddingJavascriptActions() {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");
        // crear enlace Javascript
        java.awt.Rectangle rect = new java.awt.Rectangle(50, 750, 50, 50);
        String code = "app.alert('¡Bienvenido a Aspose!');";
        editor.createJavaScriptLink(code, rect, 1, java.awt.Color.GREEN);
        // guardar el archivo de salida
        editor.save(_dataDir+"JavaScriptAdded_output.pdf");
    }
```