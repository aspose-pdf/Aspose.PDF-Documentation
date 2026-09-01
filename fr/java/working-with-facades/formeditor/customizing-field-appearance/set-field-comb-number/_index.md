---
title: Définir le numéro du peigne de champ
linktitle: Définir le numéro du peigne de champ
type: docs
weight: 60
url: /java/set-field-comb-number/
description: Découvrez comment définir un numéro de peigne pour un champ de formulaire PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Définir un numéro de peigne pour un champ de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, définir un numéro de peigne pour un champ et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Définir un numéro de peigne de champ


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `setFieldCombNumber(...)` pour le champ cible et la valeur du peigne.

3. 
Enregistrez le document mis à jour.

```java
public static void setFieldCombNumber(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldCombNumber("textCombField", 5);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
