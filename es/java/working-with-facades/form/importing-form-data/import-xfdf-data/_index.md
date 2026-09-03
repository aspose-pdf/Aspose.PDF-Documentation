---
title: Importar datos XFDF
linktitle: Importar datos XFDF
type: docs
weight: 20
url: /es/java/import-xfdf-data/
description: Aprenda cómo importar datos de formulario XFDF a un formulario PDF con Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Importar datos AcroForm desde XFDF en Java
Abstract: Este artículo muestra cómo enlazar un formulario PDF, importar valores de campos desde un flujo XFDF y guardar el documento actualizado con la fachada Form en Aspose.PDF for Java.
---
Usar `FormExamples.importXfdf(...)` para rellenar un formulario a partir de datos XFDF.

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
