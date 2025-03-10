---
title: Ajouter un en-tête et un pied de page au PDF
linktitle: Ajouter un en-tête et un pied de page au PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /fr/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for .NET vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant la classe TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Header and Footer to PDF",
    "alternativeHeadline": "Add Custom Headers and Footers to PDF Files",
    "abstract": "Aspose.PDF for .NET introduit une fonctionnalité puissante qui permet aux utilisateurs d'enrichir leurs documents PDF en ajoutant des en-têtes et des pieds de page personnalisables. En utilisant les classes TextStamp et ImageStamp, les développeurs peuvent facilement intégrer à la fois du texte et des images, en adaptant leur placement et leur apparence pour s'adapter à divers formats et styles de documents. Cela améliore le professionnalisme et la lisibilité des documents, ce qui le rend idéal pour les rapports, les factures et autres communications formelles.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1549",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant la classe TextStamp."
}
</script>

**Aspose.PDF for .NET** vous permet d'ajouter un en-tête et un pied de page dans votre fichier PDF existant. Vous pouvez ajouter des images ou du texte à un document PDF. Essayez également d'ajouter différents en-têtes dans un fichier PDF avec C#.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Ajouter du texte dans l'en-tête du fichier PDF

Vous pouvez utiliser la classe [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) pour ajouter du texte dans l'en-tête d'un fichier PDF. La classe TextStamp fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de police, le style de police et la couleur de police, etc. Pour ajouter du texte dans l'en-tête, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter le texte dans l'en-tête du PDF.

Vous devez définir la propriété TopMargin de manière à ce qu'elle ajuste le texte dans la zone d'en-tête de votre PDF. Vous devez également définir HorizontalAlignment sur Center et VerticalAlignment sur Top.

Le code suivant vous montre comment ajouter du texte dans l'en-tête d'un fichier PDF avec C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHeaderText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinHeader.pdf"))
    {
        // Create header as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Header Text")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinHeader_out.pdf");
    }
}
```

## Ajouter du texte dans le pied de page du fichier PDF

Vous pouvez utiliser la classe TextStamp pour ajouter du texte dans le pied de page d'un fichier PDF. La classe TextStamp fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de police, le style de police et la couleur de police, etc. Pour ajouter du texte dans le pied de page, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter le texte dans le pied de page du PDF.

{{% alert color="primary" %}}

Vous devez définir la propriété Bottom Margin de manière à ce qu'elle ajuste le texte dans la zone de pied de page de votre PDF. Vous devez également définir HorizontalAlignment sur Center et VerticalAlignment sur Bottom.

{{% /alert %}}

Le code suivant vous montre comment ajouter du texte dans le pied de page d'un fichier PDF avec C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFooterText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextinFooter.pdf"))
    {
        // Create footer as a TextStamp
        var textStamp = new Aspose.Pdf.TextStamp("Footer Text")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(textStamp);
        }

        // Save PDF document
        document.Save(dataDir + "TextinFooter_out.pdf");
    }
}
```

## Ajouter une image dans l'en-tête du fichier PDF

Vous pouvez utiliser la classe [ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) pour ajouter une image dans l'en-tête d'un fichier PDF. La classe Image Stamp fournit les propriétés nécessaires pour créer un tampon basé sur une image comme la taille de police, le style de police et la couleur de police, etc. Pour ajouter une image dans l'en-tête, vous devez créer un objet Document et un objet Image Stamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) de la Page pour ajouter l'image dans l'en-tête du PDF.

{{% alert color="primary" %}}

Vous devez définir la propriété TopMargin de manière à ce qu'elle ajuste l'image dans la zone d'en-tête de votre PDF. Vous devez également définir HorizontalAlignment sur Center et VerticalAlignment sur Top.

{{% /alert %}}

Le code suivant vous montre comment ajouter une image dans l'en-tête d'un fichier PDF avec C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageHeader()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageinHeader.pdf"))
    {
        // Create header as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            TopMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top
        };

        // Add image header on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageinHeader_out.pdf");
    }
}
```

## Ajouter une image dans le pied de page du fichier PDF

Vous pouvez utiliser la classe Image Stamp pour ajouter une image dans le pied de page d'un fichier PDF. La classe Image Stamp fournit les propriétés nécessaires pour créer un tampon basé sur une image comme la taille de police, le style de police et la couleur de police, etc. Pour ajouter une image dans le pied de page, vous devez créer un objet Document et un objet Image Stamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter l'image dans le pied de page du PDF.

{{% alert color="primary" %}}

Vous devez définir la propriété [BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) de manière à ce qu'elle ajuste l'image dans la zone de pied de page de votre PDF. Vous devez également définir [HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment) sur `Center` et [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment) sur `Bottom`.

{{% /alert %}}

Le code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF avec C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageFooter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInFooter.pdf"))
    {
        // Create footer as an ImageStamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            BottomMargin = 10,
            HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center,
            VerticalAlignment = Aspose.Pdf.VerticalAlignment.Bottom
        };

        // Add image footer on all pages
        foreach (var page in document.Pages)
        {
            page.AddStamp(imageStamp);
        }

        // Save PDF document
        document.Save(dataDir + "ImageInFooter_out.pdf");
    }
}
```

## Ajouter différents en-têtes dans un fichier PDF

Nous savons que nous pouvons ajouter TextStamp dans la section En-tête/Pied de page du document en utilisant les propriétés TopMargin ou Bottom Margin, mais parfois nous pouvons avoir besoin d'ajouter plusieurs en-têtes/pieds de page dans un seul document PDF. **Aspose.PDF for .NET** explique comment faire cela.

Pour accomplir cette exigence, nous allons créer des objets TextStamp individuels (le nombre d'objets dépend du nombre d'en-têtes/pieds de page requis) et les ajouter au document PDF. Nous pouvons également spécifier différentes informations de formatage pour chaque objet tampon. Dans l'exemple suivant, nous avons créé un objet Document et trois objets TextStamp, puis nous avons utilisé la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) de la Page pour ajouter le texte dans la section d'en-tête du PDF. Le code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF avec Aspose.PDF for .NET.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddDifferentHeaders()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddingDifferentHeaders.pdf"))
    {
        // Create three stamps
        var stamp1 = new Aspose.Pdf.TextStamp("Header 1");
        var stamp2 = new Aspose.Pdf.TextStamp("Header 2");
        var stamp3 = new Aspose.Pdf.TextStamp("Header 3");

        // Set stamp1 properties (Header 1)
        stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        stamp1.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
        stamp1.TextState.FontSize = 14;

        // Set stamp2 properties (Header 2)
        stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp2.Zoom = 10;

        // Set stamp3 properties (Header 3)
        stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        stamp3.RotateAngle = 35;
        stamp3.TextState.BackgroundColor = Aspose.Pdf.Color.Pink;
        stamp3.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Verdana");

        // Add the stamps to specific pages
        document.Pages[1].AddStamp(stamp1);
        document.Pages[2].AddStamp(stamp2);
        document.Pages[3].AddStamp(stamp3);

        // Save PDF document
        document.Save(dataDir + "MultiHeader_out.pdf");
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