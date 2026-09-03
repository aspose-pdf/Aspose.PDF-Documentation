---
title: Rellenar campos de casilla de verificación
linktitle: Rellenar campos de casilla de verificación
type: docs
weight: 20
url: /es/java/fill-check-box-fields/
description: Aprenda cómo rellenar campos de casilla de verificación en un formulario PDF con Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Establecer valores de campos de casilla de verificación en un formulario PDF con Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, establecer campos de casilla de verificación por nombre y guardar el documento actualizado con la fachada Form en Aspose.PDF for Java.
---
Usar `FormExamples.fillCheckBoxFields(...)` para establecer valores de casilla de verificación en un formulario.

```java
public static void fillCheckBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("subscribe_newsletter", "Yes");
        form.fillField("accept_terms", "Yes");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
