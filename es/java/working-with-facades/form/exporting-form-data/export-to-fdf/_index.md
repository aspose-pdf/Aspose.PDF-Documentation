---
title: Exportar a FDF
linktitle: Exportar a FDF
type: docs
weight: 10
url: /es/java/export-to-fdf/
description: Aprenda cómo exportar los valores de los campos de formulario PDF a FDF en Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Exportar datos de AcroForm a FDF en Java
Abstract: Este artículo muestra cómo vincular un formulario PDF y exportar sus datos de campo a un flujo FDF con la fachada Form en Aspose.PDF for Java.
---
Usar `FormExamples.exportFdf(...)` cuando necesites serializar los datos de campo AcroForm como FDF.

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
