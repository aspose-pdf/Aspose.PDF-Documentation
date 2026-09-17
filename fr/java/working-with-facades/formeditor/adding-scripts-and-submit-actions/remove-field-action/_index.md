---
title: Supprimer l'action sur le terrain
linktitle: Supprimer l'action sur le terrain
type: docs
weight: 50
url: /java/remove-field-action/
description: Découvrez comment supprimer une action de champ d'un champ de formulaire PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Supprimer une action de champ de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, supprimer l'action associée à un champ spécifique et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Supprimer une action sur le terrain


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `removeFieldAction(...)` pour le champ cible.

3. 
Enregistrez le document mis à jour.

```java
public static void removeFieldAction(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeFieldAction("Script_Demo_Button");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
