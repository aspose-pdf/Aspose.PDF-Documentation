---
title: Déplacer et Supprimer un Champ de Formulaire
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /fr/net/move-remove-form-field/
description: Explorez comment gérer les champs de formulaire dans les PDF, y compris les déplacer ou les supprimer, en utilisant Aspose.PDF for .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move and Remove Form Field",
    "alternativeHeadline": "Move and Remove Fields in PDF Forms Efficiently",
    "abstract": "La fonctionnalité Déplacer et Supprimer un Champ de Formulaire dans la classe FormEditor permet aux utilisateurs de repositionner et d'éliminer sans effort des champs de formulaire dans des documents PDF existants. En utilisant les méthodes MoveField et RemoveField, les utilisateurs peuvent personnaliser efficacement les formulaires, améliorant ainsi l'utilisabilité et la gestion des documents. Cette fonctionnalité permet aux utilisateurs d'optimiser leurs mises en page PDF sans nécessiter une expertise technique approfondie.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "416",
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
    "url": "/net/move-remove-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-remove-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Déplacer un Champ de Formulaire vers un Nouvel Emplacement dans un Fichier PDF Existant

Si vous souhaitez déplacer un champ de formulaire vers un nouvel emplacement, vous pouvez utiliser la méthode [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) de la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Vous devez simplement fournir le nom du champ et le nouvel emplacement de ce champ à la méthode [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield). Vous devez également enregistrer le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) de la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Le code suivant vous montre comment déplacer un champ de formulaire à un nouvel emplacement dans un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "MoveField.pdf");
        editor.MoveField("textbox1", 262.56f, 496.75f, 382.28f, 514.03f);
        // Save PDF document
        editor.Save(dataDir + "MoveField_out.pdf");
    }
}
```

## Supprimer un Champ de Formulaire d'un Fichier PDF Existant

Pour supprimer un champ de formulaire d'un fichier PDF existant, vous pouvez utiliser la méthode RemoveField de la classe FormEditor. Cette méthode prend un seul argument : le nom du champ. Vous devez créer un objet de la classe FormEditor, appeler la méthode [RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) pour supprimer un champ particulier du PDF, puis appeler la méthode Save pour enregistrer le fichier PDF mis à jour. Le code suivant vous montre comment supprimer des champs de formulaire d'un fichier PDF existant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "ModifyFormField.pdf");
        editor.RemoveField("textbox1");
        // Save PDF document
        editor.Save(dataDir + "RemoveField_out.pdf");
    }
}
```

## Renommer des Champs de Formulaire dans un PDF

Vous pouvez également renommer votre champ en utilisant la méthode [RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield) de la classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RenameFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "ModifyFormField.pdf");
        editor.RenameField("textbox1", "FirstName");
        // Save PDF document
        editor.Save(dataDir + "RenameField_out.pdf");
    }
}
```