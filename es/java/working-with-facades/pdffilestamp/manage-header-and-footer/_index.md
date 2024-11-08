---
title: Administrar Encabezado y Pie de Página
type: docs
weight: 40
url: /es/java/manage-header-and-footer/
description: Esta sección explica cómo administrar el Encabezado y Pie de Página con Aspose.PDF Facades utilizando la Clase PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Añadir Encabezado en un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite añadir un encabezado en un archivo PDF.
 En orden de añadir un encabezado, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Puedes dar formato al texto del encabezado utilizando la clase [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Una vez que estés listo para agregar el encabezado en el archivo, necesitas llamar al método [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). También necesitas especificar al menos el margen superior en el método [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-). Finalmente, guarda el archivo PDF de salida usando el método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). El siguiente fragmento de código te muestra cómo agregar un encabezado en un archivo PDF.

```java
 public static void AddHeader() {
        // Crear objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Crear texto formateado para el número de página
        FormattedText formattedText = new FormattedText("Aspose - ¡Tus expertos en formato de archivos!", java.awt.Color.YELLOW,
                java.awt.Color.BLACK, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // Añadir encabezado
        fileStamp.addHeader(formattedText, 20);

        // Guardar archivo PDF actualizado
        fileStamp.save(_dataDir + "AddHeader_out.pdf");

        // Cerrar fileStamp
        fileStamp.close();
    }
```

## Agregar pie de página en un archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite agregar un pie de página en un archivo PDF.
 Para agregar un pie de página, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Puedes dar formato al texto del pie de página usando la clase [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Una vez que estés listo para agregar el pie de página en el archivo, necesitas llamar al método [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). También necesitas especificar al menos el margen inferior en el método [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-). Finalmente, guarda el archivo PDF de salida usando el método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). El siguiente fragmento de código te muestra cómo agregar un pie de página en un archivo PDF.

```java
 public static void AddFooter() {
        // Crear objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Crear texto formateado para número de página
        FormattedText formattedText = new FormattedText("Aspose - ¡Tus expertos en formatos de archivo!", java.awt.Color.BLUE,
                java.awt.Color.GRAY, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // Agregar pie de página
        fileStamp.addFooter(formattedText, 10);

        // Guardar archivo PDF actualizado
        fileStamp.save(_dataDir + "AddFooter_out.pdf");

        // Cerrar fileStamp
        fileStamp.close();
    }
```

## Añadir Imagen en el Encabezado de un Archivo PDF Existente

La clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite añadir una imagen en el encabezado de un archivo PDF.
 En order a añadir una imagen en el encabezado, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Después de eso, necesitas llamar al método [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Puedes pasar la imagen al método [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-). Finalmente, guarda el archivo PDF de salida usando el método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). El siguiente fragmento de código te muestra cómo añadir una imagen en el encabezado de un archivo PDF.

```java
public static void AddImageHeader() {
        // Crear objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // Añadir encabezado
            fileStamp.addHeader(fs, 10);

            // Guardar archivo PDF actualizado
            fileStamp.save(_dataDir + "AddImage-Header_out.pdf");
        } catch (FileNotFoundException e) {

            e.printStackTrace();
        }

        // Cerrar fileStamp
        fileStamp.close();
    }
```

## Agregar Imagen en el Pie de Página de un Archivo PDF Existente

La clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite agregar una imagen en el pie de página de un archivo PDF.
 En orden de agregar una imagen en el pie de página, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Después de eso, necesitas llamar al método [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Puedes pasar la imagen al método [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-). Finalmente, guarda el archivo PDF de salida usando el método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). El siguiente fragmento de código te muestra cómo agregar una imagen en el pie de página del archivo PDF.

```java
    public static void AddImageFooter() {
        // Crear objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // Agregar pie de página
            fileStamp.addFooter(fs, 10);

            // Guardar archivo PDF actualizado
            fileStamp.save(_dataDir + "AddImage-Footer_out.pdf");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        // Cerrar fileStamp
        fileStamp.close();
    }
```