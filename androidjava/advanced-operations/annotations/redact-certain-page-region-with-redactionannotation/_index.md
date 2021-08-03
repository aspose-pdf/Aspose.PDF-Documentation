---
title: Redact certain page region with Redaction Annotation using Aspose.PDF for Java
linktitle: Redact certain page region with Redaction Annotation
type: docs
weight: 30
url: /java/redact-certain-page-region-with-redactionannotation/
description: Aspose.PDF for Java allows you to add and manipulate Annotations in an existing PDF file. You should use a class named RedactionAnnotation to resolve this task.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Java supports the feature to add as well as manipulate Annotations in an existing PDF file. Recently some of our customers posted a required to redact (remove text, image, etc elements from) a certain page region of PDF document. In order to fulfill this requirement, a class named RedactionAnnotation is provided, which can be used to redact certain page regions or it can be used to manipulate existing RedactionAnnotations and redact them (i.e. flatten annotation and remove the text under it).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleRedactAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RedactionAnnotation() {

        // Open document
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // Create RedactionAnnotation instance for specific page region
        RedactionAnnotation annot = new RedactionAnnotation(page, new Rectangle(200, 500, 300, 600));
        annot.setFillColor(Color.getGreen());
        annot.setBorderColor(Color.getYellow());
        annot.setColor(Color.getBlue());

        // Text to be printed on redact annotation
        annot.setOverlayText("REDACTED");
        annot.setTextAlignment(HorizontalAlignment.Center);

        // Repat Overlay text over redact Annotation
        annot.setRepeat(true);

        // Add annotation to annotations collection of first page
        page.getAnnotations().add(annot);

        // Flattens annotation and redacts page contents (i.e. removes text and image
        // Under redacted annotation)
        annot.redact();
        document.save(_dataDir + "RedactPage_out.pdf");
    }
```

## Facades approach

Aspose.PDF.Facades namespace also has a class named [PdfAnnotationEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) which provides the feature to manipulate existing Annotations inside PDF file. This class contains a method named [RedactArea(..)](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Redaction#getredactArea-com.aspose.pdf.Page-com.aspose.pdf.Rectangle-java.awt.Color-) which provides the capability to remove certain page regions.

```java
    public static void RedactionAnnotationFacades(){
        PdfAnnotationEditor editor = new PdfAnnotationEditor();
        
        editor.bindPdf(_dataDir + "sample.pdf");
        
        // Redact certain page region
        editor.redactArea(1, new Rectangle(100, 100, 20, 70), java.awt.Color.white);
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.save( _dataDir + "FacadesApproach_out.pdf");
    }
}
```
