---
title: Modificar Anotaciones en su Archivo PDF (facades)
type: docs
weight: 50
url: es/java/modify-annotations/
description: Esta sección explica cómo modificar anotaciones del archivo PDF a XFDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

El método [modifyAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotations-int-int-com.aspose.pdf.Annotation-) le permite cambiar atributos básicos de una anotación, es decir, Asunto, Fecha de modificación, Autor, Color de la anotación y Bandera de apertura. También puede establecer el Autor directamente utilizando el método ModifyAnnotations. Esta clase también proporciona dos métodos sobrecargados para eliminar anotaciones. El primer método llamado DeleteAnnotations elimina todas las anotaciones de un archivo PDF.

Por ejemplo, en el siguiente código, considere cambiar el autor en nuestra anotación usando [modifyAnnotationsAuthor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotationsAuthor-int-int-java.lang.String-java.lang.String-).

```java
 public static void ModifyAnnotationsAuthor() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        annotationEditor.modifyAnnotationsAuthor(1, 2, "Usuario de Aspose", "Usuario de Aspose.PDF");
        annotationEditor.save(_dataDir + "ModifyAnnotationsAuthor.pdf");
    }
```

El segundo método le permite eliminar todas las anotaciones de un tipo especificado.

```java
    public static void ModifyAnnotations() {
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // Crear un nuevo objeto de tipo Anotación para modificar los atributos de la anotación
        DefaultAppearance defaultAppearance = new DefaultAppearance();
        FreeTextAnnotation annotation = new FreeTextAnnotation(document.getPages().get_Item(1),
                new Rectangle(1, 1, 1, 1), defaultAppearance);

        annotation.setTitle("Usuario de demostración de Aspose.PDF");
        annotation.setSubject("Artículo Técnico");

        // Modificar anotaciones en el archivo PDF
        annotationEditor.modifyAnnotations(1, 1, annotation);
        annotationEditor.save(_dataDir + "ModifyAnnotations.pdf");
    }
```


## Ver también

Intenta comparar y encontrar una manera de trabajar con anotaciones que te convenga. Aprendamos la sección de [Anotaciones PDF](/pdf/java/annotations/).