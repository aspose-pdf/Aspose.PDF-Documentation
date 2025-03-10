---
title: Ajouter un objet Arc au fichier PDF
linktitle: Ajouter un Arc
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/add-arc/
description: Cet article explique comment créer un objet arc dans votre PDF en utilisant Aspose.PDF for .NET.
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
    "abstract": "La nouvelle fonctionnalité dans Aspose.PDF for .NET permet aux utilisateurs d'intégrer sans effort des objets arc dans des documents PDF, améliorant les capacités graphiques en fournissant la possibilité de dessiner des arcs dans diverses couleurs et dimensions. Cette fonctionnalité permet aux développeurs de créer des fichiers PDF plus attrayants visuellement et personnalisés en ajoutant des arcs remplis et des formes détaillées avec un contrôle précis sur des attributs tels que les bordures et les couleurs de remplissage.",
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
    "description": "Cet article explique comment créer un objet arc dans votre PDF en utilisant Aspose.PDF for .NET."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Ajouter un objet Arc

Aspose.PDF for .NET prend en charge la fonctionnalité d'ajout d'objets graphiques (par exemple graphique, ligne, rectangle, etc.) aux documents PDF. Il offre également la possibilité de remplir un objet arc avec une certaine couleur.

Suivez les étapes ci-dessous :

1. Créez une instance de [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Créez un [objet Drawing](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) avec des dimensions spécifiques.
1. Définissez la [Bordure](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) pour l'objet Drawing.
1. Ajoutez un objet [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) à la collection de paragraphes de la page.
1. Enregistrez notre fichier PDF.

Le code suivant montre comment ajouter un objet [Arc](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc).

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

## Créer un objet Arc rempli

L'exemple suivant montre comment ajouter un objet Arc qui est rempli de couleur et de dimensions spécifiques.

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

Voyons le résultat de l'ajout d'un Arc rempli :

![Arc rempli](filled_arc.png)

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