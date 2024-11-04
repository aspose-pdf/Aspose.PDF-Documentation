---
title: Ajouter un objet Arc au fichier PDF
linktitle: Ajouter Arc
type: docs
weight: 10
url: /net/add-arc/
description: Cet article explique comment créer un objet arc dans votre PDF en utilisant Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter un objet Arc au fichier PDF",
    "alternativeHeadline": "Comment créer Arc dans un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, arc dans pdf",
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
    "dateModified": "2022-02-04",
    "description": "Cet article explique comment créer un objet arc dans votre PDF en utilisant Aspose.PDF pour .NET."
}
</script>
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Ajouter un objet Arc

Aspose.PDF pour .NET prend en charge la fonctionnalité d'ajouter des objets graphiques (par exemple graphique, ligne, rectangle, etc.) aux documents PDF. Il offre également la fonctionnalité de remplir un objet arc avec une certaine couleur.

Suivez les étapes ci-dessous :

1. Créer une instance [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)

1. Créer un [objet de dessin](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) avec certaines dimensions

1. Définir une [Bordure](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) pour l'objet de dessin

1. Ajouter un objet [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) à la collection de paragraphes de la page

1. Enregistrer notre fichier PDF

Le code suivant montre comment ajouter un objet [Arc](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc).

```csharp
 public static void Arc()
        {
            // Créer une instance Document
            var document = new Document();

            // Ajouter une page à la collection de pages du fichier PDF
            var page = document.Pages.Add();

            // Créer un objet de dessin avec certaines dimensions
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Définir la bordure pour l'objet de dessin
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

            // Ajouter l'objet Graph à la collection de paragraphes de la page
            page.Paragraphs.Add(graph);

            // Enregistrer le fichier PDF
            document.Save(_dataDir + "DrawingArc_out.pdf");

        }
```
## Créer un objet Arc rempli

L'exemple suivant montre comment ajouter un objet Arc qui est rempli de couleur et de certaines dimensions.

```csharp
        public static void ArcFilled()
        {
            // Créer une instance de Document
            var document = new Document();

            // Ajouter une page à la collection de pages du fichier PDF
            var page = document.Pages.Add();

            // Créer un objet de dessin avec certaines dimensions
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Définir la bordure pour l'objet de dessin
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc = new Arc(100, 100, 95, 0, 90);
            arc.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(arc);

            var line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
            line.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(line);

            // Ajouter l'objet Graph à la collection de paragraphes de la page
            page.Paragraphs.Add(graph);

            // Sauvegarder le fichier PDF
            document.Save(_dataDir + "ExampleFilledArc_out.pdf");

        }
```
Voyons le résultat de l'ajout d'un arc rempli :

![Arc rempli](filled_arc.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Bibliothèque Aspose.PDF pour .NET",
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
                "type de contact": "ventes",
                "zone desservie": "US",
                "langue disponible": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "type de contact": "ventes",
                "zone desservie": "GB",
                "langue disponible": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "type de contact": "ventes",
                "zone desservie": "AU",
                "langue disponible": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "prix": "1199",
        "devise du prix": "USD"
    },
    "catégorie d'application": "Bibliothèque de manipulation de PDF pour .NET",
    "url de téléchargement": "https://www.nuget.org/packages/Aspose.PDF/",
    "système d'exploitation": "Windows, MacOS, Linux",
    "capture d'écran": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "version du logiciel": "2022.1",
    "notation globale": {
        "@type": "Évaluation globale",
        "valeur de l'évaluation": "5",
        "nombre d'évaluations": "16"
    }
}
</script>


