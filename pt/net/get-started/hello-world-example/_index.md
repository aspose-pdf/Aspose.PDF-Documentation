---
title: Exemplo de Hello World usando a linguagem C#
linktitle: Exemplo de Hello World
type: docs
weight: 40
url: /pt/net/hello-world-example/
description: Este exemplo demonstra como criar um documento PDF simples com o texto Hello World usando Aspose.PDF
aliases:
    - /net/hello-world/
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Exemplo de Hello World usando a linguagem C#",
    "alternativeHeadline": "Exemplo Aspose.PDF C#",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, geração de documentos",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "Este exemplo demonstra como criar um documento PDF simples com o texto Hello World usando Aspose.PDF",
    "articleBody": "Um exemplo de \"Hello World\" é tradicionalmente usado para introduzir recursos de uma linguagem de programação ou software com um caso de uso simples.\nAspose.PDF para .NET é uma API PDF rica em recursos que permite aos desenvolvedores incorporar capacidades de criação, manipulação e conversão de documentos PDF em suas aplicações .NET. Ele suporta o trabalho com muitos formatos de arquivo populares, incluindo PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX e formatos de arquivo de imagem. Neste artigo, estamos criando um documento PDF contendo o texto \"Hello World!\". Após instalar o Aspose.PDF para .NET no seu ambiente, você pode executar o exemplo de código abaixo para ver como a API Aspose.PDF funciona.\nO trecho de código abaixo segue estes passos:\n1. Instanciar um objeto Document\n2. Adicionar uma Página ao objeto do documento\n3. Criar um TextFragment\n4. Adicionar TextFragment à coleção de parágrafos da página\n5. Salvar o documento PDF resultante\nO trecho de código a seguir é um programa Hello World para exibir o funcionamento da API Aspose.PDF para .NET."
}
</script>
Um exemplo de "Hello World" é tradicionalmente usado para introduzir funcionalidades de uma linguagem de programação ou software com um caso de uso simples.

Aspose.PDF para .NET é uma API rica em recursos de PDF que permite aos desenvolvedores incorporar a criação, manipulação e capacidades de conversão de documentos PDF em suas aplicações .NET. Ela suporta o trabalho com muitos formatos de arquivo populares incluindo PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX e formatos de arquivo de imagem. Neste artigo, estamos criando um documento PDF contendo o texto "Hello World!". Após instalar o Aspose.PDF para .NET no seu ambiente, você pode executar o exemplo de código abaixo para ver como a API do Aspose.PDF funciona.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

O trecho de código abaixo segue estes passos:

1. Instancie um objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Adicione uma [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) ao objeto documento
1.
1. Adicione TextFragment à coleção [Paragraph](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) da página
1. [Salve](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) o documento PDF resultante

O seguinte trecho de código é um programa Hello World para exibir o funcionamento da API Aspose.PDF para .NET.

```csharp
namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
        public static void HelloWorld()
        {
            // Inicializa o objeto documento
            Document document = new Document();
            // Adiciona página
            Page page = document.Pages.Add();
            // Adiciona texto à nova página
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
            // Salva o PDF atualizado
            var outputFileName = System.IO.Path.Combine(_dataDir, "HelloWorld_out.pdf");
            document.Save( outputFileName );
        }
    }
}
```
