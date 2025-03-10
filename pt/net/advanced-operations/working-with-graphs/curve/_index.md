---
title: Adicionar Objeto Curva ao arquivo PDF
linktitle: Adicionar Curva
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/add-curve/
description: Este artigo explica como criar um objeto curva para seu PDF usando Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Curve Object to PDF file",
    "alternativeHeadline": "Create Curves in PDFs",
    "abstract": "O novo recurso em Aspose.PDF for .NET permite que os desenvolvedores criem e manipulem objetos curva dentro de documentos PDF, utilizando curvas de Bezier para gráficos suaves. Essa melhoria facilita o design de curvas simples e preenchidas, fornecendo uma ferramenta poderosa para gerar representações visuais complexas em PDFs, mantendo o controle sobre dimensões e estilo.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Curve, Curve object, Bezier curves, Aspose.PDF for .NET, PDF document generation, Drawing object, Filled Curve, Graph object, PDF manipulation, ASP.NET PDF",
    "wordcount": "500",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2024-11-25",
    "description": "Este artigo explica como criar um objeto curva para seu PDF usando Aspose.PDF for .NET."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Adicionar objeto Curva

Uma curva [Curve](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve) é uma união conectada de linhas projetivas, cada linha encontrando três outras em pontos duplos ordinários.

Aspose.PDF for .NET mostra como usar curvas Bézier em seus Gráficos.
As curvas Bézier são amplamente utilizadas em gráficos de computador para modelar curvas suaves. A curva está completamente contida no envoltório convexo de seus pontos de controle, os pontos podem ser exibidos graficamente e usados para manipular a curva de forma intuitiva.
Toda a curva está contida no quadrilátero cujos cantos são os quatro pontos dados (seu envoltório convexo).

Neste artigo, investigaremos curvas gráficas simples e curvas preenchidas que você pode criar em seu documento PDF.

Siga os passos abaixo:

1. Crie uma instância de [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Crie um [objeto de Desenho](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) com certas dimensões.
1. Defina a [Borda](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) para o objeto de Desenho.
1. Adicione o objeto [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) à coleção de parágrafos da página.
1. Salve nosso arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleCurve()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create a curve and set its properties
        var curve1 = new Aspose.Pdf.Drawing.Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 })
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.GreenYellow 
            }
        };

        // Add the curve to the graph shapes
        graph.Shapes.Add(curve1);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCurve1_out.pdf");
    }
}

```

A imagem a seguir mostra o resultado executado com nosso trecho de código:

![Desenhando Curva](drawing_curve.png)

## Criar Objeto Curva Preenchida

Este exemplo mostra como adicionar um objeto Curva que é preenchido com cor.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CurveFilled()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create a curve and set fill color
        var curve1 = new Aspose.Pdf.Drawing.Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 })
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            }
        };

        // Add the curve to the graph shapes
        graph.Shapes.Add(curve1);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCurve2_out.pdf");
    }
}
```

Veja o resultado da adição de uma Curva preenchida:

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