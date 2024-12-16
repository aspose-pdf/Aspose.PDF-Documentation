---
title: Convert PDF to JPG 
linktitle: Convert PDF to JPG
type: docs
weight: 10
url: /pt/androidjava/convert-pdf-to-jpg/
description: Esta página descreve como converter páginas PDF para imagem JPEG, converter todas e páginas únicas para imagens JPEG com Aspose.PDF para Android via Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Converter Páginas PDF para Imagens JPG

A classe JpegDevice permite que você converta páginas PDF em imagens JPEG. Esta classe fornece um método chamado process(..) que permite converter uma página específica do arquivo PDF em imagem JPEG.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}

## Converter uma única página PDF para imagem JPG

Aspose.PDF para Android via Java permite que você converta uma única página para o formato Jpeg.

Para converter apenas uma página em uma imagem JPEG:

1. Crie um objeto da classe Document para obter a página que você deseja converter.
1. Chame o método process(..) para converter a página em uma imagem JPEG.

O trecho de código a seguir mostra as etapas para converter a primeira página do PDF para o formato Jpeg.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Crie um objeto de fluxo para salvar a imagem de saída
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Crie um objeto Resolution
            Resolution resolution = new Resolution(300);

            // Crie um objeto JpegDevice com resolução específica
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Converta uma página específica e salve a imagem no fluxo
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Feche o fluxo
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Converter todas as páginas do PDF para imagem JPG

Aspose.PDF para Android via Java permite converter todas as páginas em um arquivo PDF para imagens:

1. Percorra todas as páginas no arquivo.
1. Converta cada página individualmente:
    - Crie um objeto da classe Document para carregar o documento PDF.
    - Obtenha a página que você deseja converter.
    - Chame o método Process para converter a página em Jpeg.

O trecho de código a seguir mostra como converter todas as páginas do PDF para imagens Jpeg.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Percorra todas as páginas do arquivo PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Crie um objeto de stream para salvar a imagem de saída
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Crie um objeto Resolution
            Resolution resolution = new Resolution(300);
            // Crie um objeto JpegDevice com uma resolução específica
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Converta uma página específica e salve a imagem no stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Feche o stream
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Converter uma página específica de PDF para imagem JPG

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Obter retângulo de uma região específica da página
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // definir valor de CropBox conforme o retângulo da região de página desejada
        document.getPages().get_Item(1).setCropBox(pageRect);
        // salvar documento cortado no stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // abrir documento PDF cortado do stream e converter para imagem
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Criar objeto Resolution
        Resolution resolution = new Resolution(300);
        // Criar dispositivo Jpeg com atributos especificados
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Converter uma página específica e salvar a imagem no stream
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```