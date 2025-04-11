---
title: Remplir AcroForm - Remplir un formulaire PDF en utilisant C#
linktitle: Remplir AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/fill-form/
description: Vous pouvez remplir des formulaires dans votre document PDF avec la bibliothèque Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Fill AcroForm - Fill PDF Form using C#",
    "alternativeHeadline": "Effortlessly Fill PDF Forms with C# Integration",
    "abstract": "La nouvelle fonctionnalité Remplir AcroForm dans la bibliothèque Aspose.PDF for .NET permet aux développeurs de remplir efficacement des formulaires PDF par programmation en utilisant C#. Cette fonctionnalité rationalise le processus de remplissage des champs de formulaire, améliorant la productivité et la précision dans la gestion des documents PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Fill PDF Form, AcroForm, Aspose.PDF for .NET, fill PDF forms C#, TextBoxField, PDF document generation, form field value, PDF manipulation library, fill form field, C# PDF library",
    "wordcount": "386",
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
    "url": "/net/fill-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/fill-form/"
    },
    "dateModified": "2025-04-11",
    "description": "Vous pouvez remplir des formulaires dans votre document PDF avec la bibliothèque Aspose.PDF for .NET."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Remplir un champ de formulaire dans un document PDF

Pour remplir un champ de formulaire, obtenez le champ de la collection Form de l'objet Document et définissez sa valeur en utilisant la propriété appropriée pour le type de champ (comme Value pour les champs de texte, Checked pour les cases à cocher, ou Selected pour les listes déroulantes).

Dans cet exemple, divers champs sont sélectionnés et leurs propriétés sont définies.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillFormField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithSomeFields.pdf"))
    {
        // Set value for TextBoxField
        var textBoxField = document.Form["textField"] as Aspose.Pdf.Forms.TextBoxField;
        textBoxField.Value = "Value to be filled in the field";

        // Add option for ListBoxField and select it
        var listBoxField = document.Form["listField"] as Aspose.Pdf.Forms.ListBoxField;
        listBoxField.AddOption("Orange");
        listBoxField.Selected = listBoxField.Options.Count;

        // Set check for CheckboxField
        var checkboxField = document.Form["checkField"] as Aspose.Pdf.Forms.CheckboxField;
        checkboxField.Checked = true;

        // Set check for first option of RadioButtonField
        var radioField = document.Form["radioGroup"] as Aspose.Pdf.Forms.RadioButtonField;
        radioField.Options[1].Selected = true;

        // Save PDF document
        document.Save(dataDir + "DocumentWithSomeFields_out.pdf");
    }
}
```

{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillFormField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DocumentWithSomeFields.pdf");

    // Set value for TextBoxField
    var textBoxField = document.Form.OfType<Aspose.Pdf.Forms.TextBoxField>().First();
    textBoxField.Value = "Value to be filled in the field";

    // Add option for ListBoxField and select it
    var listBoxField = document.Form.OfType<Aspose.Pdf.Forms.ListBoxField>().First();
    listBoxField.AddOption("Orange");
    listBoxField.Selected = listBoxField.Options.Count;

    // Set check for CheckboxField
    var checkboxField = document.Form.OfType<Aspose.Pdf.Forms.CheckboxField>().First();
    checkboxField.Checked = true;

    // Set check for first option of RadioButtonField
    var radioField = document.Form.OfType<Aspose.Pdf.Forms.RadioButtonField>().First();
    radioField.Options[1].Selected = true;

    // Save PDF document
    document.Save(dataDir + "DocumentWithSomeFields_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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