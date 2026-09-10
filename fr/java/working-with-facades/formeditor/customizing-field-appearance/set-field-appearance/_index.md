---
title: Définir l'apparence du champ
linktitle: Définir l'apparence du champ
type: docs
weight: 40
url: /java/set-field-appearance/
description: Découvrez comment modifier les indicateurs d'apparence visuelle d'un champ de formulaire PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Modifier les indicateurs d'apparence des champs de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, appliquer un indicateur d'apparence à un champ et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Définir des indicateurs d'apparence de champ


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `setFieldAppearance(...)` pour le champ cible et l'indicateur d'annotation choisi.

3. 
Enregistrez le document mis à jour.

```java
public static void setFieldAppearance(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAppearance("First Name", AnnotationFlags.Hidden);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
