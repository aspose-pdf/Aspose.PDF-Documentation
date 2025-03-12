---
title: Modification d'AcroForm
linktitle: Modification d'AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/modifing-form/
description: Modification de formulaire dans votre fichier PDF avec la bibliothèque Aspose.PDF for .NET. Vous pouvez ajouter ou supprimer des champs dans un formulaire existant, obtenir et définir la limite des champs, etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modifing AcroForm",
    "alternativeHeadline": "Modify and Manage AcroForm Fields in PDF",
    "abstract": "La nouvelle fonctionnalité de modification d'AcroForm dans la bibliothèque Aspose.PDF for .NET permet aux utilisateurs d'ajouter ou de supprimer facilement des champs des formulaires PDF existants. Cette fonctionnalité inclut également la définition des limites de champ et la personnalisation des apparences de police pour une expérience utilisateur raffinée, améliorant la gestion et l'interaction des formulaires PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Modifing AcroForm, Aspose.PDF for .NET, PDF form fields, SetFieldLimit, custom font, Add/remove fields, Document Form collection, DefaultAppearance, manage form fields, PDF manipulation",
    "wordcount": "601",
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
    "url": "/net/modifing-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modifing-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Modification de formulaire dans votre fichier PDF avec la bibliothèque Aspose.PDF for .NET. Vous pouvez ajouter ou supprimer des champs dans un formulaire existant, obtenir et définir la limite des champs, etc."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Obtenir ou définir la limite des champs

La méthode SetFieldLimit(field, limit) de la classe FormEditor vous permet de définir une limite de champ, le nombre maximum de caractères pouvant être saisis dans un champ.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFieldLimit()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create FormEditor instance
    using (var form = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Set field limit for "textbox1"
        form.SetFieldLimit("textbox1", 15);

        // Save PDF document
        form.Save(dataDir + "SetFieldLimit_out.pdf");
    }
}
```

De même, Aspose.PDF dispose d'une méthode qui obtient la limite de champ en utilisant l'approche DOM. Le code suivant montre les étapes.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldLimitUsingDOM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FieldLimit.pdf"))
    {
        // Get the field and its maximum limit
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.TextBoxField textBoxField)
        {
            Console.WriteLine("Limit: " + textBoxField.MaxLen);
        }
    }
}
```

Vous pouvez également obtenir la même valeur en utilisant l'espace de noms *Aspose.Pdf.Facades* avec le code suivant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldLimitUsingFacades()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create Form instance
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "FieldLimit.pdf");

        // Get the field limit for "textbox1"
        Console.WriteLine("Limit: " + form.GetFieldLimit("textbox1"));
    }
}
```

## Définir une police personnalisée pour le champ de formulaire

Les champs de formulaire dans les fichiers PDF Adobe peuvent être configurés pour utiliser des polices par défaut spécifiques. Dans les premières versions d'Aspose.PDF, seules les 14 polices par défaut étaient prises en charge. Les versions ultérieures ont permis aux développeurs d'appliquer n'importe quelle police. Pour définir et mettre à jour la police par défaut utilisée pour les champs de formulaire, utilisez la classe DefaultAppearance(Font font, double size, Color color). Cette classe se trouve sous l'espace de noms Aspose.Pdf.InteractiveFeatures. Pour utiliser cet objet, utilisez la propriété DefaultAppearance de la classe Field.

Le code suivant montre comment définir la police par défaut pour les champs de formulaire PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFormFieldFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FormFieldFont14.pdf"))
    {
        // Get particular form field from document
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.Field field)
        {
            // Create font object
            var font = Aspose.Pdf.Text.FontRepository.FindFont("ComicSansMS");

            // Set the font information for form field
            field.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance(font, 10, System.Drawing.Color.Black);
        }

        // Save PDF document
        document.Save(dataDir + "FormFieldFont14_out.pdf");
    }
}
```

## Ajouter/supprimer des champs dans un formulaire existant

Tous les champs de formulaire sont contenus dans la collection Form de l'objet Document. Cette collection fournit différentes méthodes qui gèrent les champs de formulaire, y compris la méthode Delete. Si vous souhaitez supprimer un champ particulier, passez le nom du champ en tant que paramètre à la méthode Delete, puis enregistrez le document PDF mis à jour. Le code suivant montre comment supprimer un champ particulier d'un document PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteFormField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteFormField.pdf"))
    {
        // Delete a particular field by name
        document.Form.Delete("textbox1");

        // Save PDF document
        document.Save(dataDir + "DeleteFormField_out.pdf");
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