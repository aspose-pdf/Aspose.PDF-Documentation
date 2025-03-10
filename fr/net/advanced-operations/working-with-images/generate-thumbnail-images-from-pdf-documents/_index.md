---
title: Générer des images miniatures à partir de PDF
linktitle: Générer des images miniatures
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /fr/net/generate-thumbnail-images-from-pdf-documents/
description: Cette section décrit comment générer des images miniatures à partir de documents PDF
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate Thumbnail Images from PDF",
    "alternativeHeadline": "Generate Thumbnails from PDF Documents Effortlessly",
    "abstract": "La nouvelle fonctionnalité permet aux utilisateurs de générer efficacement des images miniatures directement à partir de documents PDF. Cette fonctionnalité améliore la gestion des documents en transformant les pages PDF en formats d'image facilement partageables, rationalisant ainsi les flux de travail pour les développeurs et les utilisateurs. Avec le support de divers formats d'image, cette fonctionnalité simplifie le processus de visualisation du contenu PDF sans avoir besoin de logiciels externes comme Adobe Acrobat",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Generate Thumbnail Images, PDF documents, Aspose.PDF for .NET, Acrobat SDK, image formats, PDF Manipulation Library, JavaScript, interapplication communication, thumbnail images, JPEG conversion",
    "wordcount": "767",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "Cette section décrit comment générer des images miniatures à partir de documents PDF"
}
</script>

{{% alert color="primary" %}}

Le SDK Adobe Acrobat est un ensemble d'outils qui vous aide à développer des logiciels interagissant avec la technologie Acrobat. Le SDK contient des fichiers d'en-tête, des bibliothèques de types, des utilitaires simples, du code d'exemple et de la documentation.

En utilisant le SDK Acrobat, vous pouvez développer des logiciels qui s'intègrent à Acrobat et Adobe Reader de plusieurs manières :

- **JavaScript** — Écrivez des scripts, soit dans un document PDF individuel, soit de manière externe, pour étendre la fonctionnalité d'Acrobat ou d'Adobe Reader.
- **Plug-ins** — Créez des plug-ins qui sont liés dynamiquement et étendent la fonctionnalité d'Acrobat ou d'Adobe Reader.
- **Communication interapplication** — Écrivez un processus d'application séparé qui utilise la communication interapplication (IAC) pour contrôler la fonctionnalité d'Acrobat. DDE et OLE sont pris en charge sur Microsoft® Windows®, et les événements Apple/AppleScript sur Mac OS®. L'IAC n'est pas disponible sur UNIX®.

Aspose.PDF for .NET offre beaucoup de la même fonctionnalité, vous libérant de la dépendance à l'automatisation d'Adobe Acrobat. Cet article montre comment générer des images miniatures à partir de documents PDF en utilisant d'abord le SDK Acrobat puis Aspose.PDF.

{{% /alert %}}

## Développement d'application utilisant l'API de communication interapplication Acrobat

Pensez à l'API Acrobat comme ayant deux couches distinctes qui utilisent des objets de communication interapplication Acrobat (IAC) :

- La couche d'application Acrobat (AV). La couche AV vous permet de contrôler la façon dont le document est affiché. Par exemple, la vue d'un objet document réside dans la couche associée à Acrobat.
- La couche de document portable (PD). La couche PD fournit un accès aux informations d'un document, telles qu'une page. À partir de la couche PD, vous pouvez effectuer des manipulations de base des documents PDF, telles que supprimer, déplacer ou remplacer des pages, ainsi que modifier les attributs d'annotation. Vous pouvez également imprimer des pages PDF, sélectionner du texte, accéder au texte manipulé et créer ou supprimer des miniatures.

Comme notre intention est de convertir les pages PDF en images miniatures, nous nous concentrons davantage sur l'IAC. L'API IAC contient des objets tels que PDDoc, PDPage, PDAnnot, et d'autres, qui permettent à l'utilisateur de traiter la couche de document portable (PD). L'exemple de code suivant parcourt un dossier et convertit les pages PDF en images miniatures. En utilisant le SDK Acrobat, nous pourrions également lire les métadonnées PDF et récupérer le nombre de pages dans le document.

### Approche Acrobat

Pour générer les images miniatures pour chaque document, nous avons utilisé le SDK Adobe Acrobat 7.0 et le Framework Microsoft .NET 2.0.

