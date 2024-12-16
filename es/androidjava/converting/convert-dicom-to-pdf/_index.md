---
title: Convertir DICOM a PDF
linktitle: Convertir DICOM a PDF
type: docs
weight: 250
url: /es/androidjava/convert-dicom-to-pdf/
lastmod: "2021-06-05"
description: Convierta imágenes médicas guardadas en formato DICOM a un archivo PDF usando Aspose.PDF para Android a través de Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> es un estándar para manejar, almacenar, imprimir y transmitir información en imágenes médicas. Incluye una definición de formato de archivo y un protocolo de comunicaciones de red.

Aspose.PDF para Java le permite convertir archivos DICOM a formato PDF, ver el siguiente fragmento de código:

1. Cargar imagen en flujo
1. Inicializar [`objeto Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Cargar archivo de imagen DICOM de muestra
1. Guardar documento PDF de salida

```java
//    Convertir DICOM a PDF
    public void convertDICOMtoPDF () {
        // Inicializar objeto documento
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/bmode.dcm");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Cargar archivo de imagen BMP de muestra
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

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