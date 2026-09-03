---
title: Eliminar elemento de lista
linktitle: Eliminar elemento de lista
type: docs
weight: 20
url: /es/java/del-list-item/
description: Aprenda cómo eliminar un elemento de un campo de lista en un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Eliminar un elemento de lista de un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, eliminar un elemento específico de un campo de lista y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF for Java.
---
## Eliminar un elemento de un campo de lista

1. Vincular el PDF de origen a `FormEditor` fachada.
2. Llamar `delListItem(...)` para el campo objetivo y el elemento a eliminar.
3. Guarde el documento actualizado.

```java
public static void deleteListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.delListItem("Country", "UK");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
