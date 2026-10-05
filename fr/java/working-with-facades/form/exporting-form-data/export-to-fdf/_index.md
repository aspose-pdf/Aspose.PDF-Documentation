---
title: Exporter vers FDF
linktitle: Exporter vers FDF
type: docs
weight: 10
url: /java/export-to-fdf/
description: Découvrez comment exporter les valeurs des champs de formulaire PDF vers FDF en Java à l'aide de la façade Form dans Aspose.PDF.
lastmod: "2026-09-22"
TechArticle: true
AlternativeHeadline: Exporter des données AcroForm vers FDF en Java
Abstract: Cet article montre comment lier un formulaire PDF et exporter ses données de champ vers un flux FDF avec la façade Form dans Aspose.PDF for Java.
---
Utilisez `FormExamples.exportFdf(...)` lorsque vous devez sérialiser les données de champ AcroForm au format FDF.

```java
public static void exportFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(outputStream);
    } finally {
        form.close();
    }
}
```
