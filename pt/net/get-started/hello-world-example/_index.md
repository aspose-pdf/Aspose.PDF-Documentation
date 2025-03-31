---
title: Exemplo de Hello World usando a linguagem C#
linktitle: Exemplo de Hello World
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /pt/net/hello-world-example/
description: Este exemplo demonstra como criar um documento PDF simples com o texto Hello World usando Aspose.PDF
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Example of Hello World using C# language",
    "alternativeHeadline": "Aspose.PDF C# example",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2024-11-26",
    "description": "Este exemplo demonstra como criar um documento PDF simples com o texto Hello World usando Aspose.PDF",
    "articleBody": "A \"Hello World\" example is traditionally used to introduce features of a programming language or software with a simple use case.\nAspose.PDF for .NET is a feature rich PDF API that allows the developers to embed PDF document creation, manipulation & conversion capabilities in their .NET applications. It supports working with many popular file formats including PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we are creating a PDF document containing text \"Hello World!\". After installing Aspose.PDF for .NET in your environment, you can execute below code sample to see how Aspose.PDF API works.\nBelow code snippet follows these steps:\n1. // Create PDF document\n2. Add a Page to document object\n3. Create a TextFragment\n4. Add TextFragment to Paragraph collection of the page\n5. Save resultant PDF document\nFollowing code snippet is a Hello World program to exhibit working of Aspose.PDF for .NET API."
}
</script>

Um exemplo "Hello World" é tradicionalmente usado para introduzir recursos de uma linguagem de programação ou software com um caso de uso simples.

Aspose.PDF for .NET é uma API PDF rica em recursos que permite aos desenvolvedores incorporar capacidades de criação, manipulação e conversão de documentos PDF em suas aplicações .NET. Ela suporta o trabalho com muitos formatos de arquivo populares, incluindo PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX e formatos de arquivo de imagem. Neste artigo, estamos criando um documento PDF contendo o texto "Hello World!". Após instalar Aspose.PDF for .NET em seu ambiente, você pode executar o código abaixo para ver como a API Aspose.PDF funciona.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

O trecho de código abaixo segue estas etapas:

1. Instanciar um objeto [Document](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document).
1. Adicionar uma [Page](https://reference.aspose.com/pdf/pt/net/aspose.pdf/page) ao objeto documento.
1. Criar um objeto [TextFragment](https://reference.aspose.com/pdf/pt/net/aspose.pdf.text/textfragment).
1. Adicionar TextFragment à coleção de [Paragraph](https://reference.aspose.com/pdf/pt/net/aspose.pdf/page/properties/paragraphs) da página.
1. [Salvar](https://reference.aspose.com/pdf/pt/net/aspose.pdf.document/save/methods/4) o documento PDF resultante.

O seguinte trecho de código é um programa Hello World para demonstrar o funcionamento da API Aspose.PDF for .NET.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```