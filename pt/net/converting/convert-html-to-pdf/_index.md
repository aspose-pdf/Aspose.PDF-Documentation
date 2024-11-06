---
title: Converter HTML para PDF em .NET
linktitle: Converter arquivo HTML para PDF
type: docs
weight: 40
url: pt/net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: Este tópico mostra como converter HTML para PDF e MHTML para PDF usando Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
## Visão Geral

Este artigo explica como **converter HTML para PDF usando C#**. Ele abrange os seguintes tópicos.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Formato_: **HTML**
- [C# HTML para PDF](#csharp-html-to-pdf)
- [C# Converter HTML para PDF](#csharp-html-to-pdf)
- [C# Como converter HTML para PDF](#csharp-html-to-pdf)

_Formato_: **MHTML**
- [C# MHTML para PDF](#csharp-mhtml-to-pdf)
- [C# Converter MHTML para PDF](#csharp-mhtml-to-pdf)
- [C# Como converter MHTML para PDF](#csharp-mhtml-to-pdf)

_Formato_: **WebPage**
- [C# WebPage para PDF](#csharp-webpage-to-pdf)
- [C# Converter WebPage para PDF](#csharp-webpage-to-pdf)
- [C# Como converter WebPage para PDF](#csharp-webpage-to-pdf)

## Conversão de HTML para PDF em C#
## Conversão de HTML para PDF em C#

**Aspose.PDF para .NET** é uma API de manipulação de PDF que permite converter documentos HTML existentes para PDF de forma contínua. O processo de conversão de HTML para PDF pode ser personalizado flexivelmente.

## Converter HTML para PDF

O seguinte exemplo de código C# mostra como converter um documento HTML em PDF.

<a name="csharp-html-to-pdf"><strong>Passos: Converter HTML para PDF em C#</strong></a>

1. Crie uma instância da classe [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/).
2. Inicialize o objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Salve o documento PDF de saída chamando o método **Document.Save()**.

```csharp
public static void ConvertHTMLtoPDF()
{
    HtmlLoadOptions options= new HtmlLoadOptions();
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```

{{% alert color="success" %}}
**Tente converter HTML para PDF online**

Aspose apresenta a você a aplicação gratuita online ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), onde você pode experimentar investigar a funcionalidade e a qualidade com que funciona.
Aspose apresenta a você a aplicação online gratuita ["HTML para PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), onde você pode experimentar a funcionalidade e a qualidade com que funciona.
{{% /alert %}}

[![Aspose.PDF Conversão de HTML para PDF usando o App Gratuito](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)

## Conversão avançada de HTML para PDF

O motor de conversão HTML possui várias opções que nos permitem controlar o processo de conversão.

### Suporte a Media Queries

Media queries são uma técnica popular para fornecer uma folha de estilo adaptada para diferentes dispositivos. Podemos definir o tipo de dispositivo usando a propriedade [`HtmlMediaType`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype).

```csharp
public static void ConvertHTMLtoPDFAdvanced_MediaType()
{
    HtmlLoadOptions options = new HtmlLoadOptions
    {
        // definir modo Impressão ou Tela
        HtmlMediaType = HtmlMediaType.Print
    };
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```
### Ativar (desativar) incorporação de fontes

Páginas HTML frequentemente usam fontes (por exemplo, fontes de uma pasta local, Google Fonts, etc). Podemos também controlar a incorporação de fontes em um documento usando a propriedade [`IsEmbedFonts`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/isembedfonts).

```csharp
public static void ConvertHTMLtoPDFAdvanced_EmbedFonts()
{
    // Desativar incorporação de fontes
    HtmlLoadOptions options = new HtmlLoadOptions {IsEmbedFonts = false};
    Document pdfDocument= new Document(_dataDir + "test_fonts.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```

### Gerenciar carregamento de recursos externos

O Motor de Conversão fornece um mecanismo que permite controlar o carregamento de certos recursos associados ao documento HTML.
A classe [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) possui a propriedade [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) com a qual podemos definir o comportamento do carregador de recursos.
A classe [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) possui a propriedade [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) com a qual podemos definir o comportamento do carregador de recursos.
Suponha que precisemos substituir todas as imagens PNG por uma única imagem `test.jpg` e substituir URL externa por interna para outros recursos.
Para fazer isso, podemos definir um carregador personalizado `SamePictureLoader` e apontar [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) para este nome.

```csharp
public static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    HtmlLoadOptions options = new HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };
    Document pdfDocument = new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(_dataDir + "test.jpg");
        result = new LoadOptions.ResourceLoadingResult(resultBytes)
        {
            // Definir o Tipo MIME
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```
## Converter página Web para PDF

Converter uma página web é ligeiramente diferente de converter um documento HTML local. Para converter o conteúdo de uma página Web para o formato PDF, podemos primeiro buscar o conteúdo da página HTML usando uma instância HttpClient, criar um objeto Stream, passar o conteúdo para o objeto Document e renderizar a saída em formato PDF.

Ao converter uma página web hospedada em um servidor web para PDF:

<a name="csharp-webpage-to-pdf"><strong>Passos: Converter WebPage para PDF em C#</strong></a>

1. Ler o conteúdo da página usando um objeto HttpClient.
1. Instancie o objeto [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) e defina a URL base.
1. Inicialize um objeto Document enquanto passa o objeto stream.
1. Opcionalmente, defina o tamanho da página e/ou orientação.

```csharp
public static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    const string url = "https://pt.wikipedia.org/wiki/Aspose_API";
    // Definir tamanho da página A3 e orientação Paisagem;   
    HtmlLoadOptions options = new HtmlLoadOptions(url)
    {
        PageInfo = {Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(GetContentFromUrlAsStream(url), options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static Stream GetContentFromUrlAsStream(string url, ICredentials credentials = null)
{
    using (var handler = new HttpClientHandler { Credentials = credentials })
    using (var httpClient = new HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```
### Fornecer credenciais para conversão de página Web para PDF

Às vezes, precisamos realizar a conversão de arquivos HTML que requerem autenticação e privilégios de acesso, de modo que apenas usuários autênticos possam buscar o conteúdo da página. Isso também inclui o cenário em que alguns recursos/dados referenciados dentro do HTML são obtidos de algum servidor externo que requer autenticação e, para atender a essa necessidade, a propriedade [`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials) é adicionada à classe [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions). O seguinte trecho de código mostra os passos para passar credenciais para solicitar HTML e seus respectivos recursos durante a conversão de arquivo HTML para PDF.

```csharp
public static void ConvertHTMLtoPDFAdvanced_Authorized()
{
    const string url = "http://httpbin.org/basic-auth/user1/password1";
    var credentials = new NetworkCredential("user1", "password1");
    HtmlLoadOptions options = new HtmlLoadOptions(url)
    {
        ExternalResourcesCredentials = credentials
    };
    Document pdfDocument= new Document(GetContentFromUrlAsStream(url, credentials), options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static Stream GetContentFromUrlAsStream(string url, ICredentials credentials = null)
{
    using (var handler = new HttpClientHandler { Credentials = credentials })
    using (var httpClient = new HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```
### Renderizar todo o conteúdo HTML em uma única página

Aspose.PDF para .NET oferece a capacidade de renderizar todos os conteúdos em uma única página ao converter um arquivo HTML para o formato PDF. Por exemplo, se você tem algum conteúdo HTML cujo tamanho de saída é maior que uma página, você pode usar a opção para renderizar os dados de saída em uma única página PDF. Para usar essa opção, a classe HtmlLoadOptions foi estendida com a flag IsRenderToSinglePage. O trecho de código abaixo mostra como usar essa funcionalidade.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Inicializar as opções de HTMLLoadSave
HtmlLoadOptions options = new HtmlLoadOptions();
// Definir a propriedade Renderizar para uma única página
options.IsRenderToSinglePage = true;
// Carregar documento
Document pdfDocument= new Document(dataDir + "HTMLToPDF.html", options);
// Salvar
pdfDocument.Save(dataDir + "RenderContentToSamePage.pdf");
```

### Renderizar HTML com dados SVG
### Renderizar HTML com Dados SVG

Aspose.PDF para .NET fornece a capacidade de converter uma página HTML em documento PDF. Uma vez que o HTML permite adicionar o elemento gráfico SVG como uma tag na página, o Aspose.PDF também suporta a conversão de tais dados no arquivo PDF resultante. O seguinte trecho de código mostra como converter arquivos HTML com tags gráficas SVG para Documentos PDF Etiquetados.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Definir o caminho do arquivo de entrada
string inFile = dataDir + "HTMLSVG.html";
// Definir o caminho do arquivo de saída
string outFile = dataDir + "RenderHTMLwithSVGData.pdf";
// Inicializar HtmlLoadOptions
HtmlLoadOptions options = new HtmlLoadOptions(Path.GetDirectoryName(inFile));
// Inicializar objeto Document
Document pdfDocument = new Document(inFile, options);
// salvar
pdfDocument.Save(outFile);
```

## Converter MHTML para PDF

{{% alert color="success" %}}
**Tente converter MHTML para PDF online**
**Tente converter MHTML para PDF online**
{{% /alert %}}

O Aspose.PDF para .NET apresenta a você uma aplicação online gratuita ["MHTML para PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), onde você pode explorar a funcionalidade e a qualidade com que funciona.

[![Conversão de MHTML para PDF usando o Aplicativo Gratuito Aspose.PDF](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)

<abbr title="Encapsulamento MIME de documentos HTML agregados">MHTML</abbr>, abreviação para MIME HTML, é um formato de arquivo de arquivo de página web usado para combinar recursos que são tipicamente representados por links externos (como imagens, animações Flash, applets Java e arquivos de áudio) com código HTML em um único arquivo.
<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, abreviação para MIME HTML, é um formato de arquivo de arquivo de página web usado para combinar recursos que são tipicamente representados por links externos (como imagens, animações Flash, applets Java e arquivos de áudio) com código HTML em um único arquivo.

<a name="csharp-mhtml-to-pdf"><strong>Passos: Converter MHTML para PDF em C#</strong></a>

1. Crie uma instância da classe [MhtLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mhtloadoptions/).
2. Inicialize o objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Salve o documento PDF de saída chamando o método **Document.Save()**.

```csharp
public static void ConvertMHTtoPDF()
{
    MhtLoadOptions options = new MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(_dataDir + "fileformatinfo.mht", options);
    pdfDocument.Save(_dataDir + "mhtml_test.PDF");
}
```

## Veja também

Este artigo também aborda esses tópicos.
Este artigo também aborda esses tópicos.

_Format_: **HTML**
- [Código C# HTML para PDF](#csharp-html-to-pdf)
- [API C# HTML para PDF](#csharp-html-to-pdf)
- [C# HTML para PDF Programaticamente](#csharp-html-to-pdf)
- [Biblioteca C# HTML para PDF](#csharp-html-to-pdf)
- [C# Salvar HTML como PDF](#csharp-html-to-pdf)
- [C# Gerar PDF a partir de HTML](#csharp-html-to-pdf)
- [C# Criar PDF a partir de HTML](#csharp-html-to-pdf)
- [Conversor C# HTML para PDF](#csharp-html-to-pdf)

_Format_: **MHTML**
- [Código C# MHTML para PDF](#csharp-mhtml-to-pdf)
- [API C# MHTML para PDF](#csharp-mhtml-to-pdf)
- [C# MHTML para PDF Programaticamente](#csharp-mhtml-to-pdf)
- [Biblioteca C# MHTML para PDF](#csharp-mhtml-to-pdf)
- [C# Salvar MHTML como PDF](#csharp-mhtml-to-pdf)
- [C# Gerar PDF a partir de MHTML](#csharp-mhtml-to-pdf)
- [C# Criar PDF a partir de MHTML](#csharp-mhtml-to-pdf)
- [Conversor C# MHTML para PDF](#csharp-mhtml-to-pdf)

_Format_: **WebPage**
- [Código C# WebPage para PDF](#csharp-webpage-to-pdf)
- [API C# WebPage para PDF](#csharp-webpage-to-pdf)
- [C# WebPage para PDF Programaticamente](#csharp-webpage-to-pdf)
- [C# Página Web para PDF Programaticamente](#csharp-webpage-to-pdf)
- [Biblioteca C# Página Web para PDF](#csharp-webpage-to-pdf)
- [C# Salvar Página Web como PDF](#csharp-webpage-to-pdf)
- [C# Gerar PDF a partir de Página Web](#csharp-webpage-to-pdf)
- [C# Criar PDF a partir de Página Web](#csharp-webpage-to-pdf)
- [Conversor C# de Página Web para PDF](#csharp-webpage-to-pdf)
