---
title: 填充条形码字段
linktitle: 填充条形码字段
type: docs
weight: 50
url: /zh/java/fill-barcode-fields/
description: 学习如何在 Java 中使用 Aspose.PDF 的 Form 门面填充条形码表单字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 表单中填充条形码字段
Abstract: 本文展示了如何绑定 PDF 表单、设置条形码字段值，并使用 Aspose.PDF for Java 中的 Form 门面保存更新后的文档。
---
使用 `FormExamples.fillBarcodeFields(...)` 在 PDF 表单中填充条形码字段。

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
