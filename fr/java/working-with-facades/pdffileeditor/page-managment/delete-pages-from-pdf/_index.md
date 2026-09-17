---
title: Supprimer des pages d'un PDF
linktitle: Supprimer des pages d'un PDF
type: docs
weight: 20
url: /java/delete-pages-from-pdf/
description: Supprimez les pages sélectionnées d'un PDF en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer des pages spécifiques d'un document PDF avec Java
Abstract: Découvrez comment supprimer des pages d'un PDF avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor pour supprimer un ensemble défini de numéros de page et enregistrer les pages restantes en tant que nouveau document.
---
## Supprimer des pages d'un PDF



L'exemple Java supprime les pages 2 et 4 du document source.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Construisez un tableau avec les numéros de page à supprimer.
3. Appelez `delete` avec le fichier d'entrée, le tableau de pages et le fichier de sortie.

4. 
Enregistrez le PDF résultant.


### 
Exemple Java

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
