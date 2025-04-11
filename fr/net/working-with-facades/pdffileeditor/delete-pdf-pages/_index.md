---
title: Supprimer des pages PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /fr/net/delete-pdf-pages/
description: Cette section explique comment supprimer des pages PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete PDF pages",
    "alternativeHeadline": "Effortlessly Remove Pages from PDF Files",
    "abstract": "Supprimez facilement des pages spécifiques de vos documents PDF en utilisant Aspose.PDF for .NET Facades. En utilisant la classe PdfFileEditor, vous pouvez supprimer des pages indésirables à la fois des chemins de fichiers et des flux, simplifiant ainsi votre processus d'édition PDF avec un contrôle précis sur le résultat final. Améliorez vos capacités de gestion de documents avec cette fonctionnalité efficace de suppression de pages.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "262",
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
    "url": "/net/delete-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/delete-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

Si vous souhaitez supprimer un certain nombre de pages du fichier PDF qui se trouve sur le disque, vous pouvez utiliser la surcharge de la méthode [Delete](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) qui prend les trois paramètres suivants : chemin du fichier d'entrée, tableau des numéros de pages à supprimer, et chemin du fichier PDF de sortie. Le deuxième paramètre est un tableau d'entiers représentant toutes les pages qui doivent être supprimées. Les pages spécifiées sont supprimées du fichier d'entrée et le résultat est enregistré en tant que fichier de sortie. Le code suivant vous montre comment supprimer des pages PDF en utilisant des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of pages to delete
    var pagesToDelete = new int[] { 1, 2 };
    // Delete pages
    pdfEditor.Delete(dataDir + "DeletePagesInput.pdf", pagesToDelete, dataDir + "DeletePagesUsingFilePath_out.pdf");
}
```

## Supprimer des pages PDF en utilisant des flux

La méthode [Delete](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) fournit également une surcharge qui vous permet de supprimer les pages du fichier PDF d'entrée, tandis que les fichiers d'entrée et de sortie sont dans les flux. Cette surcharge prend les trois paramètres suivants : flux d'entrée, tableau d'entiers des pages PDF à supprimer, et flux de sortie. Le code suivant vous montre comment supprimer des pages PDF en utilisant des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "DeletePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "DeletePagesUsingStream_out.pdf", FileMode.Create))
        {
            // Array of pages to delete
            var pagesToDelete = new int[] { 1, 2 };
            // Delete pages
            pdfEditor.Delete(inputStream, pagesToDelete, outputStream);
        }
    }
}
```