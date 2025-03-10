---
title: Converter vários formatos de Imagens para PDF em .NET
linktitle: Converter Imagens para PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /pt/net/convert-images-format-to-pdf/
lastmod: "2021-11-01"
description: Converta vários formatos de imagens, como CDR, DJVU, BMP, CGM, JPEG, DICOM, PNG, TIFF, EMF e SVG para PDF usando C# .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert various Images formats to PDF in .NET",
    "alternativeHeadline": "Convert Multiple Image Formats to PDF with C#",
    "abstract": "Apresentando um recurso poderoso em Aspose.PDF for .NET que permite a conversão perfeita de vários formatos de imagem, incluindo BMP, CGM, DICOM, EMF, JPG, PNG, SVG, TIFF, CDR e DJVU em documentos PDF de alta qualidade. Essa funcionalidade fornece uma maneira direta de integrar conversões de imagem para PDF em suas aplicações .NET, garantindo um manuseio eficiente de diversos conteúdos gráficos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "5228",
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
    "url": "/net/convert-images-format-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-images-format-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Visão Geral

Este artigo explica como converter vários formatos de Imagens para PDF usando C#. Ele cobre os seguintes tópicos.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Formatação_: **BMP**
- [C# BMP para PDF](#csharp-bmp-to-pdf)
- [C# Converter BMP para PDF](#csharp-bmp-to-pdf)
- [C# Como converter imagem BMP para PDF](#csharp-bmp-to-pdf)

_Formatação_: **CGM**
- [C# CGM para PDF](#csharp-cgm-to-pdf)
- [C# Converter CGM para PDF](#csharp-cgm-to-pdf)
- [C# Como converter imagem CGM para PDF](#csharp-cgm-to-pdf)

_Formatação_: **DICOM**
- [C# DICOM para PDF](#csharp-dicom-to-pdf)
- [C# Converter DICOM para PDF](#csharp-dicom-to-pdf)
- [C# Como converter imagem DICOM para PDF](#csharp-dicom-to-pdf)

_Formatação_: **EMF**
- [C# EMF para PDF](#csharp-emf-to-pdf)
- [C# Converter EMF para PDF](#csharp-emf-to-pdf)
- [C# Como converter imagem EMF para PDF](#csharp-emf-to-pdf)

_Formatação_: **GIF**
- [C# GIF para PDF](#csharp-gif-to-pdf)
- [C# Converter GIF para PDF](#csharp-gif-to-pdf)
- [C# Como converter imagem GIF para PDF](#csharp-gif-to-pdf)

_Formatação_: **JPG**
- [C# JPG para PDF](#csharp-jpg-to-pdf)
- [C# Converter JPG para PDF](#csharp-jpg-to-pdf)
- [C# Como converter imagem JPG para PDF](#csharp-jpg-to-pdf)

_Formatação_: **PNG**
- [C# PNG para PDF](#csharp-png-to-pdf)
- [C# Converter PNG para PDF](#csharp-png-to-pdf)
- [C# Como converter imagem PNG para PDF](#csharp-png-to-pdf)

_Formatação_: **SVG**
- [C# SVG para PDF](#csharp-svg-to-pdf)
- [C# Converter SVG para PDF](#csharp-svg-to-pdf)
- [C# Como converter imagem SVG para PDF](#csharp-svg-to-pdf)

_Formatação_: **TIFF**
- [C# TIFF para PDF](#csharp-tiff-to-pdf)
- [C# Converter TIFF para PDF](#csharp-tiff-to-pdf)
- [C# Como converter imagem TIFF para PDF](#csharp-tiff-to-pdf)

_Formatação_: **CDR**
- [C# CDR para PDF](#csharp-cdr-to-pdf)
- [C# Converter CDR para PDF](#csharp-cdr-to-pdf)
- [C# Como converter imagem CDR para PDF](#csharp-cdr-to-pdf)

_Formatação_: **DJVU**
- [C# DJVU para PDF](#csharp-djvu-to-pdf)
- [C# Converter DJVU para PDF](#csharp-djvu-to-pdf)
- [C# Como converter imagem DJVU para PDF](#csharp-djvu-to-pdf)

Outros tópicos abordados por este artigo
- [Veja Também](#see-also)


## Conversões de Imagens para PDF em C#

**Aspose.PDF for .NET** permite que você converta diferentes formatos de imagens em arquivos PDF. Nossa biblioteca demonstra trechos de código para converter os formatos de imagem mais populares, como - BMP, CGM, DICOM, EMF, JPG, PNG, SVG e TIFF.

## Converter BMP para PDF

Converta arquivos BMP para documentos PDF usando a biblioteca **Aspose.PDF for .NET**.

<abbr title="Bitmap Image File">BMP</abbr> imagens são arquivos com extensão. BMP representa arquivos de imagem bitmap que são usados para armazenar imagens digitais bitmap. Essas imagens são independentes do adaptador gráfico e também são chamadas de formato de arquivo bitmap independente de dispositivo (DIB).
Você pode converter BMP em arquivos PDF com a API Aspose.PDF for .NET. Portanto, você pode seguir os seguintes passos para converter imagens BMP:

<a name="csharp-bmp-to-pdf" id="csharp-bmp-to-pdf"><strong>Passos: Converter BMP para PDF em C#</strong></a>

1. Inicialize um novo objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Carregue a imagem **BMP** de entrada.
3. Por fim, salve o arquivo PDF de saída.

Assim, o seguinte trecho de código segue esses passos e mostra como converter BMP para PDF usando C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertBMPtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load BMP file
        image.File = dataDir + "BMPtoPDF.bmp";
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "BMPtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Tente converter BMP para PDF online**

Aspose apresenta a você um aplicativo online gratuito ["BMP para PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão BMP para PDF usando Aplicativo Gratuito](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Converter CGM para PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> é uma extensão de arquivo para um formato de Metafile de Gráficos Computacionais comumente usado em aplicações de CAD (desenho assistido por computador) e gráficos de apresentação. CGM é um formato de gráficos vetoriais que suporta três métodos de codificação diferentes: binário (melhor para velocidade de leitura do programa), baseado em caracteres (produz o menor tamanho de arquivo e permite transferências de dados mais rápidas) ou codificação em texto claro (permite que os usuários leiam e modifiquem o arquivo com um editor de texto).

Verifique o próximo trecho de código para converter arquivos CGM para o formato PDF.

<a name="csharp-cgm-to-pdf" id="csharp-cgm-to-pdf"><strong>Passos: Converter CGM para PDF em C#</strong></a>

1. Crie uma instância da classe [CgmLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/cgmloadoptions).
2. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o nome do arquivo de origem mencionado e opções.
3. Salve o documento com o nome de arquivo desejado.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertCGMtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    var option = new Aspose.Pdf.CgmLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CGMtoPDF.cgm", option))
    {
        // Save PDF document
        document.Save(dataDir + "CGMtoPDF_out.pdf");
    }
}
```

## Converter DICOM para PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> é o padrão da indústria médica para a criação, armazenamento, transmissão e visualização de imagens médicas digitais e documentos de pacientes examinados.

**Aspose.PDF para .NET** permite que você converta imagens DICOM e SVG, mas por razões técnicas, para adicionar imagens, você precisa especificar o tipo de arquivo a ser adicionado ao PDF:

<a name="csharp-dicom-to-pdf" id="csharp-dicom-to-pdf"><strong>Passos: Converter DICOM para PDF em C#</strong></a>

1. Crie um objeto da classe Image.
2. Adicione a imagem à coleção de Parágrafos de uma página.
3. Especifique a propriedade [FileType](https://reference.aspose.com/pdf/net/aspose.pdf/image/properties/filetype).
4. Especifique o caminho ou a origem do arquivo.
    - Se uma imagem estiver em um local no disco rígido, especifique o caminho usando a propriedade Image.File.
    - Se uma imagem estiver colocada em um MemoryStream, passe o objeto que contém a imagem para a propriedade Image.ImageStream.

O seguinte trecho de código mostra como converter arquivos DICOM para o formato PDF com Aspose.PDF. Você deve carregar a imagem DICOM, colocar a imagem em uma página em um arquivo PDF e salvar a saída como PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDICOMtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        
        var image = new Aspose.Pdf.Image
        {
            FileType = ImageFileType.Dicom,
            File = dataDir + "DICOMtoPDF.dcm"
        };
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "DICOMtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Tente converter DICOM para PDF online**

Aspose apresenta a você um aplicativo online gratuito ["DICOM para PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão DICOM para PDF usando Aplicativo Gratuito](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Converter EMF para PDF

<abbr title="Enhanced metafile format">EMF</abbr> armazena imagens gráficas de forma independente do dispositivo. Metafiles de EMF consistem em registros de comprimento variável em ordem cronológica que podem renderizar a imagem armazenada após a análise em qualquer dispositivo de saída. Além disso, você pode converter EMF em imagem PDF usando os passos abaixo:

<a name="csharp-emf-to-pdf" id="csharp-emf-to-pdf"><strong>Passos: Converter EMF para PDF em C#</strong></a>

1. Primeiro, inicialize um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Carregue o arquivo de imagem **EMF**.
3. Adicione a imagem EMF carregada a uma Página.
4. Salve o documento PDF.

Além disso, o seguinte trecho de código mostra como converter um EMF para PDF com C# em seu trecho de código .NET:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertEMFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load EMF file
        image.File = dataDir + "EMFtoPDF.emf";

        // Specify page dimension properties
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Height = image.BitmapSize.Height;

        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "EMFtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Tente converter EMF para PDF online**

Aspose apresenta a você um aplicativo online gratuito ["EMF para PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão EMF para PDF usando Aplicativo Gratuito](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Converter GIF para PDF

Converta arquivos GIF para documentos PDF usando a biblioteca **Aspose.PDF for .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> é capaz de armazenar dados comprimidos sem perda de qualidade em um formato de no máximo 256 cores. O formato GIF independente de hardware foi desenvolvido em 1987 (GIF87a) pela CompuServe para transmitir imagens bitmap por meio de redes.
Você pode converter GIF em arquivos PDF com a API Aspose.PDF for .NET. Portanto, você pode seguir os seguintes passos para converter imagens GIF:

<a name="csharp-gif-to-pdf" id="csharp-gif-to-pdf"><strong>Passos: Converter GIF para PDF em C#</strong></a>

1. Inicialize um novo objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Carregue a imagem **GIF** de entrada.
3. Por fim, salve o arquivo PDF de saída.

Assim, o seguinte trecho de código segue esses passos e mostra como converter BMP para PDF usando C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertGIFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load sample GIF image file
        image.File = dataDir + "GIFtoPDF.gif";
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "GIFtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Tente converter GIF para PDF online**

Aspose apresenta a você um aplicativo online gratuito ["GIF para PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão GIF para PDF usando Aplicativo Gratuito](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Converter JPG para PDF

Não precisa se perguntar como converter JPG para PDF, porque a biblioteca **Aspose.PDF para .NET** tem a melhor solução.

Você pode converter imagens JPG em PDF com Aspose.PDF for .NET seguindo os passos:

<a name="csharp-jpg-to-pdf" id="csharp-jpg-to-pdf"><strong>Passos: Converter JPG para PDF em C#</strong></a>

1. Inicialize um objeto da classe [Document](https://reference.aspose.com/page/net/aspose.page/document).
2. Adicione uma nova Página ao documento PDF.
3. Carregue a imagem **JPG** e adicione ao parágrafo.
4. Salve o PDF de saída.

O trecho de código abaixo mostra como converter uma imagem JPG para PDF usando C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertJPGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load input JPG file
        image.File = dataDir + "JPGtoPDF.jpg";
        
        // Add image on a page
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "JPGtoPDF_out.pdf");
    }
}
```

Então você pode ver como converter uma imagem para PDF com a **mesma altura e largura da página**. Vamos obter as dimensões da imagem e, de acordo, definir as dimensões da página do documento PDF com os passos abaixo:

1. Carregue o arquivo de imagem de entrada.
1. Defina a altura, largura e margens de uma página.
1. Salve o arquivo PDF de saída.

O seguinte trecho de código mostra como converter uma Imagem para PDF com a mesma altura e largura da página usando C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertJPGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load JPEG file
        image.File = dataDir + "JPGtoPDF.jpg";
        
        // Read Height of input image
        page.PageInfo.Height = image.BitmapSize.Height;
        // Read Width of input image
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Left = 0;
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "JPGtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Tente converter JPG para PDF online**

Aspose apresenta a você um aplicativo online gratuito ["JPG para PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão JPG para PDF usando Aplicativo Gratuito](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Converter PNG para PDF

**Aspose.PDF for .NET** suporta a funcionalidade de converter imagens PNG para o formato PDF. Verifique o próximo trecho de código para realizar sua tarefa.

<abbr title="Portable Network Graphics">PNG</abbr> refere-se a um tipo de formato de arquivo de imagem raster que usa compressão sem perdas, o que o torna popular entre seus usuários.

Você pode converter PNG em imagem PDF usando os passos abaixo:

<a name="csharp-png-to-pdf" id="csharp-png-to-pdf"><strong>Passos: Converter PNG para PDF em C#</strong></a>

1. Carregue a imagem **PNG** de entrada.
2. Leia os valores de altura e largura.
3. Crie um novo objeto [Document](https://reference.aspose.com/page/net/aspose.page/document) e adicione uma Página.
4. Defina as dimensões da página.
5. Salve o arquivo de saída.

Além disso, o trecho de código abaixo mostra como converter PNG para PDF com C# em suas aplicações .NET:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPNGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load PNG file
        image.File = dataDir + "PNGtoPDF.png";
        
        // Read Height of input image
        page.PageInfo.Height = image.BitmapSize.Height;
        // Read Width of input image
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Left = 0;
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "PNGtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Tente converter PNG para PDF online**

Aspose apresenta a você um aplicativo online gratuito ["PNG para PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PNG para PDF usando Aplicativo Gratuito](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Converter SVG para PDF

**Aspose.PDF for .NET** explica como converter imagens SVG para o formato PDF e como obter as dimensões do arquivo <abbr title="Scalable Vector Graphics">SVG</abbr> de origem.

Gráficos Vetoriais Escaláveis (SVG) são uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo World Wide Web Consortium (W3C) desde 1999.

Imagens SVG e seus comportamentos são definidos em arquivos de texto XML. Isso significa que podem ser pesquisados, indexados, scriptados e, se necessário, comprimidos. Como arquivos XML, as imagens SVG podem ser criadas e editadas com qualquer editor de texto, mas muitas vezes é mais conveniente criá-las com programas de desenho, como o Inkscape.

{{% alert color="success" %}}
**Tente converter o formato SVG para PDF online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["SVG para PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão SVG para PDF com Aplicativo Gratuito](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

Para converter arquivos SVG para PDF, use a classe chamada [SvgLoadOptions](https://reference.aspose.com/net/pdf/aspose.pdf/svgloadoptions) que é usada para inicializar o objeto [`LoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions). Posteriormente, esse objeto é passado como um argumento durante a inicialização do objeto Document e ajuda o mecanismo de renderização PDF a determinar o formato de entrada do documento de origem.

<a name="csharp-svg-to-pdf" id="csharp-svg-to-pdf"><strong>Passos: Converter SVG para PDF em C#</strong></a>

1. Crie uma instância da classe [`SvgLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions).
2. Crie uma instância da classe [`Document`](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o nome do arquivo de origem mencionado e opções.
3. Salve o documento com o nome de arquivo desejado.

O seguinte trecho de código mostra o processo de conversão de um arquivo SVG para o formato PDF com Aspose.PDF for .NET.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertSVGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    var option = new Aspose.Pdf.SvgLoadOptions();
    // Open SVG file 
    using (var document = new Aspose.Pdf.Document(dataDir + "SVGtoPDF.svg", option))
    {
        // Save PDF document
        document.Save(dataDir + "SVGtoPDF_out.pdf");
    }
}
```

## Obter dimensões SVG

Também é possível obter as dimensões do arquivo SVG de origem. Essa informação pode ser útil se quisermos que o SVG cubra toda a página do PDF de saída. A propriedade AdjustPageSize da classe SvgLoadOption atende a esse requisito. O valor padrão dessa propriedade é falso. Se o valor for definido como verdadeiro, o PDF de saída terá o mesmo tamanho (dimensões) que o SVG de origem.

O seguinte trecho de código mostra o processo de obtenção das dimensões do arquivo SVG de origem e geração de um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertSVGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    var loadopt = new Aspose.Pdf.SvgLoadOptions();
    loadopt.AdjustPageSize = true;
    // Open SVG file
    using (var document = new Aspose.Pdf.Document(dataDir + "SVGtoPDF.svg", loadopt))
    {
        document.Pages[1].PageInfo.Margin.Top = 0;
        document.Pages[1].PageInfo.Margin.Left = 0;
        document.Pages[1].PageInfo.Margin.Bottom = 0;
        document.Pages[1].PageInfo.Margin.Right = 0;

        // Save PDF document
        document.Save(dataDir + "SVGtoPDF_out.pdf");
    }
    
}
```

### Recursos Suportados pelo SVG

<table>
    <thead>
        <tr>
            <th>
                <p>Tag SVG</p>
            </th>
            <th>
                <p>Uso de Exemplo</p>
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <p>circle</p>
            </td>
            <td>
                <code><pre>&lt circle id="r2" cx="10" cy="10" r="10" stroke="blue" stroke-width="2"&gt </pre></code>
            </td>
        </tr>
        <tr>
            <td>
                <p>defs</p>
            </td>
            <td>
                <code>&lt;defs&gt;&nbsp; <br> &lt;rect id="r1" width="15" height="15"
                    stroke="blue" stroke-width="2" /&gt;&nbsp; <br> &lt;circle id="r2"
                    cx="10" cy="10" r="10" stroke="blue" stroke-width="2"/&gt;&nbsp; <br>
                    &lt;circle id="r3" cx="10" cy="10" r="10" stroke="blue" stroke-width="3"/&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br> &lt;use
                    x="25" y="40" xlink:href="#r1" fill="red"/&gt;&nbsp; <br> &lt;use
                    x="35" y="15" xlink:href="#r2" fill="green"/&gt;&nbsp; <br> &lt;use
                    x="58" y="50" xlink:href="#r3" fill="blue"/&gt;</code>
            </td>
        </tr>
        <tr>
            <td>
                <p>tref</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text
                    id="ReferencedText"&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    Dados de caracteres referenciados&nbsp; <br> &nbsp;&nbsp;&nbsp;
                    &lt;/text&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br
                        class="atl-forced-newline"> &nbsp;&nbsp;&nbsp; &lt;tref
                    xlink:href="#ReferencedText"/&gt;&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>use</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text id="Text" x="400"
                    y="200"&nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
                    text-anchor="middle" &gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    Texto mascarado&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;/text&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;use xlink:href="#Text" fill="blue"&nbsp; /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ellipse&nbsp;</p>
            </td>
            <td>
                <p>&lt;ellipse cx="2.5" cy="1.5" rx="2" ry="1" fill="red" /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>g&nbsp;</p>
            </td>
            <td>
                <p>&lt;g fill="none" stroke="dimgray" stroke-width="1.5" &gt;&nbsp; <br>
                    &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7"
                    y1="-7" x2="-3" y2="-3"/&gt;&nbsp; <br> &nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="7" x2="3"
                    y2="3"/&gt;&nbsp; <br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7" y1="7" x2="-3" y2="3"/&gt;&nbsp;
                    <br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="-7" x2="3" y2="-3"/&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;/g&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>image</p>
            </td>
            <td>
                <p>&lt;image id="ShadedRelief" x="24" y="4" width="64" height="82" xlink:href="relief.jpg"
                    /&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>line</p>
            </td>
            <td>
                <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>path</p>
            </td>
            <td>
                <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
                    "/&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>style</p>
            </td>
            <td>
                <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
                    "/&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>polygon</p>
            </td>
            <td>
                <p>&lt;polygon style="stroke:#24a;stroke-width:1.5;fill:#eefefe" points="10,10 180,10 10,250 10,10"
                    /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>polyline</p>
            </td>
            <td>
                <p>&lt;polyline fill="none" stroke="dimgray" stroke-width="1" points="-3,-6 3,-6 3,1 5,1 0,7 -5,1
                    -3,1 -3,-5"/&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>rect&nbsp;</p>
            </td>
            <td>
                <p>&lt;rect x="0" y="0" width="400" height="600" stroke="none" fill="aliceblue" /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>svg</p>
            </td>
            <td>
                <p>&lt;svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="10cm" height="5cm" &gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>text</p>
            </td>
            <td>
                <p>&lt;text font-family="sans-serif" fill="dimgray" font-size="22px" font-weight="bold" x="58"
                    y="30" pointer-events="none"&gt;Título do Mapa&lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>font</p>
            </td>
            <td>
                <p>&lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br>
                    &nbsp;&nbsp;&nbsp; Texto de exemplo&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>tspan</p>
            </td>
            <td>
                <p>&lt;tspan dy="25" x="25"&gt;seis valores de entrada de cor de tinta. Aqui estará &lt;/tspan&gt;</p>
            </td>
        </tr>
    </tbody>
</table>

## Converter TIFF para PDF

O formato de arquivo **Aspose.PDF** suportado, seja uma imagem <abbr title="Tag Image File Format">TIFF</abbr> de um único quadro ou multi-quadro. Isso significa que você pode converter a imagem TIFF para PDF em suas aplicações .NET.

TIFF ou TIF, Formato de Arquivo de Imagem Marcada, representa imagens raster que são destinadas ao uso em uma variedade de dispositivos que cumprem este padrão de formato de arquivo. A imagem TIFF pode conter vários quadros com imagens diferentes. O formato de arquivo Aspose.PDF também é suportado, seja uma imagem TIFF de um único quadro ou multi-quadro.

Você pode converter TIFF para PDF da mesma maneira que os outros formatos de arquivo raster gráficos:

<a name="csharp-tiff-to-pdf" id="csharp-tiff-to-pdf"><strong>Passos: Converter TIFF para PDF em C#</strong></a>

1. Crie um novo objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) e adicione uma Página.
2. Carregue a imagem **TIFF** de entrada.
3. Salve o documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTIFFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load sample Tiff image file
        image.File = dataDir + "TIFFtoPDF.tiff";
        document.Pages[1].Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "TIFFtoPDF_out.pdf");
    }
}
```

Caso você precise converter uma imagem TIFF de várias páginas para um documento PDF de várias páginas e controlar alguns parâmetros, por exemplo, largura ou proporção, siga estes passos:

1. Instancie uma instância da classe Document.
1. Carregue a imagem TIFF de entrada.
1. Obtenha a FrameDimension dos quadros.
1. Adicione uma nova página para cada quadro.
1. Por fim, salve as imagens nas páginas PDF.

O seguinte trecho de código mostra como converter uma imagem TIFF de várias páginas ou multi-quadro para PDF com C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTIFFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        using (var bitmap = new System.Drawing.Bitmap(File.OpenRead(dataDir + "TIFFtoPDF.tif")))
        {
            // Convert multi page or multi frame TIFF to PDF
            var dimension = new FrameDimension(bitmap.FrameDimensionsList[0]);
            var frameCount = bitmap.GetFrameCount(dimension);

            // Iterate through each frame
            for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
            {
                var page = document.Pages.Add();

                bitmap.SelectActiveFrame(dimension, frameIdx);

                using (var currentImage = new MemoryStream())
                {
                    bitmap.Save(currentImage, ImageFormat.Tiff);

                    var imageht = new Aspose.Pdf.Image
                    {
                        ImageStream = currentImage,
                        //Apply some other options
                        //ImageScale = 0.5
                    };
                    page.Paragraphs.Add(imageht);
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TIFFtoPDF_out.pdf");
    }
}
```

## Converter CDR para PDF

<abbr title="CDR">CDR</abbr> é um formato de arquivo que foi desenvolvido pela Corel Corporation e é usado principalmente para imagens gráficas vetoriais e desenhos. O formato de arquivo CDR é reconhecido pela maioria dos programas de edição de imagem. O formato CDR é o formato padrão para Aplicativos Corel Draw.

Verifique o próximo trecho de código para converter arquivos CDR para o formato PDF.

<a name="csharp-cdr-to-pdf" id="csharp-cdr-to-pdf"><strong>Passos: Converter CDR para PDF em C#</strong></a>

1. Crie uma instância da classe [CdrLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/cdrloadoptions/) .
2. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o nome do arquivo de origem mencionado e opções.
3. Salve o documento com o nome de arquivo desejado.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertCDRtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open CDR file
    using (var document = new Aspose.Pdf.Document(dataDir + "CDRtoPDF.cdr", new CdrLoadOptions()))
    {
        // Save PDF document
        document.Save(dataDir + "CDRtoPDF_out.pdf");
    }
}
```

## Converter DJVU para PDF

<abbr title="DJVU">DjVu</abbr> é um formato de imagem comprimido que foi desenvolvido pela LizardTech. Este formato de arquivo foi projetado principalmente para armazenar diferentes tipos de documentos digitalizados; especialmente documentos que contêm uma combinação de texto, imagens, imagens coloridas indexadas e desenhos lineares.

Verifique o próximo trecho de código para converter arquivos DJVU para o formato PDF.

<a name="csharp-djvu-to-pdf" id="csharp-djvu-to-pdf"><strong>Passos: Converter DJVU para PDF em C#</strong></a>

1. Crie uma instância da classe [DjvuLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/djvuloadoptions/) .
2. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o nome do arquivo de origem mencionado e opções.
3. Salve o documento com o nome de arquivo desejado.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDJVUtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    
    // Open DJVU file
    using (var document = new Aspose.Pdf.Document(dataDir + "CDRtoPDF.djvu", new DjvuLoadOptions()))
    {
        // Save PDF document
        document.Save(dataDir + "CDRtoPDF_out.pdf");
    }
}
```

## Converter HEIC para PDF

Um arquivo HEIC é um formato de arquivo de Imagem de Contêiner de Alta Eficiência que pode armazenar várias imagens como uma coleção em um único arquivo.
Para carregar imagens heic, você precisa adicionar uma referência ao pacote nuget https://www.nuget.org/packages/FileFormat.Heic/.
Converta imagens HEIC para PDF usando Aspose.PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHEICtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open HEIC file
    using (var fs = new FileStream(dataDir + "HEICtoPDF.heic", FileMode.Open))
    {
        var image = FileFormat.Heic.Decoder.HeicImage.Load(fs);
        var pixels = image.GetByteArray(PixelFormat.Rgb24);
        var width = (int)image.Width;
        var height = (int)image.Height;

        using (var document = new Aspose.Pdf.Document())
        {
            var page = document.Pages.Add();
            var asposeImage = new Aspose.Pdf.Image();
            asposeImage.BitmapInfo = new Aspose.Pdf.BitmapInfo(pixels, width, height, Aspose.Pdf.BitmapInfo.PixelFormat.Rgb24);
            page.PageInfo.Height = height;
            page.PageInfo.Width = width;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Left = 0;

            page.Paragraphs.Add(asposeImage);

            // Save PDF document
            document.Save(dataDir + "HEICtoPDF_out.pdf");
        }
    }
}
```

## Aplica-se a

|**Plataforma**|**Suportado**|**Comentários**|
| :- | :- |:- |
|Windows .NET Framework|2.0-4.6| |
|Windows .NET Core |2.0-3.1| |
|.NET 5 Windows| |
|Linux .NET Core|2.0-3.1 | |
|.NET 5 Linux | |

## Veja Também

Este artigo também cobre estes tópicos. Os códigos são os mesmos que acima.

_Formatação_: **BMP**
- [C# Código BMP para PDF](#csharp-bmp-to-pdf)
- [C# API BMP para PDF](#csharp-bmp-to-pdf)
- [C# BMP para PDF Programaticamente](#csharp-bmp-to-pdf)
- [C# Biblioteca BMP para PDF](#csharp-bmp-to-pdf)
- [C# Salvar BMP como PDF](#csharp-bmp-to-pdf)
- [C# Gerar PDF a partir de BMP](#csharp-bmp-to-pdf)
- [C# Criar PDF a partir de BMP](#csharp-bmp-to-pdf)
- [C# Conversor BMP para PDF](#csharp-bmp-to-pdf)

_Formatação_: **CGM**
- [C# Código CGM para PDF](#csharp-cgm-to-pdf)
- [C# API CGM para PDF](#csharp-cgm-to-pdf)
- [C# CGM para PDF Programaticamente](#csharp-cgm-to-pdf)
- [C# Biblioteca CGM para PDF](#csharp-cgm-to-pdf)
- [C# Salvar CGM como PDF](#csharp-cgm-to-pdf)
- [C# Gerar PDF a partir de CGM](#csharp-cgm-to-pdf)
- [C# Criar PDF a partir de CGM](#csharp-cgm-to-pdf)
- [C# Conversor CGM para PDF](#csharp-cgm-to-pdf)

_Formatação_: **DICOM**
- [C# Código DICOM para PDF](#csharp-dicom-to-pdf)
- [C# API DICOM para PDF](#csharp-dicom-to-pdf)
- [C# DICOM para PDF Programaticamente](#csharp-dicom-to-pdf)
- [C# Biblioteca DICOM para PDF](#csharp-dicom-to-pdf)
- [C# Salvar DICOM como PDF](#csharp-dicom-to-pdf)
- [C# Gerar PDF a partir de DICOM](#csharp-dicom-to-pdf)
- [C# Criar PDF a partir de DICOM](#csharp-dicom-to-pdf)
- [C# Conversor DICOM para PDF](#csharp-dicom-to-pdf)

_Formatação_: **EMF**
- [C# Código EMF para PDF](#csharp-emf-to-pdf)
- [C# API EMF para PDF](#csharp-emf-to-pdf)
- [C# EMF para PDF Programaticamente](#csharp-emf-to-pdf)
- [C# Biblioteca EMF para PDF](#csharp-emf-to-pdf)
- [C# Salvar EMF como PDF](#csharp-emf-to-pdf)
- [C# Gerar PDF a partir de EMF](#csharp-emf-to-pdf)
- [C# Criar PDF a partir de EMF](#csharp-emf-to-pdf)
- [C# Conversor EMF para PDF](#csharp-emf-to-pdf)

_Formatação_: **DjVu**
- [C# Código DjVu para PDF](#csharp-djvu-to-pdf)
- [C# API DjVu para PDF](#csharp-djvu-to-pdf)
- [C# DjVu para PDF Programaticamente](#csharp-djvu-to-pdf)
- [C# Biblioteca DjVu para PDF](#csharp-djvu-to-pdf)
- [C# Salvar DjVu como PDF](#csharp-djvu-to-pdf)
- [C# Gerar PDF a partir de DjVu](#csharp-djvu-to-pdf)
- [C# Criar PDF a partir de DjVu](#csharp-djvu-to-pdf)
- [C# Conversor DjVu para PDF](#csharp-djvu-to-pdf)

_Formatação_: **CDR**
- [C# Código CDR para PDF](#csharp-cdr-to-pdf)
- [C# API CDR para PDF](#csharp-cdr-to-pdf)
- [C# CDR para PDF Programaticamente](#csharp-cdr-to-pdf)
- [C# Biblioteca CDR para PDF](#csharp-cdr-to-pdf)
- [C# Salvar CDR como PDF](#csharp-cdr-to-pdf)
- [C# Gerar PDF a partir de CDR](#csharp-cdr-to-pdf)
- [C# Criar PDF a partir de CDR](#csharp-cdr-to-pdf)
- [C# Conversor CDR para PDF](#csharp-cdr-to-pdf)