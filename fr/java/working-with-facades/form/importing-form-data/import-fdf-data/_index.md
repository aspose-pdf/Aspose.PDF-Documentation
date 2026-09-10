---
title: Importer des données FDF
linktitle: Importer des données FDF
type: docs
weight: 10
url: /java/import-fdf-data/
description: Découvrez comment importer des données de formulaire FDF dans un formulaire PDF avec Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Importer des données AcroForm depuis FDF en Java
Abstract: Cet article montre comment lier un formulaire PDF, importer des valeurs de champ à partir d'un flux FDF et enregistrer le document mis à jour avec la façade de formulaire dans Aspose.PDF pour Java.
---
Utilisez `FormExamples.importFdf(...)` pour appliquer les valeurs de champ d'un fichier FDF.

```java
public static void importFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
