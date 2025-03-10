---
title: Adicionar Objeto Arco ao arquivo PDF
linktitle: Adicionar Arco
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/add-arc/
description: Este artigo explica como criar um objeto arco no seu PDF usando Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Arc Object to PDF file",
    "alternativeHeadline": "Add Colorful Arc Shapes to  PDF Documents",
    "abstract": "O novo recurso em Aspose.PDF for .NET permite que os usuários integrem objetos arco em documentos PDF de forma contínua, aprimorando as capacidades gráficas ao fornecer a capacidade de desenhar arcos em várias cores e dimensões. Essa funcionalidade capacita os desenvolvedores a criar arquivos PDF mais visualmente atraentes e personalizados, adicionando arcos preenchidos e formas detalhadas com controle preciso sobre atributos como bordas e cores de preenchimento.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Arc Object, PDF file, Aspose.PDF for .NET, create Arc, graph objects, filled Arc object",
    "wordcount": "472",
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
    "url": "/net/add-arc/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-arc/"
    },
    "dateModified": "2024-11-25",
    "description": "Este artigo explica como criar um objeto arco no seu PDF usando Aspose.PDF for .NET."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Adicionar objeto Arco

Aspose.PDF for .NET suporta o recurso de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Também oferece a funcionalidade de preencher o objeto arco com uma determinada cor.

Siga os passos abaixo:

1. Crie uma instância de [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Crie um [objeto Drawing](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) com determinadas dimensões.
1. Defina a [Borda](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) para o objeto Drawing.
1. Adicione o objeto [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) à coleção de parágrafos da página.
1. Salve nosso arquivo PDF.

O seguinte trecho de código mostra como adicionar um objeto [Arc](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Arc()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create arcs and set their properties
        var arc1 = new Aspose.Pdf.Drawing.Arc(100, 100, 95, 0, 90)
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.GreenYellow 
            }
        };
        graph.Shapes.Add(arc1);

        var arc2 = new Aspose.Pdf.Drawing.Arc(100, 100, 90, 70, 180)
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.DarkBlue 
            }
        };
        graph.Shapes.Add(arc2);

        var arc3 = new Aspose.Pdf.Drawing.Arc(100, 100, 85, 120, 210)
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.Red 
            }
        };
        graph.Shapes.Add(arc3);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingArc_out.pdf");
    }
}
```

## Criar Objeto Arco Preenchido

O próximo exemplo mostra como adicionar um objeto Arco que é preenchido com cor e determinadas dimensões.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ArcFilled()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

        // Set border for Drawing object
        var borderInfo = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Green);
        graph.Border = borderInfo;

        // Create an arc and set fill color
        var arc = new Aspose.Pdf.Drawing.Arc(100, 100, 95, 0, 90)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            }
        };
        graph.Shapes.Add(arc);

        // Create a line and set fill color
        var line = new Aspose.Pdf.Drawing.Line(new float[] { 195, 100, 100, 100, 100, 195 })
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            }
        };
        graph.Shapes.Add(line);

        // Add Graph object to the paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "ExampleFilledArc_out.pdf");
    }
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