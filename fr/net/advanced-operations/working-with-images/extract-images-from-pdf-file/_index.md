---
title: Extraire des images d'un fichier PDF
linktitle: Extraire des images
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /fr/net/extract-images-from-pdf-file/
description: Cette section montre comment extraire des images d'un fichier PDF en utilisant la bibliothèque C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images from PDF File",
    "alternativeHeadline": "Effortlessly Extract Images from PDF Files",
    "abstract": "La nouvelle fonctionnalité d'extraction d'images à partir de fichiers PDF utilisant la bibliothèque C# permet aux développeurs de récupérer et de sauvegarder facilement les images contenues dans les documents PDF. En tirant parti de la bibliothèque Aspose.PDF, les utilisateurs peuvent accéder à des images spécifiques de n'importe quelle page et les exporter dans divers formats, rationalisant ainsi leur flux de travail pour la gestion du contenu PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extract images, PDF file, C# library, images collection, extract images from PDF, XImage object, save extracted image, PDF manipulation, Aspose.PDF for .NET, document resources",
    "wordcount": "227",
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
    "url": "/net/extract-images-from-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images-from-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Cette section montre comment extraire des images d'un fichier PDF en utilisant la bibliothèque C#."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Les images sont contenues dans la collection [Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources) de chaque page, dans la collection [Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images). Pour extraire une page particulière, récupérez ensuite l'image de la collection Images en utilisant l'index particulier de l'image.

L'index de l'image renvoie un objet [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage). Cet objet fournit une méthode Save qui peut être utilisée pour sauvegarder l'image extraite. Le code suivant montre comment extraire des images d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractImages.pdf"))
    {
        // Extract a particular image
        var xImage = document.Pages[1].Resources.Images[1];
        using (var outputImage = new FileStream(dataDir + "ExtractedImage.jpg", FileMode.Create))
        {
            // Save PDF document image
            xImage.Save(outputImage, System.Drawing.Imaging.ImageFormat.Jpeg);
        }

        // Save PDF document
        document.Save(dataDir + "ExtractImages_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>