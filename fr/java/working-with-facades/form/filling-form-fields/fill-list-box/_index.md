---
title: Remplir la zone de liste
linktitle: Remplir la zone de liste
type: docs
weight: 40
url: /java/fill-list-box/
description: Découvrez comment remplir un champ de zone de liste dans un formulaire PDF avec Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Définir une valeur de champ de zone de liste dans un formulaire PDF avec Java
Abstract: This article shows how to bind a PDF form, set a list box field value, and save the updated document with the Form facade in Aspose.PDF for Java.
---
Utilisez `FormExamples.fillListBoxFields(...)` pour remplir un champ de zone de liste.

```java
public static void fillListBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("favorite_colors", "Red");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
