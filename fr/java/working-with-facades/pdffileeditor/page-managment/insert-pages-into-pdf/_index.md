---
title: Insérer des pages dans un PDF
linktitle: Insérer des pages dans un PDF
type: docs
weight: 40
url: /java/insert-pages-into-pdf/
description: Insérez les pages sélectionnées d'un PDF dans un autre en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Insérer des pages d'un autre PDF à une position choisie avec Java
Abstract: Découvrez comment insérer des pages dans un PDF avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor pour insérer les pages sélectionnées d'un deuxième document après un numéro de page donné dans le PDF cible.
---
## Insérer des pages dans un PDF



L'exemple Java insère les pages 1 et 2 du document secondaire après la page 2 du PDF cible.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Choisissez le point d'insertion dans le document cible.
3. Sélectionnez les numéros de page à copier à partir du document source.

4. 
Appelez `insert` avec le fichier cible, le point d'insertion, le fichier source, le tableau de pages et le fichier de sortie.

5. 
Enregistrez le PDF mis à jour.


### 
Exemple Java

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
