---
title: Convertir DICOM a PDF
linktitle: Convertir DICOM a PDF
type: docs
weight: 250
url: /es/androidjava/convert-dicom-to-pdf/
lastmod: "2026-06-30"
description: Convertir imágenes médicas guardadas en formato DICOM a un archivo PDF usando Aspose.PDF para Android a través de Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> es un estándar para el manejo, almacenamiento, impresión y transmisión de información en imágenes médicas. Incluye una definición de formato de archivo y un protocolo de comunicaciones de red.

Aspsoe.PDF para Java le permite convertir archivos DICOM a formato PDF, consulte el siguiente fragmento de código:

1. Cargar imagen en flujo
1. Inicializar [`Document object`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Cargar archivo de imagen DICOM de muestra
1. Guardar documento PDF de salida

```java
//    Convert DICOM to PDF
    public void convertDICOMtoPDF () {
        // Initialize document object
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

        // Load sample BMP image file
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

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

