---
title: Redimensionner le contenu de la page PDF
linktitle: Redimensionner le contenu de la page PDF
type: docs
weight: 30
url: /java/resize-pdf-page-contents/
description: Redimensionnez le contenu des pages PDF sélectionnées en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redimensionner le contenu d'une page existante dans un document PDF avec Java
Abstract: Découvrez comment redimensionner le contenu d'une page avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor pour cibler des pages spécifiques, appliquer une nouvelle largeur et hauteur de contenu et arrêter le flux de travail si l'opération de redimensionnement échoue.
---
## Redimensionner le contenu de la page PDF



L'exemple Java redimensionne la zone de contenu des pages 1 et 3 et vérifie la valeur de retour booléenne.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Choisissez les pages dont le contenu doit être redimensionné.
3. Appelez `resizeContents` avec la largeur et la hauteur cibles.

4. 
Vérifiez la valeur de retour et gérez les échecs avant de continuer.

5. 
Enregistrez le document mis à jour.


### 
Exemple Java

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```
