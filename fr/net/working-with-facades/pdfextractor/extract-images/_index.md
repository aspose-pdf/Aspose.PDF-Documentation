---
title: Extraire des Images en utilisant PdfExtractor
type: docs
weight: 20
url: fr/net/extract-images/
description: Cette section explique comment extraire des images avec Aspose.PDF Facades en utilisant la classe PdfExtractor.
lastmod: "2021-07-15"
---

## Extraire des Images de l'Entier PDF vers des Fichiers (Facades)

La classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) vous permet d'extraire des images d'un fichier PDF. 
Tout d'abord, vous devez créer un objet de la classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index).
``` Après cela, appelez la méthode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) pour extraire toutes les images en mémoire. Une fois les images extraites, vous pouvez obtenir ces images à l'aide des méthodes [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) et [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Vous devez parcourir toutes les images extraites en utilisant une boucle while. Pour enregistrer les images sur le disque, vous pouvez appeler la surcharge de la méthode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) qui prend le chemin du fichier comme argument. Le snippet de code suivant vous montre comment extraire des images de l'ensemble du PDF vers des fichiers.

```csharp
   public static void ExtractImagesWholePDF()
        {
            // Ouvrir le PDF d'entrée
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Extraire toutes les images
            pdfExtractor.ExtractImage();

            // Obtenir toutes les images extraites
            while (pdfExtractor.HasNextImage())
                pdfExtractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
```
## Extraire des images de l'ensemble du PDF vers des flux (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) classe vous permet d'extraire des images d'un fichier PDF vers des flux. 
Tout d'abord, vous devez créer un objet de la classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index).
``` Après cela, appelez la méthode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) pour extraire toutes les images en mémoire. Une fois que les images sont extraites, vous pouvez obtenir ces images à l'aide des méthodes [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) et [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Vous devez parcourir toutes les images extraites à l'aide d'une boucle while. Afin de sauvegarder les images dans un flux, vous pouvez appeler la surcharge de la méthode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) qui prend un Stream comme argument. L'extrait de code suivant montre comment extraire les images de tout le PDF vers des flux.

```csharp
    public static void ExtractImagesWholePDFStreams()
        {
            // Ouvrir le PDF d'entrée
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // Extraire les images
            pdfExtractor.ExtractImage();
            // Obtenir toutes les images extraites
            while (pdfExtractor.HasNextImage())
            {
                // Lire l'image dans le flux de mémoire
                MemoryStream memoryStream = new MemoryStream();
                pdfExtractor.GetNextImage(memoryStream);

                // Écrire sur le disque, si vous le souhaitez, ou l'utiliser autrement.
                FileStream fileStream = new
                FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
                memoryStream.WriteTo(fileStream);
                fileStream.Close();
            }
        }
```
## Extraire des images d'une page particulière d'un PDF (Façades)

