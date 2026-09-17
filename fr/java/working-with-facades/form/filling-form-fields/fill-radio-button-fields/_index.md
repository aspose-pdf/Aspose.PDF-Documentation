---
title: Remplir les champs des boutons radio
linktitle: Remplir les champs des boutons radio
type: docs
weight: 30
url: /java/fill-radio-button-fields/
description: Découvrez comment sélectionner une valeur de bouton radio dans un formulaire PDF avec Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Sélectionnez une option de champ de bouton radio en Java
Abstract: This article shows how to bind a PDF form, select a radio button option by index, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Utilisez `FormExamples.fillRadioButtonFields(...)` pour sélectionner une option de bouton radio.

```java
public static void fillRadioButtonFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("gender", 0);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
