---
title: Cambiar el tamaño del contenido de la página PDF
linktitle: Cambiar el tamaño del contenido de la página PDF
type: docs
weight: 30
url: /java/resize-pdf-page-contents/
description: Cambie el tamaño del contenido en páginas PDF seleccionadas en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cambiar el tamaño del contenido de la página existente en un documento PDF con Java
Abstract: Aprenda a cambiar el tamaño del contenido de la página con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor para apuntar a páginas específicas, aplicar un nuevo ancho y alto de contenido y detener el flujo de trabajo si falla la operación de cambio de tamaño.
---
## Cambiar el tamaño del contenido de la página PDF



El ejemplo de Java cambia el tamaño del área de contenido en las páginas 1 y 3 y comprueba el valor de retorno booleano.


### 
Pasos


1. 
Cree una instancia `PdfFileEditor`.

2. 
Elija las páginas cuyo contenido debe cambiarse de tamaño.
3. Llame a `resizeContents` con el ancho y alto del objetivo.

4. 
Verifique el valor de retorno y solucione el error antes de continuar.

5. 
Guarde el documento actualizado.


### 
Ejemplo de Java

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```
