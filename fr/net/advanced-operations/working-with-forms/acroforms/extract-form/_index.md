---
title: Extraire AcroForm - Extraire les données de formulaire à partir de PDF en C#
linktitle: Extraire AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/extract-form/
description: Extraire le formulaire de votre document PDF avec la bibliothèque Aspose.PDF for .NET. Obtenez la valeur d'un champ individuel du fichier PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract AcroForm - Extract Form Data from PDF in C#",
    "alternativeHeadline": "Effortlessly Extract PDF Form Data Using C#",
    "abstract": "La nouvelle fonctionnalité Extraire AcroForm dans Aspose.PDF for .NET permet aux développeurs d'extraire facilement les données de formulaire à partir de documents PDF. Cette fonctionnalité permet aux utilisateurs de récupérer des valeurs à partir de champs individuels ou de tous les champs d'un PDF, améliorant ainsi les capacités de gestion et de manipulation des données dans les applications C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "extract form data, PDF in C#, Aspose.PDF for .NET, AcroForm extraction, get field values PDF, PDF form fields, individual field value, get fields in region, manipulate PDF forms, C# PDF library",
    "wordcount": "673",
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
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Extraire le formulaire de votre document PDF avec la bibliothèque Aspose.PDF for .NET. Obtenez la valeur d'un champ individuel du fichier PDF."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Extraire des données du formulaire

### Obtenir les valeurs de tous les champs du document PDF

Pour obtenir les valeurs de tous les champs d'un document PDF, vous devez naviguer à travers tous les champs de formulaire et ensuite obtenir la valeur en utilisant la propriété Value. Obtenez chaque champ de la collection Form, dans le type de champ de base appelé Field et accédez à sa propriété Value.

Les extraits de code C# suivants montrent comment obtenir les valeurs de tous les champs d'un document PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetValuesFromFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValuesFromAllFields.pdf"))
    {
        // Get values from all fields
        foreach (Aspose.Pdf.Forms.Field formField in document.Form)
        {
            Console.WriteLine("Field Name : {0} ", formField.PartialName);
            Console.WriteLine("Value : {0} ", formField.Value);
        }
    }
}
```

### Obtenir la valeur d'un champ individuel du document PDF

La propriété Value du champ de formulaire vous permet d'obtenir la valeur d'un champ particulier. Pour obtenir la valeur, obtenez le champ de formulaire de la collection Form de l'objet Document. Cet exemple C# sélectionne un [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield) et récupère sa valeur en utilisant la propriété Value.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetValueFromField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValueFromField.pdf"))
    {
        // Get a field
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.TextBoxField textBoxField)
        {
            // Get field value
            Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
            Console.WriteLine("Value : {0} ", textBoxField.Value);
        }
    }
}
```

Pour obtenir l'URL du bouton de soumission, utilisez les lignes de code suivantes.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetSubmitFormActionUrl()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValueFromField.pdf"))
    {
        // Get the SubmitFormAction from the form field
        if (document.Form[1].OnActivated is Aspose.Pdf.Annotations.SubmitFormAction act)
        {
            // Output the URL of the SubmitFormAction
            Console.WriteLine(act.Url.Name);
        }
    }
}
```

### Obtenir les champs de formulaire d'une région spécifique du fichier PDF

Parfois, vous pourriez savoir où se trouve un champ de formulaire dans un document, mais ne pas connaître son nom. Par exemple, si tout ce que vous avez est un schéma d'un formulaire imprimé. Avec Aspose.PDF for .NET, ce n'est pas un problème. Vous pouvez découvrir quels champs se trouvent dans une région donnée d'un fichier PDF. Pour obtenir des champs de formulaire d'une région spécifique d'un fichier PDF :

1. Ouvrez le fichier PDF en utilisant l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Obtenez le formulaire de la collection Forms du document.
1. Spécifiez la région rectangulaire et passez-la à la méthode GetFieldsInRect de l'objet Form. Une collection de Fields est retournée.
1. Utilisez cela pour manipuler les champs.

L'extrait de code C# suivant montre comment obtenir des champs de formulaire dans une région rectangulaire spécifique d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldsFromRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf"))
    {
        // Create rectangle object to get fields in that area
        var rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

        // Get the PDF form
        var form = document.Form;

        // Get fields in the rectangular area
        var fields = form.GetFieldsInRect(rectangle);

        // Display Field names and values
        foreach (var field in fields)
        {
            // Display image placement properties for all placements
            Console.Out.WriteLine("Field Name: " + field.FullName + "-" + "Field Value: " + field.Value);
        }
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