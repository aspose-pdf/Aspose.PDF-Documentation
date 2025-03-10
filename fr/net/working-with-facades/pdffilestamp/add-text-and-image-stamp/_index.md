---
title: Ajouter un tampon de texte et d'image
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/add-text-and-image-stamp/
description: Cette section explique comment ajouter un tampon de texte et d'image avec Aspose.PDF Facades en utilisant la classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text and Image Stamp",
    "alternativeHeadline": "Add Custom Text and Image Stamps in PDFs",
    "abstract": "Les fonctionnalités Ajouter un tampon de texte et d'image dans Aspose.PDF for .NET permettent aux utilisateurs d'appliquer facilement des tampons de texte et d'image personnalisés sur toutes ou certaines pages de documents PDF. Cette fonctionnalité améliore la personnalisation des documents, permettant un contrôle détaillé sur les attributs du tampon tels que la position, la rotation et la qualité, améliorant ainsi la présentation et la marque de vos fichiers PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1435",
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
    "url": "/net/add-text-and-image-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-and-image-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Ajouter un tampon de texte sur toutes les pages d'un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter un tampon de texte sur toutes les pages d'un fichier PDF. Pour ajouter un tampon de texte, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) et [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous devez également créer le tampon de texte en utilisant la méthode [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous pouvez définir d'autres attributs comme l'origine, la rotation, l'arrière-plan, etc. en utilisant également l'objet [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Le code suivant vous montre comment ajouter un tampon de texte sur toutes les pages d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));

        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnAllPages_out.pdf");
    }
}
```

## Ajouter un tampon de texte sur des pages particulières d'un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter un tampon de texte sur des pages particulières d'un fichier PDF. Pour ajouter un tampon de texte, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) et [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous devez également créer le tampon de texte en utilisant la méthode [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous pouvez définir d'autres attributs comme l'origine, la rotation, l'arrière-plan, etc. en utilisant également l'objet [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Comme vous souhaitez ajouter un tampon de texte sur des pages particulières du fichier PDF, vous devez également définir la propriété [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Cette propriété nécessite un tableau d'entiers contenant les numéros des pages sur lesquelles vous souhaitez ajouter le tampon. Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Le code suivant vous montre comment ajouter un tampon de texte sur des pages particulières d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));
        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnParticularPages_out.pdf");
    }
}
```

## Ajouter un tampon d'image sur toutes les pages d'un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter un tampon d'image sur toutes les pages d'un fichier PDF. Pour ajouter un tampon d'image, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) et [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous devez également créer le tampon d'image en utilisant la méthode [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous pouvez définir d'autres attributs comme l'origine, la rotation, l'arrière-plan, etc. en utilisant également l'objet [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Le code suivant vous montre comment ajouter un tampon d'image sur toutes les pages d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnAllPages_out.pdf");
    }
}
```

### Contrôler la qualité de l'image lors de l'ajout en tant que tampon

Lors de l'ajout d'une image en tant qu'objet tampon, vous pouvez également contrôler la qualité de l'image. Pour répondre à cette exigence, la propriété Quality a été ajoutée pour la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Elle indique la qualité de l'image en pourcentage (les valeurs valides sont 0..100).

## Ajouter un tampon d'image sur des pages particulières d'un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter un tampon d'image sur des pages particulières d'un fichier PDF. Pour ajouter un tampon d'image, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) et [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous devez également créer le tampon d'image en utilisant la méthode [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Vous pouvez définir d'autres attributs comme l'origine, la rotation, l'arrière-plan, etc. en utilisant également l'objet [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Comme vous souhaitez ajouter un tampon d'image sur des pages particulières du fichier PDF, vous devez également définir la propriété [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) de la classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Cette propriété nécessite un tableau d'entiers contenant les numéros des pages sur lesquelles vous souhaitez ajouter le tampon. Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Le code suivant vous montre comment ajouter un tampon d'image sur des pages particulières d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnParticularPages_out.pdf");
    }
}
```