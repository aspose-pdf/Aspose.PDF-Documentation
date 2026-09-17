---
title: Créer un champ TextBox
linktitle: Créer un champ TextBox
type: docs
weight: 10
url: /java/create-textbox-field/
description: Découvrez comment ajouter des champs de zone de texte à un document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Créer des champs de formulaire de texte dans un PDF avec Java
Abstract: Cet article montre comment lier un PDF existant, ajouter des champs de texte avec des valeurs par défaut et enregistrer le document modifié à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
Utilisez `FormEditorExamples.createTextBoxField(...)` pour ajouter des champs de texte à un formulaire PDF.


## 
Créer des champs de zone de texte


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Ajoutez chaque champ de texte avec `FieldType.Text`, le nom du champ, la valeur par défaut, le numéro de page et le rectangle.

3. 
Enregistrez le document mis à jour.

```java
public static void createTextBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.Text, "first_name", "Alexander", 1, 50, 570, 150, 590);
        editor.addField(FieldType.Text, "last_name", "Smith", 1, 235, 570, 330, 590);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
