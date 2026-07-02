---
title: Converter PDF para PNG
linktitle: Converter PDF para PNG
type: docs
weight: 20
url: /pt/androidjava/convert-pdf-to-png/
lastmod: "2026-07-01"
description: Esta página descreve como converter páginas de PDF para imagem PNG, converter todas e páginas individuais para imagens PNG com Aspose.PDF for Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Use a biblioteca **Aspose.PDF for Android via Java** para converter páginas de PDF em <abbr title="Portable Network Graphics">PNG</abbr> Imagens de forma acessível e conveniente.

A classe PngDevice permite converter páginas de PDF para imagens PNG. Esta classe fornece um método chamado Process que permite converter uma página específica do arquivo PDF para o formato de imagem PNG.

## Converter páginas de PDF para imagens PNG

Para converter todas as páginas de um arquivo PDF em arquivos PNG, itere pelas páginas individuais e converta cada uma para o formato PNG. O trecho de código a seguir mostra como percorrer todas as páginas de um arquivo PDF e converter cada uma em uma imagem PNG.

{{% alert color="primary" %}} 

Experimente online. Você pode verificar a qualidade da conversão Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## Converter página única de PDF para imagem PNG

Passe o índice da página como argumento para o método Process(..).
O trecho de código a seguir mostra as etapas para converter a primeira página do PDF para o formato PNG.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create PngDevice object with particular resolution
            PngDevice PngDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Converter todas as páginas PDF para imagem PNG

Aspose.PDF for Android via Java mostra como converter todas as páginas de um arquivo PDF em imagens:

1. Percorra todas as páginas do arquivo.
1. Converter cada página individualmente:
    1. Crie um objeto da classe Document para carregar o documento PDF.
    1. Obtenha a página que deseja converter.
    1. Chame o método Process para converter a página para Png.

O trecho de código a seguir mostra como converter todas as páginas PDF em imagens PNG.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
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
            PngDevice JpegDevice = new PngDevice(resolution);

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

## Converter página PDF específica para imagem PNG

Aspose.PDF for Android via Java mostra como converter uma página específica para o formato PNG:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
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
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
