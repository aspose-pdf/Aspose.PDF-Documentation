---
title: Extraire des images d'un PDF C#
linktitle: Extraire des images d'un PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/extract-images-from-the-pdf-file/
description: Comment extraire une partie de l'image d'un PDF en utilisant Aspose.PDF for .NET en C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Images from PDF Files in C#",
    "abstract": "Débloquez la puissance de Aspose.PDF for .NET avec la nouvelle fonctionnalité d'extraction d'images de fichiers PDF directement en C#. Cette fonctionnalité permet aux utilisateurs de récupérer et de sauvegarder facilement des images à partir de pages spécifiques, facilitant ainsi la gestion et le traitement efficaces des images dans les applications .NET.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "240",
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
    "url": "/net/extract-images-from-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images-from-the-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

Les images sont contenues dans la collection [Resources](https://reference.aspose.com/pdf/fr/net/aspose.pdf/resources) de chaque page, dans la collection [Images](https://reference.aspose.com/pdf/fr/net/aspose.pdf/resources/properties/images). Pour extraire une page particulière, récupérez ensuite l'image de la collection Images en utilisant l'index particulier de l'image.

L'index de l'image renvoie un objet [XImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf/ximage). Cet objet fournit une méthode Save qui peut être utilisée pour sauvegarder l'image extraite. Le code suivant montre comment extraire des images d'un fichier PDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractImages.pdf"))
    {
        // Extract a particular image
        var xImage = document.Pages[1].Resources.Images[1];

        using (var outputImage = new FileStream(dataDir + "outputImage.jpg", FileMode.Create))
        {
            // Save the output image
            xImage.Save(outputImage, ImageFormat.Jpeg);
        }

        // Save PDF document
        document.Save(dataDir + "ExtractImages_out.pdf");
    }
}
```