---
title: Converter PDF para TIFF 
linktitle: Converter PDF para TIFF  
type: docs
weight: 30
url: /androidjava/convert-pdf-to-tiff/
lastmod: "2021-06-05"
description: Este artigo descreve como converter páginas em um documento PDF em imagem TIFF. Você aprenderá como converter todas ou páginas únicas em imagens TIFF com Aspose.PDF para Android via Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para Android via Java** possibilita a conversão de páginas PDF para imagens TIFF.

A [classe TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) permite que você converta páginas PDF em imagens TIFF. Esta classe fornece um método chamado Process, que permite converter todas as páginas de um arquivo PDF em uma única imagem TIFF.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Converter Páginas de PDF para Uma Única Imagem TIFF

Aspose.PDF para Android via Java explica como converter todas as páginas de um arquivo PDF em uma única imagem TIFF:

1. Crie um objeto da classe Document.
1. Chame o método Process para converter o documento.
1. Para definir as propriedades do arquivo de saída, use a classe TiffSettings.

O trecho de código a seguir mostra como converter todas as páginas do PDF em uma única imagem TIFF.

```java
public void convertPDFtoTiffSinglePage() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Criar objeto Resolution
        Resolution resolution = new Resolution(300);

        // Criar objeto TiffSettings
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Criar dispositivo TIFF
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Converter uma página específica e salvar a imagem no stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Converter Página Única para Imagem TIFF

Aspose.PDF para Android via Java permite converter uma página específica em um arquivo PDF para uma imagem TIFF, usando uma versão sobrecarregada do método Process(..) que aceita um número de página como argumento para conversão. O trecho de código a seguir mostra como converter a primeira página de um PDF para o formato TIFF.

```java
public void convertPDFtoTiffAllPages() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Criar objeto Resolution
        Resolution resolution = new Resolution(300);

        // Criar objeto TiffSettings
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Criar dispositivo TIFF
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Converter uma página específica e salvar a imagem no stream
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```


## Use o algoritmo de Bradley durante a conversão

Aspose.PDF para Android via Java tem suportado o recurso de converter PDF para TIFF usando compressão LZW e, em seguida, com o uso de AForge, a Binarização pode ser aplicada. No entanto, um dos clientes solicitou que, para algumas imagens, eles precisem obter o Threshold usando Otsu, então eles também gostariam de usar Bradley.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Não implementado no Aspose.PDF para Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Não implementado no Aspose.PDF para Android
        throw new NotImplementedException();
    }
```