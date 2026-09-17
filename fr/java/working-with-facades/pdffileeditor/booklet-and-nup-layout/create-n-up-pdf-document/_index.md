---
title: Créer un document PDF N-Up
linktitle: Créer un document PDF N-Up
type: docs
weight: 10
url: /java/create-n-up-pdf-document/
description: Créez une mise en page PDF 2x2 N-Up en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Générer une mise en page PDF N-Up à partir d'un document existant en Java
Abstract: Découvrez comment créer un document PDF N-Up avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor pour placer quatre pages sources sur chaque feuille de sortie et affiche également une variante de retour booléen pour la vérification des échecs.
---
## Créer un document PDF N-Up



L'exemple Java utilise `PdfFileEditor.makeNUp` pour créer une mise en page 2x2 à partir d'un PDF existant.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Appelez `makeNUp` avec le fichier d'entrée, le fichier de sortie et le nombre de colonnes et de lignes.
3. Enregistrez le document généré.

4. 
Si vous souhaitez une vérification explicite du succès, appelez la variante boolean-return et gérez un résultat `false`.


### 
Exemple Java

```java
public static void createNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2);
}

public static void tryCreateNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    if (!nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2)) {
        System.out.println("Failed to create N-Up PDF document.");
    }
}
```
