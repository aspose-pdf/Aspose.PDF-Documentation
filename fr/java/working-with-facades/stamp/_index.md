---
title: Classe de timbre
linktitle: Classe de timbre
type: docs
weight: 150
url: /java/stamp-class/
description: Découvrez comment utiliser la classe Stamp en Java pour ajouter des tampons d'image, de PDF et de texte aux documents PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des tampons d'image, de PDF et de texte aux documents PDF en Java
Abstract: Cette section explique comment utiliser la classe Stamp avec PdfFileStamp dans Aspose.PDF pour Java pour ajouter du contenu de tampon réutilisable aux documents PDF. Les exemples Java actuels couvrent les tampons d'image, les tampons de page PDF, les tampons de texte avec un TextState personnalisé, les tampons spécifiques à la page et les tampons d'image d'arrière-plan avec des paramètres d'opacité, de taille et de rotation.
---
La classe Java `StampExamples` présente les principaux flux de travail de création de tampons disponibles via l'API Facades.


## 
Ajouter un tampon d'image



Utilisez ce flux de travail lorsqu'un fichier image doit être placé sur le PDF comme tampon.


### 
Étapes


1. 
Créez une instance `PdfFileStamp` et liez le PDF source.
2. Créez un objet `Stamp` et liez-le au fichier image.

3. 
Définissez l’identifiant du tampon et l’origine du placement.

4. 
Ajoutez le tampon au document.

5. 
Enregistrez le résultat et fermez l'objet façade.


### 
Exemple Java

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setStampId(1);
        stamp.setOrigin(36, 520);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Ajouter une page PDF comme tampon



Utilisez ce flux de travail lorsque le contenu d'une autre page PDF doit être réutilisé comme contenu de tampon.


### 
Étapes


1. 
Créez une instance `PdfFileStamp` et liez le PDF cible.

2. 
Créez un objet `Stamp`.
3. Liez le tampon à une page spécifique d'un autre fichier PDF.

4. 
Définissez le numéro de page cible et l’origine du placement.

5. 
Ajoutez le tampon, enregistrez la sortie et fermez l'objet façade.


### 
Exemple Java


```java
public static void addPdfPageAsStamp(Path inputFile, Path stampPdf, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindPdf(stampPdf.toString(), 1);
        stamp.setPageNumber(1);
        stamp.setOrigin(36, 250);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## 
Ajouter un tampon de texte avec TextState

Utilisez ce flux de travail lorsque le tampon doit contenir du texte stylisé plutôt qu'une image.


### 
Étapes


1. 
Créez une instance `PdfFileStamp` et liez le PDF source.

2. 
Créez un objet `Stamp`.

3. 
Liez un logo `FormattedText` et un `TextState` personnalisé au tampon.
4. Définissez l’origine et la rotation du tampon.

5. 
Ajoutez le tampon, enregistrez la sortie et fermez l'objet façade.


### 
Exemple Java


```java
public static void addTextStampWithTextState(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindLogo(createTextLogo("Approved by signing workflow"));
        stamp.bindTextState(createTextState());
        stamp.setOrigin(36, 700);
        stamp.setRotation(15.0f);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## 
Ajouter un tampon à des pages spécifiques



Utilisez ce flux de travail lorsque le tampon doit apparaître uniquement sur les pages sélectionnées au lieu de l'ensemble du document.

### Étapes


1. 
Créez une instance `PdfFileStamp` et liez le PDF source.

2. 
Créez un objet `Stamp` et liez-le à un fichier image.

3. 
Définissez la liste des pages cibles, l'origine et la taille de l'image.

4. 
Ajoutez le tampon au document.
5. Enregistrez le résultat et fermez l'objet façade.


### 
Exemple Java


```java
public static void addStampToSpecificPages(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setPages(new int[] {1});
        stamp.setOrigin(400, 40);
        stamp.setImageSize(120, 60);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## 
Ajouter un tampon d'image d'arrière-plan



Utilisez ce flux de travail lorsque le tampon doit apparaître derrière le contenu de la page avec une opacité et une rotation contrôlées.


### 
Étapes

1. Créez une instance `PdfFileStamp` et liez le PDF source.

2. 
Créez un objet `Stamp` et liez-le au fichier image.

3. 
Marquez le tampon comme contenu d’arrière-plan.

4. 
Configurez l'opacité, la qualité, la rotation, la taille et l'origine.

5. 
Ajoutez le tampon, enregistrez la sortie et fermez l'objet façade.

### Exemple Java

```java
public static void addBackgroundImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setBackground(true);
        stamp.setOpacity(0.35f);
        stamp.setQuality(90);
        stamp.setRotation(45.0f);
        stamp.setImageSize(160, 80);
        stamp.setOrigin(200, 300);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
