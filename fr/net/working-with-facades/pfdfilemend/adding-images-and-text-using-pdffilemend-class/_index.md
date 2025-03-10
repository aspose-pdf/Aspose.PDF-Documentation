---
title: Ajouter des images et du texte
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/adding-images-and-text-using-pdffilemend-class/
description: Cette section explique comment ajouter des images et du texte en utilisant la classe PdfFileMend.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Images and Text",
    "alternativeHeadline": "Enhance PDF by Adding Images and Text Precisely",
    "abstract": "Améliorez vos documents PDF sans effort avec la nouvelle classe PdfFileMend, qui vous permet d'ajouter des images et du texte à des emplacements spécifiés dans des PDF existants. Utilisez les méthodes intuitives AddImage et AddText pour intégrer divers formats d'image et du texte formaté de manière transparente, garantissant une précision dans le placement et la sélection des pages. Rationalisez vos tâches de manipulation de PDF avec la possibilité de personnaliser les superpositions d'images et le retour à la ligne du texte, rendant vos documents visuellement attrayants et informatifs.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1324",
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
    "url": "/net/adding-images-and-text-using-pdffilemend-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-images-and-text-using-pdffilemend-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

La classe [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) peut vous aider à ajouter des images et du texte dans un document PDF existant, à un emplacement spécifié. Elle fournit deux méthodes nommées [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) et [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). La méthode [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) vous permet d'ajouter des images de type JPG, GIF, PNG et BMP. La méthode [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) prend un argument de type [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) et l'ajoute dans le fichier PDF existant. Les images et le texte peuvent être ajoutés dans une région rectangulaire spécifiée par les coordonnées des points inférieur gauche et supérieur droit. Lors de l'ajout d'images, vous pouvez spécifier soit le chemin du fichier image, soit un flux d'un fichier image. Afin de spécifier le numéro de page sur lequel l'image ou le texte doit être ajouté, ces deux méthodes fournissent un argument de numéro de page. Ainsi, vous pouvez non seulement ajouter les images et le texte à l'emplacement spécifié, mais aussi sur une page spécifiée.

Les images sont une partie importante du contenu d'un document PDF. Manipuler des images dans un fichier PDF existant est une exigence courante pour les personnes travaillant avec des fichiers PDF. Dans cet article, nous explorerons comment les images peuvent être manipulées, dans un fichier PDF existant, avec l'aide de l'espace de noms [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) de [Aspose.PDF for .NET](/pdf/fr/net/). Toutes les opérations liées aux images de l'espace de noms [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) ont été consolidées dans cet article.

## Détails de mise en œuvre

L'espace de noms [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) vous permet d'ajouter de nouvelles images dans un fichier PDF existant. Vous pouvez également remplacer ou supprimer une image existante. Un fichier PDF peut également être converti en images. Vous pouvez soit convertir chaque page individuelle en une seule image, soit un fichier PDF complet en une image. Il vous permet de formats c'est-à-dire JPEG, BMP, PNG et TIFF, etc. Vous pouvez également extraire les images d'un fichier PDF. Vous pouvez utiliser quatre classes de l'espace de noms [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) pour mettre en œuvre ces opérations, à savoir [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) et [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter).

## Opérations sur les images

Dans cette section, nous examinerons en détail ces opérations sur les images. Nous verrons également des extraits de code pour montrer l'utilisation des classes et méthodes associées. Tout d'abord, examinons l'ajout d'une image dans un fichier PDF existant. Nous pouvons utiliser la méthode [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) de la classe [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) pour ajouter une nouvelle image. En utilisant cette méthode, vous pouvez non seulement spécifier le numéro de page sur lequel vous souhaitez ajouter l'image, mais également l'emplacement de l'image.

## Ajouter une image dans un fichier PDF existant (Facades)

Vous pouvez utiliser la méthode [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) de la classe [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend). La méthode [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) nécessite l'image à ajouter, le numéro de page sur lequel l'image doit être ajoutée et les informations de coordonnées. Après cela, enregistrez le fichier PDF mis à jour en utilisant la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close).

Dans l'exemple suivant, nous ajoutons une image à la page en utilisant imageStream :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images(); 

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                // Add image to first page
                mender.AddImage(imageStream, 1, 10, 650, 110, 750);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![Ajouter une image](/pdf/fr/net/images/add_image1.png)

Avec l'aide de [CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1), nous pouvons superposer une image sur une autre :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters for the image
                var compositingParameters = new Aspose.Pdf.CompositingParameters(Aspose.Pdf.BlendMode.Multiply);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![Ajouter une image](/pdf/fr/net/images/add_image2.png)

Il existe plusieurs façons de stocker une image dans un fichier PDF. Nous allons en démontrer une dans l'exemple suivant :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Exclusion and ImageFilterType.Flate
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Exclusion,
                    Aspose.Pdf.ImageFilterType.Flate);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Multiply, ImageFilterType.Flate and false
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Multiply,
                    Aspose.Pdf.ImageFilterType.Flate,
                    false);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_outp.pdf");
            }
        }
    }
}
```

## Ajouter du texte dans un fichier PDF existant (facades)

Nous pouvons ajouter du texte de plusieurs manières. Considérons la première. Nous prenons le [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) et l'ajoutons à la page. Ensuite, nous indiquons les coordonnées du coin inférieur gauche, puis nous ajoutons notre texte à la page.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

        // Add text to the first page at position (10, 750)
        mender.AddText(message, 1, 10, 750);

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

Vérifiez à quoi cela ressemble :

![Ajouter du texte](/pdf/fr/net/images/add_text.png)

La deuxième façon d'ajouter [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). De plus, nous indiquons un rectangle dans lequel notre texte doit s'adapter.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose! Welcome to Aspose!");

        // Add text to the first page at the specified position with wrapping
        mender.AddText(message, 1, 10, 700, 55, 810);

        // Set word wrapping mode to wrap by words
        mender.WrapMode = Aspose.Pdf.Facades.WordWrapMode.ByWords;

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

Le troisième exemple offre la possibilité d'ajouter du texte à des pages spécifiées. Dans notre exemple, ajoutons une légende sur les pages 1 et 3 du document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();

        // Create PdfFileMend object
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Bind PDF document
            mender.BindPdf(document);

            // Create formatted text
            var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

            // Specify the pages where text should be added
            int[] pageNums = new int[] { 1, 3 };

            // Add text to the specified pages at the specified coordinates
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // Save PDF document
            mender.Save(dataDir + "AddText_out.pdf");
        }
    }
}
```