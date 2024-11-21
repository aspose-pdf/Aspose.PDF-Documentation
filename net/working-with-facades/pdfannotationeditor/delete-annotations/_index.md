---
title: Delete Annotations (facades)
type: docs
weight: 10
url: /net/delete-annotations/
description: This section explains how to delete annotations with Aspose.PDF Facades using PdfAnnotationEditor Class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Delete All Annotations from an Existing PDF File

[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) allows you delete all the annotations from the existing PDF file. First off, create a [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) method to delete all the annotations from the file, and then use [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to save the updated PDF file. The following code snippet shows you how to delete all the annotations from the PDF file.

```csharp
public static void DeleteAllAnnotations()
{
    // Open document
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
    // Delete all annoations
    annotationEditor.DeleteAnnotations();
    // Save updated PDF
    annotationEditor.Save(_dataDir + "DeleteAllAnnotation.pdf");
}   
```

## Delete All Annotations by Specified Type

You can use [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class to delete all the annotations, by a specified annotation type, from the existing PDF file. In order to do that you need to create a [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) method, with the string parameter, to delete all the annotations from the file; the string parameter represents the annotation type to be deleted. Finally, use [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to save the updated PDF file. The following code snippet shows you how to delete all annotations by specified annotation type.

```csharp
public static void DeleteAnnotation()
{
    // Open document
    var document = new Document(_dataDir + "sample_cats_dogs.pdf");
    int index;
    for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
    {
        System.Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
    }
    System.Console.Write("Please enter number:");
    index = int.Parse(System.Console.ReadLine());

    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.BindPdf(document);
    annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

    // Save updated PDF
    annotationEditor.Save(_dataDir + "DeleteAnnotation.pdf");
}
```
