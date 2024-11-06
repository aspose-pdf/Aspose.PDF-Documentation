---
title: Adicionar Objeto Círculo ao arquivo PDF
linktitle: Adicionar Círculo
type: docs
weight: 20
url: pt/net/add-circle/
description: Este artigo explica como criar um objeto círculo no seu PDF usando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Objeto Círculo ao arquivo PDF",
    "alternativeHeadline": "Como criar um Objeto Círculo no arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, c#, círculo em pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação do Aspose.PDF",
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
    "url": "/net/add-circle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-circle/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo explica como criar um objeto círculo no seu PDF usando Aspose.PDF para .NET."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Adicionar objeto Circle

Como gráficos de barras, gráficos circulares podem ser usados para exibir dados em uma série de categorias separadas. No entanto, ao contrário dos gráficos de barras, os gráficos circulares só podem ser usados quando você tem dados para todas as categorias que compõem o todo. Então, vamos dar uma olhada em como adicionar um objeto [Circle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/circle) com Aspose.PDF para .NET.

Siga os passos abaixo:

1. Criar instância [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Criar [objeto de desenho](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) com certas dimensões

1. Definir [Border](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) para o objeto de desenho

1. Adicionar objeto [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) à coleção de parágrafos da página

1. Salvar nosso arquivo PDF

```csharp
        public static void Circle()
        {
            // Criar instância Document
            var document = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = document.Pages.Add();

            // Criar objeto de desenho com certas dimensões
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);
            // Definir borda para o objeto de desenho
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);

            circle.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(circle);

            // Adicionar objeto Graph à coleção de parágrafos da página
            page.Paragraphs.Add(graph);

            // Salvar arquivo PDF
            document.Save(_dataDir + "DrawingCircle1_out.pdf");
        }
```
Nosso círculo desenhado ficará assim:

![Desenho do Círculo](drawing_circle.png)

## Criar Objeto de Círculo Preenchido

Este exemplo mostra como adicionar um objeto Círculo que é preenchido com cor.

```csharp
        public static void CircleFilled()
        {
            // Criar instância do Documento
            var document = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = document.Pages.Add();

            // Criar objeto de Desenho com certas dimensões
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Definir borda para o objeto de Desenho
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);
            circle.GraphInfo.Color = Color.GreenYellow;
            circle.GraphInfo.FillColor = Color.Green;
            circle.Text = new TextFragment("Círculo");

            graph.Shapes.Add(circle);

            // Adicionar objeto Graph à coleção de parágrafos da página
            page.Paragraphs.Add(graph);

            // Salvar arquivo PDF
            document.Save(_dataDir + "DrawingCircle2_out.pdf");
        }
```
Vamos ver o resultado de adicionar um Círculo preenchido:

![Círculo Preenchido](filled_circle.png)

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
Claro, por favor, forneça o documento que você deseja traduzir para o português, mantendo o formato markdown original.
