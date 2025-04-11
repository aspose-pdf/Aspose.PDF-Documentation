---
title: Apparence et attributs des champs
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/changing-field-appearance-and-attributes/
description: Cette section explique comment vous pouvez changer l'apparence et les attributs des champs avec la classe FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Field appearance and attributes",
    "alternativeHeadline": "Enhance Form Fields with Custom Appearance and Behavior",
    "abstract": "La fonctionnalité introduite dans la classe FormEditor de l'espace de noms Aspose.Pdf.Facades permet aux utilisateurs de personnaliser à la fois l'apparence et les attributs des champs de formulaire dans les PDF. En utilisant des méthodes telles que SetFieldAppearance et SetFieldAttributes, les développeurs peuvent facilement modifier les éléments visuels et les comportements, y compris les limites des champs, pour améliorer l'interaction utilisateur et l'efficacité de la saisie des données. Cette fonctionnalité offre une plus grande flexibilité dans la conception des champs de formulaire adaptés aux besoins spécifiques de l'application.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/changing-field-appearance-and-attributes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-field-appearance-and-attributes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

{{% alert color="primary" %}}

La classe [FormEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/FormEditor) de l'[espace de noms Aspose.Pdf.Facades](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades) vous permet non seulement de changer l'apparence du champ de formulaire, mais aussi le comportement du champ. Dans cet article, nous allons voir comment nous pouvons utiliser la classe FormEditor pour changer l'apparence du champ, les attributs du champ et la limite du champ également.

{{% /alert %}}

## Détails de mise en œuvre

La méthode [SetFieldAppearance](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) est utilisée pour changer l'apparence d'un champ de formulaire. Elle prend AnnotationFlag comme paramètre. AnnotationFlag est une énumération qui a différents membres comme Hidden ou NoRotate, etc.

La méthode [SetFieldAttributes](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) est utilisée pour changer l'attribut d'un champ de formulaire. Un paramètre passé à cette méthode est l'énumération PropertyFlag qui contient des membres comme ReadOnly ou Required, etc.

La classe [FormEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/FormEditor) fournit également une méthode pour définir la limite du champ. Elle indique au champ combien de caractères il peut contenir. Le code ci-dessous montre comment toutes ces méthodes peuvent être utilisées.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddFieldAndSetAttributes()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var doc = new Aspose.Pdf.Document(dataDir + "FilledForm.pdf"))
     {
         // Create an instance of FormEditor to manipulate form fields
         using (var formEditor = new Aspose.Pdf.Facades.FormEditor(doc))
         {
             // Add a new text field to the form on page 1 at the specified coordinates and size
             formEditor.AddField(Aspose.Pdf.Facades.FieldType.Text, "text1", 1, 200, 550, 300, 575);

             // Set the field attribute to make the text field required (user must fill it)
             formEditor.SetFieldAttribute("text1", Aspose.Pdf.Facades.PropertyFlag.Required);

             // Set a character limit for the field (maximum 20 characters)
             formEditor.SetFieldLimit("text1", 20);

             // Save PDF document
             formEditor.Save(dataDir + "ChangingFieldAppearance_out.pdf");
         }
     }
 }
```