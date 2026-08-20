---
title: Importar datos XML
linktitle: Importar datos XML
type: docs
weight: 40
url: /java/import-xml-data/
description: Aprenda a importar datos de formularios XML a un formulario PDF con Java utilizando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Importar datos de AcroForm desde XML en Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, importar valores de campo desde una secuencia XML y guardar el documento actualizado con la fachada del formulario en Aspose.PDF para Java.
---
Utilice `FormExamples.importXml(...)` para completar un formulario a partir de datos XML.

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
