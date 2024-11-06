---
title: Ajouter une image à un PDF en utilisant C#
linktitle: Ajouter une image
type: docs
weight: 10
url: fr/net/add-image-to-existing-pdf-file/
description: Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant la bibliothèque C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter une image à un PDF en utilisant C#",
    "alternativeHeadline": "Comment ajouter une image à un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de document PDF",
    "keywords": "pdf, c#, ajouter une image au pdf",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe Doc Aspose.PDF",
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
    "dateModified": "2022-02-04",
    "description": "Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant la bibliothèque C#."
}
</script>
## Ajouter une image dans un fichier PDF existant

Chaque page PDF contient des propriétés Ressources et Contenus. Les ressources peuvent être des images et des formulaires par exemple, tandis que le contenu est représenté par un ensemble d'opérateurs PDF. Chaque opérateur a son nom et son argument. Cet exemple utilise des opérateurs pour ajouter une image à un fichier PDF.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Pour ajouter une image à un fichier PDF existant :

- Créez un objet Document et ouvrez le document PDF d'entrée.
- Obtenez la page à laquelle vous souhaitez ajouter une image.
- Ajoutez l'image à la collection de ressources de la page.
- Utilisez des opérateurs pour placer l'image sur la page :
  - Utilisez l'opérateur GSave pour sauvegarder l'état graphique actuel.
  - Utilisez l'opérateur ConcatenateMatrix pour spécifier où l'image doit être placée.
  - Utilisez l'opérateur Do pour dessiner l'image sur la page.
  - Enfin, utilisez l'opérateur GRestore pour sauvegarder l'état graphique mis à jour.
- Sauvegardez le fichier.
Le code suivant montre comment ajouter l'image dans un document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Ouvrir le document
Document pdfDocument = new Document(dataDir+ "AddImage.pdf");

// Définir les coordonnées
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Obtenir la page où l'image doit être ajoutée
Page page = pdfDocument.Pages[1];
// Charger l'image dans le flux
FileStream imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open);
// Ajouter l'image à la collection d'images des ressources de la page
page.Resources.Images.Add(imageStream);
// Utiliser l'opérateur GSave : cet opérateur sauvegarde l'état graphique actuel
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Créer des objets Rectangle et Matrix
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// Utiliser l'opérateur ConcatenateMatrix (concaténer la matrice) : définit comment l'image doit être placée
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Utiliser l'opérateur Do : cet opérateur dessine l'image
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// Utiliser l'opérateur GRestore : cet opérateur restaure l'état graphique
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "AddImage_out.pdf";
// Sauvegarder le document mis à jour
pdfDocument.Save(dataDir);
```
{{% alert color="primary" %}}

Par défaut, la qualité JPEG est réglée à 100%. Pour appliquer une meilleure compression et qualité, utilisez les surcharges suivantes :

{{% /alert %}}

- la surcharge de la méthode Replace est ajoutée dans la classe XImageCollection : public void Replace(int index, Stream stream, int quality)
- la surcharge de la méthode Add est ajoutée dans la classe XImageCollection : public void Add(Stream stream, int quality)

## Ajouter une Image dans un Fichier PDF Existant (Facades)

Il existe également une alternative plus simple pour ajouter une image à un fichier PDF.
Il existe également une alternative, plus simple, pour ajouter une image à un fichier PDF.

```csharp
string imageFileName = Path.Combine(_dataDir, "Images", "Sample-01.jpg");
string outputPdfFileName = Path.Combine(_dataDir, "Example-add-image-mender.pdf");
Document document = new Document();
Page page = document.Pages.Add();
page.SetPageSize(PageSize.A3.Height, PageSize.A3.Width);
page = document.Pages.Add();
Aspose.Pdf.Facades.PdfFileMend mender = new Aspose.Pdf.Facades.PdfFileMend(document);
mender.AddImage(imageFileName, 1, 0, 0, (float)page.CropBox.Width, (float)page.CropBox.Height);
document.Save(outputPdfFileName);
```

## Placer une image sur la page et préserver (contrôler) le rapport d'aspect

Si nous ne connaissons pas les dimensions de l'image, il y a toutes les chances d'obtenir une image déformée sur la page. L'exemple suivant montre l'une des manières d'éviter cela.

```csharp
public static void AddingImageAndPreserveAspectRatioIntoPDF()
{
    var bitmap = System.Drawing.Image.FromFile(_dataDir + "3410492.jpg");

    int width;
    int height;

    width = bitmap.Width;
    height = bitmap.Height;

    var document = new Aspose.Pdf.Document();

    var page = document.Pages.Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page.AddImage(_dataDir + "3410492.jpg", new Aspose.Pdf.Rectangle(10, 10, scaledWidth, scaledHeight));
    document.Save(_dataDir + "sample_image.pdf");
}
```
## Identifier si l'image dans un PDF est en couleur ou en noir et blanc

Différents types de compression peuvent être appliqués aux images pour réduire leur taille. Le type de compression appliqué dépend de l'espace colorimétrique de l'image source, c'est-à-dire si l'image est en couleur (RVB), alors la compression JPEG2000 est appliquée, et si elle est en noir et blanc, la compression JBIG2/JBIG2000 doit être appliquée. Par conséquent, identifier chaque type d'image et utiliser un type de compression approprié permettra de créer une sortie optimale.

Un fichier PDF peut contenir des éléments de texte, d'image, de graphique, de pièce jointe, d'annotation, etc. Si le fichier PDF source contient des images, nous pouvons déterminer l'espace colorimétrique de l'image et appliquer la compression appropriée pour réduire la taille du fichier PDF. Le fragment de code suivant montre les étapes pour identifier si une image dans un PDF est en couleur ou en noir et blanc.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Compteur pour les images en niveaux de gris
int grayscaled = 0;
// Compteur pour les images RVB
int rgd = 0;

using (Document document = new Document(dataDir + "ExtractImages.pdf"))
{
    foreach (Page page in document.Pages)
    {
        Console.WriteLine("--------------------------------");
        ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
        page.Accept(abs);
        // Obtenir le nombre d'images sur une page spécifique
        Console.WriteLine("Total Images = {0} sur la page numéro {1}", abs.ImagePlacements.Count, page.Number);
        // Document.Pages[29].Accept(abs);
        int image_counter = 1;
        foreach (ImagePlacement ia in abs.ImagePlacements)
        {
            ColorType colorType = ia.Image.GetColorType();
            switch (colorType)
            {
                case ColorType.Grayscale:
                    ++grayscaled;
                    Console.WriteLine("Image {0} est en niveaux de gris...", image_counter);
                    break;
                case ColorType.Rgb:
                    ++rgd;
                    Console.WriteLine("Image {0} est en RVB...", image_counter);
                    break;
            }
            image_counter += 1;
        }
    }
}
```
## Contrôler la Qualité de l'Image

Il est possible de contrôler la qualité d'une image qui est ajoutée à un fichier PDF. Utilisez la méthode [Replace](https://reference.aspose.com/pdf/net/aspose.pdf.ximagecollection/replace/methods/1) surchargée dans la classe [XImageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/ximagecollection).

Le code suivant démontre comment convertir toutes les images du document en JPEG utilisant une qualité de compression de 80%.

```csharp
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document(inFile);
foreach (Aspose.PDF.Page page in pdfDocument.Pages)
{
    int idx = 1;
    foreach (Aspose.PDF.XImage image in page.Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
            page.Resources.Images.Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }
}

// pdfDocument.OptimizeResources();

pdfDocument.Save(outFile);
```

<script type="application/ld+json">

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Bibliothèque Aspose.PDF pour .NET",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
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
```

