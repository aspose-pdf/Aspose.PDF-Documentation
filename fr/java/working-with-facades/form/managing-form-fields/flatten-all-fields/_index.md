---
title: Aplatir tous les champs
linktitle: Aplatir tous les champs
type: docs
weight: 10
url: /java/flatten-all-fields/
description: Découvrez comment aplatir tous les champs de formulaire PDF en Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Convertir tous les champs de formulaire interactifs en contenu statique en Java
Abstract: Cet article montre comment lier un formulaire PDF, aplatir chaque champ du formulaire et enregistrer le document mis à jour avec la façade de formulaire dans Aspose.PDF pour Java.
---
Utilisez `FormExamples.flattenAllFields(...)` lorsque vous devez convertir tous les champs interactifs en contenu de page statique.

```java
public static void flattenAllFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.flattenAllFields();
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
