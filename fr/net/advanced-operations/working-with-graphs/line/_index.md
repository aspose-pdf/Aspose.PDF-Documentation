---
title: Ajouter un objet Ligne au fichier PDF
linktitle: Ajouter une ligne
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/add-line/
description: Cet article explique comment créer un objet ligne dans votre PDF en utilisant Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Line Object to PDF file",
    "alternativeHeadline": "Enhance PDFs with Custom Line Objects Using .NET",
    "abstract": "Améliorez vos documents PDF en ajoutant sans effort des objets ligne avec Aspose.PDF for .NET. Cette nouvelle fonctionnalité permet un contrôle précis sur les attributs de ligne, y compris les motifs de tirets et les couleurs, permettant aux utilisateurs de créer des représentations graphiques visuellement attrayantes dans leurs fichiers PDF. Découvrez comment mettre en œuvre cette fonctionnalité facilement avec des exemples de code complets et des instructions claires étape par étape.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Line Object, PDF manipulation, Aspose.PDF for .NET, Line object, Drawing in PDF, Graph object, Rectangle in PDF, Dotted Dashed Line, Draw Line Across the Page, PDF document generation",
    "wordcount": "729",
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
    "url": "/net/add-line/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-line/"
    },
    "dateModified": "2024-11-25",
    "description": "Cet article explique comment créer un objet ligne dans votre PDF en utilisant Aspose.PDF for .NET."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Ajouter un objet Ligne

Aspose.PDF for .NET prend en charge la fonctionnalité d'ajout d'objets graphiques (par exemple graphique, ligne, rectangle, etc.) aux documents PDF. Vous avez également la possibilité d'ajouter un objet [Ligne](https://reference.aspose.com/pdf/fr/net/aspose.pdf.drawing/line) où vous pouvez également spécifier le motif de tirets, la couleur et d'autres formats pour l'élément Ligne.

Suivez les étapes ci-dessous :

1. Créez un nouveau [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document) PDF.
1. Ajoutez une [Page](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page) à la collection de pages du fichier PDF.
1. Créez une instance de [Graph](https://reference.aspose.com/pdf/fr/net/aspose.pdf.drawing/graph).
1. Ajoutez l'objet Graph à la collection de paragraphes de l'instance de page.
1. Créez une instance de [Rectangle](https://reference.aspose.com/pdf/fr/net/aspose.pdf.drawing/rectangle).
1. Définissez la largeur de ligne.
1. Ajoutez l'objet [Rectangle](https://reference.aspose.com/pdf/fr/net/aspose.pdf.drawing/rectangle) à la collection de formes de l'objet Graph.

1. Enregistrez votre fichier PDF.

Le code suivant montre comment ajouter un objet [Rectangle](https://reference.aspose.com/pdf/fr/net/aspose.pdf.drawing/rectangle) qui est rempli de couleur.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineObjectToPDF()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Line instance with specified coordinates
        var line = new Aspose.Pdf.Drawing.Line(new float[] { 100, 100, 200, 100 });

        // Specify dash settings for the line
        line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
        line.GraphInfo.DashPhase = 1;

        // Add line object to shapes collection of Graph object
        graph.Shapes.Add(line);

        // Save PDF document
        document.Save(dataDir + "AddLineObject_out.pdf");
    }
}
```

![Ajouter une ligne](add_line.png)

## Comment ajouter une ligne pointillée à votre document PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DashLengthInBlackAndDashLengthInWhite()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Drawing object with certain dimensions
        var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add drawing object to paragraphs collection of page instance
        page.Paragraphs.Add(canvas);

        // Create Line object
        var line = new Aspose.Pdf.Drawing.Line(new float[] { 100, 100, 200, 100 });

        // Set color for Line object
        line.GraphInfo.Color = Aspose.Pdf.Color.Red;

        // Specify dash array for line object
        line.GraphInfo.DashArray = new int[] { 3, 2 }; // Dash and gap lengths in points

        // Set the dash phase for Line instance
        line.GraphInfo.DashPhase = 1;

        // Add line to shapes collection of drawing object
        canvas.Shapes.Add(line);

        // Save PDF document
        document.Save(dataDir + "DashLengthInBlackAndDashLengthInWhite_out.pdf");
    }
}
```

Vérifions le résultat :

![Ligne pointillée](dash_line.png)

## Dessiner une ligne à travers la page

Nous pouvons également utiliser l'objet ligne pour dessiner une croix partant du coin inférieur gauche au coin supérieur droit et du coin supérieur gauche au coin inférieur droit.

Veuillez consulter le code suivant pour réaliser cette exigence.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleLineAcrossPage()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Set page margin on all sides as 0
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;

        // Create Graph object with Width and Height equal to page dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(
            (float)page.PageInfo.Width,
            (float)page.PageInfo.Height);

        // Create first line object starting from Lower-Left to Top-Right corner of page
        var line1 = new Aspose.Pdf.Drawing.Line(new float[]
        {
            (float)page.Rect.LLX, 0,
            (float)page.PageInfo.Width,
            (float)page.Rect.URY
        });

        // Add line to shapes collection of Graph object
        graph.Shapes.Add(line1);

        // Create second line object starting from Top-Left corner to Bottom-Right corner of page
        var line2 = new Aspose.Pdf.Drawing.Line(new float[]
        {
            0, (float)page.Rect.URY,
            (float)page.PageInfo.Width, (float)page.Rect.LLX
        });

        // Add line to shapes collection of Graph object
        graph.Shapes.Add(line2);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "ExampleLineAcrossPage_out.pdf");
    }
}
```

![Dessin de ligne](draw_line.png)

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