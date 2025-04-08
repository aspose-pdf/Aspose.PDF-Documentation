---
title: Ajouter une image à un PDF en utilisant C#
linktitle: Ajouter une image
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/add-image-to-existing-pdf-file/
description: Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant la bibliothèque C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Image to PDF using C#",
    "alternativeHeadline": "Add Images PDFs in C#",
    "abstract": "La nouvelle fonctionnalité de la bibliothèque Aspose.PDF permet aux utilisateurs d'ajouter facilement des images à des fichiers PDF existants en utilisant C#. Cette fonctionnalité simplifie la manipulation des PDF en permettant un positionnement et un redimensionnement précis des images directement dans le document, garantissant une intégration de haute qualité et un contrôle sur les éléments visuels. Avec le support de divers formats d'image et configurations, cet outil améliore la flexibilité de la gestion du contenu PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Image to PDF, C#, Aspose.PDF, PDF document generation, image compression, image aspect ratio, PDF file manipulation, add image method, XImage class, clipping mask",
    "wordcount": "2117",
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
    "url": "/net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2025-04-08",
    "description": "Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant la bibliothèque C#."
}
</script>

## Ajouter une image dans un fichier PDF existant

Chaque page PDF contient des propriétés de ressources et de contenu. Les ressources peuvent être des images et des formulaires par exemple, tandis que le contenu est représenté par un ensemble d'opérateurs PDF. Chaque opérateur a son nom et son argument. Cet exemple utilise des opérateurs pour ajouter une image à un fichier PDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Pour ajouter une image à un fichier PDF existant :

- Créez un objet Document et ouvrez le document PDF d'entrée.
- Obtenez la page à laquelle vous souhaitez ajouter une image.
- Ajoutez l'image dans la collection de ressources de la page.
- Utilisez des opérateurs pour placer l'image sur la page :
- Utilisez l'opérateur GSave pour enregistrer l'état graphique actuel.
- Utilisez l'opérateur ConcatenateMatrix pour spécifier où l'image doit être placée.
- Utilisez l'opérateur Do pour dessiner l'image sur la page.
- Enfin, utilisez l'opérateur GRestore pour enregistrer l'état graphique mis à jour.
- Enregistrez le fichier.
Le code suivant montre comment ajouter l'image dans un document PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where image needs to be added
        var page = document.Pages[1];

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "AddImage.jpg", FileMode.Open))
        {
            // Add image to Images collection of Page Resources
            page.Resources.Images.Add(imageStream);

            // Using GSave operator: this operator saves the current graphics state
            page.Contents.Add(new Aspose.Pdf.Operators.GSave());

            // Create Rectangle and Matrix objects to define image positioning
            var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
            var matrix = new Aspose.Pdf.Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });

            // Using ConcatenateMatrix operator: defines how the image must be placed
            page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

            // Retrieve the added image and use Do operator to draw it
            var ximage = page.Resources.Images[page.Resources.Images.Count];
            page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

            // Using GRestore operator: this operator restores the graphics state
            page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
        }

        // Save PDF document
        document.Save(dataDir + "AddImage_out.pdf");
    }
}
```

{{% alert color="primary" %}}

Par défaut, la qualité JPEG est réglée sur 100 %. Pour appliquer une meilleure compression et qualité, utilisez les surcharges suivantes :

{{% /alert %}}

- la surcharge de la méthode Replace est ajoutée dans la classe XImageCollection : public void Replace(int index, Stream stream, int quality)
- la surcharge de la méthode Add est ajoutée dans la classe XImageCollection : public void Add(Stam stream, int quality)

## Ajouter une image dans un fichier PDF existant (Facades)

Il existe également une méthode alternative, plus facile, pour ajouter une image à un fichier PDF. Vous pouvez utiliser la méthode [AddImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) de la classe [PdfFileMend](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilemend). La méthode [AddImage](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) nécessite l'image à ajouter, le numéro de page sur lequel l'image doit être ajoutée et les informations de coordonnées. Après cela, enregistrez le fichier PDF mis à jour en utilisant la méthode Close. Le code suivant vous montre comment ajouter une image dans un fichier PDF existant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPDFUsingPdfFileMender()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Define image file and output PDF file paths
    var imageFileName = Path.Combine(dataDir, "Images", "Sample-01.jpg");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add first page with specified size
        var page = document.Pages.Add();
        page.SetPageSize(Aspose.Pdf.PageSize.A3.Height, Aspose.Pdf.PageSize.A3.Width);

        // Add second page
        page = document.Pages.Add();

        // Create PdfFileMend object
        var mender = new Aspose.Pdf.Facades.PdfFileMend(document);

        // Add image to the first page using the mender
        mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);

        // Save PDF document
        document.Save(dataDir + "AddImageMender_out.pdf");
    }
}
```

