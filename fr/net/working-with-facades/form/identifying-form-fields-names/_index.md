---
title: Identification des noms des champs de formulaire
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/identifying-form-fields-names/
description: Aspose.Pdf.Facades vous permet d'identifier les noms des champs de formulaire en utilisant la classe Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Identifying form fields names",
    "alternativeHeadline": "Identify and Label PDF Form Fields Easily",
    "abstract": "La fonctionnalité dans Aspose.PDF for .NET simplifie le processus d'identification des noms des champs de formulaire dans les documents PDF. En utilisant la classe Form et ses attributs, les utilisateurs peuvent facilement récupérer et afficher les noms des champs aux côtés de leurs champs correspondants, rationalisant ainsi le remplissage et l'édition des formulaires PDF. Cette fonctionnalité améliore l'expérience utilisateur en garantissant une manipulation précise des champs, en particulier lors du travail avec des formulaires créés dans des outils externes comme Adobe Designer.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "511",
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
    "url": "/net/identifying-form-fields-names/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/identifying-form-fields-names/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

[Aspose.PDF for .NET](/pdf/fr/net/) fournit la capacité de créer, modifier et remplir des formulaires PDF déjà créés. Le namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) contient la classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form), qui contient la fonction nommée [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) et qui prend deux arguments, à savoir le nom du champ et la valeur du champ. Donc, pour remplir les champs du formulaire, vous devez connaître le nom exact du champ de formulaire.

## Détails de mise en œuvre

Nous rencontrons souvent un scénario où nous devons remplir un formulaire créé dans un outil, c'est-à-dire Adobe Designer, et nous ne sommes pas sûrs des noms des champs de formulaire. Donc, pour remplir les champs du formulaire, nous devons d'abord lire les noms de tous les champs de formulaire PDF. La classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) fournit la propriété nommée [FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) qui retourne tous les noms des champs et retourne null si le PDF ne contient aucun champ. Cependant, en utilisant cette propriété, nous obtenons les noms de tous les champs dans le formulaire PDF et nous ne pouvons pas être certains de quel nom correspond à quel champ sur le formulaire.

Comme solution à ce problème, nous allons utiliser les attributs d'apparence de chaque champ. La classe Form a une fonction nommée [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade) qui retourne des attributs, y compris la localisation, la couleur, le style de bordure, la police, les éléments de liste, etc. Pour enregistrer ces valeurs, nous devons utiliser la classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), qui est utilisée pour enregistrer les attributs visuels des champs. Une fois que nous avons ces attributs, nous pouvons ajouter un champ de texte sous chaque champ qui afficherait le nom du champ.

{{% alert color="primary" %}}
À ce stade, une question se pose : "comment allons-nous déterminer l'emplacement où ajouter le champ de texte ?"
{{% /alert %}}

{{% alert color="primary" %}}
La solution à ce problème est la propriété Box dans la classe [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade), qui contient l'emplacement du champ. Nous devons enregistrer ces valeurs dans un tableau de type rectangle et utiliser ces valeurs pour identifier la position où ajouter les nouveaux champs de texte.
{{% /alert %}}

Dans le namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades), nous avons une classe nommée [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) qui fournit la capacité de manipuler des formulaires PDF. Ouvrez un formulaire PDF ; ajoutez un champ de texte sous chaque champ de formulaire existant et enregistrez le formulaire PDF avec un nouveau nom.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyFormFieldsNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // First a input pdf file should be assigned
    var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf");
    // Get all field names
    var allfields = form.FieldNames;
    // Create an array which will hold the location coordinates of Form fields
    var box = new System.Drawing.Rectangle[allfields.Length];
    for (int i = 0; i < allfields.Length; i++)
    {
        // Get the appearance attributes of each field, consequtively
        var facade = form.GetFieldFacade(allfields[i]);
        // Box in FormFieldFacade class holds field's location
        box[i] = facade.Box;
    }
    // Save PDF document
    form.Save(dataDir + "IdentifyFormFields_1_out.pdf");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
    {
        // Now we need to add a textfield just upon the original one
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, 
                "TextField" + i, allfields[i], 1, 
                box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "IdentifyFormFields_out.pdf");
        }
    }
}
```