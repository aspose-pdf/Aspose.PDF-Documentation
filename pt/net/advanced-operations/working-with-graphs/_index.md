---
title: Trabalhando com Gráficos em arquivo PDF
linktitle: Trabalhando com Gráficos
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /pt/net/working-with-graphs/
description: Este artigo explica o que é um Gráfico, como criar um objeto retângulo preenchido e outras funções
lastmod: "2022-02-17"
sitemap:
changefreq: "weekly"
priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Graphs in PDF file",
    "alternativeHeadline": "Create and Manipulate Graphs in PDF Files",
    "abstract": "Descubra o poderoso novo recurso para gerar e manipular gráficos dentro de documentos PDF usando Aspose.PDF for .NET. Essa funcionalidade permite que os desenvolvedores criem uma variedade de formas de gráfico, incluindo arcos, círculos, linhas e retângulos, aprimorando a apresentação visual dos dados em suas aplicações. Otimize seu processo de geração de PDF e forneça visualizações de dados dinâmicas com facilidade",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Graph, PDF documents, Aspose.PDF for .NET, Graph class, Shapes, Arc, Circle, Line graph, Rectangle, PDF manipulation",
    "wordcount": "324",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2025-03-17",
    "description": "Este artigo explica o que é um Gráfico, como criar um objeto retângulo preenchido e outras funções"
}
</script>

## O que é Gráfico

Adicionar gráficos a documentos PDF é uma tarefa muito comum para desenvolvedores ao trabalhar com Adobe Acrobat Writer ou outras aplicações de processamento de PDF. Existem muitos tipos de gráficos que podem ser usados em aplicações PDF.
[Aspose.PDF for .NET](/pdf/pt/net/) também suporta a adição de gráficos a documentos PDF. Para esse propósito, a classe Gráfico é fornecida. Gráfico é um elemento de nível de parágrafo e pode ser adicionado à coleção de Parágrafos em uma instância de Página. Uma instância de Gráfico contém uma coleção de Formas.

Os seguintes tipos de formas são suportados pela classe [Gráfico](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph):

- [Arco](/pdf/pt/net/add-arc/) - às vezes também chamado de bandeira, é um par ordenado de vértices adjacentes, mas às vezes também chamado de linha direcionada.
- [Círculo](/pdf/pt/net/add-circle/) - exibe dados usando um círculo dividido em setores. Usamos um gráfico de círculo (também chamado de gráfico de pizza) para mostrar como os dados representam porções de um todo ou de um grupo.
- [Curva](/pdf/pt/net/add-curve/) - é uma união conectada de linhas projetivas, cada linha encontrando três outras em pontos duplos ordinários.
- [Linha](/pdf/pt/net/add-line) - gráficos de linha são usados para exibir dados contínuos e podem ser úteis na previsão de eventos futuros quando mostram tendências ao longo do tempo.
- [Retângulo](/pdf/pt/net/add-rectangle/) - é uma das muitas formas fundamentais que você verá em gráficos, pode ser muito útil para ajudá-lo a resolver um problema.
- [Elipse](/pdf/pt/net/add-ellipse/) - é um conjunto de pontos em um plano, criando uma forma oval, curva.

As seguintes operações são suportadas para tipos de forma:
- [Verificar limites](/pdf/pt/net/aspose-pdf-drawing-graph-shapes-bounds-check/) - verificar limites de forma na coleção de Formas.

Os detalhes acima também são representados nas figuras abaixo:

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