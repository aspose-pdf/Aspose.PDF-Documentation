---
title: Ajouter des pages au PDF
linktitle: Ajouter des pages au PDF
type: docs
weight: 10
url: /java/append-pages-to-pdf/
description: Ajoutez des pages d'un PDF à un autre en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter une plage de pages d'un document PDF à un autre avec Java
Abstract: Découvrez comment ajouter des pages à un PDF avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor pour ajouter une plage de pages sélectionnée d'un autre document à la fin du PDF actuel.
---
## Ajouter des pages à un PDF



L'exemple Java ajoute la page 1 d'un deuxième PDF à la fin du premier document.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Liez le PDF d'entrée principal en transmettant son chemin à `append`.
3. Fournissez la liste des fichiers sources secondaires et la plage de pages à ajouter.

4. 
Enregistrez le résultat fusionné dans le fichier de sortie.


### 
Exemple Java

```java
public static void appendPagesToPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.append(inputFile.toString(), new String[] {sampleFile.toString()}, 1, 1, outputFile.toString());
}
```
