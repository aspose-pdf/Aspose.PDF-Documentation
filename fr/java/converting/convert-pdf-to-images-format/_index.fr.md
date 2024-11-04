---
title: Convertir PDF en formats d'images 
linktitle: Convertir PDF en Images
type: docs
weight: 70
url: /java/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir des PDF en divers formats d'images. Convertissez des pages PDF en images PNG, JPEG, BMP avec quelques lignes de code.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for Java** vous permet de convertir des documents PDF en formats d'image tels que BMP, JPEG, GIF, PNG, EMF, TIFF et SVG en utilisant deux approches. La conversion est effectuée en utilisant Device et en utilisant SaveOption.

Il existe plusieurs classes dans la bibliothèque qui vous permettent d'utiliser un dispositif virtuel pour transformer des images. DocumentDevice est orienté pour la conversion de l'ensemble du document, mais ImageDevice - pour une page particulière.

## Convertir un PDF en utilisant la classe DocumentDevice

**Aspose.PDF for Java** permet de convertir des pages PDF en images TIFF.

La [classe TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) vous permet de convertir des pages PDF en images TIFF.
 Cette classe fournit une méthode nommée Process qui vous permet de convertir toutes les pages d'un fichier PDF en une seule image TIFF.

### Convertir les pages PDF en une image TIFF unique

Aspose.PDF pour Java explique comment convertir toutes les pages d'un fichier PDF en une seule image TIFF :

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Appelez la méthode [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) pour convertir le document.
1. Pour définir les propriétés du fichier de sortie, utilisez la classe [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings).

Le code suivant montre comment convertir toutes les pages PDF en une seule image TIFF.

```java
// Ouvrir le document
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// Créer un objet Resolution
Resolution resolution = new Resolution(300);

// Créer un objet TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);
tiffSettings.setSkipBlankPages(false);

// Créer un appareil TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// Convertir une page particulière et enregistrer l'image dans un flux
tiffDevice.process(document, DATA_DIR + "AllPagesToTIFF_out.tif");
```

### Convertir une page unique en image TIFF

Aspose.PDF pour Java permet de convertir une page particulière d'un fichier PDF en une image TIFF, en utilisant une version surchargée de la méthode Process(..) qui prend un numéro de page en argument pour la conversion. L'extrait de code suivant montre comment convertir la première page d'un PDF au format TIFF.

```java
// Ouvrir le document
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
String tiffFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF_out.tif").toString();
Document document = new Document(documentFileName);

// Créer un objet Resolution
Resolution resolution = new Resolution(300);

// Créer un objet TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);

// Créer un périphérique TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// Convertir une page particulière et enregistrer l'image dans le flux
tiffDevice.process(document, 1, 1, tiffFileName);
```


### Utiliser l'algorithme de Bradley pendant la conversion

Aspose.PDF pour Java prend en charge la fonctionnalité de conversion de PDF en TIFF en utilisant la compression LZW, puis avec l'utilisation d'AForge, la binarisation peut être appliquée. Cependant, l'un des clients a demandé que pour certaines images, ils aient besoin d'obtenir le seuil en utilisant Otsu, donc ils aimeraient également utiliser Bradley.

```java
// Ouvrir le document
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

String outputImageFileName = Paths.get(DATA_DIR.toString(), "resultant_out.tif").toString();
String outputBinImageFileName = Paths.get(DATA_DIR.toString(), "tiff-bin_out.tif").toString();

java.io.OutputStream outputImageFile = new java.io.FileOutputStream(outputImageFileName);
java.io.OutputStream outputBinImageFile = new java.io.FileOutputStream(outputBinImageFileName);

// Créer un objet Resolution
Resolution resolution = new Resolution(300);
// Créer un objet TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.LZW);
tiffSettings.setDepth(ColorDepth.Format1bpp);

// Créer un dispositif TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
// Convertir une page particulière et enregistrer l'image dans le flux
tiffDevice.process(document, outputImageFile);
outputImageFile.close();

// Créer un objet stream pour enregistrer l'image de sortie
java.io.InputStream inStream = new java.io.FileInputStream(outputImageFileName);
tiffDevice.binarizeBradley(inStream, outputBinImageFile, 0.1);
```


### Convertir des Pages PDF en Images TIFF Pixelisées

Pour convertir toutes les pages d'un fichier PDF au format TIFF pixelisé, utilisez l'option Pixelated de IndexedConversionType

```java
// Convertir des Pages PDF en Images TIFF Pixelisées
// Pour convertir toutes les pages d'un fichier PDF au format TIFF pixelisé, utilisez l'option Pixelated
// de IndexedConversionType.

// Ouvrir le document
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// Créer un objet stream pour enregistrer l'image de sortie
java.io.OutputStream imageStream = new java.io.FileOutputStream("Image.tiff");

// Créer un objet Resolution
com.aspose.pdf.devices.Resolution resolution = new com.aspose.pdf.devices.Resolution(300);

// Instanciation de l'objet TiffSettings
com.aspose.pdf.devices.TiffSettings tiffSettings = new com.aspose.pdf.devices.TiffSettings();

// définir la compression de l'image TIFF résultante
tiffSettings.setCompression(com.aspose.pdf.devices.CompressionType.CCITT4);
// définir la profondeur de couleur pour l'image résultante
tiffSettings.setDepth(com.aspose.pdf.devices.ColorDepth.Format4bpp);
// ignorer les pages blanches lors du rendu PDF en TIFF
tiffSettings.setSkipBlankPages(true);
// définir la luminosité de l'image
tiffSettings.setBrightness(.5f);

// définir le type de conversion indexé, la valeur par défaut est simple
tiffSettings.setIndexedConversionType(IndexedConversionType.Pixelated);

// Créer un objet TiffDevice avec une résolution particulière
TiffDevice tiffDevice = new TiffDevice(2480, 3508, resolution, tiffSettings);

// Convertir une page particulière (Page 1) et enregistrer l'image dans le flux
tiffDevice.process(document, 1, 1, imageStream);

// Fermer le flux
imageStream.close();
```


