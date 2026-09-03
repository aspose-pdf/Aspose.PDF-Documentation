---
title: Importar datos FDF
linktitle: Importar datos FDF
type: docs
weight: 10
url: /es/java/import-fdf-data/
description: Aprenda cómo importar datos de formulario FDF a un formulario PDF con Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Importar datos AcroForm desde FDF en Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, importar valores de campo desde un flujo FDF y guardar el documento actualizado con la fachada Form en Aspose.PDF for Java.
---
Usar `FormExamples.importFdf(...)` para aplicar valores de campos desde un archivo FDF.

```java
public static void importFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
