---
title: Obtenir des informations sur la page
linktitle: Obtenir des informations sur la page
type: docs
weight: 10
url: /java/get-page-info/
description: Découvrez comment inspecter la largeur, la hauteur et la rotation d'une page en Java avec la façade PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenir des informations sur une page PDF à l'aide d'Aspose.PDF pour Java
Abstract: Découvrez comment récupérer des informations de page avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileInfo pour lire la largeur, la hauteur et la rotation de la page 1 afin que vous puissiez inspecter sa mise en page avant de poursuivre le traitement.
---
## Obtenir des informations sur la page



Cet exemple lit les principales propriétés géométriques de la page 1.


### 
Étapes


1. 
Créez un objet `PdfFileInfo` pour le PDF source.

2. 
Appelez `getPageWidth`, `getPageHeight` et `getPageRotation` pour la page que vous souhaitez inspecter.
3. Utilisez ou imprimez les valeurs renvoyées.

4. 
Fermez l'instance `PdfFileInfo`.


### 
Exemple Java

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```
