---
title: Convertir archivo PDF
type: docs
weight: 20
url: /es/java/convert-pdf-file/
description: Esta sección explica cómo convertir un archivo PDF con Aspose.PDF Facades usando la clase PdfConverter.
lastmod: "2021-06-05"
draft: false
---

## Convertir páginas PDF a diferentes formatos de imagen (Facades)

Para convertir páginas PDF a diferentes formatos de imagen, necesitas crear un objeto [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter) y abrir el archivo PDF usando el método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#bindPdf-java.lang.String-).

Después de eso, necesitas llamar al método [doConvert](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#doConvert--) para tareas de inicialización.
 Luego, puedes recorrer todas las páginas usando los métodos [hasNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#hasNextImage--) y [getNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#getNextImage-java.io.OutputStream-). El método getNextImage te permite crear una imagen de una página en particular. También necesitas pasar ImageType a este método para crear una imagen de un tipo específico, es decir, JPEG, GIF o PNG, etc.

Finalmente, llama al método close de la clase [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter).

El siguiente fragmento de código te muestra cómo convertir páginas PDF a imágenes.

```java
public static void ConvertPdfPagesToImages01() {
        // Crear objeto PdfConverter
        PdfConverter converter = new PdfConverter();

        // Vincular archivo pdf de entrada
        converter.bindPdf(_dataDir + "Sample-Document-01.pdf");

        // Inicializar el proceso de conversión
        converter.doConvert();
        
        int count=0;

        // Verificar si existen páginas y luego convertir a imagen una por una
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // Cerrar el objeto PdfConverter
        converter.close();
    }
```

En el siguiente fragmento de código, mostraremos cómo se pueden cambiar algunos parámetros. Con [setCoordinateType](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setCoordinateType-int-) establecemos el marco [CropBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCoordinateType#CropBox). Además, podemos cambiar [setResolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setResolution-com.aspose.pdf.devices.Resolution-) especificando el número de puntos por pulgada. El siguiente [setFormPresentationMode](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setFormPresentationMode-int-) - modo de presentación del formulario. Luego indicamos el [setStartPage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setStartPage-int-) con el cual se establece el número de página del comienzo de la conversión. También podemos especificar la última página estableciendo un rango.

```java
public static void ConvertPdfPagesToImages02()
    {
        // Crear objeto PdfConverter
        PdfConverter converter = new PdfConverter();

        // Enlazar archivo pdf de entrada
        converter.bindPdf(_dataDir + "sample.pdf");

        // Iniciar el proceso de conversión
        converter.doConvert();
        converter.setCoordinateType(PageCoordinateType.CropBox);
        converter.setResolution (new Resolution(600));
        converter.setFormPresentationMode(FormPresentationMode.Editor);
        converter.setStartPage(2);
        int count=0;
        // Verificar si existen páginas y luego convertir a imagen una por una
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // Cerrar el objeto PdfConverter
        converter.close();
    }
```