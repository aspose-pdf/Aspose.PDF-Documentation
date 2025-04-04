---
title: Explorer les fonctionnalités de la classe FormEditor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/exploring-features-of-formeditor-class/
description: Vous pouvez apprendre les détails de l'exploration des fonctionnalités de la classe FormEditor avec la bibliothèque Aspose.PDF pour .NET
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Exploring features of FormEditor class",
    "alternativeHeadline": "Enhancing PDF Forms with FormEditor Class",
    "abstract": "Découvrez les capacités améliorées de la classe FormEditor au sein de la bibliothèque Aspose.PDF for .NET, conçue pour la manipulation sans effort des formulaires PDF interactifs. Cette fonctionnalité permet aux développeurs d'ajouter, de modifier et de configurer facilement des champs de formulaire, avec des méthodes conviviales pour rationaliser le processus de modification. Optimisez votre gestion des formulaires PDF en tirant parti des fonctionnalités complètes de FormEditor pour améliorer vos flux de travail documentaires.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "358",
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
    "url": "/net/exploring-features-of-formeditor-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/exploring-features-of-formeditor-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

{{% alert color="primary" %}}

Les documents PDF contiennent parfois des formulaires interactifs, connus sous le nom d'AcroForm. C'est comme un formulaire utilisé sur les pages web. Ces formulaires contiennent différents types de contrôles, c'est-à-dire des zones de texte, des cases à cocher et des boutons, etc. Un développeur travaillant avec des fichiers PDF peut parfois avoir besoin de modifier ces formulaires. Dans cet article, nous examinerons en détail comment le [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades) nous permet de le faire.

{{% /alert %}}

## Détails de l'implémentation

Les développeurs peuvent utiliser le [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades) non seulement pour ajouter de nouveaux formulaires et champs de formulaire dans un document PDF, mais aussi pour modifier des champs existants. La portée de cet article est limitée aux fonctionnalités de [Aspose.PDF for .NET](/pdf/fr/net/) qui traitent de l'édition de formulaires.

[FormEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formeditor) est la classe qui contient la plupart des méthodes et propriétés permettant aux développeurs de modifier les champs de formulaire. Vous pouvez non seulement ajouter de nouveaux champs, mais aussi supprimer des champs existants, déplacer un champ à une autre position, changer le nom du champ ou les attributs, etc. La liste des fonctionnalités fournies par cette classe est assez complète, et il est très facile de travailler avec les champs de formulaire en utilisant cette classe.

Ces méthodes peuvent être divisées en deux catégories principales, l'une étant utilisée pour manipuler les champs, et l'autre pour définir les nouveaux attributs de ces champs. Les méthodes que nous pouvons regrouper sous la première catégorie incluent AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField et RenameField, etc. Dans la deuxième catégorie des méthodes, on peut inclure SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit, SetFieldScript. Le code suivant vous montre certaines des méthodes de la classe FormEditor en action :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExploringFormEditorFeatures()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "inFile.pdf"))
    {
        // Create instance of FormEditor
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            // Add field in the PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "field1", 1, 300, 500, 350, 525);

            // Add List field in PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "field2", 1, 300, 200, 350, 225);

            // Add list items
            editor.AddListItem("field2", "item 1");
            editor.AddListItem("field2", "item 2");

            // Add submit button
            editor.AddSubmitBtn("submitbutton", 1, "Submit Form", "http:// Testwebsite.com/testpage", 200, 200, 250, 225);

            // Delete list item
                editor.DelListItem("field2", "item 1");

            // Move field to new position
            editor.MoveField("field1", 10, 10, 50, 50);

            // Remove existing field from the PDF
            editor.RemoveField("field1");

            // Rename an existing field
            editor.RenameField("field1", "newfieldname");

            // Reset all visual attributes to empty value
            editor.ResetFacade();

            // Set the alignment style of a text field
            editor.SetFieldAlignment("field1", Aspose.Pdf.Facades.FormFieldFacade.AlignLeft);

            // Set appearance of the field
            editor.SetFieldAppearance("field1", Aspose.Pdf.Annotations.AnnotationFlags.NoRotate);

            // Set field attributes i.e. ReadOnly, Required
            editor.SetFieldAttribute("field1", Aspose.Pdf.Facades.PropertyFlag.ReadOnly);

            // Set field limit
            editor.SetFieldLimit("field1", 25);

            // Save modifications in the output file
            editor.Save(dataDir + "FormEditorFeatures2_out.pdf");                    
        }
    }
}
```