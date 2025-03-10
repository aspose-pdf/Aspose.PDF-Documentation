---
title: Modification des tailles de page dans un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/changing-page-sizes-in-a-pdf-file/
description: Essayez d'apprendre comment modifier les tailles de page dans un fichier PDF en utilisant la classe PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Changing page sizes in PDF file",
    "alternativeHeadline": "Effortlessly Adjust PDF Page Sizes with PdfPageEditor",
    "abstract": "La fonctionnalité de la classe PdfPageEditor dans Aspose.Pdf permet aux utilisateurs de modifier facilement les tailles de page de pages individuelles ou multiples dans un fichier PDF. En utilisant la propriété PageSize et la propriété Pages, les utilisateurs peuvent choisir parmi différentes tailles de page prédéfinies et les appliquer efficacement, améliorant ainsi la flexibilité et la personnalisation des mises en page de documents PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "197",
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
    "url": "/net/changing-page-sizes-in-a-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-page-sizes-in-a-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Détails de l'implémentation

La classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) dans l'espace de noms [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) contient une propriété nommée [PageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagesize) qui peut être utilisée pour modifier la taille de la page d'une page individuelle ou de plusieurs pages simultanément. La propriété Pages peut être utilisée pour attribuer les numéros des pages sur lesquelles la nouvelle taille de page doit être appliquée. La classe PageSize contient une liste de différentes tailles de page parmi ses membres. N'importe lequel des membres de cette classe peut être attribué à la propriété PageSize de la classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). Vous pouvez également obtenir la taille d'une page quelconque en utilisant la méthode GetPageSize et en passant le numéro de la page.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfPageEditor object
    using (var pdfPageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        // Change page size of the selected pages
        pdfPageEditor.ProcessPages = new[] { 1 };

        // Select a predefined page size (LETTER) and assign it
        pdfPageEditor.PageSize = Aspose.Pdf.PageSize.PageLetter;

        // Save the file with the updated page size
        pdfPageEditor.Save(dataDir + "ChangePageSizes_out.pdf");

        // Get and display the page size assigned
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        var pageSize = pdfPageEditor.GetPageSize(1);
        Console.WriteLine($"Width: {pageSize.Width}, Height: {pageSize.Height}");
    }
}
```