---
title: Convertir TIFF a PDF 
linktitle: Convertir TIFF a PDF
type: docs
weight: 210
url: /androidjava/convert-tiff-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF para Android a través de Java permite convertir imágenes TIFF de varias páginas o varios fotogramas a aplicaciones PDF. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para Android a través de Java** admite el formato de archivo, ya sea una imagen <abbr title="Formato de Archivo de Imagen Etiquetada">TIFF</abbr> de un solo fotograma o de varios fotogramas. Esto significa que puedes convertir la imagen TIFF a PDF en tus aplicaciones Java.

TIFF o TIF, Formato de Archivo de Imagen Etiquetada, representa imágenes rasterizadas que están destinadas a ser utilizadas en una variedad de dispositivos que cumplen con este estándar de formato de archivo.
 TIFF image can contain several frames with different images. Aspose.PDF file format is also supported, be it a single frame or multi-frame TIFF image. So you can convert the TIFF image to PDF in your Java applications. Therefore, we will consider an example of converting multi-page TIFF image to multi-page PDF document with below steps:

1. Instanciar una instancia de la clase Documento
1. Cargar la imagen TIFF de entrada
1. Obtener FrameDimension de los fotogramas
1. Agregar nueva página para cada fotograma
1. Finalmente, guardar imágenes en páginas PDF

Además, el siguiente fragmento de código muestra cómo convertir una imagen TIFF de múltiples páginas o múltiples fotogramas a PDF:

```java
 public void convertTIFFtoPDF () {
        // Inicializar objeto de documento
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

        // Cargar archivo de imagen TIFF de ejemplo
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

        // Guardar documento de salida
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```