---
title: Convertir le PDF en TIFF
linktitle: Convertir le PDF en TIFF
type: docs
weight: 30
url: /fr/androidjava/convert-pdf-to-tiff/
lastmod: "2026-07-01"
description: Cet article décrit comment convertir les pages d'un document PDF en image TIFF. Vous apprendrez comment convertir toutes les pages ou une page unique en images TIFF avec Aspose.PDF for Android via Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** rend possible la conversion des PDF Pages en images TIFF.

Le [classe TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) vous permet de convertir des pages PDF en images TIFF. Cette classe fournit une méthode nommée Process qui vous permet de convertir toutes les pages d'un fichier PDF en une seule image TIFF.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## Convertir les pages PDF en une seule image TIFF

Aspose.PDF for Android via Java explique comment convertir toutes les pages d'un fichier PDF en une seule image TIFF :

1. Créez un objet de la classe Document.
1. Appelez la méthode Process pour convertir le document.
1. Pour définir les propriétés du fichier de sortie, utilisez la classe TiffSettings.

Le fragment de code suivant montre comment convertir toutes les pages PDF en une image TIFF unique.

```java
public void convertPDFtoTiffSinglePage() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## Convertir une seule page en image TIFF

Aspose.PDF for Android via Java permet de convertir une page particulière d'un fichier PDF en image TIFF, utilisez une version surchargée de la méthode Process(..) qui prend un numéro de page en argument pour la conversion. Le fragment de code suivant montre comment convertir la première page d'un PDF au format TIFF.

```java
public void convertPDFtoTiffAllPages() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Utilisez l'algorithme Bradley lors de la conversion

Aspose.PDF for Android via Java prend en charge la fonction de conversion du PDF en TIFF en utilisant la compression LZW et, ensuite, avec l’utilisation d’AForge, la binarisation peut être appliquée. Cependant, l’un des clients a demandé que pour certaines images, ils doivent obtenir le seuil en utilisant Otsu, ils aimeraient également utiliser Bradley.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }
```

