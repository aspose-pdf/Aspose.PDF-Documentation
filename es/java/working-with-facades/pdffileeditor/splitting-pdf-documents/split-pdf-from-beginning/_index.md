---
title: Dividir PDF desde el principio
linktitle: Dividir PDF desde el principio
type: docs
weight: 10
url: /es/java/split-pdf-from-beginning/
description: Dividir un PDF desde el principio en Java con la fachada PdfFileEditor.
lastmod: "2026-09-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer las primeras páginas de un PDF en un documento nuevo con Java.
Abstract: Aprenda cómo dividir un PDF desde el principio con Aspose.PDF for Java. El ejemplo en Java utiliza PdfFileEditor para tomar las primeras tres páginas de un documento y guardarlas como un PDF separado.
---
## Dividir PDF desde el principio

El ejemplo en Java extrae las primeras tres páginas del documento fuente.

### Pasos

1. Crear un `PdfFileEditor` instancia.
2. Llamar `splitFromFirst` con el archivo de origen, número de páginas a conservar y archivo de salida.
3. Guarde el nuevo documento PDF.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
