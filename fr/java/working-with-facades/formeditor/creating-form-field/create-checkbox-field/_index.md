---
title: Créer un champ CheckBox
linktitle: Créer un champ CheckBox
type: docs
weight: 20
url: /java/create-checkbox-field/
description: Découvrez comment ajouter un champ de formulaire de case à cocher à un document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Créer un champ de case à cocher dans un PDF avec Java
Abstract: Cet article montre comment lier un PDF existant, ajouter un champ de case à cocher à une position spécifiée et enregistrer le document modifié à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
Utilisez `FormEditorExamples.createCheckBoxField(...)` pour ajouter un champ de case à cocher à un formulaire PDF.


## 
Créer un champ de case à cocher


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Ajoutez le champ de case à cocher avec `FieldType.CheckBox`, le nom du champ, la légende, la page et le rectangle.

3. 
Enregistrez le document mis à jour.

```java
public static void createCheckBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.CheckBox, "checkbox1", "Check Box 1", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
