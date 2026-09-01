---
title: Ajouter un tampon au PDF
linktitle: Ajouter un tampon au PDF
type: docs
weight: 40
url: /java/add-stamp/
description: Découvrez comment ajouter un tampon d'image aux pages PDF en Java avec la façade PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des tampons d'image au PDF en Java
Abstract: Découvrez comment ajouter du contenu de tampon aux documents PDF avec Aspose.PDF pour Java à l'aide de la façade PdfFileStamp. L'ensemble d'exemples Java actuel montre comment créer un `Stamp`, le lier à un fichier image, l'ajouter au document et enregistrer le PDF tamponné.
---
## Ajouter un tampon au PDF



Utilisez ce flux de travail lorsqu'un tampon basé sur une image doit être appliqué au PDF.


### 
Étapes


1. 
Créez une instance `PdfFileStamp` et liez le PDF source.

2. 
Créez un objet `Stamp`.
3. Liez le tampon à un fichier image avec `bindImage`.

4. 
Ajoutez le tampon au document avec `addStamp`.

5. 
Enregistrez la sortie et fermez l’objet façade.


### 
Exemple Java


```java
public static void addStampToPdf(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```


La classe `PdfFileStampExamples.java` actuelle n'inclut pas d'exemple Java distinct pour la configuration des tampons de texte uniquement, de la rotation ou de l'opacité.
