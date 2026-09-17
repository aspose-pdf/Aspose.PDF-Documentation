---
title: Convertir un PDF en HTML en Java
linktitle: Convertir un PDF au format HTML
type: docs
weight: 50
url: /java/convert-pdf-to-html/
lastmod: "2026-06-16"
description: Apprenez à convertir un PDF en HTML en Java avec Aspose.PDF, y compris la sortie multipage, les dossiers d'images externes, la gestion SVG et le rendu HTML en couches.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir un PDF en HTML en Java
Abstract: Cet article explique comment convertir des fichiers PDF en HTML à l'aide d'Aspose.PDF pour Java. Il couvre l'exportation HTML de base ainsi que les options pour les dossiers d'images, le fractionnement de page, la sortie SVG, les graphiques SVG compressés, les arrière-plans de page PNG, le balisage du corps uniquement, le rendu de texte transparent et la conversion des couches de document.
---
Aspose.PDF pour Java prend en charge l'exportation HTML avec des options pour les images, SVG, le fractionnement de page, la transparence et le rendu des calques. Utilisez [`HtmlSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) pour contrôler la façon dont les pages PDF, les ressources et le balisage sont écrits dans la sortie HTML.


## 
Convertir un PDF en HTML



Utilisez cet exemple lorsqu'un PDF doit être exporté vers un document HTML standard.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une valeur par défaut [`HtmlSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) pour la sérialisation HTML standard.
1. Appelez `document.save(outputFile.toString(), saveOptions)` pour que le contenu de la page PDF soit exporté sous forme de balisage HTML.

1. 
Enregistrez la sortie HTML générée.


```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertissez le PDF en HTML et stockez les images séparément



Utilisez cet exemple lorsque les images extraites doivent être écrites sous forme de fichiers séparés lors de l'exportation HTML.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez [`HtmlSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) et définissez `setSpecialFolderForAllImages(...)` sur un répertoire de sortie d'image dédié.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que les images raster soient émises sous forme de fichiers de ressources distincts au lieu d'une sortie en ligne uniquement.

1. 
Enregistrez la sortie HTML avec les ressources d'image générées.


```java
public static void convertPdfToHtmlStoringImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForAllImages(inputFile.getParent().resolve("images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en HTML multipage



Utilisez cet exemple lorsque chaque page PDF doit être représentée séparément dans la sortie HTML.

1. Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`HtmlSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) et activez `setSplitIntoPages(true)`.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que chaque page PDF soit écrite sous forme de sortie HTML distincte.

1. 
Enregistrez les fichiers HTML générés.


```java
public static void convertPdfToHtmlMultiPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertissez le PDF en HTML et stockez le SVG séparément

Utilisez cet exemple lorsque le contenu vectoriel doit être émis en tant que ressources SVG distinctes.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`HtmlSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) et définissez `setSpecialFolderForSvgImages(...)` sur un répertoire de ressources SVG externe.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que les graphiques vectoriels soient stockés en dehors du fichier HTML principal.

1. 
Enregistrez la sortie HTML et les ressources SVG.

```java
public static void convertPdfToHtmlStoringSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir un PDF en HTML avec du SVG compressé



Utilisez cet exemple lorsque la sortie SVG doit être optimisée lors de l'exportation HTML.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`HtmlSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) et configurez un dossier dédié aux ressources SVG.

1. 
Activez `setCompressSvgGraphicsIfAny(true)` pour que les ressources SVG soient compressées lors de l'exportation.
1. Appelez `document.save(outputFile.toString(), saveOptions)` et enregistrez les fichiers HTML convertis.


```java
public static void convertPdfToHtmlCompressSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        saveOptions.setCompressSvgGraphicsIfAny(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en HTML avec des arrière-plans de page PNG



Utilisez cet exemple lorsque les arrière-plans de page doivent être rendus sous forme d'images PNG dans la sortie HTML.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`HtmlSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) et définissez le mode d'enregistrement des images raster sur les arrière-plans de page PNG.
1. Appelez `document.save(outputFile.toString(), saveOptions)` pour que le contenu de l'arrière-plan de la page soit émis sous forme de couches HTML sauvegardées au format PNG.

1. 
Enregistrez la sortie HTML convertie.


```java
public static void convertPdfToHtmlPngBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setRasterImagesSavingMode(
                HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir uniquement le contenu du corps PDF en HTML



Utilisez cet exemple lorsque seul le balisage du corps est nécessaire au lieu d’un shell de document HTML complet.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez [`HtmlSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) et définissez le mode de génération de balisage sur `WriteOnlyBodyContent`.

1. 
Gardez `setSplitIntoPages(true)` activé lorsque la sortie du corps uniquement doit toujours être séparée par des pages.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` et enregistrez la sortie HTML.


```java
public static void convertPdfToHtmlBodyContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setHtmlMarkupGenerationMode(
                HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertissez un PDF en HTML avec un rendu de texte transparent



Utilisez cet exemple lorsque le texte transparent doit être conservé dans l'exportation HTML.

1. Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`HtmlSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) et activez la préservation du texte transparent et ombré.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que l'apparence du texte liée à la transparence soit conservée dans le résultat HTML.

1. 
Enregistrez la sortie HTML convertie.


```java
public static void convertPdfToHtmlTransparentTextRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSaveTransparentTexts(true);
        saveOptions.setSaveShadowedTextsAsTransparentTexts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en HTML avec le rendu des couches de document

Utilisez cet exemple lorsque la visibilité du calque PDF doit être reflétée dans le résultat HTML.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`HtmlSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) et activez `setConvertMarkedContentToLayers(true)`.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que le contenu PDF marqué soit mappé dans des couches HTML.

1. 
Enregistrez les fichiers HTML exportés.

```java
public static void convertPdfToHtmlDocumentLayersRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setConvertMarkedContentToLayers(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
