---
title: Exporter vers XFDF
linktitle: Exporter vers XFDF
type: docs
weight: 20
url: /java/export-to-xfdf/
description: Découvrez comment exporter les données des champs d'un formulaire PDF vers XFDF en Java à l'aide de la façade de formulaire dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Exporter des données AcroForm vers XFDF en Java
Abstract: Cet article montre comment lier un formulaire PDF et exporter ses valeurs de champ vers un flux XFDF avec la façade de formulaire dans Aspose.PDF pour Java.
---
Utilisez `FormExamples.exportXfdf(...)` pour écrire les données des champs de formulaire au format XFDF.

```java
public static void exportXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(outputStream);
    } finally {
        form.close();
    }
}
```
