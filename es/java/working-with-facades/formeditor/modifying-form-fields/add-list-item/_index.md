---
title: Agregar elemento de lista
linktitle: Agregar elemento de lista
type: docs
weight: 10
url: /es/java/add-list-item/
description: Aprenda cómo agregar elementos a un campo de lista en un documento PDF en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Agregar un elemento de lista a un campo de formulario PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF existente, agregar un nuevo elemento a un campo de lista y guardar el documento actualizado usando la fachada FormEditor en Aspose.PDF for Java.
---
## Agregar un elemento a un campo de lista

1. Vincula el PDF de origen al `FormEditor` fachada.
2. Llamar `addListItem(...)` para el campo objetivo y el nuevo par de visualización/valor.
3. Guarde el documento actualizado.

```java
public static void addListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addListItem("Country", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
