---
title: Convertir un fichier PDF
type: docs
weight: 30
url: /fr/net/convert-pdf-file/
description: Cette section explique comment convertir un fichier PDF avec Aspose.PDF Facades en utilisant la classe PdfConverter.
lastmod: "2021-06-05"
draft: false
---

## Convertir les pages PDF en différents formats d'image (Facades)

Pour convertir les pages PDF en différents formats d'image, vous devez créer un objet [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) et ouvrir le fichier PDF en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, vous devez appeler la méthode [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) pour les tâches d'initialisation. Ensuite, vous pouvez parcourir toutes les pages en utilisant les méthodes [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) et [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6). La méthode [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) vous permet de créer une image d'une page particulière. Vous devez également passer le format d'image à cette méthode afin de créer une image d'un type spécifique, c'est-à-dire JPEG, GIF ou PNG, etc. Enfin, appelez la méthode [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) de la classe [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter). L'extrait de code suivant vous montre comment convertir des pages PDF en images.

```csharp
 public static void ConvertPdfPagesToImages01()
        {
            // Créer un objet PdfConverter
            PdfConverter converter = new PdfConverter();

            // Lier le fichier pdf d'entrée
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // Initialiser le processus de conversion
            converter.DoConvert();

            // Vérifier si des pages existent puis convertir en image une par une
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // Fermer l'objet PdfConverter
            converter.Close();
        }
```
Dans le prochain extrait de code, nous montrerons comment vous pouvez modifier certains paramètres. Avec [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype), nous définissons le cadre 'CropBox'. Aussi, nous pouvons changer la [Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution) en spécifiant le nombre de points par pouce. Le suivant [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - mode de présentation du formulaire. Ensuite, nous indiquons la [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage) avec laquelle le numéro de page du début de la conversion est défini. Nous pouvons également spécifier la dernière page en définissant une plage.

```csharp
  public static void ConvertPdfPagesToImages02()
        {
            // Créer un objet PdfConverter
            PdfConverter converter = new PdfConverter();

            // Lier le fichier pdf d'entrée
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // Initialiser le processus de conversion
            converter.DoConvert();
            converter.CoordinateType = PageCoordinateType.CropBox;
            converter.Resolution = new Devices.Resolution(600);
            converter.FormPresentationMode = Devices.FormPresentationMode.Production;
            converter.StartPage = 2;
            // converter.EndPage = 3;
            // Vérifier si les pages existent et convertir ensuite en image une par une
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // Fermer l'objet PdfConverter
            converter.Close();
        }
```

## Voir aussi

Aspose.PDF pour .NET permet de convertir des documents PDF en divers formats et également de convertir d'autres formats en PDF. Aussi, vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne avec l'application de conversion Aspose.PDF. Apprenez la section [Conversion](/pdf/fr/net/converting/) pour résoudre vos tâches.