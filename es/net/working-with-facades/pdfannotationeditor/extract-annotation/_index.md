---
title: Extraer Anotaciones de PDF 
type: docs
weight: 30
url: /es/net/extract-annotation/
description: Esta sección explica cómo extraer anotaciones de un archivo PDF a XFDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

El método [ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) te permite extraer anotaciones de un archivo PDF. Para extraer anotaciones, necesitas crear un objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) y enlazar el archivo PDF usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, necesitas crear una enumeración de tipos de anotación que quieras extraer del archivo PDF.

Luego puedes usar el método [ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) para extraer las anotaciones a un ArrayList. Después de eso, puedes recorrer esta lista y obtener anotaciones individuales. Y finalmente, guarda el archivo PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) del objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor). El siguiente fragmento de código te muestra cómo extraer anotaciones de un archivo PDF.

```csharp
 public static void ExtractAnnotation()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // Extract annotations
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
```