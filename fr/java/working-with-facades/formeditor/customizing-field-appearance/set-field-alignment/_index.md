---
title: Définir l'alignement des champs
linktitle: Définir l'alignement des champs
type: docs
weight: 20
url: /java/set-field-alignment/
description: Découvrez comment définir l'alignement horizontal du texte pour un champ de formulaire PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Définir l'alignement des champs du formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, définir l'alignement horizontal des champs et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Définir l'alignement horizontal du champ


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `setFieldAlignment(...)` pour le champ cible et la constante d'alignement souhaitée.

3. 
Enregistrez le document mis à jour.

```java
public static void setFieldAlignment(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignment("First Name", FormFieldFacade.ALIGN_CENTER);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
