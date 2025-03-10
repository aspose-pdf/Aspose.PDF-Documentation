---
title: Décorer un champ de formulaire dans un PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/decorate-form-field/
description: Explorez comment décorer les champs de formulaire dans un document PDF, en ajoutant des améliorations visuelles comme des bordures, en .NET avec Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Decorate Form Field in PDF",
    "alternativeHeadline": "Enhance PDF Forms with Custom Field Decorations",
    "abstract": "Présentation d'une fonctionnalité puissante qui améliore la gestion des formulaires PDF : la capacité de décorer des champs de formulaire individuels ou tous les champs de formulaire en utilisant la classe FormEditor. Cette fonctionnalité permet aux utilisateurs de personnaliser les attributs des champs tels que le style de police, la taille, la couleur de la bordure et l'alignement, simplifiant ainsi le processus de création de formulaires PDF visuellement attrayants et bien structurés. Améliorez vos flux de travail PDF avec cette méthode de décoration intuitive pour une présentation de document plus soignée.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "609",
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
    "url": "/net/decorate-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/decorate-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Décorer un champ de formulaire particulier dans un fichier PDF existant

La méthode [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) présente dans la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) vous permet de décorer un champ de formulaire particulier dans un fichier PDF. Si vous souhaitez décorer un champ particulier, vous devez passer le nom du champ à cette méthode. Cependant, avant d'appeler cette méthode, vous devez créer des objets des classes [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) et [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Vous devez également assigner l'objet [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) à la propriété [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) de l'objet [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Après cela, vous pouvez définir n'importe quel attribut fourni par l'objet [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Une fois que vous avez défini les attributs, vous pouvez appeler la méthode [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) et enfin enregistrer le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) de la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Le code suivant vous montre comment décorer un champ de formulaire particulier.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecorateField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Create a FormFieldFacade object to define decoration properties for the field
        var cityDecoration = new Aspose.Pdf.Facades.FormFieldFacade
        {
            // Set the font style to Courier
            Font = Aspose.Pdf.Facades.FontStyle.Courier,
            // Set the font size to 12
            FontSize = 12,
            // Set the border color to black
            BorderColor = System.Drawing.Color.Black,
            // Set the border width to 2
            BorderWidth = 2
        };

        // Assign the decoration facade to the FormEditor
        editor.Facade = cityDecoration;

        // Apply the decoration to the field named "City"
        editor.DecorateField("City");

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-02.pdf");
    }
}
```

## Décorer tous les champs d'un type particulier dans un fichier PDF existant

La méthode [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) vous permet de décorer tous les champs de formulaire d'un type particulier dans un fichier PDF en une seule fois. Si vous souhaitez décorer tous les champs d'un type particulier, vous devez passer le type de champ à cette méthode. Cependant, avant d'appeler cette méthode, vous devez créer des objets des classes [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) et [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Vous devez également assigner l'objet [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) à la propriété [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) de l'objet [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Après cela, vous pouvez définir n'importe quel attribut fourni par l'objet [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Une fois que vous avez défini les attributs, vous pouvez appeler la méthode [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) et enfin enregistrer le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) de la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Le code suivant vous montre comment décorer tous les champs d'un type particulier.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecorateField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Create a FormFieldFacade object to define alignment properties for text fields
        var textFieldDecoration = new Aspose.Pdf.Facades.FormFieldFacade
        {
            // Set text alignment to center
            Alignment = Aspose.Pdf.Facades.FormFieldFacade.AlignCenter
        };

        // Assign the decoration facade to the FormEditor
        editor.Facade = textFieldDecoration;

        // Apply the alignment decoration to all text fields in the PDF
        editor.DecorateField(Aspose.Pdf.Facades.FieldType.Text);

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-align-text.pdf");
    }
}
```