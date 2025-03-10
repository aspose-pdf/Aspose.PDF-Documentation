---
title: Supprimer des formulaires d'un PDF en C#
linktitle: Supprimer des formulaires
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /fr/net/remove-form/
description: Supprimer du texte basé sur le sous-type/formulaire avec la bibliothèque Aspose.PDF for .NET. Supprimer tous les formulaires du PDF.
lastmod: "2024-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete Forms from PDF in C#",
    "alternativeHeadline": "Effortless Removal of Forms from PDFs in C#",
    "abstract": "Présentation de la nouvelle fonctionnalité pour supprimer des formulaires des documents PDF en C# en utilisant la bibliothèque Aspose.PDF. Cette fonctionnalité simplifie la suppression d'éléments de formulaire spécifiques, tels que les sous-formulaires, ou même tous les formulaires d'un fichier PDF, améliorant ainsi la gestion des documents et les capacités de personnalisation pour les développeurs. Optimisez vos processus d'édition PDF avec des extraits de code précis qui garantissent une suppression efficace des fragments de texte et un enregistrement des documents.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "delete forms, remove text, PDF C#, Aspose.PDF for .NET library, TextFragmentAbsorber, remove all forms",
    "wordcount": "378",
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
    "url": "/net/remove-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Supprimer du texte basé sur le sous-type/formulaire

L'extrait de code suivant crée un nouvel objet Document en utilisant une variable d'entrée qui contient le chemin vers le fichier PDF. L'exemple accède aux formulaires présentés à la page 2 du document et vérifie les formulaires avec certaines propriétés. Si un formulaire de type "Machine à écrire" et de sous-type "Formulaire" est trouvé, il utilise TextFragmentAbsorber pour visiter et supprimer tous les fragments de texte dans ce formulaire.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ClearTextInForm(string input, string output)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextBox.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        foreach (var form in forms)
        {
            // Check if the form is of type "Typewriter" and subtype "Form"
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                // Create a TextFragmentAbsorber to find text fragments
                var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
                absorber.Visit(form);

                // Clear the text in each fragment
                foreach (var fragment in absorber.TextFragments)
                {
                    fragment.Text = "";
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }	
}
```

## Supprimer les formulaires avec "Machine à écrire" et un sous-type de "Formulaire" d'un PDF

Cet extrait de code recherche les formulaires sur la première page d'un document PDF pour des formulaires avec une intention (IT) de "Machine à écrire" et un sous-type (Sous-type) de "Formulaire". Si les deux conditions sont remplies, le formulaire est supprimé du PDF. Le document modifié est ensuite enregistré dans le fichier de sortie spécifié.

La bibliothèque Aspose.PDF fournit deux façons de supprimer de tels formulaires des PDF :

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteSpecifiedForm(string input, string output)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        for (int i = forms.Count; i > 0; i--)
        {
            if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
            {
                forms.Delete(forms[i].Name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

Méthode 2 :

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteSpecifiedForm(string input, string output)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        foreach (var form in forms)
        {
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                var name = forms.GetFormName(form);
                forms.Delete(name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

## Supprimer tous les formulaires d'un PDF

Ce code supprime tous les éléments de formulaire de la première page d'un document PDF et enregistre ensuite le document modifié dans le chemin de sortie spécifié.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveAllForms(string input, string output)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Clear all forms
        forms.Clear();

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```