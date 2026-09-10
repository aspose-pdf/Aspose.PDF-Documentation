---
title: Créer un livret PDF
linktitle: Créer un livret PDF
type: docs
weight: 20
url: /java/create-pdf-booklet/
description: Créez un PDF prêt pour un livret à partir d'un document existant en Java avec la façade PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Générer une sortie de livret à partir d'un document PDF en Java
Abstract: Découvrez comment créer un livret PDF avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileEditor pour réorganiser les pages pour l'impression de livrets et inclut également une variante de retour booléen pour une vérification simple du succès.
---
## Créer un livret PDF



Utilisez `PdfFileEditor.makeBooklet` pour réorganiser les pages d'un PDF existant dans l'ordre des livrets.


### 
Étapes


1. 
Créez une instance `PdfFileEditor`.

2. 
Appelez `makeBooklet` avec le PDF source et le fichier de sortie.
3. Enregistrez le document livret.

4. 
Si vous souhaitez vérifier l'état du retour, utilisez la variante boolean-return et gérez un résultat échoué.


### 
Exemple Java

```java
public static void createPdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString());
}

public static void tryCreatePdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    if (!bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString())) {
        System.out.println("Failed to create booklet.");
    }
}
```
