---
title: Importer des données XML
linktitle: Importer des données XML
type: docs
weight: 40
url: /java/import-xml-data/
description: Découvrez comment importer des données de formulaire XML dans un formulaire PDF avec Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Importer des données AcroForm depuis XML en Java
Abstract: Cet article montre comment lier un formulaire PDF, importer des valeurs de champ à partir d'un flux XML et enregistrer le document mis à jour avec la façade de formulaire dans Aspose.PDF pour Java.
---
Utilisez `FormExamples.importXml(...)` pour remplir un formulaire à partir de données XML.

```java
public static void importXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
