---
title: Preencha os campos do código de barras
linktitle: Preencha os campos do código de barras
type: docs
weight: 50
url: /java/fill-barcode-fields/
description: Aprenda como preencher um campo de formulário de código de barras em Java usando a fachada do formulário em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Preencher um campo de código de barras em um formulário PDF com Java
Abstract: Este artigo mostra como vincular um formulário PDF, definir um valor de campo de código de barras e salvar o documento atualizado com a fachada Form em Aspose.PDF para Java.
---
Use `FormExamples.fillBarcodeFields(...)` para preencher um campo de código de barras em um formulário PDF.

```java
public static void fillBarcodeFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillBarcodeField("product_barcode", "123456789012");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
