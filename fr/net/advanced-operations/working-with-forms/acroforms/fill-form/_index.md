---
title: Fill AcroForm - Remplir un formulaire PDF en utilisant C#
linktitle: Fill AcroForm
type: docs
weight: 20
url: /fr/net/fill-form/
keywords: Fill PDF Form C#
description: Vous pouvez remplir des formulaires dans votre document PDF avec la bibliothèque Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Fill AcroForm",
    "alternativeHeadline": "Comment remplir AcroForm dans PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document PDF",
    "keywords": "pdf, c#, fill acroform",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
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
    "url": "/net/fill-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/fill-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Vous pouvez remplir des formulaires dans votre document PDF avec la bibliothèque Aspose.PDF pour .NET."
}
</script>
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Remplir un champ de formulaire dans un document PDF

Pour remplir un champ de formulaire, récupérez le champ de la collection Form de l'objet Document, puis définissez la valeur du champ à l'aide de la propriété Value du champ.

Cet exemple sélectionne un TextBoxField et définit sa valeur à l'aide de la propriété Value.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "FillFormField.pdf");

// Obtenir un champ
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// Modifier la valeur du champ
textBoxField.Value = "Valeur à remplir dans le champ";
dataDir = dataDir + "FillFormField_out.pdf";
// Enregistrer le document mis à jour
pdfDocument.Save(dataDir);
```

