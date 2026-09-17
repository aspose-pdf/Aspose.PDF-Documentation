---
title: Copier le champ externe
linktitle: Copier le champ externe
type: docs
weight: 80
url: /java/copy-outer-field/
description: Découvrez comment copier un champ de formulaire d'un document PDF vers un autre en Java à l'aide de la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Copier un champ de formulaire PDF entre des documents en Java
Abstract: Cet article montre comment créer un PDF de destination, le lier à la façade FormEditor, copier un champ d'un autre document et enregistrer le résultat à l'aide d'Aspose.PDF pour Java.
---
## Copier un champ d'un autre PDF


1. 
Créez un PDF de destination avec au moins une page.

2. 
Liez le PDF de destination à la façade `FormEditor`.

3. 
Appelez `copyOuterField(...)` avec le chemin du document source, le nom du champ, la page cible et les coordonnées.

4. 
Enregistrez le document de destination mis à jour.

```java
public static void copyOuterField(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();
        document.save(outputFile.toString());
    }

    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(outputFile.toString());
        editor.copyOuterField(inputFile.toString(), "First Name", 1, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
