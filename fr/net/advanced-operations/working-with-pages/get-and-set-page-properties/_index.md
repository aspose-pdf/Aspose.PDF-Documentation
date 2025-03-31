---
title: Obtenir et définir les propriétés de page
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /fr/net/get-and-set-page-properties/
description: Apprenez à obtenir et à définir les propriétés de page pour les documents PDF en utilisant Aspose.PDF for .NET, permettant un formatage personnalisé des documents.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Set Page Properties",
    "alternativeHeadline": "Manage PDF Page Properties with Ease",
    "abstract": "La fonctionnalité Obtenir et définir les propriétés de page dans Aspose.PDF for .NET permet aux développeurs d'accéder et de manipuler facilement les attributs de page PDF. Cette fonctionnalité permet aux utilisateurs de récupérer des informations critiques, telles que le nombre de pages et des propriétés spécifiques comme les types de couleur, les media boxes et les trim boxes, le tout en quelques lignes de code. Améliorez vos capacités de gestion de documents PDF dès aujourd'hui en tirant parti de cette fonctionnalité robuste pour une manipulation efficace des PDF dans les applications .NET.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1117",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

Aspose.PDF for .NET vous permet de lire et de définir les propriétés des pages dans un fichier PDF dans vos applications .NET. Cette section montre comment obtenir le nombre de pages dans un fichier PDF, obtenir des informations sur les propriétés des pages PDF telles que la couleur et définir les propriétés de page. Les exemples donnés sont en C#, mais vous pouvez utiliser n'importe quel langage .NET tel que VB.NET pour atteindre le même résultat.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Obtenir le nombre de pages dans un fichier PDF

Lorsque vous travaillez avec des documents, vous souhaitez souvent savoir combien de pages ils contiennent. Avec Aspose.PDF, cela ne prend pas plus de deux lignes de code.

Pour obtenir le nombre de pages dans un fichier PDF :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document).
1. Ensuite, utilisez la propriété Count de la collection [PageCollection](https://reference.aspose.com/pdf/fr/net/aspose.pdf/pagecollection) (de l'objet Document) pour obtenir le nombre total de pages dans le document.

Le code suivant montre comment obtenir le nombre de pages d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetNumberOfPagesInAPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetNumberofPages.pdf"))
    {
        // Get page count
        System.Console.WriteLine("Page Count : {0}", document.Pages.Count);
    }
}
```

### Obtenir le nombre de pages sans enregistrer le document

Parfois, nous générons les fichiers PDF à la volée et lors de la création du fichier PDF, nous pouvons rencontrer le besoin (création de table des matières, etc.) d'obtenir le nombre de pages du fichier PDF sans enregistrer le fichier sur le système ou le flux. Afin de répondre à ce besoin, une méthode [ProcessParagraphs](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/methods/processparagraphs) a été introduite dans la classe Document. Veuillez consulter le code suivant qui montre les étapes pour obtenir le nombre de pages sans enregistrer le document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPageCountWithoutSavingTheDocument()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create loop instance
        for (var i = 0; i < 300; i++)
        {
            // Add TextFragment to paragraphs collection of page object
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Pages count test"));
        }
        // Process the paragraphs in PDF file to get accurate page count
        document.ProcessParagraphs();
        // Print number of pages in document
        Console.WriteLine("Number of pages in document = " + document.Pages.Count);
    }
}
```

## Obtenir les propriétés de page

Chaque page d'un fichier PDF a un certain nombre de propriétés, telles que la largeur, la hauteur, le bleed box, le crop box et le trim box. Aspose.PDF vous permet d'accéder à ces propriétés.

### **Comprendre les propriétés de page : la différence entre Artbox, BleedBox, CropBox, MediaBox, TrimBox et propriété Rect**

- **Media box** : La media box est la plus grande boîte de page. Elle correspond à la taille de la page (par exemple A4, A5, US Letter, etc.) sélectionnée lorsque le document a été imprimé en PostScript ou PDF. En d'autres termes, la media box détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **Bleed box** : Si le document a un bleed, le PDF aura également une bleed box. Le bleed est la quantité de couleur (ou d'œuvre) qui s'étend au-delà du bord d'une page. Il est utilisé pour s'assurer que lorsque le document est imprimé et découpé à la taille ("découpé"), l'encre ira jusqu'au bord de la page. Même si la page est mal découpée - légèrement en dehors des marques de découpe - aucun bord blanc n'apparaîtra sur la page.
- **Trim box** : La trim box indique la taille finale d'un document après impression et découpe.
- **Art box** : La art box est la boîte dessinée autour des contenus réels des pages de vos documents. Cette boîte de page est utilisée lors de l'importation de documents PDF dans d'autres applications.
- **Crop box** : La crop box est la taille de la "page" à laquelle votre document PDF est affiché dans Adobe Acrobat. En vue normale, seuls les contenus de la crop box sont affichés dans Adobe Acrobat.
  Pour des descriptions détaillées de ces propriétés, lisez la spécification Adobe.Pdf, en particulier 10.10.1 Page Boundaries.
- **Page.Rect** : l'intersection (rectangle communément visible) de la MediaBox et de la DropBox. L'image ci-dessous illustre ces propriétés.

