---
title: Modificar Anotaciones en su PDF 
type: docs
weight: 50
url: /es/net/modify-annotations/
description: Esta sección explica cómo modificar anotaciones de un archivo PDF a XFDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

El método [ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) le permite cambiar atributos básicos de una anotación, es decir, Asunto, Fecha de modificación, Autor, Color de anotación y Bandera de apertura. También puede establecer directamente el Autor utilizando el método ModifyAnnotations. Esta clase también proporciona dos métodos sobrecargados para eliminar anotaciones. El primer método llamado DeleteAnnotations elimina todas las anotaciones de un archivo PDF.

Por ejemplo, en el siguiente código, considere cambiar el autor en nuestra anotación usando [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor).

```csharp
   public static void ModifyAnnotationsAuthor()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
            annotationEditor.Save(_dataDir + "ModifyAnnotationsAuthor.pdf");
        }
```

El segundo método te permite eliminar todas las anotaciones de un tipo especificado.

```csharp
   public static void ModifyAnnotations()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // Crear un nuevo objeto de tipo Anotación para modificar los atributos de la anotación
            var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance();
            Aspose.Pdf.Annotations.FreeTextAnnotation annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
                document.Pages[1],
                new Aspose.Pdf.Rectangle(1, 1, 1, 1),
                defaultAppearance)
            {

                // Establecer nuevos atributos de anotación
                Title = "Aspose.PDF Demo User",
                Subject = "Technical Article"
            };
            // Modificar anotaciones en el archivo PDF
            annotationEditor.ModifyAnnotations(1, 1, annotation);
            annotationEditor.Save(_dataDir + "ModifyAnnotations.pdf");
        }
```

## See also

Intenta comparar y encontrar una forma de trabajar con anotaciones que te convenga. Vamos a aprender la sección de [Anotaciones de PDF](/pdf/es/net/annotations/).