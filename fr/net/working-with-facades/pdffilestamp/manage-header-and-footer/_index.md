---
title: Gérer l'en-tête et le pied de page
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/manage-header-and-footer/
description: Explorez comment manipuler les en-têtes et les pieds de page dans les fichiers PDF en .NET avec Aspose.PDF pour une meilleure structuration des documents.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manage Header and Footer",
    "alternativeHeadline": "Enhance PDFs with Custom Headers and Footers",
    "abstract": "Les fonctionnalités Gérer l'en-tête et le pied de page dans Aspose.PDF for .NET permettent aux utilisateurs d'ajouter, de personnaliser et de formater facilement les en-têtes et les pieds de page dans les documents PDF en utilisant la classe PdfFileStamp. Cette fonctionnalité prend en charge l'inclusion de texte et d'images, offrant une flexibilité dans la présentation des documents tout en garantissant un formatage professionnel. Les utilisateurs peuvent intégrer cette fonctionnalité dans leurs applications pour améliorer l'attrait visuel et l'organisation des fichiers PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1007",
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
    "url": "/net/manage-header-and-footer/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manage-header-and-footer/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Ajouter un en-tête dans un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) vous permet d'ajouter un en-tête dans un fichier PDF. Pour ajouter un en-tête, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Vous pouvez formater le texte de l'en-tête en utilisant la classe [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Une fois que vous êtes prêt à ajouter l'en-tête dans le fichier, vous devez appeler la méthode [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Vous devez également spécifier au moins la marge supérieure dans la méthode [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Le code suivant montre comment ajouter un en-tête dans un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create formatted text for the header
        var formattedText = new Aspose.Pdf.Facades.FormattedText(
            "Aspose - Your File Format Experts!",
            System.Drawing.Color.Yellow,
            System.Drawing.Color.Black,
            Aspose.Pdf.Facades.FontStyle.Courier,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false,
            14);

        // Add header
        fileStamp.AddHeader(formattedText, 10);

        // Save PDF document
        fileStamp.Save(dataDir + "AddHeader_out.pdf");
    }
}
```

## Ajouter un pied de page dans un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) vous permet d'ajouter un pied de page dans un fichier PDF. Pour ajouter un pied de page, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Vous pouvez formater le texte du pied de page en utilisant la classe [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Une fois que vous êtes prêt à ajouter le pied de page dans le fichier, vous devez appeler la méthode [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Vous devez également spécifier au moins la marge inférieure dans la méthode [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Le code suivant montre comment ajouter un pied de page dans un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create formatted text for the footer
        var formattedText = new Aspose.Pdf.Facades.FormattedText(
            "Aspose - Your File Format Experts!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Courier,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false,
            14);

        // Add footer
        fileStamp.AddFooter(formattedText, 10);

        // Save PDF document
        fileStamp.Save(dataDir + "AddFooter_out.pdf");
    }
}
```

## Ajouter une image dans l'en-tête d'un fichier PDF existant

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) vous permet d'ajouter une image dans l'en-tête d'un fichier PDF. Pour ajouter une image dans l'en-tête, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Après cela, vous devez appeler la méthode [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Vous pouvez passer l'image à la méthode [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Le code suivant montre comment ajouter une image dans l'en-tête d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Add Header
        using (var fs = new FileStream(dataDir + "ImageHeader.png", FileMode.Open))
        {
            fileStamp.AddHeader(fs, 10);  // Add image header with position offset

            // Save PDF document
            fileStamp.Save(dataDir + "AddImageHeader_out.pdf");
        }
    }
}
```

## Ajouter une image dans le pied de page d'un fichier PDF existant

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) vous permet d'ajouter une image dans le pied de page d'un fichier PDF. Pour ajouter une image dans le pied de page, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Après cela, vous devez appeler la méthode [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Vous pouvez passer l'image à la méthode [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main). Le code suivant montre comment ajouter une image dans le pied de page d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Add footer
        using (var fs = new FileStream(dataDir + "ImageFooter.png", FileMode.Open))
        {
            fileStamp.AddFooter(fs, 10);  // Add image footer with position offset

            // Save PDF document
            fileStamp.Save(dataDir + "AddImageFooter_out.pdf");
        }
    }
}
```