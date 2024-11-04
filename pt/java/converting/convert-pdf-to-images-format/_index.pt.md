---
title: Converter PDF para formatos de Imagens 
linktitle: Converter PDF para Imagens
type: docs
weight: 70
url: /java/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: Este tópico mostra como o Aspose.PDF permite converter PDF para vários formatos de imagens. Converta páginas PDF para imagens PNG, JPEG, BMP com algumas linhas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF para Java** permite converter documentos PDF para formatos de imagem como BMP, JPEG, GIF, PNG, EMF, TIFF e SVG usando duas abordagens. A conversão é feita usando Device e usando SaveOption.

Existem várias classes na biblioteca que permitem usar um dispositivo virtual para transformar imagens. DocumentDevice é orientado para a conversão de todo o documento, mas ImageDevice - para uma página específica.

## Converter PDF usando a classe DocumentDevice

**Aspose.PDF para Java** torna possível converter páginas PDF em imagens TIFF.

A [classe TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) permite converter páginas PDF em imagens TIFF.
 Esta classe fornece um método chamado Process que permite converter todas as páginas de um arquivo PDF em uma única imagem TIFF.

### Converter Páginas de PDF em Uma Imagem TIFF

Aspose.PDF para Java explica como converter todas as páginas de um arquivo PDF em uma única imagem TIFF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Chame o método [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) para converter o documento.
1. Para definir as propriedades do arquivo de saída, use a classe [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings).

O trecho de código a seguir mostra como converter todas as páginas do PDF em uma única imagem TIFF.

```java
// Abrir documento
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

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

// Converter uma página específica e salvar a imagem no stream
tiffDevice.process(document, DATA_DIR + "AllPagesToTIFF_out.tif");
```

### Converter Página Única para Imagem TIFF

Aspose.PDF para Java permite converter uma página específica em um arquivo PDF para uma imagem TIFF, usando uma versão sobrecarregada do método Process(..) que leva um número de página como argumento para conversão. O trecho de código a seguir mostra como converter a primeira página de um PDF para o formato TIFF.

```java
// Abrir documento
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
String tiffFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF_out.tif").toString();
Document document = new Document(documentFileName);

// Criar objeto Resolution
Resolution resolution = new Resolution(300);

// Criar objeto TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);

// Criar dispositivo TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// Converter uma página específica e salvar a imagem no stream
tiffDevice.process(document, 1, 1, tiffFileName);
```


### Use o algoritmo Bradley durante a conversão

Aspose.PDF para Java tem suportado o recurso de converter PDF para TIFF usando compressão LZW e, em seguida, com o uso de AForge, a Binarização pode ser aplicada. No entanto, um dos clientes solicitou que, para algumas imagens, eles precisam obter o Threshold usando Otsu, então eles também gostariam de usar Bradley.

```java
// Abrir documento
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

String outputImageFileName = Paths.get(DATA_DIR.toString(), "resultant_out.tif").toString();
String outputBinImageFileName = Paths.get(DATA_DIR.toString(), "tiff-bin_out.tif").toString();

java.io.OutputStream outputImageFile = new java.io.FileOutputStream(outputImageFileName);
java.io.OutputStream outputBinImageFile = new java.io.FileOutputStream(outputBinImageFileName);

// Criar objeto Resolution
Resolution resolution = new Resolution(300);
// Criar objeto TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.LZW);
tiffSettings.setDepth(ColorDepth.Format1bpp);

// Criar dispositivo TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
// Converter uma página específica e salvar a imagem no fluxo
tiffDevice.process(document, outputImageFile);
outputImageFile.close();

// Criar objeto de fluxo para salvar a imagem de saída
java.io.InputStream inStream = new java.io.FileInputStream(outputImageFileName);
tiffDevice.binarizeBradley(inStream, outputBinImageFile, 0.1);
```


### Converter Páginas de PDF para Imagens TIFF Pixeladas

Para converter todas as páginas de um arquivo PDF para o formato TIFF Pixelado, use a opção Pixelated de IndexedConversionType

```java
// Converter Páginas de PDF para Imagens TIFF Pixeladas
// Para converter todas as páginas de um arquivo PDF para o formato TIFF Pixelado, use a
// opção Pixelated de IndexedConversionType.

// Abrir documento
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// Criar objeto de fluxo para salvar a imagem de saída
java.io.OutputStream imageStream = new java.io.FileOutputStream("Image.tiff");

// Criar objeto de Resolução
com.aspose.pdf.devices.Resolution resolution = new com.aspose.pdf.devices.Resolution(300);

// instanciar objeto TiffSettings
com.aspose.pdf.devices.TiffSettings tiffSettings = new com.aspose.pdf.devices.TiffSettings();

// definir a compressão da imagem TIFF resultante
tiffSettings.setCompression(com.aspose.pdf.devices.CompressionType.CCITT4);
// definir a profundidade de cor para a imagem resultante
tiffSettings.setDepth(com.aspose.pdf.devices.ColorDepth.Format4bpp);
// pular páginas em branco ao renderizar PDF para TIFF
tiffSettings.setSkipBlankPages(true);
// definir o brilho da imagem
tiffSettings.setBrightness(.5f);

// definir o Tipo de Conversão Indexada, o valor padrão é simples
tiffSettings.setIndexedConversionType(IndexedConversionType.Pixelated);

// Criar objeto TiffDevice com resolução particular
TiffDevice tiffDevice = new TiffDevice(2480, 3508, resolution, tiffSettings);

// Converter uma página específica (Página 1) e salvar a imagem no fluxo
tiffDevice.process(document, 1, 1, imageStream);

// Fechar o fluxo
imageStream.close();
```


