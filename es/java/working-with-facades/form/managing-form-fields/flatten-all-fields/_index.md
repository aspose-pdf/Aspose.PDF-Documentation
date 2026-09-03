---
title: Aplanar todos los campos
linktitle: Aplanar todos los campos
type: docs
weight: 10
url: /es/java/flatten-all-fields/
description: Aprenda cómo aplanar todos los campos de formulario PDF en Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Convierta todos los campos de formulario interactivos a contenido estático en Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, aplanar cada campo de formulario y guardar el documento actualizado con la fachada Form en Aspose.PDF for Java.
---
Usar `FormExamples.flattenAllFields(...)` cuando necesites convertir todos los campos interactivos en contenido estático de página.

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
