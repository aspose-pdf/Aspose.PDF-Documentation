---
title: Renombrar campos de Form
linktitle: Renombrar campos de Form
type: docs
weight: 30
url: /es/java/rename-form-fields/
description: Aprenda cómo renombrar campos de formulario PDF en Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Renombrar campos de Form en un documento PDF con Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, renombrar campos existentes y guardar el documento actualizado con la fachada Form en Aspose.PDF for Java.
---
Utilice `FormExamples.renameFormFields(...)` renombrar campos en un formulario PDF interactivo.

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
