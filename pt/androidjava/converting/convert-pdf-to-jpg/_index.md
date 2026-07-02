---
title: Converter PDF para JPG
linktitle: Converter PDF para JPG
type: docs
weight: 10
url: /pt/androidjava/convert-pdf-to-jpg/
description:  Esta página descreve como converter páginas PDF para imagem JPEG, converter todas e páginas individuais para imagens JPEG com Aspose.PDF for Android via Java.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Converter páginas PDF para imagens JPG

A classe JpegDevice permite converter páginas PDF para imagens JPEG. Esta classe fornece um método chamado process(..) que permite converter uma página específica do arquivo PDF para imagem JPEG.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão Aspose.PDF e visualizar os resultados online neste link  [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## Converter página PDF única para imagem JPG

Aspose.PDF for Android via Java permite converter uma única página para o formato Jpeg.

Para converter apenas uma página para uma imagem JPEG:

1. Crie um objeto da classe Document para obter a página que você deseja converter.
1. Chame o método process(..) para converter a página em uma imagem JPEG.

O trecho de código a seguir mostra as etapas para converter a primeira página do PDF para o formato JPEG.

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create JpegDevice object with particular resolution
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Converter todas as páginas PDF para imagem JPG

Aspose.PDF for Android via Java permite converter todas as páginas de um arquivo PDF em imagens:

1. Percorra todas as páginas do arquivo.
1. Converter cada página individualmente:
    - Crie um objeto da classe Document para carregar o documento PDF.
    - Obtenha a página que deseja converter.
    - Chame o método Process para converter a página para Jpeg.

- O trecho de código a seguir mostra como converter todas as páginas PDF em imagens Jpeg.

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create JpegDevice object with particular resolution
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Close the stream
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

## Converter página PDF específica para imagem JPG

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get rectangle of particular page region
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // set CropBox value as per rectangle of desired page region
        document.getPages().get_Item(1).setCropBox(pageRect);
        // save cropped document into stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // open cropped PDF document from stream and convert to image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create Jpeg device with specified attributes
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
