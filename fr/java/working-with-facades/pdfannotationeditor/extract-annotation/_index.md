---
title: Extraire l'Annotation (façades)
type: docs
weight: 30
url: /fr/java/extract-annotation/
description: Cette section explique comment extraire des annotations d'un fichier PDF en XFDF avec Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[extractAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#extractAnnotations-int-int-int:A-0) méthode vous permet d'extraire des annotations d'un fichier PDF. Pour extraire des annotations, vous devez créer un objet [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) et lier le fichier PDF en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-). Après cela, vous devez créer une énumération des types d'annotations que vous souhaitez extraire du fichier PDF. Et enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode Save de l'objet PdfAnnotationEditor. Le code suivant vous montre comment extraire des annotations d'un fichier PDF.

```java
  public static void ExtractAnnotation() {
        var document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // Extraire les annotations
        var annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
        var annotations = annotationEditor.extractAnnotations(1, 2, annotationTypes);
        for (var annotation : annotations) {
            System.out.println(annotation.getContents());
        }
```