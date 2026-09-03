---
title: Copiar campo externo
linktitle: Copiar campo externo
type: docs
weight: 80
url: /es/java/copy-outer-field/
description: Aprenda cómo copiar un campo de formulario de un documento PDF a otro en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Copiar un campo de formulario PDF entre documentos en Java
Abstract: Este artículo muestra cómo crear un PDF de destino, enlazarlo con la fachada FormEditor, copiar un campo de otro documento y guardar el resultado usando Aspose.PDF for Java.
---
## Copiar un campo de otro PDF

1. Cree un PDF de destino con al menos una página.
2. Vincular el PDF de destino a `FormEditor` fachada.
3. Llamar `copyOuterField(...)` con la ruta del documento fuente, el nombre del campo, la página de destino y las coordenadas.
4. Guarda el documento de destino actualizado.

```java
public static void copyOuterField(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();
        document.save(outputFile.toString());
    }

    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(outputFile.toString());
        editor.copyOuterField(inputFile.toString(), "First Name", 1, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
