---
title: Remplir les champs des cases à cocher
linktitle: Remplir les champs des cases à cocher
type: docs
weight: 20
url: /java/fill-check-box-fields/
description: Découvrez comment remplir les champs des cases à cocher dans un formulaire PDF avec Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Définir les valeurs des champs de case à cocher dans un formulaire PDF avec Java
Abstract: Cet article montre comment lier un formulaire PDF, définir les champs de case à cocher par nom et enregistrer le document mis à jour avec la façade de formulaire dans Aspose.PDF pour Java.
---
Utilisez `FormExamples.fillCheckBoxFields(...)` pour définir les valeurs des cases à cocher dans un formulaire.

```java
public static void fillCheckBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("subscribe_newsletter", "Yes");
        form.fillField("accept_terms", "Yes");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
