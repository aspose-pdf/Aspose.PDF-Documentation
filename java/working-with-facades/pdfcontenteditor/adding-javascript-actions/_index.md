---
title: Adding Javascript actions to existing PDF file
type: docs
weight: 10
url: /java/adding-javascript-actions/
description: This section explains how to add Javascript actions to existing PDF file with Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The [PdfContentEditor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfContentEditor) class present under com.aspose.pdf.facades package provides the flexibility to add Javascript actions to a PDF file. You can create a link with the serial actions corresponding to execute a menu item in the PDF viewer. This class also provides the feature to create additional actions for document events.

The following sample code shows you how to add Javascript actions in a PDF file.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.facades.PdfContentEditor;


public class PdfContentEditorDemo {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

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
    
}
```