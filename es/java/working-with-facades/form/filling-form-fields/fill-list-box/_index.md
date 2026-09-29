---
title: Rellenar cuadro de lista
linktitle: Rellenar cuadro de lista
type: docs
weight: 40
url: /es/java/fill-list-box/
description: Aprenda cómo rellenar un campo de cuadro de lista en un formulario PDF con Java usando la fachada Form en Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Establezca un valor de campo de cuadro de lista en un formulario PDF con Java
Abstract: Este artículo muestra cómo enlazar un formulario PDF, establecer un valor de campo de cuadro de lista y guardar el documento actualizado con la fachada Form en Aspose.PDF for Java.
---
Utilice `FormExamples.fillListBoxFields(...)` para rellenar un campo de lista desplegable.

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
