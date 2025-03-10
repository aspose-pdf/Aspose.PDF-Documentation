---
title: Utilisation des annotations de lien dans PDF
linktitle: Annotations de lien
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /fr/net/link-annotations/
description: Aspose.PDF for .NET vous permet d'ajouter, d'obtenir et de supprimer des annotations de lien de votre document PDF.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Link Annotation for PDF",
    "alternativeHeadline": "How to add Link Annotation in PDF",
    "abstract": "Aspose.PDF for .NET introduit des capacités robustes pour gérer les annotations de lien dans les documents PDF, permettant aux utilisateurs d'ajouter, de récupérer et de supprimer des hyperliens sans effort. Cette fonctionnalité améliore l'interactivité des documents en permettant aux liens d'ouvrir des pages spécifiques, des fichiers externes ou des URL web, tous personnalisables avec divers styles et actions. Débloquez de nouvelles possibilités pour la navigation PDF et l'engagement des utilisateurs avec cette puissante fonctionnalité d'annotation.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, text annotation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET vous permet d'ajouter, d'obtenir et de supprimer des annotations de texte de votre document PDF."
}
</script>

## Ajout d'une annotation de lien dans un fichier PDF existant

> Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Une [annotation de lien](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) représente un hyperlien, une destination ailleurs et un document. Selon la norme PDF, l'annotation de lien peut être utilisée dans trois cas : ouvrir la vue de page, ouvrir un fichier et ouvrir une page web.

### Utilisation de l'annotation de lien pour ouvrir la vue de page

Plusieurs étapes supplémentaires ont été effectuées pour créer l'annotation. Nous avons utilisé 2 TextFragmentAbsorbers pour trouver des fragments à démontrer. Le premier est pour le texte de l'annotation de lien, et le second indique certains endroits dans le document.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Link Annotation Demo.pdf"))
    {
        // Get first page
        var page = document.Pages[1];

        // Define regular expressions for text fragments
        var regEx1 = new Regex(@"Link Annotation Demo \d");
        var regEx2 = new Regex(@"Sample text \d");

        // Create TextFragmentAbsorber for the first regular expression
        var textFragmentAbsorber1 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx1);
        textFragmentAbsorber1.Visit(document);

        // Create TextFragmentAbsorber for the second regular expression
        var textFragmentAbsorber2 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx2);
        textFragmentAbsorber2.Visit(document);

        // Get the text fragments for both absorbers
        var linkFragments = textFragmentAbsorber1.TextFragments;
        var sampleTextFragments = textFragmentAbsorber2.TextFragments;

        // Create a LinkAnnotation
        var linkAnnotation1 = new Aspose.Pdf.Annotations.LinkAnnotation(page, linkFragments[1].Rectangle)
        {
            Action = new Aspose.Pdf.Annotations.GoToAction(
                new Aspose.Pdf.Annotations.XYZExplicitDestination(
                    sampleTextFragments[1].Page,
                    sampleTextFragments[1].Rectangle.LLX,
                    sampleTextFragments[1].Rectangle.URX, 1.5))
        };

        // Add the link annotation to the page
        page.Annotations.Add(linkAnnotation1);

        // Save PDF document
        document.Save(dataDir + "AddLinkAnnotation_out.pdf");
    }
}
```

Pour créer l'annotation, nous avons suivi certaines étapes :

1. Créer `LinkAnnotation` et passer l'objet de page et le rectangle du fragment de texte qui correspond à l'annotation.
1. Définir `Action` comme `GoToAction` et passer `XYZExplicitDestination` comme destination souhaitée. Nous avons créé `XYZExplicitDestination` basé sur la page, les coordonnées gauche et haut et le zoom.
1. Ajouter l'annotation à la collection d'annotations de la page.
1. Enregistrer le document.

### Utilisation de l'annotation de lien avec une destination nommée

Lors du traitement de divers documents, une situation se présente lorsque vous tapez et ne savez pas où l'annotation pointera. Dans ce cas, vous pouvez utiliser une destination spéciale (nommée) et le code ressemblera à ceci :

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

À un autre endroit, vous pouvez créer une destination nommée.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```

### Utilisation de l'annotation de lien pour ouvrir un fichier

La même approche est utilisée lors de la création d'une annotation pour ouvrir un fichier, comme dans les exemples ci-dessus.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

La différence est que nous utiliserons `GoToRemoteAction` au lieu de `GoToAction`. Le constructeur de GoToRemoteAction prend deux paramètres : le nom du fichier et le numéro de page. Vous pouvez également utiliser une autre forme et passer le nom du fichier et une destination. Évidemment, vous devez créer une telle destination avant de l'utiliser.

### Utilisation de l'annotation de lien pour ouvrir une page web

Pour ouvrir une page web, il suffit de définir `Action` avec l'objet `GoToURIAction`. Vous pouvez passer un hyperlien comme paramètre du constructeur ou tout autre type d'URI. Par exemple, vous pouvez utiliser `callto` pour implémenter une action avec un numéro de téléphone.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Create Link Annotation and set the action to call a phone number
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```

## Ajout d'une annotation de lien décorée

Vous pouvez personnaliser l'annotation de lien en utilisant des bordures. Dans l'exemple ci-dessous, nous allons créer une bordure bleue en pointillés de 3pt de largeur.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

Un autre exemple montre comment simuler le style d'un navigateur et utiliser le soulignement pour les liens.

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### Obtenir des annotations de lien

Veuillez essayer d'utiliser le code suivant pour obtenir l'annotation de lien à partir du document PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Get all Link annotations from the first page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        // Iterate through each Link annotation
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);

            // Create a TextAbsorber to extract text within the annotation's rectangle
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;

            // Accept the absorber for the first page
            document.Pages[1].Accept(absorber);

            // Extract and print the text associated with the hyperlink
            string extractedText = absorber.Text;
            Console.WriteLine(extractedText);
        }
    }
}
```

### Supprimer des annotations de lien

Le code suivant montre comment supprimer une annotation de lien d'un fichier PDF. Pour cela, nous devons trouver et supprimer toutes les annotations de lien sur la première page. Après cela, nous enregistrerons le document avec l'annotation supprimée.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Find and delete all link annotations on the 1st page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        foreach (var la in linkAnnotations)
        {
            document.Pages[1].Annotations.Delete(la);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteLinkAnnotations_out.pdf");
    }
}
```