Parfois, il est nécessaire de recadrer une image avant de l'insérer dans un PDF. Vous pouvez utiliser la méthode `AddImage()` pour prendre en charge l'ajout d'images recadrées :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCroppedImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Define image file and output PDF file paths
    var imageFileName = Path.Combine(dataDir, "Images", "Sample-01.jpg");
    var outputPdfFileName = dataDir + "Example-add-image-mender.pdf";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Open image stream
        using (var imgStream = File.OpenRead(imageFileName))
        {
            // Define the rectangle where the image will be placed on the PDF page
            var imageRect = new Aspose.Pdf.Rectangle(17.62, 65.25, 602.62, 767.25);

            // Crop the image to half its original width and height
            var w = imageRect.Width / 2;
            var h = imageRect.Height / 2;
            var bbox = new Aspose.Pdf.Rectangle(imageRect.LLX, imageRect.LLY, imageRect.LLX + w, imageRect.LLY + h);

            // Add page
            var page = document.Pages.Add();

            // Insert the cropped image onto the page, specifying the original position (imageRect)
            // and the cropping area (bbox)
            page.AddImage(imgStream, imageRect, bbox);
        }

        // Save PDF document to the specified file path
        document.Save(dataDir + "AddCroppedImageMender_out.pdf");
    }
}
```

## Placer l'image sur la page et préserver (contrôler) le rapport d'aspect

Si nous ne connaissons pas les dimensions de l'image, il y a toutes les chances d'obtenir une image déformée sur la page. L'exemple suivant montre l'une des façons d'éviter cela.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Load the image
    using (var bitmap = System.Drawing.Image.FromFile(dataDir + "InputImage.jpg"))
    {
        // Get the original width and height of the image
        int width = bitmap.Width;
        int height = bitmap.Height;

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Define the scaled width and height while preserving the aspect ratio
            int scaledWidth = 400;
            int scaledHeight = scaledWidth * height / width;

            // Add the image to the page
            page.AddImage(dataDir + "InputImage.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));

            // Save PDF document
            document.Save(dataDir + "PreserveAspectRatio.pdf");
        }
    }
}
```

Parfois, une grande image rencontre des problèmes d'échelle lorsqu'elle est ajoutée à un PDF. Le code suivant redimensionne l'image en fonction des dimensions de la page PDF, garantissant que l'image s'adapte correctement et a un meilleur aspect.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();
    var file = dataDir + "AddImageAccordingToPage.jpg";

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var pdfImageSection = document.Pages.Add();
        using (var stream = new FileStream(file, FileMode.Open))
        {
            // Open bitmap
            using (var img = new Bitmap(stream))
            {
                // Scale image according to page dimensions
                using (var scaledImg = ScaleImage(img, (int)pdfImageSection.PageInfo.Width, (int)pdfImageSection.PageInfo.Height))
                {
                    using (var ms = new MemoryStream())
                    {
                        scaledImg.Save(ms, ImageFormat.Jpeg);
                        ms.Seek(0, SeekOrigin.Begin);
                        var image = new Aspose.Pdf.Image
                        {
                            ImageStream = ms
                        };

                        // Add the image to the page
                        pdfImageSection.Paragraphs.Add(image);

                        // Save PDF document
                        document.Save("AddImageAccordingToPage.pdf");
                    }
                }
            }
        }
    }
}

