---
title: Extraire des images à l'aide de PdfExtractor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/extract-images/
description: Cette section explique comment extraire des images avec Aspose.PDF Facades en utilisant la classe PdfExtractor.
lastmod: "2021-07-15"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images using PdfExtractor",
    "alternativeHeadline": "Extract Images from PDF with PdfExtractor Class",
    "abstract": "La fonctionnalité PdfExtractor d'Aspose.PDF permet aux utilisateurs d'extraire efficacement des images de documents PDF, offrant plusieurs options telles que l'extraction d'images de l'ensemble du document, de pages spécifiques ou de plages spécifiées. Elle prend en charge l'enregistrement des images directement dans des fichiers ou des flux mémoire, améliorant la flexibilité pour les développeurs travaillant avec des actifs PDF. Cette fonctionnalité puissante permet un contrôle précis sur les modes d'extraction d'images, facilitant la gestion des différents types de contenu PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1789",
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
    "url": "/net/extract-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Extraire des images de l'ensemble du PDF vers des fichiers (Facades)

La classe [PdfExtractor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor) vous permet d'extraire des images d'un fichier PDF. Tout d'abord, vous devez créer un objet de la classe [PdfExtractor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/facade/methods/bindpdf/index). Après cela, appelez la méthode [ExtractImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/methods/extractimage) pour extraire toutes les images en mémoire. Une fois les images extraites, vous pouvez obtenir ces images avec l'aide des méthodes [HasNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) et [GetNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Vous devez parcourir toutes les images extraites à l'aide d'une boucle while. Pour enregistrer les images sur le disque, vous pouvez appeler la surcharge de la méthode [GetNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) qui prend le chemin du fichier comme argument. Le code suivant vous montre comment extraire des images de l'ensemble du PDF vers des fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract all the images
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
    }
}
```

## Extraire des images de l'ensemble du PDF vers des flux (Facades)

La classe [PdfExtractor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor) vous permet d'extraire des images d'un fichier PDF vers des flux. Tout d'abord, vous devez créer un objet de la classe [PdfExtractor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/facade/methods/bindpdf/index). Après cela, appelez la méthode [ExtractImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/methods/extractimage) pour extraire toutes les images en mémoire. Une fois les images extraites, vous pouvez obtenir ces images avec l'aide des méthodes [HasNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) et [GetNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Vous devez parcourir toutes les images extraites à l'aide d'une boucle while. Pour enregistrer les images dans un flux, vous pouvez appeler la surcharge de la méthode [GetNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) qui prend un flux comme argument. Le code suivant vous montre comment extraire des images de l'ensemble du PDF vers des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDFStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract images
        extractor.ExtractImage();
        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Extraire des images d'une page particulière d'un PDF (Facades)

Vous pouvez extraire des images d'une page particulière d'un fichier PDF. Pour ce faire, vous devez définir les propriétés [StartPage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/properties/startpage) et [EndPage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/properties/endpage) sur la page particulière dont vous souhaitez extraire les images. Tout d'abord, vous devez créer un objet de la classe [PdfExtractor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/facade/methods/bindpdf/index). Deuxièmement, vous devez définir les propriétés [StartPage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/properties/startpage) et [EndPage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/properties/endpage). Après cela, appelez la méthode [ExtractImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/methods/extractimage) pour extraire toutes les images en mémoire. Une fois les images extraites, vous pouvez obtenir ces images avec l'aide des méthodes [HasNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) et [GetNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Vous devez parcourir toutes les images extraites à l'aide d'une boucle while. Vous pouvez soit enregistrer les images sur le disque, soit dans un flux. Vous devez simplement appeler la surcharge appropriée de la méthode [GetNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Le code suivant vous montre comment extraire des images d'une page particulière d'un PDF vers des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();
        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Extraire des images d'une plage de pages d'un PDF (Facades)

Vous pouvez extraire des images d'une plage de pages d'un fichier PDF. Pour ce faire, vous devez définir les propriétés [StartPage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/properties/startpage) et [EndPage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/properties/endpage) sur la plage de pages dont vous souhaitez extraire les images. Tout d'abord, vous devez créer un objet de la classe [PdfExtractor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/facade/methods/bindpdf/index). Deuxièmement, vous devez définir les propriétés [StartPage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/properties/startpage) et [EndPage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/properties/endpage). Après cela, appelez la méthode [ExtractImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/methods/extractimage) pour extraire toutes les images en mémoire. Une fois les images extraites, vous pouvez obtenir ces images avec l'aide des méthodes [HasNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) et [GetNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Vous devez parcourir toutes les images extraites à l'aide d'une boucle while. Vous pouvez soit enregistrer les images sur le disque, soit dans un flux. Vous devez simplement appeler la surcharge appropriée de la méthode [GetNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Le code suivant vous montre comment extraire des images d'une plage de pages d'un PDF vers des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesRangePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open input PDF
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();

        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new
            FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Extraire des images en utilisant le mode d'extraction d'images (Facades)

La classe [PdfExtractor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor) vous permet d'extraire des images d'un fichier PDF. Aspose.PDF prend en charge deux modes d'extraction ; le premier est ActuallyUsedImage qui extrait les images réellement utilisées dans le document PDF. Le deuxième mode est [DefinedInResources](https://reference.aspose.com/pdf/fr/net/aspose.pdf/extractimagemode) qui extrait les images définies dans les ressources du document PDF (mode d'extraction par défaut). Tout d'abord, vous devez créer un objet de la classe [PdfExtractor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/facade/methods/bindpdf/index). Après cela, spécifiez le mode d'extraction d'images en utilisant la propriété [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode). Ensuite, appelez la méthode [ExtractImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/methods/extractimage) pour extraire toutes les images en mémoire en fonction du mode que vous avez spécifié. Une fois les images extraites, vous pouvez obtenir ces images avec l'aide des méthodes [HasNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) et [GetNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Vous devez parcourir toutes les images extraites à l'aide d'une boucle while. Pour enregistrer les images sur le disque, vous pouvez appeler la surcharge de la méthode [GetNextImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) qui prend le chemin du fichier comme argument.

Le code suivant vous montre comment extraire des images d'un fichier PDF en utilisant l'option ExtractImageMode.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesImageExtractionMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Specify Image Extraction Mode
        //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
        extractor.ExtractImageMode = Aspose.Pdf.ExtractImageMode.DefinedInResources;

        // Extract Images based on Image Extraction Mode
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
        }
    }
}
```

Pour vérifier si le PDF contient du texte ou des images, utilisez le code suivant :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Instantiate a memoryStream object to hold the extracted text from Document
    MemoryStream ms = new MemoryStream();
    // Instantiate PdfExtractor object
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "FilledForm.pdf");
        // Extract text from the input PDF document
        extractor.ExtractText();
        // Save the extracted text to a text file
        extractor.GetText(ms);
        // Check if the MemoryStream length is greater than or equal to 1

        bool containsText = ms.Length >= 1;

        // Extract images from the input PDF document
        extractor.ExtractImage();

        // Calling HasNextImage method in while loop. When images will finish, loop will exit
        bool containsImage = extractor.HasNextImage();

        // Now find out whether this PDF is text only or image only

        if (containsText && !containsImage)
        {
            Console.WriteLine("PDF contains text only");
        }
        else if (!containsText && containsImage)
        {
            Console.WriteLine("PDF contains image only");
        }
        else if (containsText && containsImage)
        {
            Console.WriteLine("PDF contains both text and image");
        }
        else if (!containsText && !containsImage)
        {
            Console.WriteLine("PDF contains neither text or nor image");
        }
    }
}
```