---
title: Champs de boutons et images
linktitle: Champs de boutons et images
type: docs
weight: 40
url: /java/button-fields-and-images/
description: Découvrez comment ajouter une apparence d'image à un champ de bouton dans un formulaire PDF à l'aide de la façade de formulaire dans Aspose.PDF pour Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Ajouter une apparence d'image à un champ de bouton PDF en Java
Abstract: Cet article montre comment utiliser la façade de formulaire dans Aspose.PDF pour Java pour lier un formulaire PDF, charger une image sous forme de flux, remplir un champ de bouton d'image et enregistrer le document mis à jour.
---
L'exemple Java dans `FormExamples.addImageAppearanceToButtonField(...)` montre comment mettre à jour l'apparence d'un champ de bouton avec un flux d'images.



Le flux de travail est simple :


- 
lier le PDF d'entrée avec `form.bindPdf(...)`

- 
ouvrez le fichier image avec `Files.newInputStream(...)`

- 
appelez `form.fillImageField(...)` pour le champ du bouton
- enregistrer le PDF mis à jour

```java
public static void addImageAppearanceToButtonField(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        form.bindPdf(inputFile.toString());
        form.fillImageField("Image1_af_image", imageStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
