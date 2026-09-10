---
title: Concaténer plusieurs fichiers PDF
linktitle: Concaténer plusieurs fichiers PDF
type: docs
weight: 20
url: /java/concatenate-pdf-files/
description: Fusionnez des fichiers PDF en Java avec le flux de travail de concaténation PdfFileEditor basé sur un tableau.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fusionner plusieurs fichiers PDF en un seul document avec Java
Abstract: Découvrez comment concaténer des fichiers PDF avec Aspose.PDF pour Java. L'exemple de référentiel utilise la surcharge `concatenate` basée sur un tableau avec deux entrées, et le même flux de travail peut être étendu à des listes de fichiers plus longues car la méthode accepte un tableau de chaînes de chemins source.
---
## Concaténer des fichiers PDF



L'exemple Java fusionne deux fichiers en les transmettant à la surcharge `concatenate` basée sur un tableau.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Créez un tableau de chaînes avec les chemins PDF d’entrée.
3. Appelez `concatenate` avec le tableau d'entrée et le chemin du fichier de sortie.

4. 
Enregistrez le document fusionné.


```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```


Pour fusionner plus de deux fichiers, étendez le tableau de chaînes transmis à `concatenate`.
