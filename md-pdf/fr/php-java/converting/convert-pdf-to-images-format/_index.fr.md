---
title: Convertir PDF en formats d'images 
linktitle: Convertir PDF en images
type: docs
weight: 70
url: /php-java/convert-pdf-to-images-format/
lastmod: "2024-05-20"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un PDF en divers formats d'images. Convertissez des pages PDF en images PNG, JPEG, BMP avec quelques lignes de code.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF pour PHP** vous permet de convertir des documents PDF en formats d'images tels que BMP, JPEG, GIF, PNG, EMF, TIFF et SVG en utilisant deux approches. La conversion est effectuée en utilisant `Device` et en utilisant `SaveOption`.

Il existe plusieurs classes dans la bibliothèque qui vous permettent d'utiliser un dispositif virtuel pour transformer des images. `DocumentDevice` est orienté pour la conversion de l'ensemble du document, mais `ImageDevice` - pour une page particulière.

## Convertir un PDF en utilisant la classe DocumentDevice

**Aspose.PDF pour PHP** rend possible la conversion de pages PDF en images TIFF.

La [classe TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) vous permet de convertir des pages PDF en images TIFF.
 Cette classe fournit une méthode nommée Process qui vous permet de convertir toutes les pages d'un fichier PDF en une seule image TIFF.

### Convertir les Pages PDF en une Image TIFF Unique

Aspose.PDF pour PHP explique comment convertir toutes les pages d'un fichier PDF en une seule image TIFF :

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Appelez la méthode [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) pour convertir le document.
1. Pour définir les propriétés du fichier de sortie, utilisez la classe [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings).

Le code suivant montre comment convertir toutes les pages PDF en une seule image TIFF.

```php
// Charger le document PDF
$document = new Document($inputFile);

// Créer un nouvel objet TiffSettings
$tiffSettings = new devices_TiffSettings();

// Décommentez les lignes suivantes pour personnaliser les paramètres TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// Définir la résolution pour l'image TIFF
$resolution = new devices_Resolution(300);

// Créer un nouvel objet TiffDevice avec la résolution et les paramètres spécifiés
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Convertir le document PDF en TIFF à l'aide du TiffDevice
$tiffDevice->process($document, $outputFile);
```

### Convertir une seule page en image TIFF

Aspose.PDF pour PHP permet de convertir une page particulière d'un fichier PDF en une image TIFF, en utilisant une version surchargée de la méthode Process(..) qui prend un numéro de page comme argument pour la conversion. Le code suivant montre comment convertir la première page d'un PDF en format TIFF.

```php
// Charger le document PDF
$document = new Document($inputFile);

// Créer un nouvel objet TiffSettings
$tiffSettings = new devices_TiffSettings();

// Décommenter les lignes suivantes pour personnaliser les paramètres TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// Définir la résolution pour l'image TIFF
$resolution = new devices_Resolution(300);

// Créer un nouvel objet TiffDevice avec la résolution et les paramètres spécifiés
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Convertir le document PDF en TIFF en utilisant le TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);
```


### Utiliser l'algorithme de Bradley pendant la conversion

Aspose.PDF pour PHP prend en charge la fonctionnalité de conversion de PDF en TIFF en utilisant la compression LZW, puis avec l'utilisation d'AForge, la binarisation peut être appliquée. Cependant, l'un des clients a demandé que pour certaines images, ils aient besoin d'obtenir le seuil en utilisant Otsu, donc ils aimeraient également utiliser Bradley.

```php
// Créer un nouvel objet TiffSettings
$tiffSettings = new devices_TiffSettings();

// Décommentez les lignes suivantes pour personnaliser les paramètres TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// Définir la résolution pour l'image TIFF
$resolution = new devices_Resolution(300);

// Créer un nouvel objet TiffDevice avec la résolution et les paramètres spécifiés
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Convertir le document PDF en TIFF en utilisant le TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);

// Créer un objet de flux pour sauvegarder l'image de sortie
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


### Convertir les Pages PDF en Images TIFF Pixelisées

Pour convertir toutes les pages d'un fichier PDF au format TIFF pixelisé, utilisez l'option Pixelated de IndexedConversionType

```php
// Créez un nouvel objet TiffSettings
$tiffSettings = new devices_TiffSettings();

// Décommentez les lignes suivantes pour personnaliser les paramètres TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);
// régler la luminosité de l'image
$tiffSettings->setBrightness(0.5f);
// définir le type de conversion indexée, la valeur par défaut est simple
$tiffSettings->setIndexedConversionType(IndexedConversionType::Pixelated);


