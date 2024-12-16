---
title: Converter JPG para PDF 
linktitle: Converter JPG para PDF 
type: docs
weight: 190
url: /pt/androidjava/convert-jpg-to-pdf/
lastmod: "2021-06-05"
description: Aprenda como converter facilmente imagens JPG para um arquivo PDF. Além disso, você pode converter uma imagem para PDF com a mesma altura e largura da página.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Não precisa se perguntar como converter JPG para PDF, porque a biblioteca Apose.PDF para Android via Java tem a melhor solução.

Você pode converter muito facilmente imagens JPG para PDF com Aspose.PDF para Android via Java seguindo os passos:

1. Inicialize o objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
2. Carregue a imagem JPG e adicione ao parágrafo
3. Salve o PDF de saída

O trecho de código abaixo mostra como converter uma imagem JPG para PDF:

```java
public void convertJPEGtoPDF () {
        // Inicializar objeto do documento
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

        // Carregar arquivo de imagem JPEG de exemplo
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

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