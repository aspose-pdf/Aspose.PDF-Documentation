---
title: Convertir un PDF en PowerPoint en Java
linktitle: Convertir un PDF en PowerPoint
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
description: Découvrez comment convertir des fichiers PDF en PowerPoint en Java avec Aspose.PDF, y compris des diapositives PPTX modifiables, des diapositives basées sur des images et une résolution d'image personnalisée.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment convertir un PDF en PowerPoint en Java
Abstract: Cet article explique comment convertir des fichiers PDF en présentations PowerPoint à l'aide d'Aspose.PDF pour Java. Il couvre la conversion PPTX standard, la sortie de diapositive en tant qu'image et le contrôle de la résolution de l'image via `PptxSaveOptions`.
---
Aspose.PDF pour Java prend en charge l'exportation de pages PDF dans des présentations PowerPoint modifiables avec des options de rendu de diapositives. Utilisez [`PptxSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) pour contrôler la façon dont les pages PDF sont mappées dans les diapositives PowerPoint.


## 
Convertir PDF en PPTX



Utilisez cet exemple lorsqu'un document PDF doit être exporté sous forme de présentation PowerPoint standard.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une valeur par défaut [`PptxSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) pour l'exportation PowerPoint modifiable.
1. Appelez `document.save(outputFile.toString(), saveOptions)` pour que les pages PDF soient sérialisées sous forme de présentation `.pptx`.

1. 
Enregistrez le fichier PPTX converti.


```java
public static void convertPdfToPptx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en PPTX avec des diapositives sous forme d'images



Utilisez cet exemple lorsque chaque page PDF doit devenir une diapositive PowerPoint basée sur une image.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez [`PptxSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) et activez `setSlidesAsImages(true)`.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que chaque page PDF soit rendue sous forme de diapositive soutenue par une image dans la présentation.

1. 
Enregistrez le fichier PPTX généré.


```java
public static void convertPdfToPptxSlidesAsImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setSlidesAsImages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertissez un PDF en PPTX avec une résolution d'image personnalisée



Utilisez cet exemple lorsque la qualité de l’image de la diapositive doit être contrôlée lors de l’exportation PDF vers PPTX.

1. Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`PptxSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) et définissez `setImageResolution(300)` pour une fidélité d'image de diapositive plus élevée.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que le contenu des diapositives pixellisées soit généré à la résolution demandée.

1. 
Enregistrez la présentation de sortie.

```java
public static void convertPdfToPptxImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setImageResolution(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