Le [SDK Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/) combiné avec la version complète d'Adobe Acrobat expose une bibliothèque COM d'objets (malheureusement, le lecteur Adobe gratuit n'expose pas les interfaces COM) qui peuvent être utilisés pour manipuler et accéder aux informations PDF. En utilisant ces objets COM via COM Interop, chargez le document PDF, obtenez la première page et rendez cette page dans le presse-papiers. Ensuite, avec le Framework .NET, copiez cela dans un bitmap, redimensionnez et combinez l'image et enregistrez le résultat en tant que fichier GIF ou PNG.

Une fois Adobe Acrobat installé, utilisez regedit.exe et recherchez sous HKEY_CLASSES_ROOT l'entrée appelée AcroExch.PDDoc.

**Le registre montrant l'entrée AcroExch.PDDDoc**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // Acrobat objects
    Acrobat.CAcroPDDoc pdfDoc;
    Acrobat.CAcroPDPage pdfPage;
    Acrobat.CAcroRect pdfRect;
    Acrobat.CAcroPoint pdfPoint;

    AppSettingsReader appSettings = new AppSettingsReader();
    string pdfInputPath = appSettings.GetValue("pdfInputPath", typeof(string)).ToString();
    string pngOutputPath = appSettings.GetValue("pngOutputPath", typeof(string)).ToString();
    string templatePortraitFile = Application.StartupPath + @"\pdftemplate_portrait.gif";
    string templateLandscapeFile = Application.StartupPath + @"\pdftemplate_landscape.gif";

    // Get list of files to process from the input path
    string[] files = Directory.GetFiles(pdfInputPath, "*.pdf");

    for (int n = 0; n < files.Length; n++)
    {
        string inputFile = files[n];
        string outputFile = Path.Combine(pngOutputPath, Path.GetFileNameWithoutExtension(inputFile) + ".png");

        // Create PDF document
        pdfDoc = (Acrobat.CAcroPDDoc)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.PDDoc", "");

        if (pdfDoc.Open(inputFile) == 0)
        {
            throw new FileNotFoundException($"Unable to open PDF file: {inputFile}");
        }

        int pageCount = pdfDoc.GetNumPages();
        pdfPage = (Acrobat.CAcroPDPage)pdfDoc.AcquirePage(0);
        pdfPoint = (Acrobat.CAcroPoint)pdfPage.GetSize();

        pdfRect = (Acrobat.CAcroRect)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.Rect", "");
        pdfRect.Left = 0;
        pdfRect.right = pdfPoint.x;
        pdfRect.Top = 0;
        pdfRect.bottom = pdfPoint.y;

        pdfPage.CopyToClipboard(pdfRect, 0, 0, 100);
        IDataObject clipboardData = Clipboard.GetDataObject();

        if (clipboardData.GetDataPresent(DataFormats.Bitmap))
        {
            Bitmap pdfBitmap = (Bitmap)clipboardData.GetData(DataFormats.Bitmap);

            int thumbnailWidth = 45;
            int thumbnailHeight = 59;
            string templateFile = pdfPoint.x < pdfPoint.y ? templatePortraitFile : templateLandscapeFile;

            if (pdfPoint.x > pdfPoint.y)
            {
                // Swap width and height for landscape orientation
                (thumbnailWidth, thumbnailHeight) = (thumbnailHeight, thumbnailWidth);
            }

            Bitmap templateBitmap = new Bitmap(templateFile);
            Image pdfImage = pdfBitmap.GetThumbnailImage(thumbnailWidth, thumbnailHeight, null, IntPtr.Zero);

            Bitmap thumbnailBitmap = new Bitmap(thumbnailWidth + 7, thumbnailHeight + 7, System.Drawing.Imaging.PixelFormat.Format32bppArgb);

            templateBitmap.MakeTransparent();

            using (Graphics thumbnailGraphics = Graphics.FromImage(thumbnailBitmap))
            {
                thumbnailGraphics.DrawImage(pdfImage, 2, 2, thumbnailWidth, thumbnailHeight);
                thumbnailGraphics.DrawImage(templateBitmap, 0, 0);
                thumbnailBitmap.Save(outputFile, System.Drawing.Imaging.ImageFormat.Png);
            }

            Console.WriteLine("Generated thumbnail: {0}", outputFile);

            pdfDoc.Close();
            Marshal.ReleaseComObject(pdfPage);
            Marshal.ReleaseComObject(pdfRect);
            Marshal.ReleaseComObject(pdfDoc);
        }
    }
}
```

## Approche Aspose.PDF for .NET

Aspose.PDF for .NET offre un support étendu pour traiter les documents PDF. Il prend également en charge la capacité de convertir les pages de documents PDF en une variété de formats d'image. La fonctionnalité décrite ci-dessus peut être facilement réalisée en utilisant Aspose.PDF for .NET.

Aspose.PDF présente des avantages distincts :

- Vous n'avez pas besoin d'avoir Adobe Acrobat installé sur votre système pour travailler avec des fichiers PDF.
- Utiliser Aspose.PDF for .NET est simple et facile à comprendre par rapport à l'automatisation d'Acrobat.

Si nous devons convertir des pages PDF en JPEG, le namespace [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) fournit une classe nommée [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) pour rendre les pages PDF en images JPEG. Veuillez consulter l'extrait de code suivant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Retrieve names of all the PDF files in a particular directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

    // Iterate through all the files entries in array
    for (int counter = 0; counter < fileEntries.Length; counter++)
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(fileEntries[counter]))
        {
            for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
            {
                using (FileStream imageStream = new FileStream(dataDir + @"\Thumbanils" + counter.ToString() + "_" + pageCount + ".jpg", FileMode.Create))
                {
                    var resolution = new Aspose.Pdf.Devices.Resolution(300);
                    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(45, 59, resolution, 100);
                    // Convert a particular page and save the image to stream
                    jpegDevice.Process(document.Pages[pageCount], imageStream);
                }
            }
        }
    }
}
```

{{% alert color="primary" %}}

- Merci à CodeProject pour [Générer une image miniature à partir d'un document PDF](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- Merci à Acrobat pour la [référence SDK Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

{{% /alert %}}

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