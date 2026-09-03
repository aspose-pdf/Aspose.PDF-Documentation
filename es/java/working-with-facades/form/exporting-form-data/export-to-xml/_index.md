---
title: Exportar a XML
linktitle: Exportar a XML
type: docs
weight: 40
url: /es/java/export-to-xml/
description: Aprenda cómo exportar datos de formularios PDF a XML en Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Exportar datos de AcroForm a XML en Java
Abstract: Este artículo muestra cómo vincular un formulario PDF y exportar sus valores de campo a una secuencia XML con la fachada Form en Aspose.PDF for Java.
---
Usar `FormExamples.exportXml(...)` para guardar los datos del campo de formulario como XML.

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
