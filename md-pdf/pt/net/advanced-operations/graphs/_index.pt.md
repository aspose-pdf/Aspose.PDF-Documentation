---
title: Trabalhando com Gráficos em Arquivo PDF
linktitle: Trabalhando com Gráficos
type: docs
weight: 70
url: /net/graphs/
description: Este artigo explica o que é um Gráfico, como criar um objeto retângulo preenchido e outras funções
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-graphs/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Gráficos em Arquivo PDF",
    "alternativeHeadline": "Como criar gráficos em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento PDF",
    "keywords": "pdf, c#, gráficos em pdf",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo explica o que é um Gráfico, como criar um objeto retângulo preenchido e outras funções"
}
</script>

## O que é um Gráfico

Adicionar gráficos a documentos PDF é uma tarefa muito comum para desenvolvedores ao trabalhar com o Adobe Acrobat Writer ou outras aplicações de processamento de PDF. Existem muitos tipos de gráficos que podem ser usados em aplicações PDF.
[Aspose.PDF for .NET](/pdf/net/) também suporta a adição de gráficos a documentos PDF. Para esse propósito, a classe Graph é fornecida. Graph é um elemento de nível de parágrafo e pode ser adicionado à coleção Paragraphs em uma instância de Page. Uma instância de Graph contém uma coleção de Formas.

Os seguintes tipos de formas são suportados pela classe [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph):

- [Arc](/pdf/net/add-arc/) - às vezes também chamado de bandeira, é um par ordenado de vértices adjacentes, mas às vezes também chamado de linha direcionada.
- [Circle](/pdf/net/add-circle/) - exibe dados usando um círculo dividido em setores. Usamos um gráfico circular (também chamado de gráfico de pizza) para mostrar como os dados representam partes de um todo ou de um grupo.
- [Curve](/pdf/net/add-curve/) - é uma união conectada de linhas projetivas, cada linha encontrando três outras em pontos duplos comuns.
- [Curve](/pdf/net/add-curve/) - é uma união conectada de linhas projetivas, cada linha encontrando outras três em pontos duplos comuns.
- [Line](/pdf/net/add-line) - gráficos de linha são usados para exibir dados contínuos e podem ser úteis na previsão de eventos futuros quando mostram tendências ao longo do tempo.
- [Rectangle](/pdf/net/add-rectangle/) - é uma das muitas formas fundamentais que você verá em gráficos, pode ser muito útil para ajudar você a resolver um problema.
- [Ellipse](/pdf/net/add-ellipse/) - é um conjunto de pontos em um plano, criando uma forma oval e curva.

Os detalhes acima também são retratados nas figuras abaixo:

![Figuras em Gráficos](graphs.png)

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


