---
title: Eliminar Anotaciones (fachadas)
type: docs
weight: 10
url: /java/delete-annotations/
description: Esta sección explica cómo eliminar anotaciones con Aspose.PDF Facades utilizando la clase PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Puede utilizar la clase [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) para eliminar anotaciones, por un tipo de anotación especificado, del archivo PDF existente.
 Para hacer eso, necesitas crear un objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) y vincular el archivo PDF de entrada usando el método bindPdf. Después de eso, llama al método [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-), con el parámetro de cadena, para eliminar todas las anotaciones del archivo; el parámetro de cadena representa el tipo de anotación que se va a eliminar. Finalmente, utiliza el método save para guardar el archivo PDF actualizado.

El siguiente fragmento de código te muestra cómo eliminar una anotación por tipo de anotación especificado.

```java
public static void DeleteAnnotation() {
        // Abrir documento
        Scanner consoleScanner = new Scanner(System.in);
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        int index;
        for (index = 1; index <= document.getPages().get_Item(1).getAnnotations().size(); index++) {
            System.out.println(index + ". " + document.getPages().get_Item(1).getAnnotations().get_Item(index).getName()
                    + " " + document.getPages().get_Item(1).getAnnotations().get_Item(index).toString());
        }
        System.out.print("Por favor, introduce el número:");
        index = consoleScanner.nextInt();

        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);
        annotationEditor.deleteAnnotation(document.getPages().get_Item(1).getAnnotations().get_Item(1).getName());

        // Guardar PDF actualizado
        annotationEditor.save(_dataDir + "DeleteAnnotation.pdf");
        consoleScanner.close();
    }
    ```
[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) permite eliminar todas las anotaciones del archivo PDF existente.

Primero, cree un [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) y vincule el archivo PDF de entrada usando el método BindPdf.

Después de eso, llame al método [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) para eliminar todas las anotaciones del archivo, y luego use el método Save para guardar el archivo PDF actualizado. El siguiente fragmento de código muestra cómo eliminar todas las anotaciones del archivo PDF.

```java
public static void DeleteAllAnnotations() {
    // Abrir documento
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
    // Eliminar todas las anotaciones
    annotationEditor.deleteAnnotations();
    // Guardar PDF actualizado
    annotationEditor.save(_dataDir + "DeleteAllAnnotations_out.pdf");
}
```