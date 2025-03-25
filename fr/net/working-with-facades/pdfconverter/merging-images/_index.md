---
title: Fusionner des images
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/merge-images/
description: Découvrez comment fusionner des images en un seul document PDF dans .NET en utilisant Aspose.PDF pour une création de documents simplifiée.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge images",
    "alternativeHeadline": "Merge Images with Flexible Formats and Arrangements",
    "abstract": "Aspose.PDF for .NET introduit une nouvelle fonctionnalité puissante qui permet aux utilisateurs de fusionner des images sans effort. Cette fonctionnalité permet de combiner des images dans divers formats et styles tels que vertical, horizontal ou centré tout en offrant également l'option de sauvegarder le résultat final dans le format TIFF très polyvalent. Idéal pour améliorer les présentations de documents, cette fonctionnalité simplifie le processus de création de fichiers d'images fusionnées en utilisant une intégration de code simple.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "482",
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
    "url": "/net/merge-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/merge-images/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

Aspose.PDF 21.4 vous permet de combiner des images. La méthode [Merge Images](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) vérifie le contenu d'un dossier spécifique et travaille avec le type de fichiers spécifié à l'intérieur. Lors de la fusion d'images, nous spécifions 'inputImagesStreams', le format d'image et le mode de fusion d'image (par exemple - vertical) de notre fichier. Ensuite, nous sauvegardons notre résultat dans FileOutputStream.

Suivez l'extrait de code suivant pour résoudre votre tâche :

## Fusionner des images

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages01()
{
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();  // Updated to use dynamic path
    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                                .OrderBy(f => f)
                                .Select(f => File.OpenRead(f))
                                .Cast<Stream>()
                                .ToList();

    using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImages(fileStreams, Aspose.Pdf.Drawing.ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
    using (FileStream outputStream = new FileStream(dataDir + "MergeImages_out.jpg", FileMode.Create))
    {
        // Copy merged images to the output file
        inputStream.CopyTo(outputStream);
    }
}
```

Le deuxième exemple fonctionne de la même manière que le précédent, mais les images fusionnées seront enregistrées horizontalement.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                            .OrderBy(f => f)
                            .Select(f => File.OpenRead(f))
                            .Cast<Stream>()
                            .ToList();

    using (Stream inputStream =
            Aspose.Pdf.Facades.PdfConverter.MergeImages(fileStreams, Aspose.Pdf.Drawing.ImageFormat.Jpeg, ImageMergeMode.Horizontal, 1, 1))
    using (FileStream outputStream = new FileStream(dataDir + "MergeImages02_out.jpg", FileMode.Create))
    {
        // Copy merged images to the output file
        inputStream.CopyTo(outputStream);
    }
}
```

Dans le troisième exemple, nous allons fusionner les images en les centrant. Deux horizontalement, deux verticalement.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                            .OrderBy(f => f)
                            .Select(f => File.OpenRead(f))
                            .Cast<Stream>()
                            .ToList();

    using (Stream inputStream =
            Aspose.Pdf.Facades.PdfConverter.MergeImages(fileStreams, Aspose.Pdf.Drawing.ImageFormat.Jpeg, ImageMergeMode.Center, 2, 2))
    using (FileStream outputStream = new FileStream(dataDir + "MergeImages03_out.jpg", FileMode.Create))
    {
        // Copy merged images to the output file
        inputStream.CopyTo(outputStream);
    }
}
```

De plus, Aspose.PDF pour Java vous offre la possibilité de combiner des images et de les enregistrer au format Tiff, en utilisant la [MergeImagesAsTiff Method](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                            .OrderBy(f => f)
                            .Select(f => File.OpenRead(f))
                            .Cast<Stream>()
                            .ToList();

    using (Stream inputStream =
            Aspose.Pdf.Facades.PdfConverter.MergeImagesAsTiff(fileStreams))
    using (FileStream outputStream = new FileStream(dataDir + "MergeImages_out.tiff", FileMode.Create))
    {
        // Copy merged images to the output file
        inputStream.CopyTo(outputStream);
    }
}
```

Pour enregistrer les images fusionnées en une seule image sur la page PDF, nous les plaçons dans l'imageStream, plaçons le résultat sur la page avec la méthode addImage, où nous spécifions les coordonnées où nous voulons les placer.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeImages05()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Get all image files matching the pattern "MergeImages*.jpg"
    var fileStreams = Directory.GetFiles(dataDir, "MergeImages*.jpg")
                                .OrderBy(f => f)
                                .Select(f => File.OpenRead(f))
                                .Cast<Stream>()
                                .ToList();

    using (Stream inputStream =
            Aspose.Pdf.Facades.PdfConverter.MergeImages(fileStreams, Aspose.Pdf.Drawing.ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
    using (MemoryStream outputStream = new MemoryStream())  // Output to MemoryStream
    {
        // Copy merged images to the MemoryStream
        inputStream.CopyTo(outputStream);

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Add the image from the MemoryStream to the page
            page.AddImage(outputStream, new Aspose.Pdf.Rectangle(10, 120, 400, 720));

            // Save PDF document
            document.Save(dataDir + "MergeImages_out.pdf");
        }
    }
}
```