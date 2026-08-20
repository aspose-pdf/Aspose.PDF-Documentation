---
title: Exportar a XFDF
linktitle: Exportar a XFDF
type: docs
weight: 20
url: /java/export-to-xfdf/
description: Aprenda a exportar datos de campos de formulario PDF a XFDF en Java utilizando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Exportar datos de AcroForm a XFDF en Java
Abstract: Este artículo muestra cómo vincular un formulario PDF y exportar sus valores de campo a una secuencia XFDF con la fachada del formulario en Aspose.PDF para Java.
---
Utilice `FormExamples.exportXfdf(...)` para escribir datos de campo de formulario como XFDF.

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
