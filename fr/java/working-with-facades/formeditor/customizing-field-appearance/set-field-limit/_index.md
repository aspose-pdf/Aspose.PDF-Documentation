---
title: Définir la limite du champ
linktitle: Définir la limite du champ
type: docs
weight: 50
url: /java/set-field-limit/
description: Découvrez comment définir une limite maximale de caractères pour un champ de formulaire PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Définir une limite de caractères pour un champ de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, définir la limite maximale de caractères d'un champ et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Définir une limite de caractères dans les champs


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `setFieldLimit(...)` pour le champ cible et le nombre maximum de caractères.

3. 
Enregistrez le document mis à jour.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldLimit("First Name", 15);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
