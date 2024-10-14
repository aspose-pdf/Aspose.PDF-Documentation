---
title: Ajouter un objet courbe au fichier PDF
linktitle: Ajouter une courbe
type: docs
weight: 30
url: /net/add-curve/
description: Cet article explique comment créer un objet courbe dans votre PDF en utilisant Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter un objet courbe au fichier PDF",
    "alternativeHeadline": "Comment créer un objet courbe dans un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document PDF",
    "keywords": "pdf, .net, courbe dans pdf",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article explique comment créer un objet courbe dans votre PDF en utilisant Aspose.PDF pour .NET."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Ajouter un objet Curve

Un graphique [Curve](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve) est une union connectée de lignes projectives, chaque ligne rencontrant trois autres en points doubles ordinaires.

Aspose.PDF pour .NET montre comment utiliser les courbes de Bézier dans vos graphiques.
Les courbes de Bézier sont largement utilisées en infographie pour modéliser des courbes lisses. La courbe est entièrement contenue dans l'enveloppe convexe de ses points de contrôle, les points peuvent être affichés graphiquement et utilisés pour manipuler la courbe de manière intuitive.
La courbe entière est contenue dans le quadrilatère dont les coins sont les quatre points donnés (leur enveloppe convexe).

Dans cet article, nous allons examiner simplement les courbes graphiques, et les courbes remplies, que vous pouvez créer dans votre document PDF.

Suivez les étapes ci-dessous :

1. Créez une instance [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Définir un [Bord](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) pour l'objet Drawing

1. Ajouter un objet [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) à la collection de paragraphes de la page

1. Enregistrer notre fichier PDF

```csharp
 public static void ExampleCurve()
        {
            // Créer une instance de Document
            var document = new Document();

            // Ajouter une page à la collection de pages du fichier PDF
            var page = document.Pages.Add();

            // Créer un objet Drawing avec certaines dimensions
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Définir le bord pour l'objet Drawing
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Ajouter l'objet Graph à la collection de paragraphes de la page
            page.Paragraphs.Add(graph);

            // Enregistrer le fichier PDF
            document.Save(_dataDir + "DrawingCurve1_out.pdf");
        }
```
L'image suivante montre le résultat exécuté avec notre extrait de code :

![Dessin Courbe](drawing_curve.png)

## Créer un Objet Courbe Rempli

Cet exemple montre comment ajouter un objet Courbe qui est rempli de couleur.

```csharp
      public static void CurveFilled()
        {
            // Créer une instance de Document
            var document = new Document();

            // Ajouter une page à la collection de pages du fichier PDF
            var page = document.Pages.Add();

            // Créer un objet Dessin avec certaines dimensions
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Définir la bordure pour l'objet Dessin
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Ajouter l'objet Graph à la collection de paragraphes de la page
            page.Paragraphs.Add(graph);

            // Enregistrer le fichier PDF
            document.Save(_dataDir + "DrawingCurve2_out.pdf");
        }
```
Regardez le résultat de l'ajout d'une courbe remplie :

![Courbe Remplie](filled_curve.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour la bibliothèque .NET",
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

