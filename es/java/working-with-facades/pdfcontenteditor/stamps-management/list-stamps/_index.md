---
title: Lista de sellos
linktitle: Lista de sellos
type: docs
weight: 20
url: /java/list-stamps/
description: Aprenda a enumerar sellos de goma en una página en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Listar sellos de goma PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, recuperar los sellos en una página e inspeccionar la colección resultante usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Listar sellos en una página


1. 
Vincule el PDF de origen a la fachada `PdfContentEditor`.

2. 
Llame a `getStamps(pageNumber)` para recuperar los sellos en la página de destino.

3. 
Inspeccione la colección `StampInfo[]` resultante.

```java
public static void listStamps(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        StampInfo[] stamps = editor.getStamps(1);
        System.out.println("Stamps on page 1: " + stamps.length);
    } finally {
        editor.close();
    }
}
```