{{% alert color="success" %}}
**Tente converter PDF para TIFF online**

Aspose.PDF para Java apresenta a você o aplicativo online gratuito ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF conversão PDF para TIFF com App Gratuito](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Converter PDF usando a classe ImageDevice

`ImageDevice` é o ancestral para `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` e `EmfDevice`.

- A classe [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) permite converter páginas PDF em imagens <abbr title="Arquivo de Imagem Bitmap">BMP</abbr>.
- A classe [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) permite converter páginas PDF em imagens <abbr title="Arquivo Meta Melhorado">EMF</abbr>.

- A classe [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) permite converter páginas PDF em imagens JPEG.
- A classe [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) permite converter páginas de PDF em imagens <abbr title="Portable Network Graphics">PNG</abbr>.
- A classe [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) permite converter páginas de PDF em imagens <abbr title="Graphics Interchange Format">GIF</abbr>.

Vamos dar uma olhada em como converter uma página de PDF em uma imagem.

A classe [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) fornece um método chamado [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) que permite converter uma página específica do arquivo PDF para o formato de imagem BMP. As outras classes têm o mesmo método. Portanto, se precisarmos converter uma página de PDF em uma imagem, basta instanciar a classe necessária.

O trecho de código a seguir mostra essa possibilidade:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.*;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Converter PDF para Imagem.
 */
public final class ConvertPDFtoImage {
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoImage() {

    }

    public static void run() throws IOException {
        runConvertPdfUsingImageDevice();
    }

    public static void runConvertPdfUsingImageDevice() throws IOException {
        // Criar objeto de Resolução
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(DATA_DIR + "ConvertAllPagesToBmp.pdf");

        convertPDFtoImages(bmpDevice, "bmp", document);
        convertPDFtoImages(jpegDevice, "jpeg", document);
        convertPDFtoImages(gifDevice, "gif", document);
        convertPDFtoImages(pngDevice, "png", document);
        convertPDFtoImages(emfDevice, "emf", document);
    }

    public static void convertPDFtoImages(
            ImageDevice imageDevice,
            String ext,
            Document document)
            throws IOException {
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            java.io.OutputStream imageStream = new java.io.FileOutputStream(
                    DATA_DIR + "image" + pageCount + "_out." + ext);
            // Converter uma página específica e salvar a imagem no stream
            imageDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Fechar stream
            imageStream.close();
        }
    }
}
```


{{% alert color="success" %}}
**Tente converter PDF para PNG online**

Como exemplo de como nossas aplicações gratuitas funcionam, por favor verifique o próximo recurso.

Aspose.PDF para Java apresenta a você a aplicação online gratuita ["PDF para PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Como converter PDF para PNG usando App Gratuito](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Converter PDF usando a classe SaveOptions

Esta parte do artigo mostra como converter PDF para <abbr title="Scalable Vector Graphics">SVG</abbr> usando Java e a classe SaveOptions.

{{% alert color="success" %}}
**Tente converter PDF para SVG online**

Aspose.PDF para Java apresenta a você a aplicação online gratuita ["PDF para SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão PDF para SVG do Aspose.PDF com App Gratuito](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo World Wide Web Consortium (W3C) desde 1999.

As imagens SVG e seus comportamentos são definidos em arquivos de texto XML. Isso significa que podem ser pesquisados, indexados, roteirizados e, se necessário, comprimidos. Como arquivos XML, as imagens SVG podem ser criadas e editadas com qualquer editor de texto, mas geralmente é mais conveniente criá-las com programas de desenho como o Inkscape.

### Converter páginas PDF em imagens SVG

Aspose.PDF para Java suporta a funcionalidade de converter arquivo PDF para o formato SVG.
 Para cumprir este requisito, a classe [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) foi introduzida no pacote com.aspose.pdf. Instancie um objeto de [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) e passe-o como segundo argumento para o método [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

O trecho de código a seguir mostra os passos para converter um arquivo PDF para o formato SVG.

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.SvgSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Converter PDF para SVG.
 */
public class ConvertPDFtoSVG {
    // O caminho para o diretório de documentos.
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoSVG() {

    }

    public static void run() throws IOException {
        String pdfFileName = Paths.get(DATA_DIR.toString(), "input.pdf").toString();
        String svgFileName = Paths.get(DATA_DIR.toString(), "PDFToSVG_out.svg").toString();

        // Carregar documento PDF
        Document document = new Document(pdfFileName);

        // Instanciar um objeto de SvgSaveOptions
        SvgSaveOptions saveOptions = new SvgSaveOptions();

        // Não comprimir imagem SVG para arquivo Zip
        saveOptions.setCompressOutputToZipArchive(false);

        // Salvar a saída em arquivos SVG
        document.save(svgFileName, saveOptions);
        document.close();
    }
}
```