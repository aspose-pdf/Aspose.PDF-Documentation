---
title: De una sola línea a varias
linktitle: De una sola línea a varias
type: docs
weight: 60
url: /es/java/single-to-multiple/
description: Aprenda cómo convertir un campo de texto de una sola línea en un campo de varias líneas en un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Convierta un campo PDF de una sola línea a varias líneas en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, convertir un campo de una sola línea en un campo de varias líneas y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF for Java.
---
## Convierta un campo de una sola línea a múltiples líneas

1. Vincular el PDF de origen al `FormEditor` fachada.
2. Llamar `single2Multiple(...)` para el nombre del campo objetivo.
3. Guarda el documento actualizado.

```java
public static void singleToMultiple(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.single2Multiple("City");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