{{% alert color="success" %}}
**Essayez de convertir un PDF en TIFF en ligne**

Aspose.PDF pour Java vous présente une application en ligne gratuite ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF conversion PDF to TIFF avec une application gratuite](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Convertir un PDF en utilisant la classe ImageDevice

`ImageDevice` est l'ancêtre de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` et `EmfDevice`.

- La classe [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) vous permet de convertir des pages PDF en images <abbr title="Bitmap Image File">BMP</abbr>.
- La classe [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) vous permet de convertir des pages PDF en images <abbr title="Enhanced Meta File">EMF</abbr>.

- La classe [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) vous permet de convertir des pages PDF en images JPEG.
- La classe [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) vous permet de convertir des pages PDF en images <abbr title="Portable Network Graphics">PNG</abbr>.
- La classe [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) vous permet de convertir des pages PDF en images <abbr title="Graphics Interchange Format">GIF</abbr>.

Voyons comment convertir une page PDF en image.

La classe [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) fournit une méthode nommée [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) qui vous permet de convertir une page particulière du fichier PDF au format image BMP. Les autres classes ont la même méthode. Donc, si nous avons besoin de convertir une page PDF en image, nous devons simplement instancier la classe requise.

L'extrait de code suivant montre cette possibilité :

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.*;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Convertir PDF en Image.
 */
public final class ConvertPDFtoImage {
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoImage() {

    }

    public static void run() throws IOException {
        runConvertPdfUsingImageDevice();
    }

    public static void runConvertPdfUsingImageDevice() throws IOException {
        // Créer un objet Résolution
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(DATA_DIR + "ConvertAllPagesToBmp.pdf");

        convertPDFtoImages(bmpDevice, "bmp", document);
        convertPDFtoImages(jpegDevice, "jpeg", document);
        convertPDFtoImages(gifDevice, "gif", document);
        convertPDFtoImages(pngDevice, "png", document);
        convertPDFtoImages(emfDevice, "emf", document);
    }

    public static void convertPDFtoImages(
            ImageDevice imageDevice,
            String ext,
            Document document)
            throws IOException {
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            java.io.OutputStream imageStream = new java.io.FileOutputStream(
                    DATA_DIR + "image" + pageCount + "_out." + ext);
            // Convertir une page particulière et enregistrer l'image dans le flux
            imageDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Fermer le flux
            imageStream.close();
        }
    }
}
```


{{% alert color="success" %}}
**Essayez de convertir PDF en PNG en ligne**

Comme exemple de fonctionnement de nos applications gratuites, veuillez vérifier la fonctionnalité suivante.

Aspose.PDF pour Java vous présente l'application gratuite en ligne ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Comment convertir PDF en PNG en utilisant l'application gratuite](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF en utilisant la classe SaveOptions

Cette partie de l'article vous montre comment convertir PDF en <abbr title="Scalable Vector Graphics">SVG</abbr> en utilisant Java et la classe SaveOptions.

{{% alert color="success" %}}
**Essayez de convertir PDF en SVG en ligne**

Aspose.PDF pour Java vous présente l'application gratuite en ligne ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en SVG avec l'application gratuite](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** est une famille de spécifications d'un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est en développement par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'elles peuvent être recherchées, indexées, scriptées et, si nécessaire, compressées. En tant que fichiers XML, les images SVG peuvent être créées et éditées avec n'importe quel éditeur de texte, mais il est souvent plus pratique de les créer avec des programmes de dessin tels qu'Inkscape.

### Convertir des pages PDF en images SVG

Aspose.PDF for Java prend en charge la fonctionnalité de conversion de fichiers PDF au format SVG.
 Pour accomplir cette exigence, la classe [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) a été introduite dans le package com.aspose.pdf. Instanciez un objet de [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) et passez-le comme second argument à la méthode [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Le code suivant montre les étapes pour convertir un fichier PDF en format SVG.

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.SvgSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Convertir PDF en SVG.
 */
public class ConvertPDFtoSVG {
    // Le chemin vers le répertoire des documents.
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoSVG() {

    }

    public static void run() throws IOException {
        String pdfFileName = Paths.get(DATA_DIR.toString(), "input.pdf").toString();
        String svgFileName = Paths.get(DATA_DIR.toString(), "PDFToSVG_out.svg").toString();

        // Charger le document PDF
        Document document = new Document(pdfFileName);

        // Instancier un objet de SvgSaveOptions
        SvgSaveOptions saveOptions = new SvgSaveOptions();

        // Ne pas compresser l'image SVG dans une archive Zip
        saveOptions.setCompressOutputToZipArchive(false);

        // Enregistrer la sortie dans des fichiers SVG
        document.save(svgFileName, saveOptions);
        document.close();
    }
}
```