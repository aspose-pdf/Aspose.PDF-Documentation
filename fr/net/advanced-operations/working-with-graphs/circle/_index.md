---
title: Ajouter un objet cercle au fichier PDF
linktitle: Ajouter un cercle
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/add-circle/
description: Cet article explique comment créer un objet cercle dans votre PDF en utilisant Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Circle Object to PDF file",
    "alternativeHeadline": "Add Interactive Circle Objects in PDFs with Ease",
    "abstract": "La nouvelle fonctionnalité de Aspose.PDF for .NET permet aux utilisateurs de créer sans effort des objets cercles dans les fichiers PDF. Cette fonctionnalité améliore la visualisation des données en permettant l'ajout de graphiques cercles réguliers et remplis, offrant aux développeurs un moyen intuitif de représenter graphiquement des informations dans leurs documents.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Circle Object, Circle in PDF, Aspose.PDF for .NET, PDF document generation, Create filled Circle, Graph object, PDF file manipulation, C# PDF library",
    "wordcount": "441",
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
    "url": "/net/add-circle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-circle/"
    },
    "dateModified": "2024-11-25",
    "description": "Cet article explique comment créer un objet cercle dans votre PDF en utilisant Aspose.PDF for .NET."
}
</script>

Le code ci-dessous fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Ajouter un objet cercle

Comme les graphiques à barres, les graphiques circulaires peuvent être utilisés pour afficher des données dans plusieurs catégories distinctes. Contrairement aux graphiques à barres, cependant, les graphiques circulaires ne peuvent être utilisés que lorsque vous avez des données pour toutes les catégories qui composent l'ensemble. Voyons donc comment ajouter un objet [Cercle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/circle) avec Aspose.PDF for .NET.

Suivez les étapes ci-dessous :

1. Créez une instance de [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Créez un [objet de dessin](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) avec certaines dimensions.
1. Définissez la [bordure](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) pour l'objet de dessin.
1. Ajoutez un objet [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) à la collection de paragraphes de la page.
1. Enregistrez notre fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Circle()
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

        // Create a circle with the specified coordinates and radius
        var circle = new Aspose.Pdf.Drawing.Circle(100, 100, 40);

        // Set the circle's color
        circle.GraphInfo.Color = Aspose.Pdf.Color.GreenYellow;

        // Add the circle to the graph shapes
        graph.Shapes.Add(circle);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCircle1_out.pdf");
    }
}
```

Notre cercle dessiné ressemblera à ceci :

![Dessin d'un cercle](drawing_circle.png)

## Créer un objet cercle rempli

Cet exemple montre comment ajouter un objet Cercle qui est rempli de couleur.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CircleFilled()
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

        // Create a filled circle
        var circle = new Aspose.Pdf.Drawing.Circle(100, 100, 40)
        {
            GraphInfo = 
            { 
                Color = Aspose.Pdf.Color.GreenYellow, 
                FillColor = Aspose.Pdf.Color.Green 
            },
            Text = new Aspose.Pdf.Text.TextFragment("Circle")
        };

        // Add the circle to the graph shapes
        graph.Shapes.Add(circle);

        // Add Graph object to paragraphs collection of page
        page.Paragraphs.Add(graph);

        // Save PDF document
        document.Save(dataDir + "DrawingCircle2_out.pdf");
    }
}
```

Voyons le résultat de l'ajout d'un cercle rempli :

![Cercle rempli](filled_circle.png)

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