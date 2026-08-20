---
title: Dividir PDF desde el principio
linktitle: Dividir PDF desde el principio
type: docs
weight: 10
url: /java/split-pdf-from-beginning/
description: Divida un PDF desde el principio en Java con la fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrae las primeras páginas de un PDF en un nuevo documento con Java
Abstract: Aprenda a dividir un PDF desde el principio con Aspose.PDF para Java. El ejemplo de Java utiliza PdfFileEditor para tomar las tres primeras páginas de un documento y guardarlas como un PDF independiente.
---
## Dividir PDF desde el principio



El ejemplo de Java extrae las primeras tres páginas del documento fuente.


### 
Pasos


1. 
Cree una instancia `PdfFileEditor`.

2. 
Llame a `splitFromFirst` con el archivo fuente, el número de páginas a conservar y el archivo de salida.
3. Guarde el nuevo documento PDF.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
