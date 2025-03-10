---
title: Como Mesclar PDF usando C#
linktitle: Mesclar arquivos PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /pt/net/merge-pdf-documents/
description: Esta página explica como mesclar documentos PDF em um único arquivo PDF com C# ou VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Merge PDF using C#",
    "alternativeHeadline": "Combine PDF Effortlessly Using C#",
    "abstract": "Descubra a poderosa capacidade de mesclar vários documentos PDF em um único arquivo usando C# com a biblioteca Aspose.PDF. Este recurso permite que os desenvolvedores otimizem seus fluxos de trabalho combinando PDFs de forma eficiente, preservando a qualidade e a estrutura durante o processo. Perfeito para integração de software, essa funcionalidade aumenta a produtividade ao simplificar tarefas de gerenciamento de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "411",
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
    "url": "/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/merge-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "Esta página explica como mesclar documentos PDF em um único arquivo PDF com C# ou VB.NET."
}
</script>

## Mesclar ou combinar vários PDFs em um único PDF em C#

Mesclar PDFs em C# não é uma tarefa simples sem usar uma biblioteca de terceiros. Este artigo mostra como mesclar vários arquivos PDF em um único documento PDF usando Aspose.PDF for .NET. O exemplo é escrito em C#, mas a API pode ser usada em outras linguagens de programação .NET, como VB.NET. Os arquivos PDF são mesclados de forma que o primeiro seja adicionado ao final do outro documento.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Mesclar Arquivos PDF

Para concatenar dois arquivos PDF:

1. Crie dois objetos [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), cada um contendo um dos arquivos PDF de entrada.
1. Em seguida, chame o método Add da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) para o objeto Document ao qual você deseja adicionar o outro arquivo PDF.
1. Passe a coleção PageCollection do segundo objeto Document para o método Add da coleção PageCollection do primeiro.
1. Por fim, salve o arquivo PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

O seguinte trecho de código mostra como concatenar arquivos PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "Concat1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "Concat2.pdf"))
        {
            // Add pages of second document to the first
            document1.Pages.Add(document2.Pages);

            // Save PDF document
            document1.Save(dataDir + "MergeDocuments_out.pdf");
        }
    }
}
```

## Exemplo Ao Vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) é um aplicativo web gratuito online que permite que você investigue como a funcionalidade de mesclagem de apresentação funciona.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Veja também

- [Dividir PDF usando DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Concatenar documentos PDF usando Facades](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [Dividir PDF usando Facades](https://docs.aspose.com/pdf/net/split-pdf-pages/)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>