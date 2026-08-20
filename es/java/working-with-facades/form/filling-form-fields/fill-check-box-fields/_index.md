---
title: Llenar campos de casilla de verificación
linktitle: Llenar campos de casilla de verificación
type: docs
weight: 20
url: /java/fill-check-box-fields/
description: Aprenda a completar los campos de las casillas de verificación en un formulario PDF con Java usando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Establecer valores de campo de casilla de verificación en un formulario PDF con Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, establecer campos de casillas de verificación por nombre y guardar el documento actualizado con la fachada del formulario en Aspose.PDF para Java.
---
Utilice `FormExamples.fillCheckBoxFields(...)` para configurar los valores de las casillas de verificación en un formulario.

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
