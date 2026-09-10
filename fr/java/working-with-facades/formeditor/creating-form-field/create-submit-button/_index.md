---
title: Créer un bouton Soumettre
linktitle: Créer un bouton Soumettre
type: docs
weight: 60
url: /java/create-submit-button/
description: Découvrez comment ajouter un bouton de soumission à un document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Créer un bouton de soumission PDF en Java
Abstract: Cet article montre comment lier un PDF existant, ajouter un champ de bouton d'envoi avec une URL cible et enregistrer le document modifié à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
Utilisez `FormEditorExamples.createSubmitButton(...)` pour créer un bouton qui soumet les données du formulaire.


## 
Créer un bouton de soumission


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `addSubmitBtn(...)` avec le nom du bouton, la page, l'étiquette, l'URL cible et le rectangle.

3. 
Enregistrez le document mis à jour.

```java
public static void createSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
