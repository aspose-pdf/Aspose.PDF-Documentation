---
title: Exportar a XFDF
linktitle: Exportar a XFDF
type: docs
weight: 20
url: /es/java/export-to-xfdf/
description: Aprenda cómo exportar los datos de los campos de formulario PDF a XFDF en Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Exportar datos de AcroForm a XFDF en Java
Abstract: Este artículo muestra cómo vincular un formulario PDF y exportar sus valores de campo a un flujo XFDF con la fachada Form en Aspose.PDF for Java.
---
Usar `FormExamples.exportXfdf(...)` escribir datos de campos de formulario como XFDF.

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
