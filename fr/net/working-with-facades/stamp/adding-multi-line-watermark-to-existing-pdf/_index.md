---
title: Ajouter un filigrane multi-lignes
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/adding-multi-line-watermark-to-existing-pdf/
description: Cette section explique comment ajouter un filigrane multi-lignes à un PDF existant en utilisant la classe FormattedText.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding multi line watermark",
    "alternativeHeadline": "Enhance PDFs with Multi-Line Watermarks Easily",
    "abstract": "Présentation de la possibilité d'ajouter des filigranes multi-lignes à des PDF existants en utilisant l'espace de noms Aspose.Pdf.Facades. Cette nouvelle fonctionnalité simplifie le processus, permettant aux utilisateurs d'incorporer facilement plusieurs lignes de texte dans leurs documents grâce à la méthode AddNewLineText() nouvellement implémentée dans la classe FormattedText. Améliorez vos présentations PDF avec des filigranes multi-lignes personnalisés sans effort.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "188",
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
    "url": "/net/adding-multi-line-watermark-to-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-multi-line-watermark-to-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

{{% alert color="primary" %}}

Beaucoup d'utilisateurs souhaitent tamponner leurs documents PDF avec du texte multi-lignes. Ils essaient généralement d'utiliser `\n` et `<br>` mais ces types de caractères ne sont pas pris en charge par l'espace de noms Aspose.Pdf.Facades. Donc, pour rendre cela possible, nous avons ajouté une autre méthode nommée [AddNewLineText()](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index) dans la classe [FormattedText](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formattedtext) de l'espace de noms Aspose.Pdf.Facades.

{{% /alert %}}

## Détails de mise en œuvre

Veuillez vous référer au bloc de code suivant pour ajouter un filigrane multi-lignes dans un PDF existant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampToPdf()
{
    // Instantiate a stamp object
    var logoStamp = new Aspose.Pdf.Facades.Stamp();

    // Instantiate an object of FormattedText class
    var formatText = new Aspose.Pdf.Facades.FormattedText("Hello World!",
        System.Drawing.Color.FromArgb(180, 0, 0), 
        Aspose.Pdf.Facades.FontStyle.TimesItalic,
        Aspose.Pdf.Facades.EncodingType.Winansi, false, 50);

    // Add another line for Stamp
    formatText.AddNewLineText("Good Luck");
    // BindLogo to PDF
    logoStamp.BindLogo(formatText);
}
```