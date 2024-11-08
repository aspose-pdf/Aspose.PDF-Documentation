---
title: Converter DICOM para PDF 
linktitle: Converter DICOM para PDF
type: docs
weight: 250
url: /pt/androidjava/convert-dicom-to-pdf/
lastmod: "2021-06-05"
description: Converta imagens médicas salvas no formato DICOM para um arquivo PDF usando Aspose.PDF para Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> é um padrão para manipulação, armazenamento, impressão e transmissão de informações em imagens médicas. Inclui uma definição de formato de arquivo e um protocolo de comunicações de rede.

Aspose.PDF para Java permite que você converta arquivos DICOM para o formato PDF, veja o próximo trecho de código:

1. Carregar imagem no fluxo
1. Inicializar [`objeto Documento`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Carregar arquivo de imagem DICOM de exemplo
1. Salvar documento PDF de saída

```java
//    Converter DICOM para PDF
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

        // Carregar arquivo de imagem BMP de exemplo
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

        // Salvar documento de saída
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```