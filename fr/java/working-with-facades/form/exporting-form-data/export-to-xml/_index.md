---
title: Exporter vers XML
linktitle: Exporter vers XML
type: docs
weight: 40
url: /java/export-to-xml/
description: Découvrez comment exporter des données de formulaire PDF vers XML en Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Exporter des données AcroForm vers XML en Java
Abstract: Cet article montre comment lier un formulaire PDF et exporter ses valeurs de champ vers un flux XML avec la façade de formulaire dans Aspose.PDF pour Java.
---
Utilisez `FormExamples.exportXml(...)` pour enregistrer les données des champs de formulaire au format XML.

```java
public static void exportXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(outputStream);
    } finally {
        form.close();
    }
}
```
