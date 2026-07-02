---
title: Converter DICOM para PDF
linktitle: Converter DICOM para PDF
type: docs
weight: 250
url: /pt/androidjava/convert-dicom-to-pdf/
lastmod: "2026-07-01"
description: Converter imagens médicas armazenadas no formato DICOM para um arquivo PDF usando Aspose.PDF for Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> é um padrão para manipular, armazenar, imprimir e transmitir informações em imagens médicas. Inclui uma definição de formato de arquivo e um protocolo de comunicação de rede.

Aspsoe.PDF for Java permite que você converta arquivos DICOM para formato PDF, veja o próximo trecho de código:

1. Carregar imagem em stream
1. Inicializar [`Document object`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Carregar arquivo de imagem DICOM de exemplo
1. Salvar documento PDF de saída

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

