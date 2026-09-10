---
title: Remplir les champs du code-barres
linktitle: Remplir les champs du code-barres
type: docs
weight: 50
url: /java/fill-barcode-fields/
description: Découvrez comment remplir un champ de formulaire de code-barres en Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Remplir un champ de code-barres dans un formulaire PDF avec Java
Abstract: Cet article montre comment lier un formulaire PDF, définir une valeur de champ de code-barres et enregistrer le document mis à jour avec la façade de formulaire dans Aspose.PDF pour Java.
---
Utilisez `FormExamples.fillBarcodeFields(...)` pour remplir un champ de code-barres dans un formulaire PDF.

```java
public static void fillBarcodeFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillBarcodeField("product_barcode", "123456789012");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
