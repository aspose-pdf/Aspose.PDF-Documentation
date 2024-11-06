---
title: Adicionar objeto Arco ao arquivo PDF
linktitle: Adicionar Arco
type: docs
weight: 10
url: pt/net/add-arc/
description: Este artigo explica como criar um objeto arco no seu PDF usando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar objeto Arco ao arquivo PDF",
    "alternativeHeadline": "Como criar um Arco no arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento PDF",
    "keywords": "PDF, C#, arco no PDF",
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
    "url": "/net/add-arc/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-arc/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo explica como criar um objeto arco no seu PDF usando Aspose.PDF para .NET."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Adicionar objeto Arc

Aspose.PDF para .NET suporta a funcionalidade de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) aos documentos PDF. Ele também oferece a funcionalidade de preencher um objeto arc com uma determinada cor.

Siga os passos abaixo:

1. Criar instância de [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Criar [Objeto de desenho](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) com certas dimensões

1. Definir [Borda](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) para o objeto de desenho

1. Adicionar objeto [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) à coleção de parágrafos da página

1. Salvar nosso arquivo PDF

O seguinte trecho de código mostra como adicionar um objeto [Arc](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc).

```csharp
 public static void Arc()
        {
            // Criar instância de Document
            var document = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = document.Pages.Add();

            // Criar objeto de desenho com certas dimensões
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Definir borda para o objeto de desenho
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc1 = new Arc(100, 100, 95, 0, 90);
            arc1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(arc1);

            var arc2 = new Arc(100, 100, 90, 70, 180);
            arc2.GraphInfo.Color = Color.DarkBlue;
            graph.Shapes.Add(arc2);

            var arc3 = new Arc(100, 100, 85, 120, 210);
            arc3.GraphInfo.Color = Color.Red;
            graph.Shapes.Add(arc3);

            // Adicionar objeto Graph à coleção de parágrafos da página
            page.Paragraphs.Add(graph);

            // Salvar arquivo PDF
            document.Save(_dataDir + "DrawingArc_out.pdf");

        }
```
## Criar Objeto de Arco Preenchido

O próximo exemplo mostra como adicionar um objeto Arco que é preenchido com cor e dimensões específicas.

```csharp
        public static void ArcFilled()
        {
            // Criar instância de Documento
            var document = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = document.Pages.Add();

            // Criar objeto de Desenho com dimensões específicas
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Definir borda para o objeto de Desenho
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc = new Arc(100, 100, 95, 0, 90);
            arc.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(arc);

            var line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
            line.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(line);

            // Adicionar objeto de Gráfico à coleção de parágrafos da página
            page.Paragraphs.Add(graph);

            // Salvar o arquivo PDF
            document.Save(_dataDir + "ExampleFilledArc_out.pdf");

        }
```
Vamos ver o resultado de adicionar um Arco preenchido:

![Arco Preenchido](filled_arc.png)

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


