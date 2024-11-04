---
title: Convertir un Fichier PDF
type: docs
weight: 20
url: /java/convert-pdf-file/
description: Cette section explique comment convertir un fichier PDF avec Aspose.PDF Facades en utilisant la classe PdfConverter.
lastmod: "2021-06-05"
draft: false
---

## Convertir les Pages PDF en Différents Formats d'Image (Facades)

Pour convertir les pages PDF en différents formats d'image, vous devez créer un objet [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter) et ouvrir le fichier PDF en utilisant la méthode [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#bindPdf-java.lang.String-).

Après cela, vous devez appeler la méthode [doConvert](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#doConvert--) pour les tâches d'initialisation.
 Then, you can loop through all the pages using [hasNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#hasNextImage--) et [getNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#getNextImage-java.io.OutputStream-) méthodes. La méthode getNextImage vous permet de créer une image d'une page particulière. Vous devez également passer ImageType à cette méthode afin de créer une image d'un type spécifique, c'est-à-dire JPEG, GIF ou PNG, etc.

Enfin, appelez la méthode close de la classe [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter).

Le code suivant vous montre comment convertir des pages PDF en images.

```java
public static void ConvertPdfPagesToImages01() {
        // Créer un objet PdfConverter
        PdfConverter converter = new PdfConverter();

        // Lier le fichier pdf d'entrée
        converter.bindPdf(_dataDir + "Sample-Document-01.pdf");

        // Initialiser le processus de conversion
        converter.doConvert();
        
        int count = 0;

        // Vérifier si des pages existent, puis convertir en image une par une
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // Fermer l'objet PdfConverter
        converter.close();
    }
```

Dans le prochain extrait de code, nous allons montrer comment vous pouvez modifier certains paramètres. Avec [setCoordinateType](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setCoordinateType-int-), nous définissons le cadre [CropBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCoordinateType#CropBox). De plus, nous pouvons changer [setResolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setResolution-com.aspose.pdf.devices.Resolution-) en spécifiant le nombre de points par pouce. Le suivant [setFormPresentationMode](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setFormPresentationMode-int-) - mode de présentation du formulaire. Ensuite, nous indiquons le [setStartPage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setStartPage-int-) avec lequel le numéro de page du début de la conversion est défini. Nous pouvons également spécifier la dernière page en définissant une plage.

```java
public static void ConvertPdfPagesToImages02()
    {
        // Créer un objet PdfConverter
        PdfConverter converter = new PdfConverter();

        // Lier le fichier pdf d'entrée
        converter.bindPdf(_dataDir + "sample.pdf");

        // Initialiser le processus de conversion
        converter.doConvert();
        converter.setCoordinateType(PageCoordinateType.CropBox);
        converter.setResolution (new Resolution(600));
        converter.setFormPresentationMode(FormPresentationMode.Editor);
        converter.setStartPage(2);
        int count=0;
        // Vérifier si des pages existent et ensuite convertir en image une par une
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // Fermer l'objet PdfConverter
        converter.close();
    }
```