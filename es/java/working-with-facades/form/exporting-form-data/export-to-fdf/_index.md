---
title: Exportar a FDF
linktitle: Exportar a FDF
type: docs
weight: 10
url: /java/export-to-fdf/
description: Aprenda a exportar valores de campos de formulario PDF a FDF en Java utilizando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Exportar datos de AcroForm a FDF en Java
Abstract: Este artículo muestra cómo vincular un formulario PDF y exportar sus datos de campo a una secuencia FDF con la fachada del formulario en Aspose.PDF para Java.
---
Utilice `FormExamples.exportFdf(...)` cuando necesite serializar datos de campo de AcroForm como FDF.

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
