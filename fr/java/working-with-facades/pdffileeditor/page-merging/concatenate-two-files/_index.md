---
title: Concaténer deux fichiers PDF
linktitle: Concaténer deux fichiers PDF
type: docs
weight: 60
url: /java/concatenate-two-files/
description: Fusionnez deux fichiers PDF en un seul document en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Concaténer deux fichiers PDF en un seul document de sortie avec Java
Abstract: Découvrez comment concaténer deux fichiers PDF avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor et la surcharge `concatenate` basée sur un tableau pour combiner deux documents sources en un seul PDF de sortie.
---
## Concaténer deux fichiers PDF



Cet article correspond directement à l'exemple `mergePdfDocuments` dans `PdfFileEditorExamples.java`.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Transmettez les deux chemins de fichiers d’entrée sous forme de tableau de chaînes.
3. Appelez `concatenate` avec le tableau et le chemin du fichier de sortie.

4. 
Enregistrez le PDF fusionné.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
