---
title: Opérations sur les images
linktitle: Opérations sur les images
type: docs
weight: 50
url: /java/pdfcontenteditor-image-operations/
description: Découvrez la couverture actuelle des opérations d’image Java disponible dans la façade PdfContentEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Workflows d'édition d'images en Java avec PdfContentEditor
Abstract: Cette section couvre les flux de travail liés aux images actuellement pris en charge par l'ensemble d'exemples Java PdfContentEditor. Le référentiel comprend un exemple direct de remplacement d'une image, tandis que les sujets de suppression d'image non pris en charge sont conservés sous forme de notes de portée explicites.
---
La classe Java actuelle `PdfContentEditorExamples` prend directement en charge `replaceImage(...)`.


## 
Remplacer une image


1. 
Liez le PDF source à la façade `PdfContentEditor`.

2. 
Appelez `replaceImage(...)` avec le numéro de page, l'index de l'image et le chemin de l'image de remplacement.

3. 
Enregistrez le document PDF mis à jour.

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.replaceImage(1, 1, imageFile.toString());
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
