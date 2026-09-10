---
title: Ajouter un pied de page au PDF
linktitle: Ajouter un pied de page au PDF
type: docs
weight: 10
url: /java/add-footer/
description: Découvrez comment ajouter des pieds de page de texte et d'image aux pages PDF en Java avec la façade PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des pieds de page de texte et d'image au PDF en Java
Abstract: Découvrez comment ajouter du contenu de pied de page aux documents PDF avec Aspose.PDF pour Java à l'aide de la façade PdfFileStamp. Les exemples Java couvrent les pieds de page en texte brut, les pieds de page d'image chargés à partir d'un flux et les pieds de page en texte avec des marges gauche, droite et inférieure explicites.
---
## Ajouter un pied de page au PDF



Utilisez `PdfFileStamp` lorsque vous avez besoin d'un contenu de pied de page répété sur chaque page d'un document.


### 
Étapes


1. 
Créez une instance `PdfFileStamp` et liez le PDF source.

2. 
Créez le contenu du pied de page sous forme de `FormattedText` ou d'un flux d'images.
3. Appelez la surcharge `addFooter` appropriée.

4. 
Enregistrez le fichier mis à jour et fermez l'objet façade.


### 
Exemples Java

```java
public static void addTextFooter(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Footer");
        pdfStamper.addFooter(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageFooter(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addFooter(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addFooterWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("This footer has margins on all sides.");
        pdfStamper.addFooter(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
