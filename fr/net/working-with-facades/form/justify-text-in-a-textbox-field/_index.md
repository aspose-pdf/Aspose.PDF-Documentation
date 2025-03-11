---
title: Justifier le texte dans un champ de zone de texte
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/justify-text-in-a-textbox-field/
description: Cet article vous montre comment justifier le texte dans un champ de zone de texte en utilisant la classe Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Justify Text in a Textbox Field",
    "alternativeHeadline": "Justify Text in PDF Textbox Fields Effortlessly",
    "abstract": "La fonctionnalité permet aux utilisateurs de justifier le texte dans un champ de zone de texte dans des documents PDF en utilisant la classe FormEditor de l'espace de noms Aspose.Pdf.Facades. En utilisant l'option AlignJustified, les utilisateurs peuvent obtenir un alignement de texte visuellement attrayant tout en maintenant la fonctionnalité, même si l'alignement justifié n'est pas pris en charge pendant la saisie active. Cela améliore la présentation des données de formulaire dans les fichiers PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "283",
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
    "url": "/net/justify-text-in-a-textbox-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/justify-text-in-a-textbox-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

{{% alert color="primary" %}}

Dans cet article, nous vous montrerons comment justifier le texte dans un champ de zone de texte dans un fichier PDF.

{{% /alert %}}

## Détails de mise en œuvre

La classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) dans l'[espace de noms Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) offre la capacité de décorer un champ de formulaire PDF. Maintenant, si votre besoin est de justifier le texte dans un champ de zone de texte, vous pouvez facilement y parvenir en utilisant la valeur [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) de l'énumération [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) et en appelant la méthode [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index). Dans l'exemple ci-dessous, nous allons d'abord remplir un champ de zone de texte en utilisant la méthode [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) de la classe [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form). Après cela, nous utiliserons la classe FormEditor pour justifier le texte dans le champ de zone de texte. L'extrait de code suivant vous montre comment justifier le texte dans un champ de zone de texte.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void JustifyTextInTextboxField()
{
    // The path to the documents directory 
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // Open PDF document
    using (var source = File.Open(dataDir + "JustifyText.pdf", FileMode.Open))
    {
        using (var ms = new MemoryStream())
        {
            // Create Form Object
            var form = new Aspose.Pdf.Facades.Form();
            // Bind PDF document
            form.BindPdf(source);
            // Fill Text Field
            form.FillField("Text1", "Thank you for using Aspose");
            // Save PDF document in Memory Stream
            form.Save(ms);
            ms.Seek(0, SeekOrigin.Begin);

            using (var dest = new FileStream(dataDir + "JustifyText_out.pdf", FileMode.Create))
            {
                // Create formEditor Object
                using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
                {
                    // Open PDF from memory stream
                    formEditor.BindPdf(ms);
                    // Set Text Alignment as Justified
                    formEditor.Facade.Alignment = Aspose.Pdf.Facades.FormFieldFacade.AlignJustified;
                    // Decorate form field
                    formEditor.DecorateField();
                    // Save PDF document
                    formEditor.Save(dest);
                }
            }
        }
    }
}
```
Veuillez noter que l'alignement justifié n'est pas pris en charge par le PDF, c'est pourquoi le texte sera aligné à gauche lorsque vous saisissez le texte dans le champ de zone de texte. Mais lorsque le champ n'est pas actif, le texte est justifié.