---
title: Aplanar todos los campos
linktitle: Aplanar todos los campos
type: docs
weight: 10
url: /java/flatten-all-fields/
description: Aprenda a aplanar todos los campos de un formulario PDF en Java utilizando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Convierta todos los campos del formulario interactivo en contenido estático en Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, aplanar cada campo del formulario y guardar el documento actualizado con la fachada del formulario en Aspose.PDF para Java.
---
Utilice `FormExamples.flattenAllFields(...)` cuando necesite convertir todos los campos interactivos en contenido de página estática.

```java
public static void flattenAllFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.flattenAllFields();
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
