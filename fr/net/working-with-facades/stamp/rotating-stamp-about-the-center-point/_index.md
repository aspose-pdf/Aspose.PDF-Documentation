---
title: Rotation du tampon autour du point central
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/rotating-stamp-about-the-center-point/
description: Cette section explique comment faire pivoter un tampon autour du point central en utilisant la classe Stamp.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotating stamp about the center point",
    "alternativeHeadline": "Rotate Stamps Precisely Around Their Center Point",
    "abstract": "La fonctionnalité dans Aspose.PDF for .NET permet aux utilisateurs de faire pivoter des tampons dans des fichiers PDF précisément autour de leur point central. En utilisant la classe Stamp, les développeurs peuvent facilement définir des valeurs de rotation de 0 à 360 degrés, améliorant ainsi la flexibilité et la personnalisation du placement des filigranes dans les documents. Cette fonctionnalité est idéale pour créer des PDF visuellement dynamiques avec des orientations de tampon personnalisées.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "339",
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
    "url": "/net/rotating-stamp-about-the-center-point/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotating-stamp-about-the-center-point/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

{{% alert color="primary" %}}

[L'espace de noms Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dans [Aspose.PDF for .NET](/pdf/net/) vous permet d'ajouter un tampon dans un fichier PDF existant. Parfois, les utilisateurs ont besoin de faire pivoter le tampon. Dans cet article, nous allons voir comment faire pivoter un tampon autour de son point central.

{{% /alert %}}

## Détails de mise en œuvre

La classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) vous permet d'ajouter un filigrane dans un fichier PDF. Vous pouvez spécifier l'image à ajouter en tant que tampon en utilisant la méthode [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1). La méthode [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) vous permet de définir l'origine du tampon ajouté ; cette origine est les coordonnées inférieures gauche du tampon. Vous pouvez également définir la taille de l'image en utilisant la méthode [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize).

Maintenant, nous allons voir comment le tampon peut être tourné autour du centre du tampon. La classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) fournit une propriété nommée Rotation. Cette propriété définit ou obtient la rotation de 0 à 360 du contenu du tampon. Nous pouvons spécifier n'importe quelle valeur de rotation de 0 à 360. En spécifiant la valeur de rotation, nous pouvons faire pivoter le tampon autour de son point central. Si un tampon est un objet de type Stamp, alors la valeur de rotation peut être spécifiée comme aStamp.Rotation = 90. Dans ce cas, le tampon sera tourné à 90 degrés autour du centre du contenu du tampon. Le code suivant vous montre comment faire pivoter le tampon autour du point central :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRotatingStampToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();  

    // Create PdfFileInfo object to get height and width of the pages
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "RotatingStamp.pdf"))
    {
        // Create Stamp object
        var aStamp = new Aspose.Pdf.Facades.Stamp();

        // Bind image file with the Stamp object
        aStamp.BindImage(dataDir + "RotatingStamp.jpg");

        // Specify whether the stamp will be added as a background or not
        aStamp.IsBackground = false;

        // Specifies at which pages to add the watermark
        aStamp.Pages = new int[] { 1 };

        // Specifies the watermark rotation - rotate at 90 degrees
        aStamp.Rotation = 90;

        // Specifies the position of stamp - lower left corner of the stamp
        aStamp.SetOrigin(fileInfo.GetPageWidth(1) / 2, fileInfo.GetPageHeight(1) / 2);

        // Set the size of the watermark
        aStamp.SetImageSize(100, 100);

        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "RotatingStamp_out.pdf"))
        {
            // Create PdfFileStamp class to bind input and output files
            using (var stamper = new Aspose.Pdf.Facades.PdfFileStamp(document))
            {
                // Add the stamp in the PDF file
                stamper.AddStamp(aStamp);
            }
        }
    }
}
```