private static Image ScaleImage(Image image, int maxWidth, int maxHeight)
{
    var ratioX = (double)maxWidth / image.Width;
    var ratioY = (double)maxHeight / image.Height;
    var ratio = Math.Min(ratioX, ratioY);
    var newWidth = (int)(image.Width * ratio);
    var newHeight = (int)(image.Height * ratio);
    var newImage = new Bitmap(newWidth, newHeight);
    using (var graphics = System.Drawing.Graphics.FromImage(newImage))
    {
        graphics.DrawImage(image, 0, 0, newWidth, newHeight);
    }
    return newImage;
}
```

## Identifier si l'image dans le PDF est en couleur ou en noir et blanc

Différents types de compression peuvent être appliqués sur les images pour réduire leur taille. Le type de compression appliqué sur l'image dépend de l'espace colorimétrique de l'image source, c'est-à-dire que si l'image est en couleur (RGB), alors appliquez la compression JPEG2000, et si elle est en noir et blanc, alors la compression JBIG2/JBIG2000 doit être appliquée. Par conséquent, identifier chaque type d'image et utiliser un type de compression approprié créera la meilleure sortie optimisée.

Un fichier PDF peut contenir des éléments tels que du texte, des images, des graphiques, des pièces jointes, des annotations, etc., et si le fichier PDF source contient des images, nous pouvons déterminer l'espace colorimétrique de l'image et appliquer une compression appropriée pour réduire la taille du fichier PDF. Le code suivant montre les étapes pour identifier si l'image dans le PDF est en couleur ou en noir et blanc.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageTypesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Counters for grayscale and RGB images
    int grayscaled = 0;
    int rgb = 0;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractImages.pdf"))
    {
        // Iterate through all pages in the document
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            Console.WriteLine("--------------------------------");
            var abs = new Aspose.Pdf.ImagePlacementAbsorber();
            page.Accept(abs);

            // Get the count of images on the current page
            Console.WriteLine("Total Images = {0} on page number {1}", abs.ImagePlacements.Count, page.Number);

            // Iterate through all the image placements on the page
            int image_counter = 1;
            foreach (Aspose.Pdf.ImagePlacement ia in abs.ImagePlacements)
            {
                // Determine the color type of the image
                var colorType = ia.Image.GetColorType();
                switch (colorType)
                {
                    case Aspose.Pdf.ColorType.Grayscale:
                        ++grayscaled;
                        Console.WriteLine("Image {0} is Grayscale...", image_counter);
                        break;
                    case Aspose.Pdf.ColorType.Rgb:
                        ++rgb;
                        Console.WriteLine("Image {0} is RGB...", image_counter);
                        break;
                }
                image_counter += 1;
            }
        }
    }
}
```

## Contrôler la qualité de l'image

Il est possible de contrôler la qualité d'une image qui est ajoutée à un fichier PDF. Utilisez la méthode surchargée [Replace](https://reference.aspose.com/pdf/fr/net/aspose.pdf.ximagecollection/replace/methods/1) dans la classe [XImageCollection](https://reference.aspose.com/pdf/fr/net/aspose.pdf/ximagecollection).

Le code suivant démontre comment convertir toutes les images du document en JPEG utilisant 80 % de qualité pour la compression.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceImagesInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ReplaceImages.pdf"))
    {
        // Iterate through all pages in the document
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            int idx = 1;
            // Iterate through all images in the page's resources
            foreach (Aspose.Pdf.XImage image in page.Resources.Images)
            {
                using (var imageStream = new MemoryStream())
                {
                    // Save the image as JPEG with 80% quality
                    image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
                    // Replace the image in the page's resources
                    page.Resources.Images.Replace(idx, imageStream, 80);
                    idx = idx + 1;
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "ReplaceImages_out.pdf");
    }
}
```

## Support pour l'application d'un masque de découpe aux images

Placer une forme vectorielle sur l'image bitmap de base fonctionne comme un masque, exposant uniquement la partie du design de base qui s'aligne avec la forme vectorielle. Toutes les zones en dehors de la forme seront dissimulées.

Le code suivant charge un PDF, ouvre deux fichiers image et applique ces images comme masques de pochoir aux deux premières images de la première page du PDF.

Un masque de pochoir peut être ajouté par la méthode 'XImage.AddStencilMask(Stream maskStream)' :

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStencilMasksToImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddStencilMasksToImages.pdf"))
    {
        // Open the first mask image file
        using (var fs1 = new FileStream(dataDir + "mask1.jpg", FileMode.Open))
        {
            // Open the second mask image file
            using (var fs2 = new FileStream(dataDir + "mask2.png", FileMode.Open))
            {
                // Apply stencil mask to the first image on the first page
                document.Pages[1].Resources.Images[1].AddStencilMask(fs1);

                // Apply stencil mask to the second image on the first page
                document.Pages[1].Resources.Images[2].AddStencilMask(fs2);
            }
        }

        // Save PDF document
        document.Save(dataDir + "AddStencilMasksToImages_out.pdf");
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