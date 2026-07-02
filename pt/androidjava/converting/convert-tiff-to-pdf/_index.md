---
title: Converter TIFF para PDF
linktitle: Converter TIFF para PDF
type: docs
weight: 210
url: /pt/androidjava/convert-tiff-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java permite converter imagens TIFF de várias páginas ou de vários quadros para aplicativos PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** formato de arquivo suportado, seja um quadro único ou múltiplos quadros <abbr title="Tag Image File Format">TIFF</abbr> imagem. Isso significa que você pode converter a imagem TIFF para PDF em suas aplicações Java.

TIFF ou TIF, Tagged Image File Format, representa imagens raster que destinam‑se ao uso em uma variedade de dispositivos que obedecem a este padrão de formato de arquivo. A imagem TIFF pode conter vários quadros com imagens diferentes. O formato de arquivo Aspose.PDF também é suportado, seja um quadro único ou uma imagem TIFF de múltiplos quadros. Assim, você pode converter a imagem TIFF para PDF em suas aplicações Java. Portanto, consideraremos um exemplo de conversão de imagem TIFF de várias páginas para documento PDF de várias páginas com os passos abaixo:

1. Instanciar uma instância da classe Document
1. Carregar a imagem TIFF de entrada
1. Obter FrameDimension dos quadros
1. Adicionar nova página para cada quadro
1. Finalmente, salvar imagens nas páginas PDF

Além disso, o trecho de código a seguir mostra como converter uma imagem TIFF com várias páginas ou vários quadros em PDF:

```java
 public void convertTIFFtoPDF () {
        // Initialize document object
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

        // Load sample TIFF image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

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

