---
title: Ajouter un objet Ellipse au fichier PDF
linktitle: Ajouter Ellipse
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /fr/net/add-ellipse/
description: Cet article explique comment créer un objet Ellipse dans votre PDF en utilisant Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Ellipse Object to PDF file",
    "alternativeHeadline": "Add Ellipse Objects in PDF Files Effortlessly",
    "abstract": "Présentation de la nouvelle fonctionnalité d'objet Ellipse pour Aspose.PDF en .NET, qui permet aux développeurs d'incorporer sans effort des formes elliptiques dans leurs documents PDF. Cette fonctionnalité prend en charge l'ajout d'ellipses remplies et même de texte à l'intérieur des formes, améliorant la présentation visuelle et la personnalisation des fichiers PDF. Optimisez votre génération de documents avec des éléments graphiques riches qui augmentent l'engagement des utilisateurs.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Ellipse, PDF manipulation, Aspose.PDF for .NET, create ellipse object, filled ellipse, text inside ellipse, drawing object, color fill, PDF document generation",
    "wordcount": "541",
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
    "url": "/net/add-ellipse/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-ellipse/"
    },
    "dateModified": "2024-11-25",
    "description": "Cet article explique comment créer un objet Ellipse dans votre PDF en utilisant Aspose.PDF for .NET."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Ajouter un objet Ellipse

Aspose.PDF for .NET prend en charge l'ajout d'objets [Ellipse](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) aux documents PDF. Il offre également la fonctionnalité de remplir un objet ellipse avec une certaine couleur.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Ellipse()
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

        // Create first ellipse with specified coordinates and radii
        var ellipse1 = new Aspose.Pdf.Drawing.Ellipse(150, 100, 120, 60)
        {
            GraphInfo = { Color = Aspose.Pdf.Color.GreenYellow },
            Text = new Aspose.Pdf.Text.TextFragment("Ellipse")
        };
        graph.Shapes.Add(ellipse1);

        // Create second ellipse with different dimensions and color
        var ellipse2 = new Aspose.Pdf.Drawing.Ellipse(50, 50, 18, 300)
        {
            GraphInfo = { Color = Aspose.Pdf.Color.DarkRed }
        };
        graph.Shapes.Add(ellipse2);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingEllipse_out.pdf");
    }
}
```

![Ajouter Ellipse](ellipse.png)

## Créer un objet Ellipse rempli

Le code suivant montre comment ajouter un objet [Ellipse](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) qui est rempli de couleur.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EllipseFilled()
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

        // Create first ellipse and set its fill color
        var ellipse1 = new Aspose.Pdf.Drawing.Ellipse(100, 100, 120, 180)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            }
        };
        graph.Shapes.Add(ellipse1);

        // Create second ellipse and set its fill color
        var ellipse2 = new Aspose.Pdf.Drawing.Ellipse(200, 150, 180, 120)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.DarkRed 
            }
        };
        graph.Shapes.Add(ellipse2);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingEllipse_out.pdf");
    }
}
```

![Ellipse remplie](fill_ellipse.png)

## Ajouter du texte à l'intérieur de l'Ellipse

Aspose.PDF for .NET prend en charge l'ajout de texte à l'intérieur de l'objet Graph. La propriété texte de l'objet Graph offre l'option de définir le texte de l'objet Graph. Le code suivant montre comment ajouter du texte à l'intérieur d'un objet Rectangle.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EllipseWithText()
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

        // Create TextFragment for adding text to shapes
        var textFragment = new Aspose.Pdf.Text.TextFragment("Ellipse")
        {
            TextState =
            {
                Font = Aspose.Pdf.Text.FontRepository.FindFont("Helvetica"),
                FontSize = 24
            }
        };

        // Create first ellipse and set properties
        var ellipse1 = new Aspose.Pdf.Drawing.Ellipse(100, 100, 120, 180)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.GreenYellow 
            },
            Text = textFragment
        };
        graph.Shapes.Add(ellipse1);

        // Create second ellipse and set properties
        var ellipse2 = new Aspose.Pdf.Drawing.Ellipse(200, 150, 180, 120)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.DarkRed 
            },
            Text = textFragment
        };
        graph.Shapes.Add(ellipse2);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingEllipseText_out.pdf");
    }
}
 ```

![Texte à l'intérieur de l'Ellipse](text_ellipse.png)

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