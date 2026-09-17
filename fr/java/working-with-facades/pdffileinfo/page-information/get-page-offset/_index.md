---
title: Obtenir le décalage de page
linktitle: Obtenir le décalage de page
type: docs
weight: 20
url: /java/get-page-offset/
description: Découvrez comment inspecter les décalages des pages X et Y en Java avec la façade PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenir des décalages de page PDF à l'aide de Java
Abstract: Découvrez comment récupérer les décalages de page avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileInfo pour lire les décalages X et Y de la page 1 et convertit les valeurs de points en pouces pour faciliter l'analyse de la mise en page.
---
## Obtenir le décalage de page



Utilisez ce flux de travail lorsque vous avez besoin de comprendre comment le contenu de la page est positionné par rapport à l'origine du PDF.


### 
Étapes


1. 
Créez un objet `PdfFileInfo` pour le PDF d'entrée.

2. 
Appelez `getPageXOffset` et `getPageYOffset` pour la page cible.
3. Convertissez les valeurs de points en pouces en divisant par `72.0`.

4. 
Utilisez ou imprimez les valeurs converties.

5. 
Fermez l'instance `PdfFileInfo`.


### 
Exemple Java

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
