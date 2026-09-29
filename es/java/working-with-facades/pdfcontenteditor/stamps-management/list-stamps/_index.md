---
title: Listar sellos
linktitle: Listar sellos
type: docs
weight: 20
url: /es/java/list-stamps/
description: Aprenda cómo listar sellos de caucho en una página en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Listar sellos de caucho PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, recuperar los sellos en una página y examinar la colección resultante usando la fachada PdfContentEditor en Aspose.PDF for Java.
---
## Listar sellos en una página

1. Vincule el PDF de origen a la fachada `PdfContentEditor`.
2. Llame `getStamps(pageNumber)` para recuperar los sellos en la página de destino.
3. Inspeccione la colección `StampInfo[]` devuelta.

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
