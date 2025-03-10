---
title: Obtenir la valeur de l'option du bouton
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/get-button-option-value/
description: Cette section explique comment obtenir la valeur de l'option du bouton avec Aspose.PDF Facades en utilisant la classe Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Button Option Value",
    "alternativeHeadline": "Retrieve Button Option Values from PDF Efficiently",
    "abstract": "Découvrez comment récupérer efficacement les valeurs des options de bouton à partir de fichiers PDF existants en utilisant les Facades Aspose.PDF. Avec les méthodes GetButtonOptionValues et GetButtonOptionCurrentValue de la classe Form, vous pouvez facilement obtenir toutes les options disponibles pour les boutons radio, ainsi que la valeur actuellement sélectionnée, améliorant ainsi vos capacités de gestion des formulaires PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "275",
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
    "url": "/net/get-button-option-value/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-button-option-value/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Obtenir les valeurs des options de bouton à partir d'un fichier PDF existant

Les boutons radio fournissent un moyen de montrer différentes options. La classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) vous permet d'obtenir toutes les valeurs des options de bouton pour un bouton radio particulier. Vous pouvez obtenir ces valeurs en utilisant la méthode [GetButtonOptionValues](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues). Cette méthode nécessite le nom du bouton radio comme paramètre d'entrée et renvoie un Hashtable. Vous pouvez parcourir ce Hashtable pour obtenir les valeurs des options. Le code suivant vous montre comment obtenir les valeurs des options de bouton à partir d'un fichier PDF existant.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetButtonOptions()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        var optionValues = pdfForm.GetButtonOptionValues("Gender");

        IDictionaryEnumerator optionValueEnumerator = optionValues.GetEnumerator();

        while (optionValueEnumerator.MoveNext())
        {
            Console.WriteLine("Key : {0} , Value : {1} ", optionValueEnumerator.Key, optionValueEnumerator.Value);
        }
    }
}
```

## Obtenir la valeur actuelle de l'option du bouton à partir d'un fichier PDF existant

Les boutons radio fournissent un moyen de définir des valeurs d'option, cependant, un seul d'entre eux peut être sélectionné à la fois. Si vous souhaitez obtenir la valeur de l'option actuellement sélectionnée, vous pouvez utiliser la méthode [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue). La classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) fournit cette méthode. La méthode [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) nécessite le nom du bouton radio comme paramètre d'entrée et renvoie la valeur sous forme de chaîne. Le code suivant vous montre comment obtenir la valeur actuelle de l'option du bouton à partir d'un fichier PDF existant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetCurremtButtonOptionValue()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        string optionValue = pdfForm.GetButtonOptionCurrentValue("Gender");

        Console.WriteLine("Current Value : {0} ", optionValue);
    }
}
```