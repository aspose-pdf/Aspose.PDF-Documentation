---
title: Copiar campo exterior
linktitle: Copiar campo exterior
type: docs
weight: 80
url: /java/copy-outer-field/
description: Aprenda a copiar un campo de formulario de un documento PDF a otro en Java usando la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Copie un campo de formulario PDF entre documentos en Java
Abstract: Este artículo muestra cómo crear un PDF de destino, vincularlo a la fachada de FormEditor, copiar un campo de otro documento y guardar el resultado usando Aspose.PDF para Java.
---
## Copiar un campo de otro PDF


1. 
Cree un PDF de destino con al menos una página.

2. 
Vincule el PDF de destino a la fachada `FormEditor`.

3. 
Llame a `copyOuterField(...)` con la ruta del documento de origen, el nombre del campo, la página de destino y las coordenadas.

4. 
Guarde el documento de destino actualizado.

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
