---
title: Rellenar campos de botones de opción
linktitle: Rellenar campos de botones de opción
type: docs
weight: 30
url: /es/java/fill-radio-button-fields/
description: Aprenda cómo seleccionar un valor de botón de opción en un formulario PDF con Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Seleccionar una opción de campo de botón de opción en Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, seleccionar una opción de botón de opción por índice y guardar el documento actualizado con la fachada Form en Aspose.PDF for Java.
---
Usar `FormExamples.fillRadioButtonFields(...)` para seleccionar una opción de botón de radio.

```java
public static void fillRadioButtonFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("gender", 0);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
