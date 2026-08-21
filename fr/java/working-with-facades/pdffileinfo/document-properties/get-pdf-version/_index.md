---
title: Obtenir la version PDF
linktitle: Obtenir la version PDF
type: docs
weight: 20
url: /java/get-pdf-version/
description: Découvrez comment récupérer la version d'un document PDF en Java avec la façade PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Récupérer la version PDF à l'aide d'Aspose.PDF pour Java
Abstract: Découvrez comment récupérer la version PDF avec Aspose.PDF pour Java. L'exemple Java crée un objet PdfFileInfo, lit la chaîne de version avec `getPdfVersion()`, imprime le résultat et ferme l'objet d'informations sur le fichier.
---
## Obtenir la version PDF



Utilisez ce flux de travail lorsque vous devez vérifier la compatibilité des fichiers ou acheminer un document via une logique de traitement spécifique à la version.


### 
Étapes


1. 
Créez un objet `PdfFileInfo` pour le fichier PDF.

2. 
Appelez `getPdfVersion()` pour récupérer la version signalée.
3. Utilisez ou imprimez la valeur de la version.

4. 
Fermez l'instance `PdfFileInfo`.


### 
Exemple Java

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
