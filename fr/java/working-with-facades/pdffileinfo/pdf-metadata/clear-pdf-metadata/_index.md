---
title: Effacer les métadonnées PDF
linktitle: Effacer les métadonnées PDF
type: docs
weight: 10
url: /java/clear-pdf-metadata/
description: Découvrez comment effacer les métadonnées PDF en Java avec la façade PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Effacement des métadonnées PDF à l'aide d'Aspose.PDF pour Java
Abstract: Découvrez comment effacer les métadonnées PDF avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileInfo pour supprimer les informations stockées sur le document avec `clearInfo()`, puis enregistre le PDF nettoyé dans un nouveau fichier.
---
## Effacer les métadonnées du PDF



Utilisez ce flux de travail lorsque vous devez supprimer les informations stockées sur un document avant de partager ou d'archiver un PDF.


### 
Étapes


1. 
Créez un objet `PdfFileInfo` pour le PDF d'entrée.

2. 
Appelez `clearInfo()` pour supprimer les métadonnées du document.
3. Enregistrez le résultat dans un nouveau fichier avec `save()`.

4. 
Fermez l'instance `PdfFileInfo`.


### 
Exemple Java

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
