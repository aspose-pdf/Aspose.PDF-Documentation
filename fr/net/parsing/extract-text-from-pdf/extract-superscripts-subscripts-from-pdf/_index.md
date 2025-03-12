---
title: Extraire le texte des SuperScripts et SubScripts à partir de PDF
linktitle: Extraire les SuperScripts et SubScripts
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/extract-superscripts-subscripts-from-pdf/
description: Cet article décrit diverses manières d'extraire le texte des SuperScripts et SubScripts à partir de PDF en utilisant Aspose.PDF en C#.
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract SuperScripts and SubScripts text from PDF",
    "alternativeHeadline": "Extract SuperScripts and SubScripts from PDF Documents",
    "abstract": "La nouvelle fonctionnalité d'extraction du texte des SuperScripts et SubScripts à partir des documents PDF utilisant la bibliothèque Aspose.PDF for .NET permet aux utilisateurs de récupérer avec précision le formatage de texte spécialisé trouvé dans les documents techniques. Cette amélioration simplifie le processus de gestion des expressions mathématiques et des spécifications chimiques en fournissant aux développeurs des outils pour manipuler facilement ces éléments textuels.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "323",
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
    "url": "/net/extract-superscripts-subscripts-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-superscripts-subscripts-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Extraire le texte des SuperScripts et SubScripts

L'extraction de texte à partir d'un document PDF est une chose courante. Cependant, dans ce texte, lorsqu'il est extrait, les **SuperScripts et SubScripts** qu'il contient, qui sont typiques des documents techniques et des articles, peuvent ne pas s'afficher. Un SubScript ou SuperScript est un caractère, un nombre ou une lettre placé en dessous ou au-dessus d'une ligne de texte régulière. Il est généralement plus petit que le reste du texte.

Les **SubScripts et SuperScripts** sont le plus souvent utilisés dans les formules, les expressions mathématiques et les spécifications des composés chimiques. Il est difficile de les éditer lorsqu'il peut y en avoir beaucoup dans le même passage de texte. Dans l'une des dernières versions, la bibliothèque **Aspose.PDF for .NET** a ajouté le support pour l'extraction du texte des SuperScripts et SubScripts à partir de PDF.

Utilisez la classe **TextFragmentAbsorber** et vous pouvez déjà faire tout ce que vous voulez avec le texte trouvé, c'est-à-dire que vous pouvez simplement utiliser tout le texte. Essayez le code suivant :

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScripts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            // Write the extracted text in text file
            writer.WriteLine(absorber.Text);
        }
    }
}
```

Ou utilisez les **TextFragments** séparément et faites toutes sortes de manipulations avec eux, par exemple, trier par coordonnées ou par taille.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScriptsWithTextFragments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                // Write the extracted text in text file
                writer.Write(textFragment.Text);
            }

        }
    }
}
```