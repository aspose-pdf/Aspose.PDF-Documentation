---
title: Import and Export Annotations to XFDF format using Aspose.PDF for Java
linktitle: Import and Export Annotations to XFDF format
type: docs
weight: 40
url: /java/import-export-xfdf/
description: You may import and export annotation with XFDF format using Aspose.PDF for Java library. 
lastmod: "2021-02-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF stand for XML Forms Data Format. It is an XML based file format. This file format is used to represent form data or annotations contained in a PDF form. XFDF can be used for many different purposes, but in our case, it can be used to either send or receive form data or annotations to other computers or servers etc, or it can be used to archive the form data or annotations. In this article, we will see how Aspose.Pdf.Facades has taken this concept into consideration and how we can import and export annotations data to XFDF file.

{{% /alert %}}

**Aspose.PDF for Java** is a feature rich component when it comes to editing the PDF documents. As we know XFDF is an important aspect of PDF forms manipulation, Aspose.Pdf.Facades namespace in Aspose.PDF for Java has considered this very well, and have provided methods to import and export annotations data to XFDF files.

[PDFAnnotationEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) class contains two methods to work with import and export of annotations to XFDF file. [ExportAnnotationsXfdf](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) method provides the functionality to export annotations from a PDF document to XFDF file, while [ImportAnnotationFromXfdf](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) method allows you to import annotations from an existing XFDF file. In order to import or export annotations we need to specify the annotation types. We can specify these types in the form of an enumeration and then pass this enumeration as an argument to any of these methods. This way, the annotations of the specified types will only be imported or exported to an XFDF file.

The following code snippet shows you how to export annotations to an XFDF file:

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;
import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleAnnotationImportExport {
    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    /*
     * Importing annotations from XFDF file XML Forms Data Format (XFDF) file
     * created by Adobe Acrobat, a PDF authoring application; stores descriptions of
     * page form elements and their values, such as the names and values for text
     * fields; used for saving form data that can be imported into a PDF document.
     * You can import annotation data from the XFDF file to PDF using the
     * ImportAnnotationsFromXfdf method in PdfAnnotationEditor class.
     */

    public static void ExportAnnotationXFDF() throws IOException {
        // Create PdfAnnotationEditor object
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

        // Bind PDF document to the Annotation Editor
        AnnotationEditor.bindPdf(_dataDir + "AnnotationDemo1.pdf");

        // Export annotations
        FileOutputStream fileStream = new FileOutputStream(_dataDir + "exportannotations.xfdf");
        int[] annotType = { AnnotationType.Line, AnnotationType.Square };
        AnnotationEditor.exportAnnotationsXfdf(fileStream, 1, 1, annotType);
        fileStream.flush();
        fileStream.close();
    }
```

The next code snippet describes how import annotations to an XFDF file:

```java
public static void ImportAnnotationXFDF()
{
    // Create PdfAnnotationEditor object
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // Create a new PDF document
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // Import annotation
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // Save output PDF
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## Yet another way to export/import annotations at once

In the code below an ImportAnnotations method allows import annotations directly from another PDF doc.

```java
    public static void ImportAnnotationFromPDF() throws IOException {
        // Create PdfAnnotationEditor object
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
        // Create a new PDF document
        Document document = new Document();

        document.getPages().add();
        AnnotationEditor.bindPdf(document);
        String exportFileName = _dataDir + "exportannotations.xfdf";
        java.io.File f = new java.io.File(exportFileName);
        if (!f.exists()) {
            ExportAnnotationXFDF();
        }

        // Annotation Editor allows import annotations from several PDF documents,
        // but in this example, we use only one.
        String[] fileNames = { _dataDir + "AnnotationDemo1.pdf" };
        AnnotationEditor.importAnnotations(fileNames);

        // Save output PDF
        document.save(_dataDir + "AnnotationDemo3.pdf");
    }
}
```
