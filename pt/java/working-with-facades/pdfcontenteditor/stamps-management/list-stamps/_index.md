---
title: Listar selos
linktitle: Listar selos
type: docs
weight: 20
url: /java/list-stamps/
description: Aprenda como listar carimbos em uma página em Java usando a fachada PdfContentEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Listar carimbos de borracha PDF em Java
Abstract: Este artigo mostra como vincular um PDF, recuperar os carimbos em uma página e inspecionar a coleção resultante usando a fachada PdfContentEditor em Aspose.PDF para Java.
---
## Listar carimbos em uma página

1. Vincule o PDF de origem à fachada `PdfContentEditor`.
2. Chame `getStamps(pageNumber)` para recuperar os carimbos na página de destino.
3. Inspecione a coleção `StampInfo[]` resultante.

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
