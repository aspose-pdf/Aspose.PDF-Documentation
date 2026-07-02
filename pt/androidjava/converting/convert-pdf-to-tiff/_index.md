---
title: Converter PDF para TIFF
linktitle: Converter PDF para TIFF
type: docs
weight: 30
url: /pt/androidjava/convert-pdf-to-tiff/
lastmod: "2026-07-01"
description: Este artigo descreve como converter páginas de um documento PDF em imagem TIFF. Você aprenderá como converter todas as páginas ou páginas individuais em imagens TIFF com Aspose.PDF for Android via Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** torna possível converter páginas PDF para imagens TIFF.

O [Classe TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) permite converter páginas de PDF em imagens TIFF. Esta classe fornece um método chamado Process que permite converter todas as páginas de um arquivo PDF em uma única imagem TIFF.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Converter páginas de PDF em uma única imagem TIFF

Aspose.PDF for Android via Java explica como converter todas as páginas de um arquivo PDF em uma única imagem TIFF:

1. Crie um objeto da classe Document.
1. Chame o método Process para converter o documento.
1. Para definir as propriedades do arquivo de saída, use a classe TiffSettings.

O trecho de código a seguir mostra como converter todas as páginas do PDF em uma única imagem TIFF.

```java
public void convertPDFtoTiffSinglePage() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Converter página única para imagem TIFF

Aspose.PDF for Android via Java permite converter uma página específica de um arquivo PDF para uma imagem TIFF; use uma versão sobrecarregada do método Process(..) que recebe o número da página como argumento para a conversão. O trecho de código a seguir demonstra como converter a primeira página de um PDF para o formato TIFF.

```java
public void convertPDFtoTiffAllPages() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Use o algoritmo Bradley durante a conversão

Aspose.PDF for Android via Java tem suportado o recurso de converter PDF para TIFF usando compressão LZW e, em seguida, com o uso do AForge, a Binarização pode ser aplicada. Contudo, um dos clientes solicitou que, para algumas imagens, seja obtido o limiar usando Otsu, portanto eles também gostariam de usar o Bradley.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }
```

