---
title: Converter PDF para Diferentes Formatos de Imagem em C#
linktitle: Converter PDF para Imagens
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /pt/net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: Este tópico mostra como usar Aspose.PDF para converter PDF em vários formatos de imagem, como TIFF, BMP, EMF, JPEG, PNG, GIF, SVG com algumas linhas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Different Image Formats in C#",
    "alternativeHeadline": "Convert PDF Files to Multiple Image Formats in C#",
    "abstract": "O recurso em Aspose.PDF for .NET permite que os usuários convertam arquivos PDF em vários formatos de imagem, como TIFF, BMP, EMF, JPEG, PNG, GIF e SVG. Essa funcionalidade simplifica o manuseio de documentos, permitindo a conversão com apenas algumas linhas de código C#, tornando-se uma ferramenta essencial para desenvolvedores que buscam aprimorar suas aplicações com capacidades versáteis de processamento de PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2012",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/convert-pdf-to-images-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-images-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Visão Geral

Este artigo explica como converter PDF para diferentes formatos de imagem usando C#. Ele cobre os seguintes tópicos.

_Formatação de Imagem_: **TIFF**
- [C# PDF para TIFF](#csharp-pdf-to-tiff)
- [C# Converter PDF para TIFF](#csharp-pdf-to-tiff)
- [C# Converter Páginas Únicas ou Específicas de PDF para TIFF](#csharp-pdf-to-tiff-pages)

_Formatação de Imagem_: **BMP**
- [C# PDF para BMP](#csharp-pdf-to-bmp)
- [C# Converter PDF para BMP](#csharp-pdf-to-bmp)
- [C# PDF para Conversor BMP](#csharp-pdf-to-bmp)

_Formatação de Imagem_: **EMF**
- [C# PDF para EMF](#csharp-pdf-to-emf)
- [C# Converter PDF para EMF](#csharp-pdf-to-emf)
- [C# PDF para Conversor EMF](#csharp-pdf-to-emf)

_Formatação de Imagem_: **JPG**
- [C# PDF para JPG](#csharp-pdf-to-jpg)
- [C# Converter PDF para JPG](#csharp-pdf-to-jpg)
- [C# PDF para Conversor JPG](#csharp-pdf-to-jpg)

_Formatação de Imagem_: **PNG**
- [C# PDF para PNG](#csharp-pdf-to-png)
- [C# Converter PDF para PNG](#csharp-pdf-to-png)
- [C# PDF para Conversor PNG](#csharp-pdf-to-png)

_Formatação de Imagem_: **GIF**
- [C# PDF para GIF](#csharp-pdf-to-gif)
- [C# Converter PDF para GIF](#csharp-pdf-to-gif)
- [C# PDF para Conversor GIF](#csharp-pdf-to-gif)

_Formatação de Imagem_: **SVG**
- [C# PDF para SVG](#csharp-pdf-to-svg)
- [C# Converter PDF para SVG](#csharp-pdf-to-svg)
- [C# PDF para Conversor SVG](#csharp-pdf-to-svg)

## C# Converter PDF para Imagem

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

**Aspose.PDF for .NET** usa várias abordagens para converter PDF em imagem. De maneira geral, usamos duas abordagens: conversão usando a abordagem Device e conversão usando SaveOption. Esta seção mostrará como converter documentos PDF em formatos de imagem, como BMP, JPEG, GIF, PNG, EMF, TIFF e SVG usando uma dessas abordagens.

Existem várias classes na biblioteca que permitem usar um dispositivo virtual para transformar imagens. DocumentDevice é orientado para a conversão de todo o documento, mas ImageDevice - para uma página específica.

## Converter PDF usando a classe DocumentDevice

**Aspose.PDF for .NET** torna possível converter páginas PDF em imagens TIFF.

A classe TiffDevice (baseada em DocumentDevice) permite converter páginas PDF em imagens TIFF. Esta classe fornece um método chamado `Process` que permite converter todas as páginas em um arquivo PDF em uma única imagem TIFF.

{{% alert color="success" %}}
**Tente converter PDF para TIFF online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["PDF para TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF conversão PDF para TIFF com Aplicativo Gratuito](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Converter Páginas PDF em Uma Imagem TIFF

Aspose.PDF for .NET explica como converter todas as páginas em um arquivo PDF em uma única imagem TIFF:

<a name="csharp-pdf-to-tiff"><strong>Passos: Converter PDF para TIFF em C#</strong></a>

1. Crie um objeto da classe **Document**.
2. Crie objetos **TiffSettings** e **TiffDevice**.
3. Chame o método **TiffDevice.Process()** para converter o documento PDF em TIFF.
4. Para definir as propriedades do arquivo de saída, use a classe **TiffSettings**.

O seguinte trecho de código mostra como converter todas as páginas PDF em uma única imagem TIFF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTIFF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFtoTIFF.pdf"))
    {
        // Create Resolution object
        var resolution = new Aspose.Pdf.Devices.Resolution(300);

        // Create TiffSettings object
        var tiffSettings = new Aspose.Pdf.Devices.TiffSettings
        {
            Compression = Aspose.Pdf.Devices.CompressionType.None,
            Depth = Aspose.Pdf.Devices.ColorDepth.Default,
            Shape = Aspose.Pdf.Devices.ShapeType.Landscape,
            SkipBlankPages = false
        };

        // Create TIFF device
        var tiffDevice = new Aspose.Pdf.Devices.TiffDevice(resolution, tiffSettings);

        // Convert a particular page and save the image to stream
        tiffDevice.Process(document, dataDir + "PDFtoTIFF_out.tif");
    }
}
```

### Converter Uma Página em Imagem TIFF

Aspose.PDF for .NET permite converter uma página específica em um arquivo PDF em uma imagem TIFF, usando uma versão sobrecarregada do método Process(..) que aceita um número de página como argumento para conversão. O seguinte trecho de código mostra como converter a primeira página de um PDF para o formato TIFF.

<a name="csharp-pdf-to-tiff-pages"><strong>Passos: Converter Páginas Únicas ou Específicas de PDF para TIFF em C#</strong></a>

1. Crie um objeto da classe **Document**.
2. Crie objetos **TiffSettings** e **TiffDevice**.
3. Chame o método sobrecarregado **TiffDevice.Process()** com os parâmetros **fromPage** e **toPage** para converter as páginas do documento PDF em TIFF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTiffSinglePage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFtoTiffSinglePage.pdf"))
    {
        // Create Resolution object
        var resolution = new Aspose.Pdf.Devices.Resolution(300);

        // Create TiffSettings object
        var tiffSettings = new Aspose.Pdf.Devices.TiffSettings
        {
            Compression = Aspose.Pdf.Devices.CompressionType.None,
            Depth = Aspose.Pdf.Devices.ColorDepth.Default,
            Shape = Aspose.Pdf.Devices.ShapeType.Landscape,
        };

        // Create TIFF device
        var tiffDevice = new Aspose.Pdf.Devices.TiffDevice(resolution, tiffSettings);

        // Convert a particular page and save the image to stream
        tiffDevice.Process(document, 1, 1, dataDir + "PDFtoTiffSinglePage_out.tif");
    }
}
```

### Usar o algoritmo Bradley durante a conversão

Aspose.PDF for .NET tem suportado o recurso de converter PDF para TIF usando compressão LZW e, em seguida, com o uso de AForge, a Binarização pode ser aplicada. No entanto, um dos clientes solicitou que para algumas imagens, eles precisavam obter o Threshold usando Otsu, então eles também gostariam de usar Bradley.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTiffBradleyBinarization()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFtoTiffBradleyBinarization.pdf"))
    {
        string outputImageFile = dataDir + "PDFtoTiffBradleyBinarization_out.tif";
        string outputBinImageFile = dataDir + "PDFtoTiffBradleyBinarization-bin_out.tif";

        // Create Resolution object
        var resolution = new Aspose.Pdf.Devices.Resolution(300);

        // Create TiffSettings object
        var tiffSettings = new Aspose.Pdf.Devices.TiffSettings
        {
            Compression = Aspose.Pdf.Devices.CompressionType.LZW,
            Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
        };

        // Create TIFF device
        var tiffDevice = new Aspose.Pdf.Devices.TiffDevice(resolution, tiffSettings);

        // Convert a particular page and save the image to stream
        tiffDevice.Process(document, outputImageFile);

        // Binarize the image using Bradley method
        using (var inStream = new FileStream(outputImageFile, FileMode.Open))
        {
            using (var outStream = new FileStream(outputBinImageFile, FileMode.Create))
            {
                tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
            }
        }
    }
}
```

## Converter PDF usando a classe ImageDevice

`ImageDevice` é o ancestral de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` e `EmfDevice`.

- A classe [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) permite converter páginas PDF em imagens <abbr title="Bitmap Image File">BMP</abbr>.
- A classe [EmfDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/emfdevice) permite converter páginas PDF em imagens <abbr title="Enhanced Meta File">EMF</abbr>.
- A classe [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) permite converter páginas PDF em imagens JPEG.
- A classe [PngDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/pngdevice) permite converter páginas PDF em imagens <abbr title="Portable Network Graphics">PNG</abbr>.
- A classe [GifDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/gifdevice) permite converter páginas PDF em imagens <abbr title="Graphics Interchange Format">GIF</abbr>.

Vamos dar uma olhada em como converter uma página PDF em uma imagem.

A classe `BmpDevice` fornece um método chamado [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) que permite converter uma página específica do arquivo PDF em formato de imagem BMP. As outras classes têm o mesmo método. Portanto, se precisarmos converter uma página PDF em uma imagem, basta instanciar a classe necessária.

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>
    
Os seguintes passos e o trecho de código em C# mostram essa possibilidade
 
 - [Converter PDF para BMP em C#](#csharp-pdf-to-image)
 - [Converter PDF para EMF em C#](#csharp-pdf-to-image)
 - [Converter PDF para JPG em C#](#csharp-pdf-to-image)
 - [Converter PDF para PNG em C#](#csharp-pdf-to-image)
 - [Converter PDF para GIF em C#](#csharp-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Passos: PDF para Imagem (BMP, EMF, JPG, PNG, GIF) em C#</strong></a>

1. Carregue o arquivo PDF usando a classe **Document**.
2. Crie uma instância da subclasse de **ImageDevice**, ou seja,
   * **BmpDevice** (para converter PDF em BMP).
   * **EmfDevice** (para converter PDF em Emf).
   * **JpegDevice** (para converter PDF em JPG).
   * **PngDevice** (para converter PDF em PNG).
   * **GifDevice** (para converter PDF em GIF).
3. Chame o método **ImageDevice.Process()** para realizar a conversão de PDF para Imagem.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFusingImageDevice()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create Resolution object            
    var resolution = new Aspose.Pdf.Devices.Resolution(300);
    var bmpDevice = new Aspose.Pdf.Devices.BmpDevice(resolution);
    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(resolution);
    var gifDevice = new Aspose.Pdf.Devices.GifDevice(resolution);
    var pngDevice = new Aspose.Pdf.Devices.PngDevice(resolution);
    var emfDevice = new Aspose.Pdf.Devices.EmfDevice(resolution);

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertAllPagesToBmp.pdf"))
    {
        ConvertPDFtoImage(bmpDevice, "bmp", document, dataDir);
        ConvertPDFtoImage(jpegDevice, "jpeg", document, dataDir);
        ConvertPDFtoImage(gifDevice, "gif", document, dataDir);
        ConvertPDFtoImage(pngDevice, "png", document, dataDir);
        ConvertPDFtoImage(emfDevice, "emf", document, dataDir);
    }
}

private static void ConvertPDFtoImage(ImageDevice imageDevice,
        string ext, Document document, var dataDir)
{
    for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
    {
        using (FileStream imageStream =
            new FileStream($"{dataDir}image{pageCount}_out.{ext}",
            FileMode.Create))
        {
            // Convert a particular page and save the image to stream
            imageDevice.Process(document.Pages[pageCount], imageStream);
        }
    }
}
```

{{% alert color="success" %}}
**Tente converter PDF para PNG online**

Como um exemplo de como nossos aplicativos gratuitos funcionam, por favor, verifique o próximo recurso.

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["PDF para PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Como converter PDF para PNG usando Aplicativo Gratuito](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Converter PDF usando a classe SaveOptions

Esta parte do artigo mostra como converter PDF para <abbr title="Scalable Vector Graphics">SVG</abbr> usando C# e a classe SaveOptions.

{{% alert color="success" %}}
**Tente converter PDF para SVG online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["PDF para SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para SVG com Aplicativo Gratuito](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo World Wide Web Consortium (W3C) desde 1999.

Imagens SVG e seus comportamentos são definidos em arquivos de texto XML. Isso significa que podem ser pesquisados, indexados, scriptados e, se necessário, comprimidos. Como arquivos XML, imagens SVG podem ser criadas e editadas com qualquer editor de texto, mas muitas vezes é mais conveniente criá-las com programas de desenho, como o Inkscape.

Aspose.PDF for .NET suporta o recurso de converter imagens SVG para o formato PDF e também oferece a capacidade de converter arquivos PDF para o formato SVG. Para cumprir esse requisito, a classe [`SvgSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/svgsaveoptions/methods/index) foi introduzida no namespace Aspose.PDF. Instancie um objeto de SvgSaveOptions e passe-o como segundo argumento para o método [`Document.Save(..)`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

O seguinte trecho de código mostra os passos para converter um arquivo PDF para o formato SVG com .NET.

<a name="csharp-pdf-to-svg"><strong>Passos: Converter PDF para SVG em C#</strong></a>

1. Crie um objeto da classe **Document**.
2. Crie um objeto **SvgSaveOptions** com as configurações necessárias.
3. Chame o método **Document.Save()** e passe o objeto **SvgSaveOptions** para converter o documento PDF em SVG.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFtoSVG.pdf"))
    {
        // Instantiate an object of SvgSaveOptions
        var saveOptions = new Aspose.Pdf.SvgSaveOptions
        {
            // Do not compress SVG image to Zip archive
            CompressOutputToZipArchive = false,
            TreatTargetFileNameAsDirectory = true                
        };

        // Save SVG file
        document.Save(dataDir + "PDFToSVG_out.svg", saveOptions);
    }
}
```