---
title: Définir l'alignement du champ vertical
linktitle: Définir l'alignement du champ vertical
type: docs
weight: 30
url: /java/set-field-alignment-vertical/
description: Découvrez comment définir l'alignement vertical d'un champ de formulaire PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Définir l'alignement vertical d'un champ de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, définir l'alignement vertical des champs et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Définir l'alignement vertical du champ


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `setFieldAlignmentV(...)` pour le champ cible et la constante d'alignement vertical souhaitée.

3. 
Enregistrez le document mis à jour.

```java
public static void setFieldAlignmentVertical(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignmentV("First Name", FormFieldFacade.ALIGN_BOTTOM);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
