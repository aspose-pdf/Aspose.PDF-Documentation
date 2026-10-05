---
title: Dividir PDF desde el principio
linktitle: Dividir PDF desde el principio
type: docs
weight: 10
url: /es/java/split-pdf-from-beginning/
description: Divida un PDF desde el principio en Java con la fachada PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga las primeras páginas de un PDF en un nuevo documento con Java
Abstract: Aprenda cómo dividir un PDF desde el principio con Aspose.PDF for Java. El ejemplo en Java utiliza PdfFileEditor para tomar las primeras tres páginas de un documento y guardarlas como un PDF separado.
---
## Dividir PDF desde el principio

El ejemplo en Java extrae las primeras tres páginas del documento fuente.

### Pasos

1. Cree una instancia de `PdfFileEditor`.
2. Llame a `splitFromFirst` con el archivo fuente, número de páginas a conservar y archivo de salida.
3. Guarde el nuevo documento PDF.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
