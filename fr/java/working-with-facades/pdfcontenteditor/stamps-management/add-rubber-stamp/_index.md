---
title: Ajouter un tampon en caoutchouc
linktitle: Ajouter un tampon en caoutchouc
type: docs
weight: 10
url: /java/add-rubber-stamp/
description: Découvrez comment ajouter une annotation de tampon à un document PDF en Java à l'aide de la façade PdfContentEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Ajouter un tampon en caoutchouc à un PDF en Java
Abstract: Cet article montre comment lier un PDF, créer une annotation de tampon avec le texte et la couleur de l'étiquette, et enregistrer le document mis à jour à l'aide de la façade PdfContentEditor dans Aspose.PDF pour Java.
---
## Ajouter un tampon en caoutchouc


1. 
Liez le PDF source à la façade `PdfContentEditor`.

2. 
Appelez `createRubberStamp(...)` avec le numéro de page, le rectangle, le titre, le contenu et la couleur.

3. 
Enregistrez le document PDF mis à jour.

```java
public static void addRubberStamp(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createRubberStamp(1, new Rectangle(120, 450, 180, 60), "Approved", "Approved by reviewer", Color.GREEN);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
