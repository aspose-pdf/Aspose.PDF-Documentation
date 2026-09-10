---
title: Multimédia
linktitle: Multimédia
type: docs
weight: 70
url: /java/pdfcontenteditor-multimedia/
description: Découvrez la couverture multimédia actuelle disponible dans la façade Java PdfContentEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Workflows d'annotation multimédia en Java avec PdfContentEditor
Abstract: Cette section couvre les flux de travail liés au multimédia actuellement pris en charge par l'ensemble d'exemples Java PdfContentEditor. Le référentiel comprend un exemple d'annotation directe de film, tandis que les sujets sonores non pris en charge sont conservés sous forme de notes de portée explicites.
---
La classe Java actuelle `PdfContentEditorExamples` prend directement en charge `addMovieAnnotation(...)`.


## 
Ajouter une annotation de film


1. 
Liez le PDF source à la façade `PdfContentEditor`.

2. 
Appelez `createMovie(...)` avec le rectangle d'annotation, le chemin du fichier vidéo et le numéro de page.

3. 
Enregistrez le document PDF mis à jour.

```java
public static void addMovieAnnotation(Path inputFile, Path movieFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createMovie(new Rectangle(80, 500, 220, 120), movieFile.toString(), 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
