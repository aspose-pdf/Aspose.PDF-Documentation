---
title: Annotation de surlignage PDF utilisant C#
linktitle: Annotation de surlignage
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/highlights-annotation/
description: Apprenez à ajouter des annotations de surlignage aux documents PDF en .NET en utilisant Aspose.PDF pour l'accentuation et la révision du texte.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Highlight Annotation using C#",
    "alternativeHeadline": "PDF Annotations with Customizable Highlighting Options",
    "abstract": "La nouvelle fonctionnalité d'annotation de surlignage PDF utilisant C# permet aux utilisateurs d'ajouter et de personnaliser facilement des annotations de balisage de texte dans leurs documents PDF. Cette fonctionnalité comprend des options pour les surlignages, les soulignements, les barrages et les soulignements en zigzag, tous pouvant être modifiés pour la couleur, l'opacité et les métadonnées, améliorant ainsi l'interactivité et la clarté du document.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF Highlight Annotation, C#, text markup annotation, highlight settings, strikethrough settings, underline settings, add annotation, delete annotation, Aspose.PDF.Drawing, markup annotations",
    "wordcount": "958",
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
    "url": "/net/highlights-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/highlights-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Les annotations de balisage sont présentées dans le texte sous forme de surlignages, de soulignements, de barrages ou de soulignements en zigzag dans le texte d'un document."
}
</script>

Les annotations de balisage de texte apparaîtront sous forme de surlignages, de soulignements, de barrages ou de soulignements en zigzag dans le texte d'un document. Lorsqu'elles sont ouvertes, elles afficheront une fenêtre contextuelle contenant le texte de la note associée.

Les propriétés des annotations de balisage de texte dans le document PDF peuvent être modifiées à l'aide de la fenêtre des propriétés fournie dans le contrôle du visualiseur PDF. La couleur, l'opacité, l'auteur et le sujet de l'annotation de balisage de texte peuvent être modifiés.

Il est possible d'obtenir ou de définir les paramètres des annotations de surlignage à l'aide de la propriété highlightSettings. La propriété highlightSettings est utilisée pour définir les propriétés de couleur, d'opacité, d'auteur, de sujet, de date de modification et de verrouillage des annotations de surlignage.

Il est également possible d'obtenir ou de définir les paramètres des annotations de barré à l'aide de la propriété strikethroughSettings. La propriété strikethroughSettings est utilisée pour définir les propriétés de couleur, d'opacité, d'auteur, de sujet, de date de modification et de verrouillage des annotations de barré.

La fonctionnalité suivante est la possibilité d'obtenir ou de définir les paramètres des annotations de soulignement à l'aide de la propriété underlineSettings. La propriété underlineSettings est utilisée pour définir les propriétés de couleur, d'opacité, d'auteur, de sujet, de date de modification et de verrouillage des annotations de soulignement.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Ajouter une annotation de balisage de texte

Pour ajouter une annotation de balisage de texte au document PDF, nous devons effectuer les actions suivantes :

