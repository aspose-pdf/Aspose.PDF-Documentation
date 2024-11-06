---
title: Converter PDF para Diferentes Formatos de Imagem em C#
linktitle: Converter PDF para Imagens
type: docs
weight: 70
url: pt/net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: Este tópico mostra como usar o Aspose.PDF para converter PDF para vários formatos de imagem como TIFF, BMP, EMF, JPEG, PNG, GIF, SVG com poucas linhas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Visão Geral

Este artigo explica como converter PDF para diferentes formatos de imagem usando C#. Ele aborda os seguintes tópicos.

_Formato de Imagem_: **TIFF**
- [C# PDF para TIFF](#csharp-pdf-to-tiff)
- [C# Converter PDF para TIFF](#csharp-pdf-to-tiff)
- [C# Converter Páginas Únicas ou Específicas do PDF para TIFF](#csharp-pdf-to-tiff-pages)

_Formato de Imagem_: **BMP**
- [C# PDF para BMP](#csharp-pdf-to-bmp)
- [C# Converter PDF para BMP](#csharp-pdf-to-bmp)
- [C# Conversor de PDF para BMP](#csharp-pdf-to-bmp)

_Formato de Imagem_: **EMF**
- [C# PDF para EMF](#csharp-pdf-to-emf)
- [C# Converter PDF para EMF](#csharp-pdf-to-emf)
- [C# Conversor de PDF para EMF](#csharp-pdf-to-emf)
- [Conversor de PDF para EMF em C#](#csharp-pdf-to-emf)

_Formato de Imagem_: **JPG**
- [C# PDF para JPG](#csharp-pdf-to-jpg)
- [C# Converter PDF para JPG](#csharp-pdf-to-jpg)
- [Conversor de PDF para JPG em C#](#csharp-pdf-to-jpg)

_Formato de Imagem_: **PNG**
- [C# PDF para PNG](#csharp-pdf-to-png)
- [C# Converter PDF para PNG](#csharp-pdf-to-png)
- [Conversor de PDF para PNG em C#](#csharp-pdf-to-png)

_Formato de Imagem_: **GIF**
- [C# PDF para GIF](#csharp-pdf-to-gif)
- [C# Converter PDF para GIF](#csharp-pdf-to-gif)
- [Conversor de PDF para GIF em C#](#csharp-pdf-to-gif)

_Formato de Imagem_: **SVG**
- [C# PDF para SVG](#csharp-pdf-to-svg)
- [C# Converter PDF para SVG](#csharp-pdf-to-svg)
- [Conversor de PDF para SVG em C#](#csharp-pdf-to-svg)

## C# Converter PDF para Imagem

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

**Aspose.PDF para .NET** utiliza várias abordagens para converter PDF em imagem.
**Aspose.PDF para .NET** usa várias abordagens para converter PDF em imagem.

Existem várias classes na biblioteca que permitem usar um dispositivo virtual para transformar imagens. DocumentDevice é orientado para a conversão de todo o documento, mas ImageDevice - para uma página específica.

## Converter PDF usando a classe DocumentDevice

**Aspose.PDF para .NET** torna possível converter páginas de PDF em imagens TIFF.

A classe TiffDevice (baseada em DocumentDevice) permite converter páginas de PDF em imagens TIFF. Esta classe fornece um método chamado `Process` que permite converter todas as páginas de um arquivo PDF em uma única imagem TIFF.

{{% alert color="success" %}}
**Tente converter PDF para TIFF online**

Aspose.PDF para .NET apresenta a você a aplicação gratuita online ["PDF para TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), onde você pode tentar investigar a funcionalidade e qualidade com que funciona.

[![Conversão de Aspose.PDF de PDF para TIFF com Aplicativo Gratuito](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Converter Páginas de PDF para Uma Imagem TIFF

Aspose.PDF for .NET explica como converter todas as páginas de um arquivo PDF em uma única imagem TIFF:

<a name="csharp-pdf-to-tiff"><strong>Passos: Converter PDF para TIFF em C#</strong></a>

1. Crie um objeto da classe **Document**.
2. Crie objetos **TiffSettings** e **TiffDevice**
3. Chame o método **TiffDevice.Process()** para converter o documento PDF em TIFF.
4. Para definir as propriedades do arquivo de saída, use a classe **TiffSettings**.

O seguinte trecho de código mostra como converter todas as páginas do PDF em uma única imagem TIFF.

```csharp
public static void ConvertPDFtoTIFF()
{
    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Criar objeto Resolution
    Resolution resolution = new Resolution(300);

    // Criar objeto TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
        SkipBlankPages = false
    };

    // Criar dispositivo TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Converter uma página específica e salvar a imagem em stream
    tiffDevice.Process(pdfDocument, _dataDir + "AllPagesToTIFF_out.tif");
}
```
### Converter Uma Página para Imagem TIFF

Aspose.PDF para .NET permite converter uma página específica de um arquivo PDF para uma imagem TIFF, use uma versão sobrecarregada do método Process(..) que recebe um número de página como argumento para a conversão. O seguinte trecho de código mostra como converter a primeira página de um PDF para o formato TIFF.

<a name="csharp-pdf-to-tiff-pages"><strong>Passos: Converter Páginas Únicas ou Específicas de PDF para TIFF em C#</strong></a>

1. Crie um objeto da classe **Document**.
2. Crie objetos **TiffSettings** e **TiffDevice**
3. Chame o método sobrecarregado **TiffDevice.Process()** com os parâmetros **fromPage** e **toPage** para converter páginas do documento PDF para TIFF.

```csharp
public static void ConvertPDFtoTiffSinglePage()
{
    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Criar objeto Resolution
    Resolution resolution = new Resolution(300);

    // Criar objeto TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
    };

    // Criar dispositivo TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Converter uma página específica e salvar a imagem em stream
    tiffDevice.Process(pdfDocument, 1, 1, _dataDir + "PageToTIFF_out.tif");
}
```
### Use o algoritmo Bradley durante a conversão

Aspose.PDF para .NET tem suportado o recurso de converter PDF para TIF usando compressão LZW e então com o uso de AForge, Binarização pode ser aplicada. No entanto, um dos clientes solicitou que para algumas imagens, eles precisam obter o Limiar usando Otsu, então eles também gostariam de usar Bradley.

```csharp
  public static void ConvertPDFtoTiffBradleyBinarization()
{
     // Abrir documento
     Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    string outputImageFile = _dataDir + "resultant_out.tif";
    string outputBinImageFile = _dataDir + "37116-bin_out.tif";

    // Criar objeto Resolution
    Resolution resolution = new Resolution(300);
    // Criar objeto TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.LZW,
        Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
    };
    // Criar dispositivo TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
    // Converter uma página específica e salvar a imagem no stream
    tiffDevice.Process(pdfDocument, outputImageFile);

    using (FileStream inStream = new FileStream(outputImageFile, FileMode.Open))
    {
        using (FileStream outStream = new FileStream(outputBinImageFile, FileMode.Create))
        {
            tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
        }
    }
} 
```
## Converter PDF usando a classe ImageDevice

`ImageDevice` é o ancestral para `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` e `EmfDevice`.

- A classe [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) permite converter páginas de PDF em imagens <abbr title="Bitmap Image File">BMP</abbr>.
- A classe [EmfDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/emfdevice) permite converter páginas de PDF em imagens <abbr title="Enhanced Meta File">EMF</abbr>.
- A classe [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) permite converter páginas de PDF em imagens JPEG.
- A classe [PngDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/pngdevice) permite converter páginas de PDF em imagens <abbr title="Portable Network Graphics">PNG</abbr>.
- A classe [GifDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/gifdevice) permite converter páginas de PDF em imagens <abbr title="Graphics Interchange Format">GIF</abbr>.

Vamos ver como converter uma página de PDF em uma imagem.
Vamos ver como converter uma página de PDF em uma imagem.

A classe `BmpDevice` fornece um método chamado [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) que permite converter uma página específica do arquivo PDF para o formato de imagem BMP. As outras classes possuem o mesmo método. Então, se precisarmos converter uma página de PDF para uma imagem, simplesmente instanciamos a classe necessária.

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>
    
Os seguintes passos e trecho de código em C# mostram essa possibilidade
 
 - [Converter PDF para BMP em C#](#csharp-pdf-to-image)
 - [Converter PDF para EMF em C#](#csharp-pdf-to-image)
 - [Converter PDF para JPG em C#](#csharp-pdf-to-image)
 - [Converter PDF para PNG em C#](#csharp-pdf-to-image)
 - [Converter PDF para GIF em C#](#csharp-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Passos: PDF para Imagem (BMP, EMF, JPG, PNG, GIF) em C#</strong></a>

1.
1.
2. Crie uma instância de uma subclasse de **ImageDevice** i.e.
   * **BmpDevice** (para converter PDF em BMP)
   * **EmfDevice** (para converter PDF em Emf)
   * **JpegDevice** (para converter PDF em JPG)
   * **PngDevice** (para converter PDF em PNG)
   * **GifDevice** (para converter PDF em GIF)
3. Chame o método **ImageDevice.Process()** para realizar a conversão de PDF para imagem.

```csharp
public static class ExampleConvertPdfToImage
{
     private static readonly string _dataDir = @"C:\Samples\";
    // BMP, JPEG, GIF, PNG, EMF
    public static void ConvertPDFusingImageDevice()
    {
        // Crie o objeto Resolution            
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(_dataDir + 
            "ConvertAllPagesToBmp.pdf");
            
        ConvertPDFtoImage(bmpDevice, "bmp", document);
        ConvertPDFtoImage(jpegDevice,"jpeg", document);
        ConvertPDFtoImage(gifDevice, "gif", document);
        ConvertPDFtoImage(pngDevice, "png", document);
        ConvertPDFtoImage(emfDevice, "emf", document);
            
    }
}

public static void ConvertPDFtoImage(ImageDevice imageDevice, 
        string ext, Document pdfDocument)
{
    for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
    {
        using (FileStream imageStream = 
        new FileStream($"{_dataDir}image{pageCount}_out.{ext}", 
        FileMode.Create))
        {
            // Converta uma página específica e salve a imagem no stream
            imageDevice.Process(pdfDocument.Pages[pageCount], imageStream);

            // Feche o stream
            imageStream.Close();
        }
    }
}
```
{{% alert color="success" %}}
**Tente converter PDF para PNG online**

Como exemplo de como nossas aplicações gratuitas funcionam, por favor, confira o recurso a seguir.

Aspose.PDF para .NET apresenta a aplicação gratuita online ["PDF para PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), onde você pode explorar a funcionalidade e a qualidade com que ela funciona.

[![Como converter PDF para PNG usando o aplicativo gratuito](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Converter PDF usando a classe SaveOptions

Esta parte do artigo mostra como converter PDF para <abbr title="Scalable Vector Graphics">SVG</abbr> usando C# e a classe SaveOptions.

{{% alert color="success" %}}
**Tente converter PDF para SVG online**

Aspose.PDF para .NET apresenta a aplicação gratuita online ["PDF para SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), onde você pode explorar a funcionalidade e a qualidade com que ela funciona.
{{% /alert %}}

[![Conversão de PDF para SVG com o aplicativo gratuito Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
[![Conversão de PDF para SVG com Aplicativo Gratuito da Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)

**Gráficos Vetoriais Escaláveis (SVG)** é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo Consórcio World Wide Web (W3C) desde 1999.

As imagens SVG e seus comportamentos são definidos em arquivos de texto XML. Isso significa que eles podem ser pesquisados, indexados, scriptados e, se necessário, comprimidos. Como arquivos XML, as imagens SVG podem ser criadas e editadas com qualquer editor de texto, mas é frequentemente mais conveniente criá-las com programas de desenho como o Inkscape.

Aspose.PDF para .NET suporta a funcionalidade de converter imagens SVG para o formato PDF e também oferece a capacidade de converter arquivos PDF para o formato SVG.
Aspose.PDF para .NET suporta a funcionalidade de converter imagens SVG para o formato PDF e também oferece a capacidade de converter arquivos PDF para o formato SVG.

O seguinte trecho de código mostra os passos para converter um arquivo PDF para o formato SVG com .NET.

<a name="csharp-pdf-to-svg"><strong>Passos: Converter PDF para SVG em C#</strong></a>

1. Crie um objeto da classe **Document**.
2. Crie um objeto **SvgSaveOptions** com as configurações necessárias.
3. Chame o método **Document.Save()** e passe o objeto **SvgSaveOptions** para converter o documento PDF em SVG.

```csharp
public static void ConvertPDFtoSVG()
{
    // Carregar documento PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "input.pdf"));
    // Instanciar um objeto de SvgSaveOptions
    SvgSaveOptions saveOptions = new SvgSaveOptions
    {
        // Não comprimir a imagem SVG para arquivo Zip
        CompressOutputToZipArchive = false,
        TreatTargetFileNameAsDirectory = true                
    };
            
    // Salvar a saída em arquivos SVG
    document.Save(System.IO.Path.Combine(_dataDir, "PDFToSVG_out.svg"), saveOptions);
}
```

