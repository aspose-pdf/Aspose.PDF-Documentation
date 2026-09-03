---
title: Listar sellos
linktitle: Listar sellos
type: docs
weight: 20
url: /es/java/list-stamps/
description: Aprenda cómo listar sellos de caucho en una página en Java usando la fachada PdfContentEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Listar sellos de caucho PDF en Java
Abstract: Este artículo muestra cómo vincular un PDF, recuperar los sellos en una página y examinar la colección resultante usando la fachada PdfContentEditor en Aspose.PDF para Java.
---
## Listar sellos en una página

1. Vincular el PDF de origen al `PdfContentEditor` fachada.
2. Llamar `getStamps(pageNumber)` para recuperar los sellos en la página objetivo.
3. Inspecciona lo resultante `StampInfo[]` colección.

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
