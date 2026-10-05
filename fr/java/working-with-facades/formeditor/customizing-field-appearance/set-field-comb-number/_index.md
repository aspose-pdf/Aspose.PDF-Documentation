---
title: Définir le nombre de cases du champ
linktitle: Définir le nombre de cases du champ
type: docs
weight: 60
url: /java/set-field-comb-number/
description: Découvrez comment définir le nombre de cases pour un champ de formulaire PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-09-22"
TechArticle: true
AlternativeHeadline: Définir le nombre de cases pour un champ de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, définir le nombre de cases pour un champ et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF for Java.
---
## Définir le nombre de cases d’un champ

1. Liez le PDF source à la façade `FormEditor`.

2. Appelez `setFieldCombNumber(...)` pour le champ cible et le nombre de cases.

3. Enregistrez le document mis à jour.

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
