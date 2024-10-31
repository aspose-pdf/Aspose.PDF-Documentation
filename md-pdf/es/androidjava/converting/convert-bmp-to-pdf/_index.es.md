---
title: Convertir BMP a PDF 
linktitle: Convertir BMP a PDF
type: docs
weight: 220
url: /androidjava/convert-bmp-to-pdf/
lastmod: "2021-06-05"
description: Puede convertir fácilmente archivos bitmap BMP a PDF utilizados para almacenar imágenes bitmap digitales por separado del dispositivo de visualización usando Aspose.PDF para Android a través de Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Las imágenes BMP son archivos con extensión .BMP que representan archivos de imagen Bitmap que se utilizan para almacenar imágenes digitales bitmap. Estas imágenes son independientes del adaptador gráfico y también se les llama formato de archivo de mapa de bits independiente del dispositivo (DIB).
Puede convertir BMP a PDF con Aspose.PDF para Java API. Por lo tanto, puede seguir los siguientes pasos para convertir imágenes BMP:

1. Inicializar un nuevo Documento
1. Cargar archivo de imagen BMP de muestra
1. Finalmente, guardar el archivo PDF de salida

El siguiente fragmento de código sigue estos pasos y muestra cómo convertir BMP a PDF usando Java:

```java
public void convertBMPtoPDF () {
        // Inicializar objeto documento
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

        // Cargar archivo de imagen BMP de muestra
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

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