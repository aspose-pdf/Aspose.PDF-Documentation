---
title: Extraire des pièces jointes d'un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/extract-attachments/
description: Découvrez comment extraire et gérer des pièces jointes dans des documents PDF en .NET en utilisant Aspose.PDF pour une meilleure gestion des documents.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Attachments from PDF File",
    "alternativeHeadline": "Effortlessly Extract and Manage PDF Attachments",
    "abstract": "La nouvelle fonctionnalité d'extraction de pièces jointes dans Aspose.PDF for .NET permet aux développeurs de récupérer et de gérer facilement les pièces jointes de fichiers au sein des documents PDF. En utilisant la classe PdfExtractor, les utilisateurs peuvent extraire des pièces jointes et obtenir des informations essentielles, telles que les noms et les détails des pièces jointes, améliorant ainsi les capacités de traitement des documents.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "208",
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
    "url": "/net/extract-attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

L'une des principales catégories sous les capacités d'extraction du [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) est l'extraction de pièces jointes. Cette catégorie fournit un ensemble de méthodes, qui non seulement aident à extraire les pièces jointes, mais fournissent également des méthodes qui peuvent vous donner des informations liées aux pièces jointes, c'est-à-dire que les méthodes [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) et [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) fournissent respectivement des informations sur les pièces jointes et le nom de la pièce jointe. Afin d'extraire puis d'obtenir les pièces jointes, nous utilisons les méthodes [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) et [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment).

Le code suivant vous montre comment utiliser les méthodes PdfExtractor :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Create the extractor
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "GetAlltheAttachments.pdf");

        // Extract attachments
        pdfExtractor.ExtractAttachment();

        // Get attachment names
        if (pdfExtractor.GetAttachNames().Count > 0)
        {
            Console.WriteLine("Extracting and storing...");

            // Get extracted attachments
            pdfExtractor.GetAttachment(dataDir + "GetAlltheAttachments_out.pdf");
        }
    }
}
```