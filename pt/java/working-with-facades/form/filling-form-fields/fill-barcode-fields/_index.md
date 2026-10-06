---
title: Preencher Campos de Código de Barras
linktitle: Preencher Campos de Código de Barras
type: docs
weight: 50
url: /pt/java/fill-barcode-fields/
description: Aprenda como preencher um campo de formulário de código de barras em Java usando a fachada Form no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Preencha um campo de código de barras em um formulário PDF com Java
Abstract: Este artigo mostra como vincular um formulário PDF, definir o valor de um campo de código de barras e salvar o documento atualizado com a fachada Form no Aspose.PDF for Java.
---
Usar `FormExamples.fillBarcodeFields(...)` para preencher um campo de código de barras em um formulário PDF.

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
