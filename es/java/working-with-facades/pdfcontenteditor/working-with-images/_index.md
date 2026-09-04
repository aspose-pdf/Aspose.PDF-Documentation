---
title: Trabajando con Imágenes
type: docs
weight: 30
url: /es/java/working-with-image/
description: Esta sección explica cómo reemplazar imágenes con Aspose.PDF Facades - un conjunto de herramientas para operaciones populares con PDF.
lastmod: "2021-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Eliminar Imágenes de una Página Particular de un PDF (Facades)

La clase [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) permite reemplazar imágenes en un archivo PDF existente.
 El método [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) te ayuda a lograr este objetivo. Necesitas crear un objeto de la clase [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) y vincular el archivo PDF de entrada usando el método bindPdf. Después de eso, necesitas llamar al método [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) con tres parámetros: un número de página, índice de la imagen a reemplazar y la ruta de la imagen que se va a reemplazar.

El siguiente fragmento de código te muestra cómo reemplazar una imagen en un archivo PDF existente.

```java
public class PdfContentEditorImages {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/facades/PdfContentEditor/";

    public static void DeleteImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage(2, new int [] { 1,3 });
        editor.save(_dataDir + "PdfContentEditorDemo10.pdf");
    }
```

## Eliminar Todas las Imágenes de un Archivo PDF (Facades)

Todas las imágenes pueden ser eliminadas de un archivo PDF usando el método [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) de [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). Llame al método [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) – la sobrecarga sin ningún parámetro – para eliminar todas las imágenes, y luego guarde el archivo PDF actualizado usando el método Save.

```java
   public static void DeleteImages()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage();
        editor.save(_dataDir + "PdfContentEditorDemo11.pdf");
    }
```

## Reemplazar Imágenes en un Archivo PDF (Facades)

Puede reemplazar imágenes en el archivo PDF usando el método [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) de [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
   public static void ReplaceImage()
    {
        // Editor de contenido de PDF
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
        // Reemplazar imagen
        editor.replaceImage(2, 4, _dataDir+"cat04.jpg");
        // Guardar documento
        editor.save(_dataDir + "PdfContentEditorDemo12.pdf");
    }
```