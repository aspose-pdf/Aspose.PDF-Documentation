---
title: Ajouter un tampon de page PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/add-pdf-page-stamp/
description: Découvrez comment ajouter des tampons aux pages PDF en .NET, y compris du texte et des images, pour le filigrane ou le branding en utilisant Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Page Stamp",
    "alternativeHeadline": "Enhance PDFs with Custom Stamps and Page Numbers",
    "abstract": "Présentation de la fonctionnalité de tampon de page PDF qui permet aux utilisateurs d'ajouter facilement des tampons personnalisés sur toutes ou certaines pages d'un document PDF en utilisant la classe PdfFileStamp. Cette fonctionnalité améliore la personnalisation des documents en permettant divers attributs tels que la rotation, l'arrière-plan et les styles de numérotation personnalisés pour les tampons de page, rendant vos fichiers PDF non seulement uniques mais aussi professionnellement soignés.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1309",
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
    "url": "/net/add-pdf-page-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pdf-page-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Ajouter un tampon de page PDF sur toutes les pages d'un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter un tampon de page PDF sur toutes les pages d'un fichier PDF. Pour ajouter un tampon de page PDF, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp) et [Stamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf/stamp). Vous devez également créer le tampon de page PDF en utilisant la méthode [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp) de la classe [Stamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf/stamp). Vous pouvez définir d'autres attributs comme l'origine, la rotation, l'arrière-plan, etc. en utilisant également l'objet [Stamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf/stamp). Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [AddStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp). Le code suivant vous montre comment ajouter un tampon de page PDF sur toutes les pages d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "AddPageStampOnAllPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnAllPages_out.pdf");
    }
}
```

## Ajouter un tampon de page PDF sur des pages particulières d'un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter un tampon de page PDF sur des pages particulières d'un fichier PDF. Pour ajouter un tampon de page PDF, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp) et [Stamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf/stamp). Vous devez également créer le tampon de page PDF en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.facade/bindpdf/methods/3) de la classe [Stamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf/stamp). Vous pouvez définir d'autres attributs comme l'origine, la rotation, l'arrière-plan, etc. en utilisant également l'objet [Stamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf/stamp). Comme vous souhaitez ajouter un tampon de page PDF sur des pages particulières du fichier PDF, vous devez également définir la propriété [Pages](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/stamp/properties/pages) de la classe [Stamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf/stamp). Cette propriété nécessite un tableau d'entiers contenant les numéros des pages sur lesquelles vous souhaitez ajouter le tampon. Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [AddStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp). Le code suivant vous montre comment ajouter un tampon de page PDF sur des pages particulières d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnCertainPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "PageStampOnCertainPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;
        stamp.Pages = new[] { 1, 3 };  // Apply stamp to specific pages (1 and 3)

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnCertainPages_out.pdf");
    }
}
```

## Ajouter un numéro de page dans un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp) vous permet d'ajouter des numéros de page dans un fichier PDF. Pour ajouter des numéros de page, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp). Si vous souhaitez afficher le numéro de page comme "Page X sur N" où X est le numéro de la page actuelle et N le nombre total de pages dans le fichier PDF, vous devez d'abord obtenir le nombre de pages en utilisant la propriété [NumberOfpages](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) de la classe [PdfFileInfo](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileinfo). Pour obtenir le numéro de la page actuelle, vous pouvez utiliser le signe **#** dans votre texte où vous le souhaitez. Vous pouvez formater le texte du numéro de page en utilisant la classe [FormattedText](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formattedtext). Si vous souhaitez commencer la numérotation des pages à partir d'un numéro spécifique, vous pouvez définir la propriété [StartingNumber](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber). Une fois que vous êtes prêt à ajouter le numéro de page dans le fichier, vous devez appeler la méthode [AddPageNumber](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [Close](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/facade/methods/close) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp). Le code suivant vous montre comment ajouter un numéro de page dans un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;
        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```

### Style de numérotation personnalisé

La classe PdfFileStamp offre la fonctionnalité d'ajouter des informations de numéro de page en tant qu'objet tampon à l'intérieur du document PDF. Avant cette version, la classe ne supportait que 1,2,3,4 comme style de numérotation des pages. Cependant, il y a eu une demande de certains clients pour utiliser un style de numérotation personnalisé lors de la mise en place d'un tampon de numéro de page à l'intérieur du document PDF. Pour répondre à cette demande, la propriété [NumberingStyle](https://reference.aspose.com/pdf/fr/net/aspose.pdf/numberingstyle) a été introduite, qui accepte les valeurs de l'énumération [NumberingStyle](https://reference.aspose.com/pdf/fr/net/aspose.pdf/numberingstyle). Les valeurs spécifiées ci-dessous sont offertes dans cette énumération.

- LettresMinuscules.
- LettresMajuscules.
- ChiffresArabes.
- ChiffresRomainsMinuscules.
- ChiffresRomainsMajuscules.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCustomPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Specify numbering style as Numerals Roman UpperCase
        fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;

        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddCustomPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```