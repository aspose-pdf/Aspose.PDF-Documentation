---
title: Alterar o Tamanho da Página do PDF com C#
linktitle: Alterar o Tamanho da Página do PDF
type: docs
weight: 40
url: /net/change-page-size/
description: Altere o tamanho da página do seu documento PDF usando a biblioteca Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Alterar o Tamanho da Página do PDF com C#",
    "alternativeHeadline": "Redimensionar Página do PDF com .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, alterar tamanho do pdf, redimensionar pdf",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2022-02-04",
    "description": "Altere o tamanho da página do seu documento PDF usando a biblioteca Aspose.PDF para .NET."
}
</script>
## Alterar Tamanho da Página PDF

Aspose.PDF para .NET permite que você altere o tamanho da página PDF com linhas simples de código em suas aplicações .NET. Este tópico explica como atualizar/alterar as dimensões (tamanho) da página de um arquivo PDF existente.

O trecho de código a seguir também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

A classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) contém o método SetPageSize(...) que permite definir o tamanho da página. O trecho de código abaixo atualiza as dimensões da página em poucos passos fáceis:

1. Carregar o arquivo PDF fonte.
1. Obter as páginas no objeto [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. Obter uma página específica.
1. Chamar o método SetPageSize(..) para atualizar suas dimensões.
1. Chamar o método Save(..) da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) para gerar o arquivo PDF com as dimensões da página atualizadas.

{{% alert color="primary" %}}

Por favor, note que as propriedades de altura e largura usam pontos como unidade básica, onde 1 polegada = 72 pontos e 1 cm = 1/2.54 polegada = 0.3937 polegada = 28.3 pontos.
Observe que as propriedades de altura e largura usam pontos como unidade básica, onde 1 polegada = 72 pontos e 1 cm = 1/2.54 polegada = 0.3937 polegada = 28.3 pontos.

{{% /alert %}}

O seguinte trecho de código mostra como alterar as dimensões da página PDF para o tamanho A4.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-UpdateDimensions-UpdateDimensions.cs" >}}

## Obter Tamanho da Página PDF

Você pode ler o tamanho da página de um arquivo PDF existente usando Aspose.PDF para .NET. O seguinte exemplo de código mostra como ler as dimensões da página PDF usando C#.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetDimensions-GetDimensions.cs" >}}

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


