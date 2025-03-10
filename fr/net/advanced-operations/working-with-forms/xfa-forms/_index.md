---
title: Travailler avec des formulaires XFA
linktitle: Formulaires XFA
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/xfa-forms/
description: Aspose.PDF for .NET API vous permet de travailler avec des champs XFA et XFA Acroform dans un document PDF. Le Aspose.Pdf.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with XFA Forms",
    "alternativeHeadline": "Enhance PDF handling with XFA form support",
    "abstract": "Aspose.PDF for .NET offre désormais des capacités avancées pour travailler avec des formulaires XFA, permettant aux développeurs de remplir, convertir et gérer des champs XFA Acroform dans des documents PDF. Cette fonctionnalité simplifie la manipulation des formulaires dynamiques, permettant un accès fluide aux valeurs et propriétés des champs tout en fournissant une conversion efficace de XFA à AcroForms standard. Améliorez votre flux de travail de traitement PDF avec cette solution robuste pour gérer des structures de formulaires complexes",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "XFA Forms, Aspose.PDF for .NET, fill XFA form, convert XFA to Acroform, get XFA field properties, dynamic forms, XML Forms Architecture, manipulate XFA fields, AcroForm fields, PDF document generation",
    "wordcount": "684",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET API vous permet de travailler avec des champs XFA et XFA Acroform dans un document PDF. Le Aspose.Pdf.Facades."
}
</script>

{{% alert color="primary" %}}

Les formulaires dynamiques sont basés sur une spécification XML connue sous le nom de XFA, l'« Architecture des formulaires XML ». Il peut également convertir un formulaire XFA dynamique en Acroform standard. Les informations concernant le formulaire (en ce qui concerne le PDF) sont très vagues – elles spécifient que des champs existent, avec des propriétés et des événements JavaScript, mais ne spécifient aucun rendu. Les objets du formulaire XFA sont dessinés au moment du chargement du document.

{{% /alert %}}

La classe Form fournit la capacité de traiter des AcroForms statiques et vous pouvez obtenir une instance de champ particulière en utilisant la méthode GetFieldFacade(..) de la classe Form. Cependant, les champs XFA ne peuvent pas être accessibles via la méthode Form.GetFieldFacade(..). Au lieu de cela, utilisez [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) pour obtenir/définir les valeurs des champs et manipuler le modèle de champ XFA (définir les propriétés des champs).

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Remplir les champs XFA

Le code suivant vous montre comment remplir des champs dans un formulaire XFA.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillXFAFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FillXFAFields.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
    }
}
```

## Convertir XFA en Acroform

{{% alert color="primary" %}}

Essayez en ligne
Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien : [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Les formulaires dynamiques sont basés sur une spécification XML connue sous le nom de XFA, l'« Architecture des formulaires XML ». Les informations concernant le formulaire (en ce qui concerne un PDF) sont très vagues – elles spécifient que des champs existent, avec des propriétés et des événements JavaScript, mais ne spécifient aucun rendu.

Actuellement, le PDF prend en charge deux méthodes différentes pour intégrer des données et des formulaires PDF :

- AcroForms (également connus sous le nom de formulaires Acrobat), introduits et inclus dans la spécification du format PDF 1.2.
- Formulaires d'Architecture XML d'Adobe (XFA), introduits dans la spécification du format PDF 1.5 comme une fonctionnalité optionnelle (La spécification XFA n'est pas incluse dans la spécification PDF, elle est seulement référencée.)

Nous ne pouvons pas extraire ou manipuler les pages des formulaires XFA, car le contenu du formulaire est généré à l'exécution (lors de la visualisation du formulaire XFA) au sein de l'application essayant d'afficher ou de rendre le formulaire XFA. Aspose.PDF dispose d'une fonctionnalité qui permet aux développeurs de convertir des formulaires XFA en AcroForms standard.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDynamicXFAToAcroForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load dynamic XFA form
    using (var document = new Aspose.Pdf.Document(dataDir + "DynamicXFAToAcroForm.pdf"))
    {
        // Set the form fields type as standard AcroForm
        document.Form.Type = Aspose.Pdf.Forms.FormType.Standard;

        // Save PDF document
        document.Save(dataDir + "StandardAcroForm_out.pdf");
    }
}
```

## Obtenir les propriétés des champs XFA

Pour accéder aux propriétés des champs, utilisez d'abord Document.Form.XFA.Template pour accéder au modèle de champ. Le code suivant montre les étapes pour obtenir les coordonnées X et Y d'un champ de formulaire XFA.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXFAProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXFAProperties.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Get field position
        if (names.Length > 0)
        {
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
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