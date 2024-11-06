---
title: Convertir JPG a PDF 
linktitle: Convertir JPG a PDF 
type: docs
weight: 190
url: es/androidjava/convert-jpg-to-pdf/
lastmod: "2021-06-05"
description: Aprende cómo convertir fácilmente imágenes JPG a un archivo PDF. Además, puedes convertir una imagen a PDF con la misma altura y ancho de la página.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

No necesitas preguntarte cómo convertir JPG a PDF, porque Apose.PDF para Android a través de la biblioteca Java tiene la mejor solución.

Puedes convertir muy fácilmente imágenes JPG a PDF con Aspose.PDF para Android a través de Java siguiendo estos pasos:

1. Inicializa un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Carga la imagen JPG y añádela al párrafo
1. Guarda el PDF de salida

El fragmento de código a continuación muestra cómo convertir una imagen JPG a PDF:

```java
public void convertJPEGtoPDF () {
        // Inicializar objeto documento
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.jpg");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Cargar archivo de imagen JPEG de muestra
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

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