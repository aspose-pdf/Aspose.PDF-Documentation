---
title: Supprimer le champ
linktitle: Supprimer le champ
type: docs
weight: 40
url: /java/remove-field/
description: Découvrez comment supprimer un champ de formulaire existant d'un document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Supprimer un champ de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, supprimer un champ spécifié et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Supprimer un champ


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `removeField(...)` pour le nom du champ cible.

3. 
Enregistrez le document mis à jour.

```java
public static void removeField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeField("Country");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