1. Charger le fichier PDF - nouvel objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Créer des annotations :
    - [HighlightAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/highlightannotation) et définir les paramètres (titre, couleur).
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) et définir les paramètres (titre, couleur).
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squigglyannotation) et définir les paramètres (titre, couleur).
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/underlineannotation) et définir les paramètres (titre, couleur).
1. Ensuite, nous devrions ajouter toutes les annotations à la page.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextMarkupAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a TextFragmentAbsorber to find the text "PDF"
        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
        tfa.Visit(document.Pages[1]);

        // Create annotations for the found text fragments
        var highlightAnnotation = new Aspose.Pdf.Annotations.HighlightAnnotation(document.Pages[1], tfa.TextFragments[1].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.LightGreen
        };

        var strikeOutAnnotation = new Aspose.Pdf.Annotations.StrikeOutAnnotation(document.Pages[1], tfa.TextFragments[2].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Blue
        };

        var squigglyAnnotation = new Aspose.Pdf.Annotations.SquigglyAnnotation(document.Pages[1], tfa.TextFragments[3].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Red
        };

        var underlineAnnotation = new Aspose.Pdf.Annotations.UnderlineAnnotation(document.Pages[1], tfa.TextFragments[4].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Violet
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(highlightAnnotation);
        document.Pages[1].Annotations.Add(squigglyAnnotation);
        document.Pages[1].Annotations.Add(strikeOutAnnotation);
        document.Pages[1].Annotations.Add(underlineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddTextMarkupAnnotations_out.pdf");
    }
}
```

Si vous souhaitez surligner un fragment multi-lignes, vous devez utiliser un exemple avancé :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHighlightAnnotationAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var page = document.Pages[1];
        var tfa = new TextFragmentAbsorber(@"Adobe\W+Acrobat\W+Reader", new TextSearchOptions(true));
        tfa.Visit(page);
        foreach (var textFragment in tfa.TextFragments)
        {
            var highlightAnnotation = HighLightTextFragment(page, textFragment, Color.Yellow);
            page.Annotations.Add(highlightAnnotation);
        }

        // Save PDF document
        document.Save(dataDir + "AddHighlightAnnotationAdvanced_out.pdf");
    }
}

private static HighlightAnnotation HighLightTextFragment(Page page,
    Aspose.Pdf.Text.TextFragment textFragment, Aspose.Pdf.Color color)
{
    if (textFragment.Segments.Count == 1)
    {
        return new Aspose.Pdf.Annotations.HighlightAnnotation(page, textFragment.Segments[1].Rectangle)
        {
            Title = "Aspose User",
            Color = color,
            Modified = DateTime.Now,
            QuadPoints = new Aspose.Pdf.Point[]
            {
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.URY),
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.URY),
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.LLY),
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.LLY)
            }
        };
    }

    var offset = 0;
    var quadPoints = new Aspose.Pdf.Point[textFragment.Segments.Count * 4];
    foreach (Aspose.Pdf.Text.TextSegment segment in textFragment.Segments)
    {
        quadPoints[offset + 0] = new Aspose.Pdf.Point(segment.Rectangle.LLX, segment.Rectangle.URY);
        quadPoints[offset + 1] = new Aspose.Pdf.Point(segment.Rectangle.URX, segment.Rectangle.URY);
        quadPoints[offset + 2] = new Aspose.Pdf.Point(segment.Rectangle.LLX, segment.Rectangle.LLY);
        quadPoints[offset + 3] = new Aspose.Pdf.Point(segment.Rectangle.URX, segment.Rectangle.LLY);
        offset += 4;
    }

    var llx = quadPoints.Min(pt => pt.X);
    var lly = quadPoints.Min(pt => pt.Y);
    var urx = quadPoints.Max(pt => pt.X);
    var ury = quadPoints.Max(pt => pt.Y);
    return new Aspose.Pdf.Annotations.HighlightAnnotation(page, new Aspose.Pdf.Rectangle(llx, lly, urx, ury))
    {
        Title = "Aspose User",
        Color = color,
        Modified = DateTime.Now,
        QuadPoints = quadPoints
    };
}

private static void GetHighlightedText()
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var highlightAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Highlight)
            .Cast<Aspose.Pdf.Annotations.HighlightAnnotation>();
        foreach (var ta in highlightAnnotations)
        {
            Console.WriteLine($"[{ta.GetMarkedText()}]");
        }
    }
}
```

## Obtenir une annotation de balisage de texte

Veuillez essayer d'utiliser le code suivant pour obtenir une annotation de balisage de texte à partir du document PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTextMarkupAnnotation()
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Highlight
            || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Squiggly)
            .Cast<Aspose.Pdf.Annotations.TextMarkupAnnotation>();
        foreach (var ta in textMarkupAnnotations)
        {
            Console.WriteLine($"[{ta.AnnotationType} {ta.Rect}]");
        }
    }
}
```

## Supprimer une annotation de balisage de texte

Le code suivant montre comment supprimer une annotation de balisage de texte d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteTextMarkupAnnotation()
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Highlight
            ||a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Squiggly)
            .Cast<Aspose.Pdf.Annotations.TextMarkupAnnotation>();
        foreach (var ta in textMarkupAnnotations)
        {
            document.Pages[1].Annotations.Delete(ta);
        }
        
        // Save PDF document
        document.Save(dataDir + "DeleteTextMarkupAnnotation_out.pdf");
    }
}
```

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