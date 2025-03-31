---
title: Criar documento PDF programaticamente
linktitle: Criar PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/create-document/
description: Esta página descreve como criar um documento PDF do zero com a biblioteca Aspose.PDF.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Creation Made Easy with C#",
    "abstract": "O novo recurso em Aspose.PDF for .NET permite que os desenvolvedores criem documentos PDF programaticamente usando C# e VB.NET, simplificando o processo para várias aplicações .NET como WinForms e ASP.NET. Com métodos simples para adicionar páginas e texto, os usuários podem gerar facilmente arquivos PDF personalizados do zero, aprimorando a funcionalidade de suas aplicações e a experiência do usuário.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "307",
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
    "url": "/net/create-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Aspose.PDF for .NET API permite que você crie e leia arquivos PDF usando C# e VB.NET. A API pode ser usada em uma variedade de aplicações .NET, incluindo WinForms, ASP.NET e várias outras. Neste artigo, vamos mostrar como usar a API Aspose.PDF for .NET para gerar e ler arquivos PDF facilmente em aplicações .NET.

## Como Criar um Arquivo PDF usando C#

Para criar um arquivo PDF usando C#, os seguintes passos podem ser utilizados.

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Adicione um objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à coleção [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) do objeto Document.
1. Adicione [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) à coleção [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) da página.
1. Salve o documento PDF resultante.

O próximo trecho de código também funciona com a biblioteca [Aspose.Drawing](/pdf/pt/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

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

Neste caso, criamos um documento PDF de uma página com tamanho de página A4, orientação retrato. Nossa página conterá um "Olá, Mundo" na parte superior esquerda da página.