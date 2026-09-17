---
title: Renommer le champ
linktitle: Renommer le champ
type: docs
weight: 50
url: /java/rename-field/
description: Découvrez comment renommer un champ de formulaire existant dans un document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Renommer un champ de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, renommer un champ spécifié et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Renommer un champ


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `renameField(...)` avec le nom du champ actuel et le nouveau nom du champ.

3. 
Enregistrez le document mis à jour.

```java
public static void renameField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.renameField("City", "Town");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
