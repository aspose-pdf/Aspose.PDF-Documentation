---
title: Rellenar campos de texto
linktitle: Rellenar campos de texto
type: docs
weight: 10
url: /es/java/fill-text-fields/
description: Aprenda cómo rellenar campos de texto en un formulario PDF con Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Rellenar campos de formulario de texto en un PDF con Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, establecer valores de campos de texto por nombre y guardar el documento actualizado con la fachada Form en Aspose.PDF for Java.
---
Usar `FormExamples.fillTextFields(...)` para poblar campos de formulario basados en texto.

```java
public static void fillTextFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("name", "John Doe");
        form.fillField("address", "123 Main St, Anytown, USA");
        form.fillField("email", "john.doe@example.com");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
