---
title: Renombrar campos de formulario
linktitle: Renombrar campos de formulario
type: docs
weight: 30
url: /es/java/rename-form-fields/
description: Aprenda cómo renombrar campos de formulario PDF en Java utilizando la fachada Form en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Renombrar campos de formulario en un documento PDF con Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, renombrar los campos existentes y guardar el documento actualizado con la fachada Form en Aspose.PDF for Java.
---
Usar `FormExamples.renameFormFields(...)` para renombrar campos en un formulario PDF interactivo.

```java
public static void renameFormFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.renameField("First Name", "NewFirstName");
        form.renameField("Last Name", "NewLastName");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
