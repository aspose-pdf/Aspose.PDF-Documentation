---
title: Saut de page dans un PDF existant
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/page-break-in-existing-pdf/
description: Découvrez comment insérer des sauts de page dans un fichier PDF existant en .NET en utilisant Aspose.PDF pour une meilleure gestion des pages.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Page Break in existing PDF",
    "alternativeHeadline": "Insert Custom Page Breaks in PDF Files",
    "abstract": "Présentation de la fonctionnalité de saut de page dans la classe PdfFileEditor, permettant aux utilisateurs de contrôler la mise en page des documents PDF existants avec précision. Cette fonctionnalité permet l'insertion de sauts de page à des emplacements spécifiques dans le document, améliorant la personnalisation et la présentation globale du contenu. Avec des appels de méthode simples, les utilisateurs peuvent facilement modifier leurs PDF pour répondre à des exigences de formatage spécifiques.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "369",
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
    "url": "/net/page-break-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/page-break-in-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

En tant que mise en page par défaut, les contenus à l'intérieur des fichiers PDF sont ajoutés dans une mise en page de haut en bas à gauche. Une fois que le contenu dépasse la marge inférieure de la page, le saut de page se produit. Cependant, vous pouvez rencontrer un besoin d'insérer un saut de page en fonction des exigences. Une méthode nommée AddPageBreak(...) a été ajoutée dans la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) pour accomplir cette exigence.)

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/1).
1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/2).
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/addpagebreak).

- src est le document/source chemin vers le document/flux avec le document source.
- dest est le document/chemin de destination où le document sera enregistré/flux où le document sera enregistré.
- PageBreak est un tableau d'objets de saut de page. Il a deux propriétés : l'index de la page où le saut de page doit être placé et la position verticale du saut de page sur la page.

## Exemple 1 (Ajouter un saut de page)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PageBrakeExample01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_PageBreak();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PageBreak.pdf"))
    {
        // Create PDF document
        using (var dest = new Aspose.Pdf.Document())
        {
            // Create PdfFileEditor object
            var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();
            fileEditor.AddPageBreak(document, dest, new Aspose.Pdf.Facades.PdfFileEditor.PageBreak[]
            {
                new Aspose.Pdf.Facades.PdfFileEditor.PageBreak(1, 450)
            });
            // Save PDF document
            dest.Save(dataDir + "PageBreak_out.pdf");
        }
    }
}
```

## Exemple 2

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PageBrakeExample02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_PageBreak();

    // Create PdfFileEditor object
    var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

    fileEditor.AddPageBreak(dataDir + "PageBreak.pdf",
        dataDir + "PageBreakWithDestPath_out.pdf",
        new Aspose.Pdf.Facades.PdfFileEditor.PageBreak[]
        {
            new Aspose.Pdf.Facades.PdfFileEditor.PageBreak(1, 450)
        });
}
```

## Exemple 3

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PageBrakeExample03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_PageBreak();

    using (var src = new FileStream(dataDir + "PageBreak.pdf", FileMode.Open, FileAccess.Read))
    {
        using (var dest = new FileStream(dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite))
        {
            // Create PdfFileEditor object
            var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

            // Add page break
            fileEditor.AddPageBreak(src, dest,
                new[]
                {
                    new Aspose.Pdf.Facades.PdfFileEditor.PageBreak(1, 450)
                });
        }
    }
}
```