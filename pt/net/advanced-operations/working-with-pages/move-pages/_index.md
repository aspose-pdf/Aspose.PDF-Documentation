---
title: Mova Páginas PDF Programaticamente em C#
linktitle: Mover Páginas PDF
type: docs
weight: 20
url: /pt/net/move-pages/
description: Tente mover páginas para o local desejado ou para o final de um arquivo PDF usando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Mova Páginas PDF Programaticamente em C#",
    "alternativeHeadline": "Como mover Páginas PDF com .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, mover página pdf",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Tente mover páginas para o local desejado ou para o final de um arquivo PDF usando Aspose.PDF para .NET."
}
</script>

## Movendo uma Página de um Documento PDF para Outro

Este tópico explica como mover uma página de um documento PDF para o final de outro documento usando C#.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

Para mover uma página, devemos:

1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF de origem.
1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF de destino.
1. Obter a Página da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Adicionar](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) página ao documento de destino.
1. Salvar o PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Deletar](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) a página no documento de origem.
1.
O seguinte trecho de código mostra como mover uma página.

```csharp
var srcFileName = "<insira o nome do arquivo>";
var dstFileName = "<insira o nome do arquivo>";
var srcDocument = new Document(srcFileName);
var dstDocument = new Document();
var page = srcDocument.Pages[2];
dstDocument.Pages.Add(page);
// Salvar arquivo de saída
dstDocument.Save(srcFileName);
srcDocument.Pages.Delete(2);
srcDocument.Save(dstFileName);
```

## Movendo um conjunto de páginas de um documento PDF para outro

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF fonte.
1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF de destino.
1. Defina um array com os números das páginas a serem movidas.
1. Execute um loop através do array:
    1. Obtenha a Página da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. Salve o PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) a página no documento fonte usando um array.
1. Salve o PDF fonte usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

O seguinte trecho de código mostra como mover um conjunto de páginas de um documento PDF para outro.

```csharp
var srcFileName = "<enter file name>";
var dstFileName = "<enter file name>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);
var dstDocument = new Aspose.Pdf.Document();
var pages = new []{ 1, 3 };
foreach (var pageIndex in pages)
{
    var page = srcDocument.Pages[pageIndex];
    dstDocument.Pages.Add(page);
}                       
// Salva os arquivos de saída
dstDocument.Save(dstFileName);
srcDocument.Pages.Delete(pages);
srcDocument.Save(srcFileName);
```

## Movendo uma Página para uma nova localização no Documento PDF atual

1.
1. Obtenha a página da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Adicione](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) a página para um novo local (por exemplo, no final).
1. [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) a página na localização anterior.
1. Salve o PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

```csharp
var srcFileName = "<enter file name>";
var dstFileName = "<enter file name>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);

var page = srcDocument.Pages[2];
srcDocument.Pages.Add(page);
srcDocument.Pages.Delete(2);          

// Save output file
srcDocument.Save(dstFileName);
```

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


