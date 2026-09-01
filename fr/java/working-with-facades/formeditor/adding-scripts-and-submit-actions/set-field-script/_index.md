---
title: Définir le script de champ
linktitle: Définir le script de champ
type: docs
weight: 20
url: /java/set-field-script/
description: Découvrez comment attribuer ou mettre à jour une action JavaScript sur un champ de formulaire PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Définir une action JavaScript sur un champ de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, ajouter un script initial, le remplacer par un script mis à jour et enregistrer le document modifié à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Définir un script de champ


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Ajoutez une action JavaScript initiale au champ.

3. 
Remplacez-le par le texte du script mis à jour.

4. 
Enregistrez le document mis à jour.

```java
public static void setFieldScript(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addFieldScript("Script_Demo_Button", "app.alert('Script 1 has been executed');");
        editor.setFieldScript("Script_Demo_Button", "app.alert('Script 2 has been executed');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
