---
title: Eliminar elemento de la lista
linktitle: Eliminar elemento de la lista
type: docs
weight: 20
url: /java/del-list-item/
description: Aprenda cómo eliminar un elemento de un campo de lista en un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Eliminar un elemento de lista de un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, eliminar un elemento específico de un campo de lista y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF para Java.
---
## Eliminar un elemento de un campo de lista


1. 
Vincule el PDF de origen a la fachada `FormEditor`.

2. 
Llame a `delListItem(...)` para obtener el campo de destino y el elemento que desea eliminar.

3. 
Guarde el documento actualizado.

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
