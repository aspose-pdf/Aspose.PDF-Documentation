---
title: Remplir les champs de texte
linktitle: Remplir les champs de texte
type: docs
weight: 10
url: /java/fill-text-fields/
description: Découvrez comment remplir les champs de texte d'un formulaire PDF avec Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Remplir les champs de formulaire de texte dans un PDF avec Java
Abstract: Cet article montre comment lier un formulaire PDF, définir les valeurs des champs de texte par nom et enregistrer le document mis à jour avec la façade de formulaire dans Aspose.PDF pour Java.
---
Utilisez `FormExamples.fillTextFields(...)` pour remplir les champs de formulaire textuels.

```java
public static void fillTextFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("name", "John Doe");
        form.fillField("address", "123 Main St, Anytown, USA");
        form.fillField("email", "john.doe@example.com");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
