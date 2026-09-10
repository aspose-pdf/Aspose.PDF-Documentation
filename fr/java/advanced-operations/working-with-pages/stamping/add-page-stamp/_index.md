---
title: Ajouter des tampons de page au PDF en Java
linktitle: Ajout de tampons de page
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: Découvrez comment ajouter des tampons de page PDF en tant que superpositions ou arrière-plans en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des tampons basés sur des pages aux fichiers PDF avec Java
Abstract: Cet article explique comment ajouter un tampon de page à un document PDF à l'aide d'Aspose.PDF pour Java. L'exemple charge une autre page PDF comme tampon, la configure comme arrière-plan et l'applique à une page cible.
---
Aspose.PDF pour Java peut appliquer une page d'un autre PDF comme tampon ou ajouter des superpositions de numérotation de pages.


## 
Ajouter un cachet de page à partir d'un autre PDF



Utilisez cet exemple lorsqu'une page d'un PDF distinct doit être utilisée comme tampon d'arrière-plan.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [PdfPageStamp] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfpagestamp/) à partir de la page PDF externe.
1. Configurez le tampon et ajoutez-le à la page cible, puis enregistrez le résultat.


```java
public static void addPageStamp(Path inputFile, Path pageStampFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfPageStamp pageStamp = new PdfPageStamp(pageStampFile.toString(), 1);
        pageStamp.setBackground(true);
        document.getPages().get_Item(1).addStamp(pageStamp);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter un tampon de numéro de page standard



Utilisez cet exemple lorsque la page cible doit afficher le numéro actuel avec un formatage de texte personnalisé.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez et configurez un [PageNumberStamp] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
1. Ajoutez le tampon à la page et enregistrez le document.


```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter un tampon de numéro de page en chiffres romains



Utilisez cet exemple lorsque la numérotation des pages doit commencer à partir d’une valeur personnalisée et utiliser des chiffres romains majuscules.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [PageNumberStamp] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) et configurez la numérotation en chiffres romains.
1. Ajoutez le tampon à toutes les pages et enregistrez le PDF.

```java
public static void addPageNumStampRoman(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(42);
        pageNumberStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        for (Page page : document.getPages()) {
            page.addStamp(pageNumberStamp);
        }
        document.save(outputFile.toString());
    }
}
```
