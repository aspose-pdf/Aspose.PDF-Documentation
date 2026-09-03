---
title: Crear folleto PDF
linktitle: Crear folleto PDF
type: docs
weight: 20
url: /java/create-pdf-booklet/
description: Cree un PDF listo para folletos a partir de un documento existente en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Generar salida de folleto a partir de un documento PDF en Java
Abstract: Aprenda a crear un folleto en PDF con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor para reordenar las páginas para la impresión de folletos y también incluye una variante de retorno booleano para una comprobación sencilla del éxito.
---
## Crear un folleto en PDF



Utilice `PdfFileEditor.makeBooklet` para reorganizar las páginas de un PDF existente en orden de folleto.


### 
Pasos


1. Cree una instancia `PdfFileEditor`.

2. Llame a `makeBooklet` con el PDF de origen y el archivo de salida.
3. Guarde el documento del folleto.

4. Si desea comprobar el estado de la devolución, utilice la variante de devolución booleana y maneje un resultado fallido.


### 
Ejemplo de Java

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
