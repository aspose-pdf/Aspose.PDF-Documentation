---
title: Convertir JPG a PDF
linktitle: Convertir JPG a PDF
type: docs
weight: 190
url: /es/androidjava/convert-jpg-to-pdf/
lastmod: "2026-06-30"
description: Aprenda cómo convertir fácilmente imágenes JPG a un archivo PDF. Además, puede convertir una imagen a PDF con la misma altura y anchura de la página.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

No es necesario preguntarse cómo convertir JPG a PDF, porque Apose.PDF for Android via Java library tiene la mejor solución.

Puede convertir muy fácilmente imágenes JPG a PDF con Aspose.PDF for Android via Java siguiendo los pasos:

1. Inicializar objeto de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) clase
1. Cargar imagen JPG y agregar al párrafo
1. Guardar PDF de salida

El fragmento de código a continuación muestra cómo convertir una imagen JPG a PDF:

```java
public void convertJPEGtoPDF () {
        // Initialize document object
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

        // Load sample JPEG image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

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
