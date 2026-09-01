---
title: Copier le champ intérieur
linktitle: Copier le champ intérieur
type: docs
weight: 70
url: /java/copy-inner-field/
description: Découvrez comment copier un champ de formulaire vers un nouvel emplacement dans le même document PDF en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Copiez un champ de formulaire PDF dans le même document en Java
Abstract: Cet article montre comment lier un PDF existant, dupliquer un champ sur une autre page et à un autre emplacement, et enregistrer le document mis à jour à l'aide de la façade FormEditor dans Aspose.PDF pour Java.
---
## Copiez un champ dans le même PDF


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Appelez `copyInnerField(...)` avec le nom du champ source, le nouveau nom du champ, la page et les coordonnées.

3. 
Enregistrez le document mis à jour.

```java
public static void copyInnerField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.copyInnerField("First Name", "First Name Copy", 2, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
