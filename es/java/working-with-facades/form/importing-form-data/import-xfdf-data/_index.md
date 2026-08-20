---
title: Importar datos XFDF
linktitle: Importar datos XFDF
type: docs
weight: 20
url: /java/import-xfdf-data/
description: Aprenda a importar datos de formularios XFDF a un formulario PDF con Java utilizando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Importar datos de AcroForm desde XFDF en Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, importar valores de campo desde una secuencia XFDF y guardar el documento actualizado con la fachada del formulario en Aspose.PDF para Java.
---
Utilice `FormExamples.importXfdf(...)` para completar un formulario a partir de datos XFDF.

```java
public static void importXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
