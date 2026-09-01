---
title: Fractionner un PDF depuis le début
linktitle: Fractionner un PDF depuis le début
type: docs
weight: 10
url: /java/split-pdf-from-beginning/
description: Divisez un PDF depuis le début en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrayez les premières pages d'un PDF dans un nouveau document avec Java
Abstract: Apprenez à diviser un PDF depuis le début avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor pour prendre les trois premières pages d'un document et les enregistrer dans un PDF distinct.
---
## Diviser le PDF depuis le début



L'exemple Java extrait les trois premières pages du document source.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Appelez `splitFromFirst` avec le fichier source, le nombre de pages à conserver et le fichier de sortie.
3. Enregistrez le nouveau document PDF.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
