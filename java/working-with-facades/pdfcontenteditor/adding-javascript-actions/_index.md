---
title: Adding Javascript actions to existing PDF file
type: docs
weight: 10
url: /java/adding-javascript-actions/
description: This section explains how to add Javascript actions to existing PDF file with Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The [PdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class present under com.aspose.pdf.facades package provides the flexibility to add Javascript actions to a PDF file. You can create a link with the serial actions corresponding to execute a menu item in the PDF viewer. This class also provides the feature to create additional actions for document events. 

First of all, an object is drawn in the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document), in our example a [Rectangle](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Rectangle). And set the action [createJavaScriptLink](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createJavaScriptLink-java.lang.String-java.awt.Rectangle-int-java.awt.Color-) to the Rectangle. After you may save your document.

```java
 public static void AddingJavascriptActions() {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");
        // create Javascript link
        java.awt.Rectangle rect = new java.awt.Rectangle(50, 750, 50, 50);
        String code = "app.alert('Welcome to Aspose!');";
        editor.createJavaScriptLink(code, rect, 1, java.awt.Color.GREEN);
        // save the output file
        editor.save(_dataDir+"JavaScriptAdded_output.pdf");
    }
```