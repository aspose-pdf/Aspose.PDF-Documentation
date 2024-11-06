---
title: Converter TIFF para PDF 
linktitle: Converter TIFF para PDF
type: docs
weight: 210
url: pt/androidjava/convert-tiff-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF para Android via Java permite converter imagens TIFF de várias páginas ou quadros para aplicativos PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para Android via Java** suporta o formato de arquivo, seja uma imagem <abbr title="Tag Image File Format">TIFF</abbr> de um único quadro ou de vários quadros. Isso significa que você pode converter a imagem TIFF para PDF em suas aplicações Java.

TIFF ou TIF, Tagged Image File Format, representa imagens rasterizadas que se destinam ao uso em uma variedade de dispositivos que cumprem este padrão de formato de arquivo.
 TIFF image pode conter vários quadros com imagens diferentes. O formato de arquivo Aspose.PDF também é suportado, seja uma imagem TIFF de um único quadro ou de múltiplos quadros. Assim, você pode converter a imagem TIFF para PDF em suas aplicações Java. Portanto, consideraremos um exemplo de conversão de imagem TIFF de várias páginas para documento PDF de várias páginas com os passos abaixo:

1. Instanciar uma instância da classe Document
1. Carregar a imagem TIFF de entrada
1. Obter FrameDimension dos quadros
1. Adicionar nova página para cada quadro
1. Finalmente, salvar as imagens nas páginas do PDF

Além disso, o trecho de código a seguir mostra como converter uma imagem TIFF de várias páginas ou múltiplos quadros para PDF:

```java
 public void convertTIFFtoPDF () {
        // Inicializar objeto documento
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

        // Carregar arquivo de imagem TIFF de exemplo
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

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