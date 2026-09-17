---
title: Diviser le PDF jusqu'à la fin
linktitle: Diviser le PDF jusqu'à la fin
type: docs
weight: 40
url: /java/split-pdf-to-end/
description: Divisez un PDF d'une page choisie jusqu'à la fin en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire des pages du point de départ à la fin d'un PDF avec Java
Abstract: Apprenez à diviser un PDF jusqu'à la fin avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor pour extraire toutes les pages à partir de la page 2 jusqu'à la fin du document source.
---
## Diviser le PDF pour terminer



L'exemple Java extrait toutes les pages à partir de la page 2.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Appelez `splitToEnd` avec le fichier source, le numéro de la page de démarrage et le fichier de sortie.
3. Enregistrez le document PDF résultant.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
