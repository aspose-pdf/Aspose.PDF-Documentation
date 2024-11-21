---
title: Modify Annotations in your PDF 
type: docs
weight: 50
url: /net/modify-annotations/
description: This section explains how to modify annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Modify annotation

[ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) method allows you to change basic attributes of an annotation i.e. Subject, Modified date, Author, Annotation color, and Open flag. You can also set Author directly by using ModifyAnnotations method. This class also provides two overloaded methods to delete annotations. The first method called DeleteAnnotations deletes all the annotations from a PDF file.  

For example, in the following code, consider changing the author in our annotation using [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor).

```csharp
public static void ModifyAnnotationsAuthor()
{
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
    annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
    annotationEditor.Save(_dataDir + "ModifyAnnotationsAuthor.pdf");
}
```

The second method allows you to delete all the annotations of a specified type.

```csharp
public static void ModifyAnnotations()
{
    var document = new Document(_dataDir + "sample_cats_dogs.pdf");
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.BindPdf(document);

    // Create a new object of type Annotation to modify annotation attributes
    var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance();
    Aspose.Pdf.Annotations.FreeTextAnnotation annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
        document.Pages[1],
        new Aspose.Pdf.Rectangle(1, 1, 1, 1),
        defaultAppearance)
    {
        // Set new annotation attributees
        Title = "Aspose.PDF Demo User",
        Subject = "Technical Article"
    };
    // Modify annotations in the PDF file
    annotationEditor.ModifyAnnotations(1, 1, annotation);
    annotationEditor.Save(_dataDir + "ModifyAnnotations.pdf");
}
```

## See also

Try to compare and find a way to work with annotations that suits you. Lets learn [PDF Annotations](/pdf/net/annotations/) section.