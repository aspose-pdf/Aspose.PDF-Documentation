---
title: Convertir BMP a PDF
linktitle: Convertir BMP a PDF
type: docs
weight: 220
url: /es/androidjava/convert-bmp-to-pdf/
lastmod: "2026-06-30"
description: Puede convertir fácilmente archivos BMP bitmap a PDF utilizados para almacenar imágenes bitmap digitales de forma independiente del dispositivo de visualización usando Aspose.PDF. para Android vía Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Las imágenes BMP son archivos con extensión .BMP que representan archivos de imagen bitmap y se utilizan para almacenar imágenes digitales bitmap. Estas imágenes son independientes del adaptador gráfico y también se denominan formato de bitmap independiente del dispositivo (DIB).
Puede convertir BMP a PDF con la API Aspose.PDF para Java. Por lo tanto, puede seguir los siguientes pasos para convertir imágenes BMP:

1. Inicializar un nuevo Document
1. Cargar archivo de imagen BMP de ejemplo
1. Finalmente, guarde el archivo PDF de salida

Así que el siguiente fragmento de código sigue estos pasos y muestra cómo convertir BMP a PDF usando Java:

```java
public void convertBMPtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.bmp");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

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

