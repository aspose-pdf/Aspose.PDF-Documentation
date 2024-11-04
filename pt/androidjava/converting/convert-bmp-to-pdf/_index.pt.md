---
title: Converter BMP para PDF 
linktitle: Converter BMP para PDF
type: docs
weight: 220
url: /androidjava/convert-bmp-to-pdf/
lastmod: "2021-06-05"
description: Você pode facilmente converter arquivos bitmap BMP para PDF usados para armazenar imagens bitmap digitais separadamente do dispositivo de exibição usando Aspose.PDF. para Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Imagens BMP são arquivos com extensão .BMP que representam arquivos de imagem bitmap usados para armazenar imagens digitais bitmap. Essas imagens são independentes do adaptador gráfico e também são chamadas de formato de arquivo bitmap independente de dispositivo (DIB).
Você pode converter BMP para PDF com a API Aspose.PDF para Java. Portanto, você pode seguir os seguintes passos para converter imagens BMP:

1. Inicialize um novo Documento
1. Carregue o arquivo de imagem BMP de exemplo
1. Finalmente, salve o arquivo PDF de saída

Assim, o trecho de código a seguir segue essas etapas e mostra como converter BMP para PDF usando Java:

```java
public void convertBMPtoPDF () {
        // Inicializar objeto de documento
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

        // Carregar arquivo de imagem BMP de exemplo
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

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