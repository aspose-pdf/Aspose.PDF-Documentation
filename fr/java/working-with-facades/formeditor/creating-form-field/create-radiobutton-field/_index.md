---
title: Créer un champ RadioButton
linktitle: Créer un champ RadioButton
type: docs
weight: 50
url: /java/create-radiobutton-field/
description: Découvrez comment ajouter un champ de bouton radio à un document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Créer un champ de bouton radio dans un PDF avec Java
Abstract: Cet article montre comment lier un PDF existant, configurer les paramètres de disposition des boutons radio, créer un champ de bouton radio et enregistrer le document modifié à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
Utilisez `FormEditorExamples.createRadioButtonField(...)` pour créer un champ de bouton radio avec des options prédéfinies.


## 
Créer un champ de bouton radio


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Configurez l'espacement des boutons radio, l'orientation et la taille de l'élément.

3. 
Définissez les éléments des boutons radio.
4. Ajoutez le champ du bouton radio avec sa sélection et son rectangle par défaut.

5. 
Enregistrez le document mis à jour.

```java
public static void createRadioButtonField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setRadioGap(4);
        editor.setRadioHoriz(false);
        editor.setRadioButtonItemSize(20);
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.Radio, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
