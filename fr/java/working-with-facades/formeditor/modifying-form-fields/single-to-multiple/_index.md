---
title: Convertir un champ monoligne en champ multiligne
linktitle: Convertir un champ monoligne en champ multiligne
type: docs
weight: 60
url: /java/single-to-multiple/
description: Découvrez comment convertir un champ de texte sur une seule ligne en un champ multiligne dans un document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-09-22"
TechArticle: true
AlternativeHeadline: Convertir un champ PDF sur une seule ligne en multiligne en Java
Abstract: Cet article montre comment lier un PDF existant, convertir un champ sur une seule ligne en champ multiligne et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF for Java.
---
## Convertir un champ monoligne en champ multiligne

1. Liez le PDF source à la façade `FormEditor`.

2. Appelez `single2Multiple(...)` pour le nom du champ cible.

3. Enregistrez le document mis à jour.

```java
public static void singleToMultiple(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.single2Multiple("City");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
