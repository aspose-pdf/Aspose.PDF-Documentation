---
title: Ajouter un objet cercle au fichier PDF
linktitle: Ajouter un cercle
type: docs
weight: 20
url: /fr/net/add-circle/
description: Cet article explique comment créer un objet cercle dans votre PDF en utilisant Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter un objet cercle au fichier PDF",
    "alternativeHeadline": "Comment créer un objet cercle dans un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, cercle dans pdf",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "description": "Cet article explique comment créer un objet cercle dans votre PDF en utilisant Aspose.PDF pour .NET."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Ajouter un objet Cercle

Comme les graphiques en barres, les graphiques circulaires peuvent être utilisés pour afficher des données dans un certain nombre de catégories distinctes. Contrairement aux graphiques en barres, cependant, les graphiques circulaires ne peuvent être utilisés que lorsque vous avez des données pour toutes les catégories qui composent l'ensemble. Alors, regardons comment ajouter un objet [Cercle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/circle) avec Aspose.PDF pour .NET.

Suivez les étapes ci-dessous :

1. Créer une instance [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Créer un [objet de dessin](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) avec certaines dimensions

1. Définir une [Bordure](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) pour l'objet de dessin

1. Ajouter un objet [Graphique](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) à la collection de paragraphes de la page

1. Sauvegarder notre fichier PDF

```csharp
        public static void Circle()
        {
            // Créer une instance Document
            var document = new Document();

            // Ajouter une page à la collection de pages du fichier PDF
            var page = document.Pages.Add();

            // Créer un objet de dessin avec certaines dimensions
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);
            // Définir une bordure pour l'objet de dessin
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);

            circle.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(circle);

            // Ajouter l'objet Graphique à la collection de paragraphes de la page
            page.Paragraphs.Add(graph);

            // Sauvegarder le fichier PDF
            document.Save(_dataDir + "DrawingCircle1_out.pdf");
        }
```
Notre cercle dessiné ressemblera à ceci :

![Dessin Cercle](drawing_circle.png)

## Créer un objet Cercle rempli

Cet exemple montre comment ajouter un objet Cercle qui est rempli de couleur.

```csharp
        public static void CircleFilled()
        {
            // Créer une instance de Document
            var document = new Document();

            // Ajouter une page à la collection de pages du fichier PDF
            var page = document.Pages.Add();

            // Créer un objet Dessin avec certaines dimensions
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Définir une bordure pour l'objet Dessin
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);
            circle.GraphInfo.Color = Color.GreenYellow;
            circle.GraphInfo.FillColor = Color.Green;
            circle.Text = new TextFragment("Cercle");

            graph.Shapes.Add(circle);

            // Ajouter l'objet Graph à la collection de paragraphes de la page
            page.Paragraphs.Add(graph);

            // Sauvegarder le fichier PDF
            document.Save(_dataDir + "DrawingCircle2_out.pdf");
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
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
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


