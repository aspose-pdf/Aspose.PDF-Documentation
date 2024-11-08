---
title: Como Mesclar PDF usando C#
linktitle: Mesclar arquivos PDF
type: docs
weight: 50
url: /pt/net/merge-pdf-documents/
keywords: "merge multiple pdf into single pdf c#, combine multiple pdf into one c#, merge multiple pdf into one c#"
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
    "headline": "Como Mesclar PDF usando C#",
    "alternativeHeadline": "Combinar documentos PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "manipulação de documentos PDF",
    "keywords": "pdf, c#, mesclar pdf, concatenar, combinar pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/net/merge-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta página explica como mesclar documentos PDF em um único arquivo PDF com C# ou VB.NET."
}
</script>

## Mesclar ou combinar vários PDFs em um único PDF em C#

Mesclar PDFs em C# não é uma tarefa direta sem o uso de uma biblioteca de terceiros.
Este artigo mostra como mesclar vários arquivos PDF em um único documento PDF usando Aspose.PDF para .NET. O exemplo está escrito em C#, mas a API também pode ser usada em outras linguagens de programação .NET, como VB.NET. Os arquivos PDF são mesclados de forma que o primeiro seja unido ao final do outro documento.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Mesclar arquivos PDF usando C# e DOM

Para concatenar dois arquivos PDF:

1. Crie dois objetos [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), cada um contendo um dos arquivos PDF de entrada.
1. Em seguida, chame o método Add da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) para o objeto Document ao qual você deseja adicionar o outro arquivo PDF.
1.
1. Finalmente, salve o arquivo PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

O seguinte trecho de código mostra como concatenar arquivos PDF.

```csharp
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Abrir primeiro documento
Document pdfDocument1 = new Document(dataDir + "Concat1.pdf");
// Abrir segundo documento
Document pdfDocument2 = new Document(dataDir + "Concat2.pdf");

// Adicionar páginas do segundo documento ao primeiro
pdfDocument1.Pages.Add(pdfDocument2.Pages);

dataDir = dataDir + "ConcatenatePdfFiles_out.pdf";
// Salvar arquivo de saída concatenado
pdfDocument1.Save(dataDir);
```

## Exemplo ao Vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) é uma aplicação web gratuita que permite investigar como a funcionalidade de mesclagem de apresentação funciona.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Veja também

- [Dividir PDF usando DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
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
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
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


