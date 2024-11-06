---
title: Annotation de surbrillance PDF en utilisant C#
linktitle: Annotation de surbrillance
type: docs
weight: 20
url: fr/net/highlights-annotation/
description: Les annotations de balisage sont présentées dans le texte sous forme de surlignages, de soulignements, de barrages ou de soulignements irréguliers dans le texte d'un document.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Annotation de surbrillance PDF en utilisant C#",
    "alternativeHeadline": "Comment ajouter une annotation de surbrillance dans PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, annotation de surbrillance, annotation de balisage de texte",
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
    "url": "/net/highlights-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/highlights-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Les annotations de balisage sont présentées dans le texte sous forme de surlignages, de soulignements, de barrages ou de soulignements irréguliers dans le texte d'un document."
}
</script>
Les annotations de balisage de texte apparaîtront comme des surlignages, des soulignements, des barrés ou des soulignements irréguliers (« ondulés ») dans le texte d'un document. Lorsqu'elles sont ouvertes, elles afficheront une fenêtre contextuelle contenant le texte de la note associée.

Les propriétés des annotations de balisage de texte dans le document PDF peuvent être modifiées en utilisant la fenêtre des propriétés fournie dans le contrôle de visualisation PDF. La couleur, l'opacité, l'auteur et le sujet de l'annotation de balisage de texte peuvent être modifiés.

Il est possible d'obtenir ou de définir les paramètres des annotations de surlignage à l'aide de la propriété highlightSettings. La propriété highlightSettings est utilisée pour définir la couleur, l'opacité, l'auteur, le sujet, la date de modification et les propriétés isLocked des annotations de surlignage.

Il est également possible d'obtenir ou de définir les paramètres des annotations de barré à l'aide de la propriété strikethroughSettings. La propriété strikethroughSettings est utilisée pour définir la couleur, l'opacité, l'auteur, le sujet, la date de modification et les propriétés isLocked des annotations de barré.

La prochaine fonctionnalité est la possibilité d'obtenir ou de définir les paramètres des annotations de soulignement à l'aide de la propriété underlineSettings.
La prochaine fonctionnalité est la capacité d'obtenir ou de définir les paramètres des annotations de soulignement en utilisant la propriété underlineSettings.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Ajouter une annotation de balisage de texte

Pour ajouter une annotation de balisage de texte au document PDF, nous devons effectuer les actions suivantes :

