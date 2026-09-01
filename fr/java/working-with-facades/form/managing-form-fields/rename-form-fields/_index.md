---
title: Renommer les champs du formulaire
linktitle: Renommer les champs du formulaire
type: docs
weight: 30
url: /java/rename-form-fields/
description: Découvrez comment renommer les champs d'un formulaire PDF en Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Renommer les champs de formulaire dans un document PDF avec Java
Abstract: Cet article montre comment lier un formulaire PDF, renommer les champs existants et enregistrer le document mis à jour avec la façade de formulaire dans Aspose.PDF pour Java.
---
Utilisez `FormExamples.renameFormFields(...)` pour renommer les champs d'un formulaire PDF interactif.

```java
public static void renameFormFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.renameField("First Name", "NewFirstName");
        form.renameField("Last Name", "NewLastName");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
