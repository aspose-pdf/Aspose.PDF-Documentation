---
title: Llenar cuadro de lista
linktitle: Llenar cuadro de lista
type: docs
weight: 40
url: /java/fill-list-box/
description: Aprenda a completar un campo de cuadro de lista en un formulario PDF con Java usando la fachada del formulario en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Establecer un valor de campo de cuadro de lista en un formulario PDF con Java
Abstract: Este artículo muestra cómo vincular un formulario PDF, establecer un valor de campo de cuadro de lista y guardar el documento actualizado con la fachada del formulario en Aspose.PDF para Java.
---
Utilice `FormExamples.fillListBoxFields(...)` para completar un campo de cuadro de lista.

```java
public static void fillListBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("favorite_colors", "Red");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
