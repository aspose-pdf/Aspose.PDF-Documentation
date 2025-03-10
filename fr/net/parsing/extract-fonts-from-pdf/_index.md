---
title: Extraire des polices à partir de PDF C#
linktitle: Extraire des polices à partir de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/extract-fonts-from-pdf/
description: Utilisez la bibliothèque Aspose.PDF pour .NET pour extraire toutes les polices intégrées de votre document PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Fonts from PDF C#",
    "alternativeHeadline": "Effortlessly Extract All Fonts from PDF Documents",
    "abstract": "Déverrouillez la puissance de vos documents PDF avec la fonctionnalité de la bibliothèque Aspose.PDF for .NET qui vous permet d'extraire facilement toutes les polices intégrées. En utilisant la méthode FontUtilities.GetAllFonts(), les développeurs peuvent facilement accéder et lister les polices dans n'importe quel fichier PDF, améliorant ainsi les capacités d'analyse et de personnalisation des documents.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "156",
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
    "url": "/net/extract-fonts-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-fonts-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

Dans le cas où vous souhaitez obtenir toutes les polices d'un document PDF, vous pouvez utiliser la méthode FontUtilities.GetAllFonts() fournie dans la classe Document. Veuillez consulter le code suivant afin d'obtenir toutes les polices d'un document PDF existant :

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).
  
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractFonts.pdf"))
    {
        Aspose.Pdf.Text.Font[] fonts = document.FontUtilities.GetAllFonts();
        foreach (Aspose.Pdf.Text.Font font in fonts)
        {
            Console.WriteLine(font.FontName);
        }
    }
}
```