Pour plus de détails, veuillez visiter [cette page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Accéder aux propriétés de page**

La classe [Page](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page) fournit toutes les propriétés liées à une page PDF particulière. Toutes les pages des fichiers PDF sont contenues dans la collection [PageCollection](https://reference.aspose.com/pdf/fr/net/aspose.pdf/pagecollection) de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document).

À partir de là, il est possible d'accéder soit à des objets Page individuels en utilisant leur index, soit de parcourir la collection, en utilisant une boucle foreach, pour obtenir toutes les pages. Une fois qu'une page individuelle est accessible, nous pouvons obtenir ses propriétés. Le code suivant montre comment obtenir les propriétés de page.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessingPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetProperties.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Get page properties
        System.Console.WriteLine("ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.ArtBox.Height, pdfPage.ArtBox.Width, pdfPage.ArtBox.LLX,
            pdfPage.ArtBox.LLY, pdfPage.ArtBox.URX, pdfPage.ArtBox.URY);
        System.Console.WriteLine("BleedBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.BleedBox.Height, pdfPage.BleedBox.Width, pdfPage.BleedBox.LLX,
            pdfPage.BleedBox.LLY, pdfPage.BleedBox.URX, pdfPage.BleedBox.URY);
        System.Console.WriteLine("CropBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.CropBox.Height, pdfPage.CropBox.Width, pdfPage.CropBox.LLX,
            pdfPage.CropBox.LLY, pdfPage.CropBox.URX, pdfPage.CropBox.URY);
        System.Console.WriteLine("MediaBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.MediaBox.Height, pdfPage.MediaBox.Width, pdfPage.MediaBox.LLX,
            pdfPage.MediaBox.LLY, pdfPage.MediaBox.URX, pdfPage.MediaBox.URY);
        System.Console.WriteLine("TrimBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.TrimBox.Height, pdfPage.TrimBox.Width, pdfPage.TrimBox.LLX,
            pdfPage.TrimBox.LLY, pdfPage.TrimBox.URX, pdfPage.TrimBox.URY);
        System.Console.WriteLine("Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.Rect.Height, pdfPage.Rect.Width, pdfPage.Rect.LLX, pdfPage.Rect.LLY,
            pdfPage.Rect.URX, pdfPage.Rect.URY);
        System.Console.WriteLine("Page Number : {0}", pdfPage.Number);
        System.Console.WriteLine("Rotate : {0}", pdfPage.Rotate);
    }
}
```

## Obtenir une page particulière du fichier PDF

Aspose.PDF vous permet de [diviser un PDF en pages individuelles](/pdf/fr/net/split-pdf-document/) et de les enregistrer en tant que fichiers PDF. Obtenir une page spécifiée dans un fichier PDF et l'enregistrer en tant que nouveau PDF est une opération très similaire : ouvrez le document source, accédez à la page, créez un nouveau document et ajoutez la page à celui-ci.

La collection [PageCollection](https://reference.aspose.com/pdf/fr/net/aspose.pdf/pagecollection) de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document) contient les pages du fichier PDF. Pour obtenir une page particulière de cette collection :

1. Spécifiez l'index de la page en utilisant la propriété Pages.
1. Créez un nouvel objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document).
1. Ajoutez l'objet [Page](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page) au nouvel objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document).
1. Enregistrez la sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf.document/save/methods/4).

Le code suivant montre comment obtenir une page particulière d'un fichier PDF et l'enregistrer en tant que nouveau fichier.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAParticularPageOfThePdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get particular page
        var pdfPage = document.Pages[2];
        // Save the page as PDF file
        using (var newDocument = new Aspose.Pdf.Document())
        {
            newDocument.Pages.Add(pdfPage);
            // Save PDF document
            newDocument.Save(dataDir + "GetParticularPage_out.pdf");
        }
    }
}
```

## Déterminer la couleur de la page

La classe [Page](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page) fournit les propriétés liées à une page particulière dans un document PDF, y compris le type de couleur - RGB, noir et blanc, niveaux de gris ou indéfini - utilisé par la page.

Toutes les pages des fichiers PDF sont contenues dans la collection [PageCollection](https://reference.aspose.com/pdf/fr/net/aspose.pdf/pagecollection). La propriété ColorType spécifie la couleur des éléments sur la page. Pour obtenir ou déterminer les informations de couleur pour une page PDF particulière, utilisez la propriété [ColorType](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page/properties/colortype) de l'objet [Page](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page).

Le code suivant montre comment parcourir chaque page d'un fichier PDF pour obtenir des informations de couleur.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeterminePageColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through all the page of PDF file
        for (var pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Get the color type information for particular PDF page
            Aspose.Pdf.ColorType pageColorType = document.Pages[pageCount].ColorType;
            switch (pageColorType)
            {
                case Aspose.Pdf.ColorType.BlackAndWhite:
                    Console.WriteLine("Page # -" + pageCount + " is Black and white..");
                    break;
                case Aspose.Pdf.ColorType.Grayscale:
                    Console.WriteLine("Page # -" + pageCount + " is Gray Scale...");
                    break;
                case Aspose.Pdf.ColorType.Rgb:
                    Console.WriteLine("Page # -" + pageCount + " is RGB..", pageCount);
                    break;
                case Aspose.Pdf.ColorType.Undefined:
                    Console.WriteLine("Page # -" + pageCount + " Color is undefined..");
                    break;
            }
        }
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