---
title: Importar datos XML
linktitle: Importar datos XML
type: docs
weight: 40
url: /es/java/import-xml-data/
description: Aprenda cómo importar datos de formulario XML a un formulario PDF con Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Importar datos AcroForm desde XML en Java
Abstract: Este artículo muestra cómo enlazar un formulario PDF, importar valores de campo desde una secuencia XML y guardar el documento actualizado con la fachada Form en Aspose.PDF for Java.
---
Usar `FormExamples.importXml(...)` para rellenar un formulario a partir de datos XML.

```java
public static void importXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
