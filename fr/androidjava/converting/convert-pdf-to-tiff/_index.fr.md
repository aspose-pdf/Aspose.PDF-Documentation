---
title: Convertir PDF en TIFF 
linktitle: Convertir PDF en TIFF  
type: docs
weight: 30
url: /androidjava/convert-pdf-to-tiff/
lastmod: "2021-06-05"
description: Cet article décrit comment convertir les pages d'un document PDF en image TIFF. Vous apprendrez comment convertir toutes ou une seule page en images TIFF avec Aspose.PDF pour Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF pour Android via Java** permet de convertir des pages PDF en images TIFF.

La [classe TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) vous permet de convertir des pages PDF en images TIFF. Cette classe fournit une méthode nommée Process qui vous permet de convertir toutes les pages d'un fichier PDF en une seule image TIFF.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Convertir les Pages PDF en Une Image TIFF

Aspose.PDF pour Android via Java explique comment convertir toutes les pages d'un fichier PDF en une seule image TIFF :

1. Créez un objet de la classe Document.
1. Appelez la méthode Process pour convertir le document.
1. Pour définir les propriétés du fichier de sortie, utilisez la classe TiffSettings.

Le code suivant montre comment convertir toutes les pages PDF en une seule image TIFF.

```java
public void convertPDFtoTiffSinglePage() {
        // Ouvrir le document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Créer un objet Resolution
        Resolution resolution = new Resolution(300);

        // Créer un objet TiffSettings
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Créer un dispositif TIFF
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Convertir une page particulière et enregistrer l'image dans le flux
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Convertir une Page Unique en Image TIFF

Aspose.PDF pour Android via Java permet de convertir une page particulière d'un fichier PDF en une image TIFF, en utilisant une version surchargée de la méthode Process(..) qui prend un numéro de page comme argument pour la conversion. Le code suivant montre comment convertir la première page d'un PDF au format TIFF.

```java
public void convertPDFtoTiffAllPages() {
        // Ouvrir le document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Créer un objet Resolution
        Resolution resolution = new Resolution(300);

        // Créer un objet TiffSettings
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Créer un périphérique TIFF
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Convertir une page particulière et enregistrer l'image dans un flux
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```


## Utiliser l'algorithme de Bradley pendant la conversion

Aspose.PDF pour Android via Java a pris en charge la fonctionnalité de conversion de PDF en TIFF utilisant la compression LZW, puis avec l'utilisation de AForge, la binarisation peut être appliquée. Cependant, l'un des clients a demandé que pour certaines images, ils ont besoin d'obtenir le seuil en utilisant Otsu, donc ils aimeraient aussi utiliser Bradley.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Non implémenté dans Aspose.PDF pour Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Non implémenté dans Aspose.PDF pour Android
        throw new NotImplementedException();
    }
```