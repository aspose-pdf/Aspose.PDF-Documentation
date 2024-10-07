---
title: Extraire des images d'un PDF et reconnaître les codes-barres
type: docs
weight: 20
url: /net/extract-images-from-pdf-and-recognize-barcodes/
---

{{% alert color="primary" %}}

Les documents PDF sont généralement composés de texte, d'images, de tableaux, de pièces jointes, de graphiques, d'annotations et d'autres objets connexes. Il arrive que des codes-barres soient intégrés dans un fichier PDF et certains clients ont besoin d'identifier les codes-barres présents dans le fichier PDF. L'article suivant explique les étapes pour extraire les images des pages PDF et identifier les codes-barres à l'intérieur.

{{% /alert %}}

Selon le Document Object Model de Aspose.PDF pour .NET, un fichier PDF contient une ou plusieurs pages où chaque page contient une collection d'images, de formulaires et de polices dans l'objet Resources.
Selon le Document Object Model d'Aspose.PDF pour .NET, un fichier PDF contient une ou plusieurs pages où chaque page contient une collection d'Images, de Formulaires et de Polices dans l'objet Ressources.

**C#**

```csharp

//ouvrir le document
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// parcourir les pages individuelles du fichier PDF

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
{
    // parcourir chaque image extraite des pages PDF
    foreach (XImage xImage in pdfDocument.Pages[pageCount].Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            //sauvegarder l'image de sortie
            xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
   
            // positionner le flux au début du Stream
            imageStream.Position = 0;
   
            // Instancier l'objet BarCodeReader
   
            Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
   
            while (barcodeReader.Read())
            {
                // obtenir le texte du BarCode à partir de l'image du BarCode
                string code = barcodeReader.GetCodeText();
   
                // écrire le texte du BarCode à la sortie Console
                Console.WriteLine("BARCODE : " + code);
            }
   
            // fermer l'objet BarCodeReader pour libérer le fichier Image
   
            barcodeReader.Close();
        }
    }
}

```
Pour plus de détails sur les sujets abordés dans cet article, veuillez visiter les liens suivants :

- [Extraire des images du fichier PDF](/net/extract-images-from-the-pdf-file/)
- [Lire des codes-barres](https://docs.aspose.com/barcode/net/read-barcodes/)
