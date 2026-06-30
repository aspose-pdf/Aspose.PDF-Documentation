---
title: Convertir TIFF a PDF
linktitle: Convertir TIFF a PDF
type: docs
weight: 210
url: /es/androidjava/convert-tiff-to-pdf/
lastmod: "2026-06-30"
description: Aspose.PDF for Android via Java permite convertir imágenes TIFF de varias páginas o varios fotogramas a aplicaciones PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** formato de archivo compatible, ya sea un solo fotograma o varios fotogramas <abbr title="Tag Image File Format">TIFF</abbr> imagen. Significa que puedes convertir la imagen TIFF a PDF en tus aplicaciones Java.

TIFF o TIF, Tagged Image File Format, representa imágenes raster que están destinadas a usarse en una variedad de dispositivos que cumplen con este estándar de formato de archivo. La imagen TIFF puede contener varios fotogramas con distintas imágenes. El formato de archivo Aspose.PDF también es compatible, ya sea un fotograma único o una imagen TIFF de varios fotogramas. Por lo tanto, puedes convertir la imagen TIFF a PDF en tus aplicaciones Java. Por consiguiente, consideraremos un ejemplo de conversión de una imagen TIFF de varias páginas a un documento PDF de varias páginas con los pasos siguientes:

1. Instanciar una instancia de la clase Document
1. Cargar la imagen TIFF de entrada
1. Obtener FrameDimension de los marcos
1. Agregar una nueva página para cada marco
1. Finalmente, guardar imágenes en páginas PDF

Además, el siguiente fragmento de código muestra cómo convertir una imagen TIFF multipágina o multimarco a PDF:

```java
 public void convertTIFFtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.tiff");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample TIFF image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

