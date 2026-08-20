---
title: Importar datos FDF
linktitle: Importar datos FDF
type: docs
weight: 10
url: /java/import-fdf-data/
description: Aprenda a importar datos de formularios FDF a un formulario PDF con Java utilizando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Importar datos de AcroForm desde FDF en Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, importar valores de campo desde una secuencia FDF y guardar el documento actualizado con la fachada del formulario en Aspose.PDF para Java.
---
Utilice `FormExamples.importFdf(...)` para aplicar valores de campo de un archivo FDF.

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
