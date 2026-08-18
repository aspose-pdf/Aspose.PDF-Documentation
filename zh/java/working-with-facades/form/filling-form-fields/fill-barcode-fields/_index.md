---
title: 填写条形码字段
linktitle: 填写条形码字段
type: docs
weight: 50
url: /java/fill-barcode-fields/
description: 了解如何使用 Aspose.PDF 中的表单外观在 Java 中填写条形码表单字段。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 填充 PDF 表单中的条形码字段
Abstract: 本文介绍如何在 Aspose.PDF for Java 中绑定 PDF 表单、设置条形码字段值以及使用表单外观保存更新的文档。
---
使用 `FormExamples.fillBarcodeFields(...)` 填充 PDF 表单中的条形码字段。

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
