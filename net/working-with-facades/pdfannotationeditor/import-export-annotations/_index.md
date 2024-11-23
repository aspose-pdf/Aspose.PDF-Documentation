---
title: Import and Export Annotations to XFDF 
type: docs
weight: 20
url: /net/import-export-annotations/
description: This section explains how to import and export annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF stand for XML Forms Data Format. It is an XML based file format. This file format is used to represent form data or annotations contained in a PDF form. XFDF can be used for many different purposes, but in our case, it can be used to either send or receive form data or annotations to other computers or servers etc, or it can be used to archive the form data or annotations. In this article, we will see how  Aspose.Pdf.Facades has taken this concept into consideration and how we can import and export annotations data to XFDF file.

## Importing and Exporting Annotations to XFDF

[Aspose.PDF for .NET](/pdf/net/) is a feature rich component when it comes to editing the PDF documents. As we know XFDF is an important aspect of PDF forms manipulation, [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) in [Aspose.PDF for .NET](/pdf/net/) has considered this very well, and have provided methods to import and export annotations data to XFDF files.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class contains two methods to work with import and export of annotations to XFDF file. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) method provides the functionality to export annotations from a PDF document to XFDF file, while [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) method allows you to import annotations from an existing XFDF file. In order to import or export annotations we need to specify the annotation types. We can specify these types in the form of an enumeration and then pass this enumeration as an argument to any of these methods. This way, the annotations of the specified types will only be imported or exported to an XFDF file.

The following code snippet shows you how to import annotations to an XFDF file:

```csharp
public static void ImportAnnotation()
{
    var sources = new string[] { dataDir + "sample_cats_dogs.pdf" };
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.BindPdf(dataDir + "sample.pdf");
    annotationEditor.ImportAnnotations(sources);
    annotationEditor.Save(dataDir + "sample_demo.pdf");
}
```

The next code snippet describes how import/export annotations to an XFDF file:

```csharp
public static void ImportExportXFDF01()
{
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.BindPdf(dataDir + "sample_cats_dogs.pdf");
    System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(dataDir + "sample.xfdf");
    annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
    xmlOutputStream.Close();
    var document = new Document();
    document.Pages.Add();
    annotationEditor.BindPdf(document);
    annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(dataDir + "sample.xfdf"));
    annotationEditor.Save(dataDir + "ImportedAnnotation.pdf");
}
```

This way, the annotations of the specified types will only be imported or exported to an XFDF file.

```csharp
public static void ImportExportXFDF02()
{
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.BindPdf(dataDir + "sample_cats_dogs.pdf");
    System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(dataDir + "sample.xfdf");
    var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
    annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 2, 2, annotationTypes);
    xmlOutputStream.Close();

    var document = new Document(dataDir + "sample.pdf");
    document.Pages.Add();
    annotationEditor.BindPdf(document);
    annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(dataDir + "sample.xfdf"));
    annotationEditor.Save(dataDir + "ImportedAnnotation.pdf");
}
```