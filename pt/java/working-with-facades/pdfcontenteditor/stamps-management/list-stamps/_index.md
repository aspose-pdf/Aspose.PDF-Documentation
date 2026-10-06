---
title: Listar carimbos
linktitle: Listar carimbos
type: docs
weight: 20
url: /pt/java/list-stamps/
description: Aprenda como listar carimbos de borracha em uma página em Java usando a fachada PdfContentEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Listar carimbos de borracha PDF em Java
Abstract: Este artigo mostra como vincular um PDF, recuperar os carimbos em uma página e inspecionar a coleção resultante usando a fachada PdfContentEditor no Aspose.PDF for Java.
---
## Listar carimbos em uma página

1. Vincule o PDF de origem ao `PdfContentEditor` fachada.
2. Chamar `getStamps(pageNumber)` para recuperar os carimbos na página de destino.
3. Inspecione o resultado `StampInfo[]` coleção.

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
