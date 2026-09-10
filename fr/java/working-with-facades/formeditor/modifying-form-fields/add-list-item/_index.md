---
title: Ajouter un élément de liste
linktitle: Ajouter un élément de liste
type: docs
weight: 10
url: /java/add-list-item/
description: Découvrez comment ajouter des éléments à un champ de liste dans un document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Ajouter un élément de liste à un champ de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, ajouter un nouvel élément à un champ de liste et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Ajouter un élément à un champ de liste


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `addListItem(...)` pour le champ cible et la nouvelle paire affichage/valeur.

3. 
Enregistrez le document mis à jour.

```java
public static void addListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addListItem("Country", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
