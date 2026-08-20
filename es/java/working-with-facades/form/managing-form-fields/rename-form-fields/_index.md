---
title: Cambiar el nombre de los campos del formulario
linktitle: Cambiar el nombre de los campos del formulario
type: docs
weight: 30
url: /java/rename-form-fields/
description: Aprenda a cambiar el nombre de los campos de un formulario PDF en Java utilizando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Cambiar el nombre de los campos de formulario en un documento PDF con Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, cambiar el nombre de los campos existentes y guardar el documento actualizado con la fachada del formulario en Aspose.PDF para Java.
---
Utilice `FormExamples.renameFormFields(...)` para cambiar el nombre de los campos en un formulario PDF interactivo.

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
