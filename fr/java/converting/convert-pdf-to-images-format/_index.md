---
title: Convertir un PDF en formats d'image en Java
linktitle: Convertir un PDF en images
type: docs
weight: 70
url: /java/convert-pdf-to-images-format/
lastmod: "2026-06-16"
description: Apprenez à restituer des pages PDF sous forme de fichiers TIFF, BMP, EMF, JPEG, PNG, GIF et SVG en Java avec Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Convertir des pages PDF en TIFF, PNG, JPEG, GIF, BMP, EMF et SVG en Java
Abstract: Cet article explique comment convertir des fichiers PDF en formats d'image courants avec Aspose.PDF pour Java. Il couvre l'exportation TIFF à l'échelle du document, la génération de raster par page avec des périphériques d'image, la substitution facultative de polices lors de l'exportation PNG et la sortie SVG avec `SvgSaveOptions`.
---
Aspose.PDF pour Java peut restituer les pages PDF aux formats d'image raster et vectorielle avec des options de périphérique spécifiques au format.


## 
Convertir un PDF en BMP



Utilisez cet exemple lorsque les pages PDF doivent être rendues sous forme d'images BMP.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [`BmpDevice`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) avec un [`Resolution`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Parcourez `document.getPages()` et appelez `device.process(...)` pour chaque page.

1. 
Enregistrez les images BMP générées dans des chemins de sortie numérotés.


```java
public static void convertPdfToBmp(Path inputFile, Path outputPrefix) {
       try (Document document = new Document(inputFile.toString())) {
           BmpDevice device = new BmpDevice(new Resolution(300));
           for (int page = 1; page <= document.getPages().size(); page++) {
               device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "bmp"));
           }
       }
       System.out.println(inputFile + " converted into " + outputPrefix);
   }
```

## 
Convertir un PDF en EMF



Utilisez cet exemple lorsque les pages PDF doivent être exportées sous forme d’images vectorielles EMF.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez un [`EmfDevice`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) avec un [`Resolution`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.

1. 
Parcourez les pages et appelez `device.process(...)` pour chaque page.

1. 
Enregistrez les sorties EMF dans des chemins de fichiers numérotés.


```java
public static void convertPdfToEmf(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        EmfDevice device = new EmfDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "emf"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
Convertir un PDF en GIF



Utilisez cet exemple lorsque les pages PDF doivent être converties en images GIF.

1. Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [`GifDevice`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) avec un [`Resolution`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.

1. 
Parcourez les pages et appelez `device.process(...)` pour afficher chaque page.

1. 
Enregistrez les fichiers GIF dans des chemins de sortie numérotés.


```java
public static void convertPdfToGif(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        GifDevice device = new GifDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "gif"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
Convertir un PDF en JPEG

Utilisez cet exemple lorsque les pages PDF doivent être exportées sous forme d'images JPEG.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [`JpegDevice`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) avec un [`Resolution`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.

1. 
Parcourez les pages et appelez `device.process(...)` pour pixelliser chaque page au format JPEG.

1. 
Enregistrez les fichiers de sortie JPEG dans des chemins numérotés.

```java
public static void convertPdfToJpeg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        JpegDevice device = new JpegDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "jpeg"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Convertir un PDF en PNG



Utilisez cet exemple lorsque les pages PDF doivent être converties en images PNG.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [`PngDevice`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) avec un [`Resolution`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.

1. 
Parcourez les pages et appelez `device.process(...)` pour chaque page PDF.
1. Enregistrez les sorties PNG dans des chemins de fichiers numérotés.


```java
public static void convertPdfToPng(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
Convertir un PDF en PNG avec une police de secours par défaut



Utilisez cet exemple lorsque le rendu doit utiliser une police de secours pour les glyphes manquants.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [`PngDevice`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) avec un [`Resolution`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI.
1. Activez `document.setAbsentFontTryToSubstitute(true)` pour que les glyphes manquants puissent revenir à des polices de substitution lors du rendu.

1. 
Rendez les pages et enregistrez les fichiers PNG.


```java
public static void convertPdfToPngWithDefaultFont(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        document.setAbsentFontTryToSubstitute(true);
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
Convertir un PDF en SVG



Utilisez cet exemple lorsque les pages PDF doivent être exportées sous forme de graphiques SVG.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez [`SvgSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) et désactivez la compression ZIP lorsque la sortie brute `.svg` est requise.

1. 
Activez `setTreatTargetFileNameAsDirectory(true)` pour que la sortie SVG par page puisse être organisée sous le chemin cible.

1. 
Enregistrez la sortie SVG.


```java
public static void convertPdfToSvg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        SvgSaveOptions saveOptions = new SvgSaveOptions();
        saveOptions.setCompressOutputToZipArchive(false);
        saveOptions.setTreatTargetFileNameAsDirectory(true);
        document.save(outputPrefix + ".svg", saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
Convertir un PDF en TIFF



Utilisez cet exemple lorsqu'une ou plusieurs pages PDF doivent être exportées au format TIFF.

1. Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`TiffSettings`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) et configurez la compression, la profondeur de couleur et le comportement des pages blanches.

1. 
Créez un [`TiffDevice`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) avec un [`Resolution`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) de 300 DPI et les paramètres TIFF préparés.

1. 
Effectuez le rendu des pages et enregistrez la sortie TIFF.

```java
public static void convertPdfToTiff(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.LZW);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setSkipBlankPages(false);

        TiffDevice tiffDevice = new TiffDevice(new Resolution(300), tiffSettings);
        tiffDevice.process(document, outputPrefix + ".tiff");
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```
