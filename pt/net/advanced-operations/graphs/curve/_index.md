---
title: Adicionar Objeto Curva ao arquivo PDF
linktitle: Adicionar Curva
type: docs
weight: 30
url: /pt/net/add-curve/
description: Este artigo explica como criar um objeto curva no seu PDF usando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Objeto Curva ao arquivo PDF",
    "alternativeHeadline": "Como criar Objeto Curva em arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, .net, curva no pdf",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo explica como criar um objeto curva no seu PDF usando Aspose.PDF para .NET."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Adicionar objeto Curve

Um gráfico [Curve](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve) é uma união conectada de linhas projetivas, cada linha encontrando outras três em pontos duplos ordinários.

Aspose.PDF para .NET mostra como usar curvas de Bézier em seus gráficos.
Curvas de Bézier são amplamente utilizadas em gráficos computacionais para modelar curvas suaves. A curva está completamente contida no casco convexo de seus pontos de controle, os pontos podem ser exibidos graficamente e usados para manipular a curva de forma intuitiva.
A curva inteira está contida no quadrilátero cujos cantos são os quatro pontos dados (seu casco convexo).

Neste artigo, investigaremos simplesmente curvas de gráficos e curvas preenchidas, que você pode criar em seu documento PDF.

Siga os passos abaixo:

1. Crie uma instância de [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Defina [Borda](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) para o objeto de Desenho

1. Adicione o objeto [Gráfico](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) à coleção de parágrafos da página

1. Salve nosso arquivo PDF

```csharp
 public static void ExampleCurve()
        {
            // Crie uma instância de Documento
            var document = new Document();

            // Adicione uma página à coleção de páginas do arquivo PDF
            var page = document.Pages.Add();

            // Crie um objeto de Desenho com dimensões específicas
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Defina a borda para o objeto de Desenho
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Adicione o objeto Gráfico à coleção de parágrafos da página
            page.Paragraphs.Add(graph);

            // Salve o arquivo PDF
            document.Save(_dataDir + "DrawingCurve1_out.pdf");
        }
```
A imagem a seguir mostra o resultado executado com nosso trecho de código:

![Desenhando Curva](drawing_curve.png)

## Criar Objeto de Curva Preenchida

Este exemplo mostra como adicionar um objeto Curva que é preenchido com cor.

```csharp
      public static void CurveFilled()
        {
            // Criar instância de Documento
            var document = new Document();

            // Adicionar página à coleção de páginas do arquivo PDF
            var page = document.Pages.Add();

            // Criar objeto de Desenho com certas dimensões
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Definir borda para o objeto de Desenho
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Adicionar objeto de Gráfico à coleção de parágrafos da página
            page.Paragraphs.Add(graph);

            // Salvar arquivo PDF
            document.Save(_dataDir + "DrawingCurve2_out.pdf");
        }
```
Veja o resultado de adicionar uma Curva preenchida:

![Curva Preenchida](filled_curve.png)

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


