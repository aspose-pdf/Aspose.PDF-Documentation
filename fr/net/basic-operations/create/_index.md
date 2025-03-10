---
title: Créer un document PDF par programmation
linktitle: Créer un PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/create-document/
description: Cette page décrit comment créer un document PDF à partir de zéro avec la bibliothèque Aspose.PDF.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Creation Made Easy with C#",
    "abstract": "La nouvelle fonctionnalité dans Aspose.PDF for .NET permet aux développeurs de créer des documents PDF par programmation en utilisant C# et VB.NET, simplifiant le processus pour diverses applications .NET comme WinForms et ASP.NET. Avec des méthodes simples pour ajouter des pages et du texte, les utilisateurs peuvent générer sans effort des fichiers PDF personnalisés à partir de zéro, améliorant ainsi la fonctionnalité de leur application et l'expérience utilisateur.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "307",
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
    "url": "/net/create-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

Aspose.PDF for .NET API vous permet de créer et de lire des fichiers PDF en utilisant C# et VB.NET. L'API peut être utilisée dans une variété d'applications .NET, y compris WinForms, ASP.NET et plusieurs autres. Dans cet article, nous allons montrer comment utiliser l'API Aspose.PDF for .NET pour générer et lire facilement des fichiers PDF dans des applications .NET.

## Comment créer un fichier PDF en utilisant C#

Pour créer un fichier PDF en utilisant C#, les étapes suivantes peuvent être utilisées.

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Ajoutez un objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à la collection [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) de l'objet Document.
1. Ajoutez un [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) à la collection [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) de la page.
1. Enregistrez le document PDF résultant.

Le code suivant fonctionne également avec la bibliothèque [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

Dans ce cas, nous créons un document PDF d'une page avec une taille de page A4, orientation portrait. Notre page contiendra un "Bonjour, le monde" dans la partie supérieure gauche de la page.