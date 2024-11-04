---
title: Convertir les pages PDF en images et reconnaître les codes-barres
type: docs
weight: 10
url: /net/convert-pdf-pages-to-images-and-recognize-barcodes/
---

{{% alert color="primary" %}}

Les documents PDF comprennent généralement du texte, des images, des tableaux, des pièces jointes, des graphiques, des annotations et d'autres objets. Certains de nos clients ont besoin d'intégrer des codes-barres dans les documents puis d'identifier les codes-barres dans le fichier PDF. L'article suivant explique comment transformer les pages d'un fichier PDF en images et identifier les codes-barres dans les images avec Aspose.Barcode pour .NET.

{{% /alert %}}
### **Conversion de pages en images et reconnaissance de codes-barres**

{{% alert color="primary" %}}

Aspose.PDF pour .NET est un produit très puissant pour la gestion des documents PDF. Il facilite la conversion des pages de documents PDF en images. Aspose.BarCode pour .NET est un produit tout aussi puissant pour générer et reconnaître des codes-barres.
{{% /alert %}}

La classe PdfConverter sous l'espace de noms Aspose.PDF.Facades prend en charge la conversion des pages PDF en divers formats d'image.
#### **Utilisation d'Aspose.PDF.Facades**

{{% alert color="primary" %}}

La classe PdfConverter contient une méthode nommée GetNextImage qui génère une image à partir de la page PDF actuelle. Pour spécifier le format d'image de sortie, cette méthode accepte un argument de l'énumération System.Drawing.Imaging.ImageFormat.

Aspose.Barcode contient un espace de noms, BarCodeRecognition, qui contient la classe BarCodeReader. La classe BarCodeReader vous permet de lire, déterminer et identifier les codes-barres à partir de fichiers image.

Dans le cadre de cet exemple, convertissez d'abord une page d'un fichier PDF en image avec Aspose.PDF.Facades.PdfConverter.
##### **Exemples de programmation**
**C#**

{{< highlight csharp >}}

 //Créer un objet PdfConverter

PdfConverter converter = new PdfConverter();

//Lier le fichier PDF d'entrée

converter.BindPdf("Source.pdf");

// Spécifier la première page à traiter

converter.StartPage = 1;

// Spécifier la dernière page à traiter

converter.EndPage = 1;

// Créer un objet Résolution pour spécifier la résolution de l'image résultante

converter.Resolution = new Aspose.PDF.Devices.Resolution(300);

//Initialiser le processus de conversion

converter.DoConvert();

// Créer un objet MemoryStream pour contenir l'image résultante

MemoryStream imageStream = new MemoryStream();

//Vérifier si des pages existent puis les convertir en image une par une

while (converter.HasNextImage())

{

    // Sauvegarder l'image dans le format d'image donné

    converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

    // Réinitialiser la position du flux au début du flux

{{% /alert %}}
    // Définir la position du flux au début du flux

    imageStream.Position = 0;

    // Instancier un objet BarCodeReader

    Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

    // String txtResult.Text = "";

    while (barcodeReader.Read())

    {

        // Obtenir le texte du code-barres à partir de l'image du code-barres

        string code = barcodeReader.GetCodeText();

        // Écrire le texte du code-barres dans la sortie Console

        Console.WriteLine("BARCODE : " + code);

    }

    // Fermer l'objet BarCodeReader pour libérer le fichier image

    barcodeReader.Close();

}

// Fermer l'instance de PdfConverter et libérer les ressources

converter.Close();

// Fermer le flux contenant l'objet image

imageStream.Close();

{{< /highlight >}}

{{% alert color="primary" %}}

Dans les extraits de code ci-dessus, l'image de sortie est enregistrée dans un objet MemoryStream.
Dans les extraits de code ci-dessus, l'image de sortie est enregistrée dans un objet MemoryStream.

{{% /alert %}}

{anchor:devices]
#### **Utilisation de la classe PngDevice**
Dans Aspose.PDF.Devices, se trouve la classe PngDevice. Cette classe vous permet de convertir des pages de documents PDF en images PNG.

Dans le cadre de cet exemple, chargez le fichier PDF source dans le Document et convertissez les pages du document en images PNG. Une fois les images créées, utilisez la classe BarCodeReader sous Aspose.BarCodeRecognition pour identifier et lire les codes-barres dans les images.

{{% alert color="primary" %}}

Les exemples de code donnés ici parcourent les pages du document PDF et tentent d'identifier les codes-barres sur chaque page.

{{% /alert %}}
##### **Exemples de programmation**
**C#**

{{< highlight csharp >}}

 //Ouvrir le document PDF

Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// Parcourir les pages individuelles du fichier PDF

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)

{

    using (MemoryStream imageStream = new MemoryStream())

    using (MemoryStream imageStream = new MemoryStream())
    {
        //Créer un objet Resolution
        Aspose.PDF.Devices.Resolution resolution = new Aspose.PDF.Devices.Resolution(300);

        // Instancier un objet PngDevice en passant un objet Resolution en argument à son constructeur
        Aspose.PDF.Devices.PngDevice pngDevice = new Aspose.PDF.Devices.PngDevice(resolution);

        //Convertir une page spécifique et sauvegarder l'image dans le flux
        pngDevice.Process(pdfDocument.Pages[pageCount], imageStream);

        // Définir la position du flux au début du flux
        imageStream.Position = 0;

        // Instancier un objet BarCodeReader
        Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

        // String txtResult.Text = "";

        while (barcodeReader.Read())
        {
            // Obtenir le texte du code-barres à partir de l'image du code-barres
            string code = barcodeReader.GetCodeText();
```
```csharp
string code = barcodeReader.GetCodeText();

// Écrire le texte du code-barres dans la sortie Console

Console.WriteLine("BARCODE : " + code);

}

// Fermer l'objet BarCodeReader pour libérer le fichier image

barcodeReader.Close();

}

}

{{< /highlight >}}



{{% alert color="primary" %}}

Pour plus d'informations sur les sujets abordés dans cet article, veuillez consulter :

- Convertir des pages PDF en différents formats d'image (Facades)
- Convertir toutes les pages PDF en images PNG
- [Lire les codes-barres](https://docs.aspose.com/barcode/net/read-barcodes/)


{{% /alert %}}
```
