---
title: Converter JPG para PDF
linktitle: Converter JPG para PDF
type: docs
weight: 190
url: /pt/androidjava/convert-jpg-to-pdf/
lastmod: "2026-07-01"
description: Aprenda como converter facilmente imagens JPG em arquivo PDF. Além disso, você pode converter uma imagem para PDF com a mesma altura e largura da página.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Não há necessidade de se perguntar como converter JPG para PDF, pois a biblioteca Apose.PDF for Android via Java tem a melhor solução.

Você pode converter imagens JPG para PDF muito facilmente com Aspose.PDF for Android via Java seguindo os passos:

1. Inicialize o objeto de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) classe
1. Carregar imagem JPG e adicionar ao parágrafo
1. Salvar PDF de saída

O trecho de código abaixo mostra como converter uma Imagem JPG para PDF:

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
