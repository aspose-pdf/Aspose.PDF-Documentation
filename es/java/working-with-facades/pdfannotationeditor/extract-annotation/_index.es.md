---
title: Extraer Anotación (fachadas)
type: docs
weight: 30
url: /java/extract-annotation/
description: Esta sección explica cómo extraer anotaciones de un archivo PDF a XFDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[extractAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#extractAnnotations-int-int-int:A-0) método te permite extraer anotaciones de un archivo PDF. Para extraer anotaciones, necesitas crear un objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) y vincular el archivo PDF usando el método [BindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-). Después de eso, necesitas crear una enumeración de tipos de anotaciones que deseas extraer del archivo PDF. Y finalmente, guarda el archivo PDF actualizado usando el método Save del objeto PdfAnnotationEditor. El siguiente fragmento de código te muestra cómo extraer anotaciones de un archivo PDF.

```java
  public static void ExtractAnnotation() {
        var document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // Extraer anotaciones
        var annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
        var annotations = annotationEditor.extractAnnotations(1, 2, annotationTypes);
        for (var annotation : annotations) {
            System.out.println(annotation.getContents());
        }
```