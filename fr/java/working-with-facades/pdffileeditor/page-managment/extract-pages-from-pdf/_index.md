---
title: Extraire des pages d'un PDF
linktitle: Extraire des pages d'un PDF
type: docs
weight: 30
url: /java/extract-pages-from-pdf/
description: Extrayez les pages sélectionnées d'un PDF en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire les pages PDF sélectionnées dans un nouveau document avec Java
Abstract: Découvrez comment extraire des pages d'un PDF avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor pour collecter des numéros de page spécifiques et les écrire dans un PDF de sortie distinct.
---
## Extraire des pages d'un PDF



L'exemple Java extrait les pages 1, 4 et 3 dans un nouveau document PDF.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Définissez les numéros de page à extraire.
3. Appelez `extract` avec le fichier source, le tableau de pages et le fichier de sortie.

4. 
Enregistrez les pages extraites en tant que nouveau PDF.


### 
Exemple Java

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
