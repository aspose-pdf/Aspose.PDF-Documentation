---
title: Converter HTML para PDF em .NET
linktitle: Converter arquivo HTML para PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /pt/net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: Este tópico mostra como converter HTML para PDF e MHTML para PDF usando Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert HTML to PDF in .NET",
    "alternativeHeadline": "Convert HTML and MHTML to PDF with C#",
    "abstract": "O recurso de conversão em Aspose.PDF for .NET permite a transformação contínua de documentos HTML e MHTML em arquivos PDF de alta qualidade. Com opções de personalização avançadas, os usuários podem controlar a incorporação de fontes, consultas de mídia e gerenciamento de recursos externos, garantindo que páginas da web ou arquivos HTML locais sejam renderizados com precisão no formato PDF com flexibilidade adaptada às suas necessidades específicas.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1889",
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
    "url": "/net/convert-html-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-html-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Visão Geral 

Este artigo explica como **converter HTML para PDF usando C#**. Ele cobre os seguintes tópicos.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Formatação_: **HTML**
- [C# HTML para PDF](#csharp-html-to-pdf)
- [C# Converter HTML para PDF](#csharp-html-to-pdf)
- [C# Como converter HTML para PDF](#csharp-html-to-pdf)

_Formatação_: **MHTML**
- [C# MHTML para PDF](#csharp-mhtml-to-pdf)
- [C# Converter MHTML para PDF](#csharp-mhtml-to-pdf)
- [C# Como converter MHTML para PDF](#csharp-mhtml-to-pdf)

_Formatação_: **WebPage**
- [C# WebPage para PDF](#csharp-webpage-to-pdf)
- [C# Converter WebPage para PDF](#csharp-webpage-to-pdf)
- [C# Como converter WebPage para PDF](#csharp-webpage-to-pdf)

## Conversão de C# HTML para PDF

**Aspose.PDF for .NET** é uma API de manipulação de PDF que permite converter qualquer documento HTML existente para PDF de forma contínua. O processo de conversão de HTML para PDF pode ser personalizado de forma flexível.

## Converter HTML para PDF

O seguinte exemplo de código C# mostra como converter um documento HTML para um PDF.

<a name="csharp-html-to-pdf"><strong>Passos: Converter HTML para PDF em C#</strong></a>

1. Crie uma instância da classe [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/).
2. Inicialize o objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Salve o documento PDF de saída chamando o método **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions();

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Tente converter HTML para PDF online**

A Aspose apresenta a você um aplicativo online gratuito ["HTML para PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão HTML para PDF usando Aplicativo Gratuito](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Conversão avançada de HTML para PDF

O mecanismo de conversão HTML possui várias opções que nos permitem controlar o processo de conversão.

### Suporte a Consultas de Mídia

Consultas de mídia são uma técnica popular para fornecer uma folha de estilo personalizada para diferentes dispositivos. Podemos definir o tipo de dispositivo usando a propriedade [`HtmlMediaType`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvancedMediaType()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions with Print media type
    var options = new HtmlLoadOptions
    {
        // Set Print or Screen mode
        HtmlMediaType = Aspose.Pdf.HtmlMediaType.Print
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDFAdvancedMediaType_out.pdf");
    }
}
```

### Habilitar (desabilitar) incorporação de fontes

Páginas HTML frequentemente usam fontes (por exemplo, fontes da pasta local, Google Fonts, etc). Também podemos controlar a incorporação de fontes em um documento usando a propriedade [`IsEmbedFonts`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/isembedfonts).

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedEmbedFonts()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Load the HTML file into a document using HtmlLoadOptions with the font embedding option set
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Disable font embedding
         IsEmbedFonts = false
     };

     // Open HTML document
     using (var document = new Aspose.Pdf.Document(dataDir + "test_fonts.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "ConvertHTMLtoPDFAdvanced_EmbedFonts_out.pdf");
     }
 }
```

### Gerenciar o carregamento de recursos externos

O mecanismo de conversão fornece um mecanismo que permite controlar o carregamento de certos recursos associados ao documento HTML. A classe [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) possui a propriedade [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) com a qual podemos definir o comportamento do carregador de recursos. Suponha que precisamos substituir todas as imagens PNG por uma única imagem `test.jpg` e substituir a URL externa por interna para outros recursos. Para fazer isso, podemos definir um carregador personalizado `SamePictureLoader` e apontar [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) para esse nome.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document with a custom resource loader for external images
    var options = new Aspose.Pdf.HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Aspose.Pdf.LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    Aspose.Pdf.LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(dataDir + "test.jpg");
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(resultBytes)
        {
            // Set MIME Type
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new System.Net.Http.HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```

## Converter página da Web para PDF

Converter uma página da web é ligeiramente diferente de converter um documento HTML local. Para converter o conteúdo da página da Web para o formato PDF, podemos primeiro buscar o conteúdo da página HTML usando uma instância HttpClient, criar um objeto Stream, passar o conteúdo para o objeto Document e renderizar a saída no formato PDF.

Ao converter uma página da web hospedada em um servidor web para PDF:

<a name="csharp-webpage-to-pdf"><strong>Passos: Converter WebPage para PDF em C#</strong></a>

1. Leia o conteúdo da página usando um objeto HttpClient.
1. Instancie o objeto [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) e defina a URL base.
1. Inicialize um objeto Document passando o objeto stream.
1. Opcionalmente, defina o tamanho da página e/ou orientação.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    const string url = "https://en.wikipedia.org/wiki/Aspose_API";

    // Set page size A3 and Landscape orientation;   
    var options = new Aspose.Pdf.HtmlLoadOptions(url)
    {
        PageInfo =
        {
            Width = 842,
            Height = 1191,
            IsLandscape = true
        }
    };

    // Load the web page content as a stream and create a PDF document
    using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url), options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### Fornecer credenciais para conversão de página da Web para PDF

Às vezes, precisamos realizar a conversão de arquivos HTML que requerem autenticação e privilégios de acesso, para que apenas usuários autênticos possam buscar o conteúdo da página. Isso também inclui o cenário em que alguns recursos/dados referenciados dentro do HTML são buscados de algum servidor externo que requer autenticação e, para atender a essa necessidade, a propriedade [`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials) foi adicionada à classe [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions). O seguinte trecho de código mostra os passos para passar credenciais para solicitar HTML e seus respectivos recursos ao converter um arquivo HTML para PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedAuthorized()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     const string url = "http://httpbin.org/basic-auth/user1/password1";
     var credentials = new System.Net.NetworkCredential("user1", "password1");

     var options = new Aspose.Pdf.HtmlLoadOptions(url)
     {
         ExternalResourcesCredentials = credentials
     };

     using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url, credentials), options))
     {
         // Save PDF document
         document.Save(dataDir + "HtmlTest_out.pdf");
     }
 }

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### Renderizar todo o conteúdo HTML em uma única página

Aspose.PDF for .NET fornece a capacidade de renderizar todo o conteúdo em uma única página ao converter um arquivo HTML para o formato PDF. Por exemplo, se você tiver algum conteúdo HTML cujo tamanho de saída seja maior que uma página, pode usar a opção para renderizar os dados de saída em uma única página PDF. Para usar essa opção, a classe HtmlLoadOptions foi estendida com a flag IsRenderToSinglePage. O trecho de código abaixo mostra como usar essa funcionalidade.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedSinglePageRendering()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Initialize HtmlLoadOptions
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Set Render to single page property
         IsRenderToSinglePage = true
     };

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "HTMLToPDF.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "RenderContentToSamePage_out.pdf");
     }
 }
```

### Renderizar HTML com Dados SVG

Aspose.PDF for .NET fornece a capacidade de converter uma página HTML em um documento PDF. Como o HTML permite adicionar elementos gráficos SVG como uma tag na página, Aspose.PDF também suporta a conversão de tais dados no arquivo PDF resultante. O seguinte trecho de código mostra como converter arquivos HTML com tags gráficas SVG em Documentos PDF Marcados.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions(Path.GetDirectoryName(dataDir + "HTMLSVG.html"));

    // Initialize Document object
    using (var document = new Aspose.Pdf.Document(dataDir + "HTMLSVG.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "RenderHTMLwithSVGData_out.pdf");
    }
}
```

## Converter MHTML para PDF 

{{% alert color="success" %}}
**Tente converter MHTML para PDF online**

Aspose.PDF for .NET apresenta a você um aplicativo online gratuito ["MHTML para PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão MHTML para PDF usando Aplicativo Gratuito](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="Encapsulamento MIME de documentos HTML agregados">MHTML</abbr>, abreviação de MIME HTML, é um formato de arquivo de arquivamento de página da web usado para combinar recursos que são tipicamente representados por links externos (como imagens, animações Flash, applets Java e arquivos de áudio) com código HTML em um único arquivo. O conteúdo de um arquivo MHTML é codificado como se fosse uma mensagem de email HTML, usando o tipo MIME multipart/related. Aspose.PDF for .NET pode converter arquivos HTML para o formato PDF e, com o lançamento do Aspose.PDF for .NET 9.0.0, introduzimos um novo recurso que permite converter arquivos MHTML para o formato PDF. O próximo trecho de código mostra como converter arquivos MHTML para o formato PDF com C#:

<a name="csharp-mhtml-to-pdf"><strong>Passos: Converter MHTML para PDF em C#</strong></a>

1. Crie uma instância da classe [MhtLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mhtloadoptions/).
2. Inicialize o objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Salve o documento PDF de saída chamando o método **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertMHTtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize MhtLoadOptions with page setup
    var options = new Aspose.Pdf.MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true }
    };

    // Initialize Document object using the MHT file and options
    using (var document = new Aspose.Pdf.Document(dataDir + "fileformatinfo.mht", options))
    {
        // Save PDF document
        document.Save(dataDir + "MhtmlTest_out.pdf");
    }
}
```

## Veja Também 

Este artigo também cobre estes tópicos. Os códigos são os mesmos que os acima.

_Formatação_: **HTML**
- [C# Código HTML para PDF](#csharp-html-to-pdf)
- [C# API HTML para PDF](#csharp-html-to-pdf)
- [C# HTML para PDF Programaticamente](#csharp-html-to-pdf)
- [C# Biblioteca HTML para PDF](#csharp-html-to-pdf)
- [C# Salvar HTML como PDF](#csharp-html-to-pdf)
- [C# Gerar PDF a partir de HTML](#csharp-html-to-pdf)
- [C# Criar PDF a partir de HTML](#csharp-html-to-pdf)
- [C# Conversor HTML para PDF](#csharp-html-to-pdf)

_Formatação_: **MHTML**
- [C# Código MHTML para PDF](#csharp-mhtml-to-pdf)
- [C# API MHTML para PDF](#csharp-mhtml-to-pdf)
- [C# MHTML para PDF Programaticamente](#csharp-mhtml-to-pdf)
- [C# Biblioteca MHTML para PDF](#csharp-mhtml-to-pdf)
- [C# Salvar MHTML como PDF](#csharp-mhtml-to-pdf)
- [C# Gerar PDF a partir de MHTML](#csharp-mhtml-to-pdf)
- [C# Criar PDF a partir de MHTML](#csharp-mhtml-to-pdf)
- [C# Conversor MHTML para PDF](#csharp-mhtml-to-pdf)

_Formatação_: **WebPage**
- [C# Código WebPage para PDF](#csharp-webpage-to-pdf)
- [C# API WebPage para PDF](#csharp-webpage-to-pdf)
- [C# WebPage para PDF Programaticamente](#csharp-webpage-to-pdf)
- [C# Biblioteca WebPage para PDF](#csharp-webpage-to-pdf)
- [C# Salvar WebPage como PDF](#csharp-webpage-to-pdf)
- [C# Gerar PDF a partir de WebPage](#csharp-webpage-to-pdf)
- [C# Criar PDF a partir de WebPage](#csharp-webpage-to-pdf)
- [C# Conversor WebPage para PDF](#csharp-webpage-to-pdf)