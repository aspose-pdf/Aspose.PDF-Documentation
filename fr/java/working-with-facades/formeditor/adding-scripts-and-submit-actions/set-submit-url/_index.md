---
title: Définir l'URL de soumission
linktitle: Définir l'URL de soumission
type: docs
weight: 30
url: /java/set-submit-url/
description: Découvrez comment définir une URL de soumission pour un bouton de formulaire PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Configurer une URL de soumission de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, définir une URL de soumission et un indicateur de soumission pour un champ de bouton, et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Définir une URL de soumission


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `setSubmitUrl(...)` pour le champ du bouton.

3. 
Appliquez l'indicateur de soumission pour le format de soumission.

4. 
Enregistrez le document mis à jour.

```java
public static void setSubmitUrl(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
        editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
