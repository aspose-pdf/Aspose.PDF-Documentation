---
title: Supprimer un élément de liste
linktitle: Supprimer un élément de liste
type: docs
weight: 20
url: /java/del-list-item/
description: Découvrez comment supprimer un élément d'un champ de liste dans un document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Supprimer un élément de liste d'un champ de formulaire PDF en Java
Abstract: Cet article montre comment lier un PDF existant, supprimer un élément spécifique d'un champ de liste et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Supprimer un élément d'un champ de liste


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `delListItem(...)` pour le champ cible et l'élément à supprimer.

3. 
Enregistrez le document mis à jour.

```java
public static void deleteListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.delListItem("Country", "UK");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
