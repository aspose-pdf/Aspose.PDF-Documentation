---
title: Définir les informations sur le fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/set-pdf-file-information/
description: Cette section explique comment définir les informations sur le fichier PDF avec Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set PDF File Information",
    "alternativeHeadline": "Set Custom Metadata for PDF Files Effortlessly",
    "abstract": "Améliorez la gestion de vos fichiers PDF avec la nouvelle fonctionnalité dans Aspose.PDF for .NET qui vous permet de définir et de mettre à jour facilement des informations spécifiques au fichier telles que l'auteur, le titre et les mots-clés. Utilisez la classe PdfFileInfo pour modifier efficacement vos PDF, en ajoutant des métadonnées précieuses pour améliorer l'organisation et la recherche. Rationalisez votre flux de travail en enregistrant ces mises à jour sans effort avec la méthode SaveNewInfo",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "251",
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
    "url": "/net/set-pdf-file-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-pdf-file-information/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

La classe [PdfFileInfo](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileinfo) vous permet de définir des informations spécifiques au fichier d'un fichier PDF. Vous devez créer un objet de la classe [PdfFileInfo](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileinfo) puis définir différentes propriétés spécifiques au fichier telles que l'auteur, le titre, le mot-clé et le créateur, etc. Enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode [SaveNewInfo](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) de l'objet [PdfFileInfo](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileinfo).

Le code suivant vous montre comment définir les informations sur le fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfFileInfo object to work with PDF metadata
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set PDF information
        fileInfo.Author = "Aspose";
        fileInfo.Title = "Hello World!";
        fileInfo.Keywords = "Peace and Development";
        fileInfo.Creator = "Aspose";
        
        // Save the PDF with updated information
        fileInfo.SaveNewInfo(dataDir + "SetFileInfo_out.pdf");
    }
}
```

## Définir les informations méta

La méthode [SetMetaInfo](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) vous permet d'ajouter n'importe quelle information. Dans notre exemple, nous avons ajouté un champ. Consultez le code suivant : 

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMetaInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of the PdfFileInfo object
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set a new custom attribute as meta info
        fileInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

        // Save the updated file
        fileInfo.SaveNewInfo(dataDir + "SetMetaInfo_out.pdf");
    }
}
```