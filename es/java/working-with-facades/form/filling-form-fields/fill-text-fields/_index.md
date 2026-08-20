---
title: Llenar campos de texto
linktitle: Llenar campos de texto
type: docs
weight: 10
url: /java/fill-text-fields/
description: Aprenda a completar campos de texto en un formulario PDF con Java usando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Complete los campos de formulario de texto en un PDF con Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, establecer valores de campo de texto por nombre y guardar el documento actualizado con la fachada del formulario en Aspose.PDF para Java.
---
Utilice `FormExamples.fillTextFields(...)` para completar campos de formulario basados ​​en texto.

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
