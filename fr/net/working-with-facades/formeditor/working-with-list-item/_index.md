---
title: Travailler avec les éléments de liste
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /fr/net/working-with-list-item/
description: Cette section explique comment travailler avec les éléments de liste avec Aspose.PDF Facades en utilisant la classe FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with List Item",
    "alternativeHeadline": "Enhance PDF Forms with List Item Management",
    "abstract": "Améliorez vos formulaires PDF avec la fonctionnalité d'élément de liste dans Aspose.PDF for .NET. Ajoutez ou supprimez facilement des éléments des champs ListBox en utilisant la classe FormEditor, permettant une saisie utilisateur dynamique et personnalisable. Cette fonctionnalité simplifie la gestion des formulaires, rendant plus facile l'adaptation du contenu à vos besoins.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "325",
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
    "url": "/net/working-with-list-item/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-list-item/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Ajouter un élément de liste dans un fichier PDF existant

La méthode [AddListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addlistitem) vous permet d'ajouter un élément dans un champ [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). Le premier argument est le nom du champ et le deuxième argument est l'élément du champ. Vous pouvez soit passer un seul élément de champ, soit passer un tableau de chaînes contenant une liste d'éléments. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Le code suivant vous montre comment ajouter des éléments de liste dans un fichier PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a ListBox field for selecting country, placed at the specified coordinates on page 1
         formEditor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f,
             514.03f);

         // Add list items to the 'Country' ListBox field
         formEditor.AddListItem("Country", "USA");
         formEditor.AddListItem("Country", "Canada");
         formEditor.AddListItem("Country", "France");
         formEditor.AddListItem("Country", "Spain");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## Supprimer un élément de liste d'un fichier PDF existant

La méthode [DelListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/dellistitem) vous permet de supprimer un élément particulier du [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). Le premier paramètre est le nom du champ tandis que le deuxième paramètre est l'élément que vous souhaitez supprimer de la liste. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Le code suivant vous montre comment supprimer un élément de liste du fichier PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void DelListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-04.pdf");

         // Delete the list item "France" from the 'Country' ListBox field
         formEditor.DelListItem("Country", "France");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-04-mod.pdf");
     }
 }
```