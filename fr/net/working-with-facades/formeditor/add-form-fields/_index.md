---
title: Ajouter des champs de formulaire PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/add-form-fields/
description: Ce sujet explique comment travailler avec des champs de formulaire avec Aspose.PDF Facades en utilisant la classe FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Form Fields",
    "alternativeHeadline": "Effortlessly Enhance PDFs with Custom Form Fields",
    "abstract": "Améliorez vos documents PDF avec une interactivité dynamique en ajoutant des champs de formulaire à l'aide de la classe FormEditor dans Aspose.PDF for .NET. Cette fonctionnalité vous permet d'incorporer facilement des champs de texte, des boutons de soumission avec des URL et des fonctionnalités JavaScript pour des boutons, rationalisant ainsi la saisie des utilisateurs et la soumission de données dans vos PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/add-form-fields/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-form-fields/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Ajouter un champ de formulaire dans un fichier PDF existant

Pour ajouter un champ de formulaire dans un fichier PDF existant, vous devez utiliser la méthode [AddField](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/addfield/index) de la classe [FormEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor). Cette méthode nécessite que vous spécifiiez le type de champ que vous souhaitez ajouter ainsi que le nom et l'emplacement du champ. Vous devez créer un objet de la classe [FormEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor), utiliser la méthode [AddField](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/addfield/index) pour ajouter un nouveau champ dans le PDF. De plus, vous pouvez spécifier une limite sur le nombre de caractères dans votre champ avec [SetFieldLimit](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) et enfin utiliser la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/form/methods/save/index) pour enregistrer le fichier PDF mis à jour. Le code suivant vous montre comment ajouter un champ de formulaire dans un fichier PDF existant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a text field named "Country" to the first page of the PDF
        // Specify the coordinates of the field (left, bottom, right, top)
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);

        // Set a character limit for the "Country" field to 20 characters
        editor.SetFieldLimit("Country", 20);

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```

## Ajouter l'URL du bouton de soumission dans un fichier PDF existant

La méthode [AddSubmitBtn](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) vous permet de définir l'URL du bouton de soumission dans un fichier PDF. C'est l'URL où les données sont envoyées lorsque le bouton de soumission est cliqué. Dans notre exemple de code, nous spécifions l'URL, le nom de notre champ, le numéro de page sur lequel nous voulons ajouter, et les coordonnées de placement du bouton. La méthode [AddSubmitBtn](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) nécessite le nom du champ du bouton de soumission et l'URL. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Le code suivant vous montre comment définir l'URL du bouton de soumission.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddSubmitBtn()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var editor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         editor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a submit button named "Submit" to the first page of the PDF
         // Specify the button text ("Submit"), the URL to which the form data will be submitted,
         // and the coordinates of the button (left, bottom, right, top)
         editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);

         // Save PDF document
         editor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## Ajouter JavaScript pour le bouton poussoir

La méthode [AddFieldScript](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/addfieldscript) vous permet d'ajouter du JavaScript à un bouton poussoir dans un fichier PDF. Cette méthode nécessite le nom du bouton poussoir et le JavaScript. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Le code suivant vous montre comment définir le JavaScript pour un bouton poussoir.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFieldScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a JavaScript action to the field named "Last Name"
        // The script displays an alert box with the message "Only one last name"
        editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```