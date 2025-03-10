---
title: Converter PDF para HTML em .NET
linktitle: Converter PDF para formato HTML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /pt/net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Este tópico mostra como converter um arquivo PDF para o formato HTML com a biblioteca Aspose.PDF C#.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to HTML in .NET",
    "alternativeHeadline": "Convert PDF Files to HTML with Simplified Options in C#",
    "abstract": "Apresentando um novo recurso poderoso em Aspose.PDF for .NET que permite a conversão perfeita de documentos PDF para o formato HTML. Essa funcionalidade suporta saída de várias páginas, gerenciamento de imagens SVG e opções para renderização de texto transparente, permitindo que os desenvolvedores transformem facilmente PDFs em conteúdo pronto para a web com apenas algumas linhas de código C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1368",
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
    "url": "/net/convert-pdf-to-html/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-html/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Visão Geral

Este artigo explica como **converter PDF para HTML usando C#**. Ele cobre os seguintes tópicos.

_Formatação_: **HTML**
- [C# PDF para HTML](#csharp-pdf-to-html)
- [C# Converter PDF para HTML](#csharp-pdf-to-html)
- [C# Como converter arquivo PDF para HTML](#csharp-pdf-to-html)

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Converter PDF para HTML

**Aspose.PDF for .NET** oferece muitos recursos para converter vários formatos de arquivo em documentos PDF e converter arquivos PDF em vários formatos de saída. Este artigo discute como converter um arquivo PDF em <abbr title="HyperText Markup Language">HTML</abbr>. Aspose.PDF for .NET fornece a capacidade de converter arquivos HTML em formato PDF usando a abordagem InLineHtml. Recebemos muitos pedidos por uma funcionalidade que converte um arquivo PDF em formato HTML e fornecemos esse recurso. Observe que esse recurso também suporta XHTML 1.0.

**Aspose.PDF for .NET** suporta os recursos para converter um arquivo PDF em HTML. As principais tarefas que você pode realizar com a biblioteca Aspose.PDF estão listadas:

- Converter PDF para HTML.
- Dividir a saída em HTML de várias páginas.
- Especificar a pasta para armazenar arquivos SVG.
- Compactar imagens SVG durante a conversão.
- Salvar imagens como fundo PNG.
- Especificar a pasta de imagens.
- Criar arquivos subsequentes apenas com conteúdos do corpo.
- Renderização de texto transparente.
- Renderização de camadas de documentos PDF.

{{% alert color="success" %}}
**Tente converter PDF para HTML online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["PDF para HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para HTML com Aplicativo Gratuito](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF for .NET fornece um código de duas linhas para transformar um arquivo PDF de origem em HTML. A [`enumeração SaveFormat`](https://reference.aspose.com/pdf/net/aspose.pdf/saveformat) contém o valor Html que permite salvar o arquivo de origem em HTML. O seguinte trecho de código mostra o processo de conversão de um arquivo PDF em HTML.

<a name="csharp-pdf-to-html"><strong>Passos: Converter PDF para HTML em C#</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) com o documento PDF de origem.
2. Salve-o no formato **SaveFormat.Html** chamando o método **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Save the output HTML
        document.Save(dataDir + "output_out.html", Aspose.Pdf.SaveFormat.Html);
    }
}
```

### Dividir a saída em HTML de várias páginas

Ao converter um arquivo PDF grande com várias páginas para o formato HTML, a saída aparece como uma única página HTML. Isso pode acabar sendo muito longo. Para controlar o tamanho da página, é possível dividir a saída em várias páginas durante a conversão de PDF para HTML. Tente usar o seguinte trecho de código.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoMultiPageHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "MultiPageHTML_out.html", htmlOptions);
    }
}
```

### Especificar a pasta para armazenar arquivos SVG

Durante a conversão de PDF para HTML, é possível especificar a pasta onde as imagens SVG devem ser salvas. Use a [`classe HtmlSaveOption`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlsaveoptions) [`propriedade SpecialFolderForSvgImages`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlsaveoptions/fields/specialfolderforsvgimages) para especificar um diretório especial para imagens SVG. Esta propriedade obtém ou define o caminho para o diretório onde as imagens SVG devem ser salvas quando encontradas durante a conversão. Se o parâmetro estiver vazio ou nulo, então quaisquer arquivos SVG são salvos junto com outros arquivos de imagem.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML save options object
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the folder where SVG images are saved during PDF to HTML conversion
            SpecialFolderForSvgImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
    }
}
```

### Compactar imagens SVG durante a conversão

Para compactar imagens SVG durante a conversão de PDF para HTML, tente usar o seguinte código:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoCompressedHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Compress the SVG images if there are any
            CompressSvgGraphicsIfAny = true
        };

        // Save the output HTML
        document.Save(dataDir + "CompressedSVGHTML_out.html", newOptions);
    }
}
```

