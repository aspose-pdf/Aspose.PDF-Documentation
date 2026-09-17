---
title: Ajouter un numéro de page au PDF
linktitle: Ajouter un numéro de page au PDF
type: docs
weight: 30
url: /java/page-number/
description: Découvrez comment ajouter des numéros de page aux documents PDF en Java avec la façade PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des numéros de page au PDF en Java
Abstract: Découvrez comment ajouter des numéros de page aux documents PDF avec Aspose.PDF pour Java à l'aide de la façade PdfFileStamp. Les exemples Java couvrent le placement par défaut, les coordonnées explicites, le placement aligné avec des marges et la sortie en numérotation romaine avec un numéro de départ personnalisé.
---
## Ajouter un numéro de page au PDF



Utilisez `PdfFileStamp` lorsque la numérotation des pages doit être appliquée après que le contenu PDF a déjà été créé.


### 
Étapes


1. 
Créez une instance `PdfFileStamp` et liez le PDF source.

2. 
Choisissez la stratégie de placement par numéro de page dont vous avez besoin.
3. Définissez éventuellement le style de numérotation et le numéro de départ avant le tamponnage.

4. 
Appelez `addPageNumber` avec la surcharge requise.

5. 
Enregistrez la sortie et fermez l’objet façade.


### 
Exemples Java

```java
public static void addPageNumbersDefault(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #");
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersAtCoordinates(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", 300, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithPositionAndMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_BOTTOM_RIGHT, 10, 10, 10, 10);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithRomanStyle(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pdfStamper.setStartingNumber(42);
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_UPPER_RIGHT);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