1. Charger le fichier PDF - nouvel objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Créer des annotations :
    - [HighlightAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/highlightannotation) et définir les paramètres (titre, couleur).
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) et définir les paramètres (titre, couleur).
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squigglyannotation) et définir les paramètres (titre, couleur).
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/underlineannotation) et définir les paramètres (titre, couleur).
- [UnderlineAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/underlineannotation) et définir les paramètres (titre, couleur).
1. Après, nous devrions ajouter toutes les annotations à la page.

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Text;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleTextMarkupAnnotation
    {
        // Le chemin vers le répertoire des documents.
        private const string _dataDir = "..\\..\\..\\..\\Samples";

        public static void AddTextMarkupAnnotation()
        {
            try
            {
                // Charger le fichier PDF
                Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
                var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
                tfa.Visit(document.Pages[1]);

                // Créer des annotations
                HighlightAnnotation highlightAnnotation = new HighlightAnnotation(document.Pages[1],
                   tfa.TextFragments[1].Rectangle )
                {
                    Title = "Utilisateur Aspose",
                    Color = Color.LightGreen
                };

                StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                   document.Pages[1],
                   tfa.TextFragments[2].Rectangle)
                {
                    Title = "Utilisateur Aspose",
                    Color = Color.Blue
                };
                SquigglyAnnotation squigglyAnnotation = new SquigglyAnnotation(document.Pages[1],
                    tfa.TextFragments[3].Rectangle)
                {
                    Title = "Utilisateur Aspose",
                    Color = Color.Red
                };
                UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(document.Pages[1],
                    tfa.TextFragments[4].Rectangle)
                {
                    Title = "Utilisateur Aspose",
                    Color = Color.Violet
                };
                // Ajouter l'annotation à la page
                document.Pages[1].Annotations.Add(highlightAnnotation);
                document.Pages[1].Annotations.Add(squigglyAnnotation);
                document.Pages[1].Annotations.Add(strikeOutAnnotation);
                document.Pages[1].Annotations.Add(underlineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
Si vous souhaitez mettre en évidence un fragment sur plusieurs lignes, vous devriez utiliser l'exemple avancé :

```csharp
        /// <summary>
        /// Exemple avancé si vous souhaitez mettre en évidence un fragment sur plusieurs lignes
        /// </summary>
        public static void AddHighlightAnnotationAdvanced()
        {
            var document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            var page = document.Pages[1];
            var tfa = new TextFragmentAbsorber(@"Adobe\W+Acrobat\W+Reader", new TextSearchOptions(true));
            tfa.Visit(page);
            foreach (var textFragment in tfa.TextFragments)
            {
                var highlightAnnotation = HighLightTextFragment(page, textFragment, Color.Yellow);
                page.Annotations.Add(highlightAnnotation);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
        }
        private static HighlightAnnotation HighLightTextFragment(Aspose.Pdf.Page page,
            TextFragment textFragment, Color color)
        {
            if (textFragment.Segments.Count == 1)
                return new HighlightAnnotation(page, textFragment.Segments[1].Rectangle)
                {
                    Title = "Utilisateur Aspose",
                    Color = color,
                    Modified = DateTime.Now,
                    QuadPoints = new Point[]
                    {
                        new Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.URY),
                        new Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.URY),
                        new Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.LLY),
                        new Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.LLY)
                    }
                };

            var offset = 0;
            var quadPoints = new Point[textFragment.Segments.Count * 4];
            foreach (var segment in textFragment.Segments)
            {
                quadPoints[offset + 0] = new Point(segment.Rectangle.LLX, segment.Rectangle.URY);
                quadPoints[offset + 1] = new Point(segment.Rectangle.URX, segment.Rectangle.URY);
                quadPoints[offset + 2] = new Point(segment.Rectangle.LLX, segment.Rectangle.LLY);
                quadPoints[offset + 3] = new Point(segment.Rectangle.URX, segment.Rectangle.LLY);
                offset += 4;
            }

            var llx = quadPoints.Min(pt => pt.X);
            var lly = quadPoints.Min(pt => pt.Y);
            var urx = quadPoints.Max(pt => pt.X);
            var ury = quadPoints.Max(pt => pt.Y);
            return new HighlightAnnotation(page, new Rectangle(llx, lly, urx, ury))
            {
                Title = "Utilisateur Aspose",
                Color = color,
                Modified = DateTime.Now,
                QuadPoints = quadPoints
            };
        }

        /// <summary>
        /// Comment obtenir un texte en surbrillance
        /// </summary>
        public static void GetHighlightedText()
        {
            // Charger le fichier PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
            var highlightAnnotations = document.Pages[1].Annotations
                .Where(a => a.AnnotationType == AnnotationType.Highlight)
                .Cast<HighlightAnnotation>();
            foreach (var ta in highlightAnnotations)
            {
                Console.WriteLine($"[{ta.GetMarkedText()}]");
            }
        }
```
## Obtenir l'annotation de balisage de texte

Veuillez essayer d'utiliser le code suivant pour obtenir l'annotation de balisage de texte d'un document PDF.

```csharp
    public static void GetTextMarkupAnnotation()
    {
        // Charger le fichier PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == AnnotationType.Highlight
            || a.AnnotationType == AnnotationType.Squiggly)
            .Cast<TextMarkupAnnotation>();
            foreach (var ta in textMarkupAnnotations)
            {
                Console.WriteLine($"[{ta.AnnotationType} {ta.Rect}]");
            }
    }
```

## Supprimer l'annotation de balisage de texte

Le code suivant montre comment supprimer l'annotation de balisage de texte d'un fichier PDF.

```csharp
    public static void DeleteTextMarkupAnnotation()
    {
        // Charger le fichier PDF
        Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_mod.pdf"));
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == AnnotationType.Highlight
            ||a.AnnotationType == AnnotationType.Squiggly)
            .Cast<TextMarkupAnnotation>();
            foreach (var ta in textMarkupAnnotations)
            {
            document.Pages[1].Annotations.Delete(ta);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "sample_del.pdf"));
    }
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour .NET Library",
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
```

