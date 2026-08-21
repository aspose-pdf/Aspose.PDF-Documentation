---
title: Ajouter des sauts de page dans un PDF
linktitle: Ajouter des sauts de page dans un PDF
type: docs
weight: 20
url: /java/add-page-breaks-in-pdf/
description: Insérez des sauts de page dans un PDF en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insérer des sauts de page à des positions fixes dans un document PDF avec Java
Abstract: Découvrez comment ajouter des sauts de page avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor.PageBreak pour diviser une page à une position verticale spécifique et enregistrer le résultat sous forme de nouveau PDF.
---
## Ajouter des sauts de page dans un PDF



Utilisez ce flux de travail lorsqu'une page doit être divisée en plusieurs pages à une position Y connue.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Créez une ou plusieurs entrées `PdfFileEditor.PageBreak` avec le numéro de page et la position de rupture.
3. Transmettez le tableau de saut de page à `addPageBreak`.

4. 
Enregistrez le document PDF mis à jour.


### 
Exemple Java

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```