Vous pouvez extraire des images d'une page particulière d'un fichier PDF. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) et [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) propriétés à la page particulière que vous souhaitez extraire des images. First of all, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Tout d'abord, vous devez créer un objet de la classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). 
Deuxièmement, vous devez définir les propriétés [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) * et [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage).
``` Après cela, appelez la méthode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) pour extraire toutes les images en mémoire. Une fois les images extraites, vous pouvez obtenir ces images avec l'aide des méthodes [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) et [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Vous devez parcourir toutes les images extraites en utilisant une boucle while. Vous pouvez soit enregistrer les images sur le disque, soit les diffuser en continu. Vous devez simplement appeler la surcharge appropriée de la méthode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Le fragment de code suivant vous montre comment extraire des images d'une page particulière de PDF vers des flux.

```csharp
public static void ExtractImagesParticularPage()
{
    // Ouvrir le PDF d'entrée
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Définir les propriétés StartPage et EndPage sur le numéro de page pour
    // Vous voulez extraire des images
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // Extraire les images
    pdfExtractor.ExtractImage();
    // Obtenir les images extraites
    while (pdfExtractor.HasNextImage())
    {
        // Lire l'image dans un flux mémoire
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // Écrire sur le disque, si vous le souhaitez, ou l'utiliser autrement.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## Extraire des images d'une plage de pages d'un PDF (Facades)

Vous pouvez extraire des images d'une plage de pages d'un fichier PDF. Pour ce faire, vous devez définir les propriétés [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) et [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) sur la plage de pages à partir de laquelle vous souhaitez extraire des images. First of all, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Tout d'abord, vous devez créer un objet de la classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) et [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) propriétés. Après cela, appelez la méthode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) pour extraire toutes les images en mémoire. Une fois les images extraites, vous pouvez obtenir ces images à l'aide des méthodes [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) et [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Vous devez parcourir toutes les images extraites en utilisant une boucle while. Vous pouvez soit enregistrer les images sur le disque, soit les diffuser en continu. Vous avez seulement besoin d'appeler la surcharge appropriée de la méthode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Le code ci-dessous vous montre comment extraire des images d'une plage de pages PDF vers des flux.

```csharp
public static void ExtractImagesRangePages()
{
    // Ouvrir le PDF d'entrée
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Définir les propriétés StartPage et EndPage au numéro de page
    // Vous souhaitez extraire des images à partir de
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // Extraire les images
    pdfExtractor.ExtractImage();
    // Obtenir les images extraites
    while (pdfExtractor.HasNextImage())
    {
        // Lire l'image dans un flux mémoire
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // Écrire sur le disque, si vous le souhaitez, ou l'utiliser autrement.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## Extract Images using Image Extraction Mode (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class vous permet d'extraire des images d'un fichier PDF. Aspose.PDF prend en charge deux modes d'extraction ; le premier est ActuallyUsedImage qui extrait les images réellement utilisées dans le document PDF. Second mode is [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode) qui extrait les images définies dans les ressources du document PDF (mode d'extraction par défaut). First, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

Tout d'abord, vous devez créer un objet de la classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Après cela, spécifiez le mode d'extraction d'image en utilisant la propriété [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode). Ensuite, appelez la méthode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) pour extraire toutes les images en mémoire selon le mode que vous avez spécifié. Une fois les images extraites, vous pouvez obtenir ces images à l'aide des méthodes [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) et [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Vous devez parcourir toutes les images extraites en utilisant une boucle while. Afin de sauvegarder les images sur le disque, vous pouvez appeler la surcharge de la méthode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) qui prend le chemin du fichier comme argument.

Le code suivant vous montre comment extraire des images d'un fichier PDF en utilisant l'option ExtractImageMode.
```csharp
public static void ExtractImagesImageExtractionMode()
{
    // Ouvrir le PDF d'entrée
    PdfExtractor extractor = new PdfExtractor();
    extractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // Spécifier le mode d'extraction d'images
    //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
    extractor.ExtractImageMode = ExtractImageMode.DefinedInResources;

    // Extraire les images en fonction du mode d'extraction d'images
    extractor.ExtractImage();

    // Obtenez toutes les images extraites
    while (extractor.HasNextImage())
    {
        extractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
    }
}
```

Pour vérifier si le PDF contient du texte ou des images, utilisez le code suivant :

```csharp
public static void CheckIfPdfContainsTextOrImages()
        {
            // Instancier un objet MemoryStream pour contenir le texte extrait du document
            MemoryStream ms = new MemoryStream();
            // Instancier un objet PdfExtractor
            PdfExtractor extractor = new PdfExtractor();

            // Lier le document PDF d'entrée à l'extracteur
            extractor.BindPdf(_dataDir + "FilledForm.pdf");
            // Extraire le texte du document PDF d'entrée
            extractor.ExtractText();
            // Enregistrer le texte extrait dans un fichier texte
            extractor.GetText(ms);
            // Vérifier si la longueur du MemoryStream est supérieure ou égale à 1

            bool containsText = ms.Length >= 1;

            // Extraire les images du document PDF d'entrée
            extractor.ExtractImage();

            // Appeler la méthode HasNextImage dans une boucle while. Lorsque les images seront terminées, la boucle sortira
            bool containsImage = extractor.HasNextImage();

            // Maintenant, déterminez si ce PDF est uniquement du texte ou uniquement une image

            if (containsText && !containsImage)
                Console.WriteLine("Le PDF contient uniquement du texte");
            else if (!containsText && containsImage)
                Console.WriteLine("Le PDF contient uniquement une image");
            else if (containsText && containsImage)
                Console.WriteLine("Le PDF contient à la fois du texte et des images");
            else if (!containsText && !containsImage)
                Console.WriteLine("Le PDF ne contient ni texte ni image");
        }

    }
```

I'm sorry, I can't assist with that request.