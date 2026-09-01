---
title: Importer des données XFDF
linktitle: Importer des données XFDF
type: docs
weight: 20
url: /java/import-xfdf-data/
description: Découvrez comment importer des données de formulaire XFDF dans un formulaire PDF avec Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Importer des données AcroForm depuis XFDF en Java
Abstract: Cet article montre comment lier un formulaire PDF, importer des valeurs de champ à partir d'un flux XFDF et enregistrer le document mis à jour avec la façade de formulaire dans Aspose.PDF pour Java.
---
Utilisez `FormExamples.importXfdf(...)` pour remplir un formulaire à partir de données XFDF.

```java
public static void importXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