### Salvar imagens como fundo PNG

O formato de saída padrão para salvar imagens é SVG. Durante a conversão, algumas imagens do PDF são transformadas em imagens vetoriais SVG. Isso pode ser lento. Em vez disso, as imagens podem ser transformadas em um arquivo de fundo PNG para cada página.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToHtmlSaveImagesAsPngBackground()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion_PDFToHTMLFormat();
           
    // Create HtmlSaveOption with tested feature
    var htmlSaveOptions = new HtmlSaveOptions();
           
    // Option to save images in PNG format as background for each page.
    htmlSaveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;

    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
       document.Save(dataDir + "imagesAsPngBackground_out.html", htmlSaveOptions);         
    }
}
```

### Especificar a pasta de imagens

Também podemos especificar a pasta onde as imagens serão salvas durante a conversão de PDF para HTML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSeparateImageFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the separate folder to save images
            SpecialFolderForAllImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "HTMLWithSeparateImageFolder_out.html", newOptions);
    }
}
```

### Criar arquivos subsequentes apenas com conteúdos do corpo

Recentemente, fomos solicitados a introduzir um recurso onde arquivos PDF são convertidos em HTML e o usuário pode obter apenas o conteúdo da tag `<body>` para cada página. Isso produziria um arquivo com detalhes de CSS, `<html>`, `<head>` e todas as páginas em outros arquivos apenas com conteúdos de `<body>`.

Para atender a essa necessidade, uma nova propriedade, HtmlMarkupGenerationMode, foi introduzida na classe HtmlSaveOptions.

Com o seguinte trecho de código simples, você pode dividir a saída HTML em páginas. Nas páginas de saída, todos os objetos HTML devem ir exatamente para onde vão agora (processamento e saída de fontes, criação e saída de CSS, criação e saída de imagens), exceto que o HTML de saída conterá conteúdos atualmente colocados dentro das tags (agora as tags “body” serão omitidas). No entanto, ao usar essa abordagem, o link para o CSS é responsabilidade do seu código, pois coisas como serão removidas. Para esse propósito, você pode ler o CSS via File.ReadAllText() e enviá-lo via AJAX para uma página da web onde será aplicado pelo jQuery.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithBodyContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // Set HtmlMarkupGenerationMode to generate only body content
            HtmlMarkupGenerationMode =
                Aspose.Pdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent,

            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "CreateSubsequentFiles_out.html", options);
    }
}
```

### Renderização de texto transparente

Caso o arquivo PDF de origem/entrada contenha textos transparentes sombreado por imagens de primeiro plano, pode haver problemas de renderização de texto. Portanto, para atender a tais cenários, as propriedades SaveShadowedTextsAsTransparentTexts e SaveTransparentTexts podem ser usadas.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithTransparentTextRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable transparent text rendering
            SaveShadowedTextsAsTransparentTexts = true,
            SaveTransparentTexts = true
        };

        // Save the output HTML
        document.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
    }
}
```

### Renderização de camadas de documentos PDF

Podemos renderizar camadas de documentos PDF em um elemento de tipo de camada separado durante a conversão de PDF para HTML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithLayersRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable rendering of PDF document layers separately in the output HTML
            ConvertMarkedContentToLayers = true
        };

        // Save the output HTML
        document.Save(dataDir + "LayersRendering_out.html", htmlOptions);
    }
}
```

## Veja Também 

Este artigo também cobre estes tópicos. Os códigos são os mesmos que acima.

_Formatação_: **HTML**
- [C# PDF para HTML Código](#csharp-pdf-to-html)
- [C# PDF para HTML API](#csharp-pdf-to-html)
- [C# PDF para HTML Programaticamente](#csharp-pdf-to-html)
- [C# PDF para HTML Biblioteca](#csharp-pdf-to-html)
- [C# Salvar PDF como HTML](#csharp-pdf-to-html)
- [C# Gerar HTML a partir de PDF](#csharp-pdf-to-html)
- [C# Criar HTML a partir de PDF](#csharp-pdf-to-html)
- [C# PDF para HTML Conversor](#csharp-pdf-to-html)