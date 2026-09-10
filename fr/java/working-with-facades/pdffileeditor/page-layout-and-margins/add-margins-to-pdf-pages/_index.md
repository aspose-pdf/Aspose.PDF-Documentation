---
title: Ajouter des marges aux pages PDF
linktitle: Ajouter des marges aux pages PDF
type: docs
weight: 10
url: /java/add-margins-to-pdf-pages/
description: Ajoutez des marges aux pages PDF sélectionnées en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des marges à des pages spécifiques dans un document PDF avec Java
Abstract: Découvrez comment ajouter des marges aux pages sélectionnées avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor pour cibler des numéros de page individuels et appliquer des valeurs de marge égales en haut, en bas, à gauche et à droite.
---
## Ajouter des marges aux pages PDF



L'exemple Java ajoute des marges de 36 points aux pages 1 et 3 du document source.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Sélectionnez les numéros de page qui doivent recevoir de nouvelles marges.
3. Appelez `addMargins` avec le fichier d'entrée, le fichier de sortie, la liste de pages et les valeurs de marge.

4. 
Enregistrez le PDF mis à jour.


### 
Exemple Java

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