$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// Définir la résolution pour l'image TIFF
$resolution = new devices_Resolution(300);

// Créez un nouvel objet TiffDevice avec la résolution et les paramètres spécifiés
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Convertissez le document PDF en TIFF en utilisant le TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);

// Créez un objet de flux pour enregistrer l'image de sortie
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


{{% alert color="success" %}}
**Essayez de convertir PDF en TIFF en ligne**

Aspose.PDF pour PHP vous présente l'application en ligne gratuite ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF conversion PDF en TIFF avec application gratuite](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Convertir PDF en utilisant la classe ImageDevice

`ImageDevice` est l'ancêtre de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` et `EmfDevice`.

- La classe [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) vous permet de convertir des pages PDF en images <abbr title="Bitmap Image File">BMP</abbr>.
- La classe [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) vous permet de convertir des pages PDF en images <abbr title="Enhanced Meta File">EMF</abbr>.

- La classe [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) vous permet de convertir des pages PDF en images JPEG.
- La classe [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) vous permet de convertir des pages PDF en images <abbr title="Portable Network Graphics">PNG</abbr>.
- La classe [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) vous permet de convertir des pages PDF en images <abbr title="Graphics Interchange Format">GIF</abbr>.

Voyons comment convertir une page PDF en image.

La classe [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) fournit une méthode nommée [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) qui vous permet de convertir une page particulière du fichier PDF en format d'image BMP. Les autres classes ont la même méthode. Donc, si nous devons convertir une page PDF en image, nous devons simplement instancier la classe requise.

L'extrait de code suivant montre cette possibilité :

```php
// Charger le document PDF
$document = new Document($inputFile);

// Obtenir la collection de pages dans le document
$pages = $document->getPages();

// Obtenir le nombre total de pages dans le document
$count = $pages->size();

// Définir la résolution pour les images PNG
$resolution = new devices_Resolution(300);

// Créer un nouveau périphérique PNG avec la résolution spécifiée
$imageDevice = new devices_PngDevice($resolution);

// Parcourir chaque page du document
for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {
    // Définir le nom de fichier image de sortie pour la page en cours
    $imageFileName = $imageFileNameTemplate . $pageCount . '.png';

    // Obtenir la page en cours de la collection
    $page = $document->getPages()->get_Item($pageCount);

    // Traiter la page en cours et l'enregistrer en tant qu'image PNG
    $imageDevice->process($page, $imageFileName);
}
```


{{% alert color="success" %}}
**Essayez de convertir PDF en PNG en ligne**

À titre d'exemple de fonctionnement de nos applications gratuites, veuillez vérifier la fonctionnalité suivante.

Aspose.PDF pour PHP vous présente l'application gratuite en ligne ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Comment convertir PDF en PNG en utilisant l'application gratuite](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF en utilisant la classe SaveOptions

Cette partie de l'article vous montre comment convertir PDF en <abbr title="Scalable Vector Graphics">SVG</abbr> en utilisant Java et la classe SaveOptions.

{{% alert color="success" %}}
**Essayez de convertir PDF en SVG en ligne**

Aspose.PDF pour PHP vous présente l'application gratuite en ligne ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion PDF en SVG avec Aspose.PDF et l'application gratuite](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** est une famille de spécifications d'un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est un standard ouvert qui est en développement par le World Wide Web Consortium (W3C) depuis 1999.

Les images SVG et leurs comportements sont définis dans des fichiers texte XML. Cela signifie qu'elles peuvent être recherchées, indexées, scriptées et, si nécessaire, compressées. En tant que fichiers XML, les images SVG peuvent être créées et éditées avec n'importe quel éditeur de texte, mais il est souvent plus pratique de les créer avec des programmes de dessin tels que Inkscape.

### Convertir des pages PDF en images SVG

Aspose.PDF pour PHP prend en charge la conversion de fichiers PDF au format SVG.
 Pour accomplir cette exigence, la classe [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) a été introduite dans le package com.aspose.pdf. Instanciez un objet de [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) et passez-le comme deuxième argument à la méthode [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Le code suivant montre les étapes pour convertir un fichier PDF en format SVG.

```php
// Charger le document PDF
$document = new Document($inputFile);

// Créer une instance de la classe SvgSaveOptions
$saveOption = new SvgSaveOptions();

// Enregistrer le document PDF en tant que SVG
$document->save($outputFile, $saveOption);
```