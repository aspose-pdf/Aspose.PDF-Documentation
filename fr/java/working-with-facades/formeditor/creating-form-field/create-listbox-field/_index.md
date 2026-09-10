---
title: Créer un champ ListBox
linktitle: Créer un champ ListBox
type: docs
weight: 40
url: /java/create-listbox-field/
description: Découvrez comment ajouter un champ de zone de liste à un document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Créer un champ de zone de liste dans un PDF avec Java
Abstract: Cet article montre comment lier un PDF existant, définir des éléments de liste, ajouter un champ de zone de liste et enregistrer le document modifié à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
Utilisez `FormEditorExamples.createListBoxField(...)` pour créer une zone de liste avec des éléments prédéfinis.


## 
Créer un champ de zone de liste


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Définissez les éléments de liste disponibles avec `setItems(...)`.

3. 
Ajoutez le champ de la zone de liste avec sa valeur par défaut et son rectangle.
4. Enregistrez le document mis à jour.

```java
public static void createListBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.ListBox, "listbox1", "Australia", 1, 230, 398, 350, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
