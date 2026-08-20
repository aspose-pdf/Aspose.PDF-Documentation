---
title: Único a múltiple
linktitle: Único a múltiple
type: docs
weight: 60
url: /java/single-to-multiple/
description: Aprenda cómo convertir un campo de texto de una sola línea en un campo de varias líneas en un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Convierta un campo PDF de una sola línea a varias líneas en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, convertir un campo de una sola línea en un campo de varias líneas y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Convertir un campo de una sola línea en varias líneas


1. 
Vincule el PDF de origen a la fachada `FormEditor`.

2. 
Llame a `single2Multiple(...)` para obtener el nombre del campo de destino.

3. 
Guarde el documento actualizado.

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
