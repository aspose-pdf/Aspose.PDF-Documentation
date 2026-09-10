---
title: Diviser le PDF en pages uniques
linktitle: Diviser le PDF en pages uniques
type: docs
weight: 30
url: /java/split-pdf-into-single-pages/
description: Divisez un PDF en fichiers de sortie d'une seule page en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exportez chaque page d'un PDF vers son propre fichier avec Java
Abstract: Découvrez comment diviser un PDF en fichiers d'une seule page avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor pour écrire chaque page dans un PDF de sortie individuel basé sur un modèle de nom de fichier.
---
## Diviser le PDF en pages uniques



Utilisez ce flux de travail lorsque chaque page source doit devenir son propre fichier PDF.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Préparez un modèle de fichier de sortie qui inclut un espace réservé de page tel que `%NUM%`.
3. Appelez `splitToPages` avec le fichier source et le modèle de sortie.

4. 
Enregistrez les fichiers d'une seule page générés.

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
