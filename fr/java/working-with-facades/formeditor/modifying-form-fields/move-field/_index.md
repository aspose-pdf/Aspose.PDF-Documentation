---
title: Déplacer le champ
linktitle: Déplacer le champ
type: docs
weight: 30
url: /java/move-field/
description: Découvrez comment déplacer un champ de formulaire existant dans un document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Déplacer un champ de formulaire PDF vers une nouvelle position en Java
Abstract: Cet article montre comment lier un PDF existant, déplacer un champ vers de nouvelles coordonnées et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Déplacer un champ


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `moveField(...)` avec le nom du champ cible et les nouvelles coordonnées du rectangle.

3. 
Enregistrez le document mis à jour.

```java
public static void moveField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.moveField("Country", 200, 600, 280, 620);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
