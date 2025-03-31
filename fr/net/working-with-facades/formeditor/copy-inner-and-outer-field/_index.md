---
title: Copier le champ intérieur et extérieur
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /fr/net/copy-inner-and-outer-field/
description: Cette section explique comment copier le champ intérieur et extérieur avec Aspose.PDF Facades en utilisant la classe FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Copy Inner and Outer Field",
    "alternativeHeadline": "Seamlessly Copy Inner and Outer Fields in PDF",
    "abstract": "La fonctionnalité Copier le champ intérieur et extérieur dans Aspose.PDF for .NET améliore l'édition de formulaires en permettant aux utilisateurs de dupliquer des champs dans le même PDF ou de les transférer depuis un fichier PDF externe. Avec les méthodes faciles à utiliser CopyInnerField et CopyOuterField fournies par la classe FormEditor, les utilisateurs peuvent gérer efficacement les champs de formulaire, garantissant la cohérence et économisant du temps dans la préparation des documents.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "337",
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
    "url": "/net/copy-inner-and-outer-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/copy-inner-and-outer-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

La méthode [CopyInnerField](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) vous permet de copier un champ dans le même fichier, aux mêmes coordonnées, sur la page spécifiée. Cette méthode nécessite le nom du champ que vous souhaitez copier, le nouveau nom du champ et le numéro de la page sur laquelle le champ doit être copié. La classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) fournit cette méthode. L'extrait de code suivant vous montre comment copier le champ au même emplacement dans le même fichier.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyInnerField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor object
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Form-01.pdf"))
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the field "Last Name" from the first page to "Last Name 2" on the second page
            formEditor.CopyInnerField("Last Name", "Last Name 2", 2);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
        }
    }
}
```

## Copier le champ extérieur dans un fichier PDF existant

La méthode [CopyOuterField](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) vous permet de copier un champ de formulaire depuis un fichier PDF externe et de l'ajouter ensuite au fichier PDF d'entrée au même emplacement et au numéro de page spécifié. Cette méthode nécessite le fichier PDF à partir duquel le champ doit être copié, le nom du champ et le numéro de la page sur laquelle le champ doit être copié. Cette méthode est fournie par la classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). L'extrait de code suivant vous montre comment copier un champ depuis un fichier PDF externe.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyOuterField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor 
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Create empty document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the outer field "First Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "First Name", 1);

            // Copy the outer field "Last Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "Last Name", 1);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-02-mod.pdf");
        }
    }
}
```