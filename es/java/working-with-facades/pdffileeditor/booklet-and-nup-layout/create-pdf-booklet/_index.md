---
title: Crear folleto PDF
linktitle: Crear folleto PDF
type: docs
weight: 20
url: /es/java/create-pdf-booklet/
description: Crear un PDF listo para folleto a partir de un documento existente en Java con la fachada PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Generar salida en formato de folleto a partir de un documento PDF en Java
Abstract: Aprenda cómo crear un folleto PDF con Aspose.PDF for Java. El ejemplo en Java usa PdfFileEditor para reordenar páginas para la impresión de folletos y también incluye una variante que devuelve un booleano para comprobar el éxito de manera sencilla.
---
## Crear un folleto PDF

Utilice `PdfFileEditor.makeBooklet` para reorganizar las páginas de un PDF existente en orden de folleto.

### Pasos

1. Cree una instancia de `PdfFileEditor`.
2. Llame `makeBooklet` con el PDF de origen y el archivo de salida.
3. Guarde el documento del folleto.
4. Si desea comprobar el estado de retorno, usa la variante que devuelve un booleano y maneje un resultado fallido.

### Ejemplo en Java

```java
public static void createPdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString());
}

public static void tryCreatePdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    if (!bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString())) {
        System.out.println("Failed to create booklet.");
    }
}
```
