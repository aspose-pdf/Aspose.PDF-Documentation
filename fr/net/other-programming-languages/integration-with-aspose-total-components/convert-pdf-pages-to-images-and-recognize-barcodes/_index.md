---
title: Convertir les pages PDF en images et reconnaître les codes-barres
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF Pages to Images and Recognize Barcodes",
    "alternativeHeadline": "Convert PDF Pages to Images with Barcode Recognition in C#",
    "abstract": "La nouvelle fonctionnalité permet une conversion transparente des pages PDF en divers formats d'image, facilitant l'identification des codes-barres intégrés à l'aide d'Aspose.Barcode pour .NET. Cette fonctionnalité rationalise le traitement des documents en permettant aux utilisateurs de transformer le contenu PDF en images et de reconnaître avec précision les codes-barres pour une gestion efficace des données.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "858",
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
    "url": "/net/convert-pdf-pages-to-images-and-recognize-barcodes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-pages-to-images-and-recognize-barcodes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

{{% alert color="primary" %}}

Les documents PDF comprennent généralement du texte, des images, des tableaux, des pièces jointes, des graphiques, des annotations et d'autres objets. Certains de nos clients ont besoin d'intégrer des codes-barres dans des documents, puis d'identifier les codes-barres dans le fichier PDF. L'article suivant explique comment transformer les pages d'un fichier PDF en images et identifier les codes-barres dans les images avec Aspose.Barcode pour .NET.

{{% /alert %}}

## Conversion des pages en images et reconnaissance des codes-barres

{{% alert color="primary" %}}

Aspose.PDF for .NET est un produit très puissant pour la gestion des documents PDF. Il facilite la conversion des pages des documents PDF en images. Aspose.BarCode pour .NET est un produit tout aussi puissant pour générer et reconnaître des codes-barres.

La classe PdfConverter sous l'espace de noms Aspose.Pdf.Facades prend en charge la conversion des pages PDF en divers formats d'image. Le PngDevice sous l'espace de noms Aspose.Pdf.Devices prend en charge la conversion des pages PDF en fichiers PNG. Chacune de ces classes peut être utilisée pour transformer les pages d'un fichier PDF en images.

Lorsque les pages ont été converties en un format d'image, nous pouvons utiliser Aspose.BarCode pour .NET pour identifier les codes-barres à l'intérieur. Les exemples de code ci-dessous montrent comment convertir des pages en utilisant soit PdfConverter soit PngDevice.

{{% /alert %}}

### Utilisation d'Aspose.Pdf.Facades

{{% alert color="primary" %}}

La classe PdfConverter contient une méthode nommée GetNextImage qui génère une image à partir de la page PDF actuelle. Pour spécifier le format d'image de sortie, cette méthode accepte un argument de l'énumération System.Drawing.Imaging.ImageFormat.

Aspose.Barcode contient un espace de noms, BarCodeRecognition, qui contient la classe BarCodeReader. La classe BarCodeReader vous permet de lire, de déterminer et d'identifier les codes-barres à partir de fichiers image.

Pour les besoins de cet exemple, convertissez d'abord une page d'un fichier PDF en une image avec Aspose.Pdf.Facades.PdfConverter. Ensuite, utilisez la classe Aspose.BarCodeRecognition.BarCodeReader pour reconnaître le code-barres dans l'image.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodesConverter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create a PdfConverter object
    var converter = new Aspose.Pdf.Facades.PdfConverter();

    // Bind PDF document
    converter.BindPdf(dataDir + "IdentifyBarcodes.pdf");

    // Specify the start page to be processed
    converter.StartPage = 1;

    // Specify the end page for processing
    converter.EndPage = 1;

    // Create a Resolution object to specify the resolution of resultant image
    converter.Resolution = new Aspose.Pdf.Devices.Resolution(300);

    // Initialize the convertion process
    converter.DoConvert();

    // Create a MemoryStream object to hold the resultant image
    using (var imageStream = new MemoryStream())
    {
        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Save the image in the given image Format
            converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

            // Set the stream position to the beginning of the stream
            imageStream.Position = 0;

            // Instantiate a BarCodeReader object
            var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

            // String txtResult.Text = "";
            while (barcodeReader.Read())
            {
                // Get the barcode text from the barcode image
                var code = barcodeReader.GetCodeText();

                // Write the barcode text to Console output
                Console.WriteLine("BARCODE : " + code);
            }

            // Close the BarCodeReader object to release the image file
            barcodeReader.Close();
        }

        // Close the PdfConverter instance and release the resources
        converter.Close();
    }
}
```

{{% alert color="primary" %}}

Dans les extraits de code ci-dessus, l'image de sortie est enregistrée dans un objet MemoryStream. L'image peut également être enregistrée sur le disque. Pour ce faire, remplacez l'objet MemoryStream par un objet chaîne qui représente le chemin du fichier dans la méthode GetNextImage de la classe PdfConverter.

{{% /alert %}}

#### Utilisation de la classe PngDevice

Dans l'espace de noms Aspose.Pdf.Devices, se trouve le PngDevice. Cette classe vous permet de convertir les pages des documents PDF en images PNG.

Pour les besoins de cet exemple, chargez le fichier PDF source dans le Document] et convertissez les pages en images PNG. Lorsque les images ont été créées, utilisez la classe BarCodeReader sous Aspose.BarCodeRecognition pour identifier et lire les codes-barres dans les images.

{{% alert color="primary" %}}

Les exemples de code donnés ici parcourent les pages du document PDF et essaient d'identifier les codes-barres sur chaque page.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "IdentifyBarcodes.pdf"))
    {
        // Traverse through the individual pages of the PDF file
        for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            using (var imageStream = new MemoryStream())
            {
                // Create a Resolution object
                var resolution = new Aspose.Pdf.Devices.Resolution(300);

                // Instantiate a PngDevice object while passing a Resolution object as an argument to its constructor
                var pngDevice = new Aspose.Pdf.Devices.PngDevice(resolution);

                // Convert a particular page and save the image to stream
                pngDevice.Process(document.Pages[pageCount], imageStream);

                // Set the stream position to the beginning of Stream
                imageStream.Position = 0;

                // Instantiate a BarCodeReader object
                var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

                // String txtResult.Text = "";
                while (barcodeReader.Read())
                {
                    // Get the barcode text from the barcode image
                    var code = barcodeReader.GetCodeText();

                    // Write the barcode text to Console output
                    Console.WriteLine("BARCODE : " + code);
                }

                // Close the BarCodeReader object to release the image file
                barcodeReader.Close();
            }
        }
    }
}
```

{{% alert color="primary" %}}

Pour plus d'informations sur les sujets abordés dans cet article, allez à :

- Convertir les pages PDF en différents formats d'image (Facades)
- Convertir toutes les pages PDF en images PNG
- [Lire les codes-barres](https://docs.aspose.com/barcode/net/barcode-recognition/)

{{% /alert %}}