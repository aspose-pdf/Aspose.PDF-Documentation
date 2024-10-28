---
title: Modify Annotations in your PDF File (facades)
type: docs
weight: 50
url: /java/modify-annotations/
description: This section explains how to modify annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[modifyAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotations-int-int-com.aspose.pdf.Annotation-) method allows you to change basic attributes of an annotation i.e. Subject, Modified date, Author, Annotation color, and Open flag. You can also set Author directly by using ModifyAnnotations method. This class also provides two overloaded methods to delete annotations. The first method called DeleteAnnotations deletes all the annotations from a PDF file.  

For example, in the following code, consider changing the author in our annotation using [modifyAnnotationsAuthor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotationsAuthor-int-int-java.lang.String-java.lang.String-).

```java
 public static void ModifyAnnotationsAuthor() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        annotationEditor.modifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
        annotationEditor.save(_dataDir + "ModifyAnnotationsAuthor.pdf");
    }
```

The second method allows you to delete all the annotations of a specified type.

```java
    public static void ModifyAnnotations() {
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // Create a new object of type Annotation to modify annotation attributes
        DefaultAppearance defaultAppearance = new DefaultAppearance();
        FreeTextAnnotation annotation = new FreeTextAnnotation(document.getPages().get_Item(1),
                new Rectangle(1, 1, 1, 1), defaultAppearance);

        annotation.setTitle("Aspose.PDF Demo User");
        annotation.setSubject("Technical Article");

        // Modify annotations in the PDF file
        annotationEditor.modifyAnnotations(1, 1, annotation);
        annotationEditor.save(_dataDir + "ModifyAnnotations.pdf");
    }
```

## See also

Try to compare and find a way to work with annotations that suits you. Lets learn [PDF Annotations](/pdf/java/annotations/) section.