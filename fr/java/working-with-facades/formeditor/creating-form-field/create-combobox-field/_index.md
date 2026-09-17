---
title: Créer un champ ComboBox
linktitle: Créer un champ ComboBox
type: docs
weight: 30
url: /java/create-combobox-field/
description: Découvrez comment ajouter un champ de zone de liste déroulante à un document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Créer un champ de zone de liste déroulante dans un PDF avec Java
Abstract: Cet article montre comment lier un PDF existant, ajouter un champ de zone de liste déroulante, le remplir avec des éléments et enregistrer le document modifié à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
Utilisez `FormEditorExamples.createComboBoxField(...)` pour créer une zone de liste déroulante et ajouter des éléments sélectionnables.


## 
Créer un champ de zone de liste déroulante


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Ajoutez le champ de la zone de liste déroulante avec sa valeur par défaut et son rectangle cible.

3. 
Ajoutez les éléments de la zone de liste déroulante sélectionnables.
4. Enregistrez le document mis à jour.

```java
public static void createComboBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.ComboBox, "combobox1", "Australia", 1, 230, 498, 350, 514);
        editor.addListItem("combobox1", new String[] {"Australia", "Australia"});
        editor.addListItem("combobox1", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
