---
title: 签名管理
linktitle: 签名管理
type: docs
weight: 80
url: /zh/java/signature-management/
description: 了解如何在 Java 中使用 PdfFileSignature 类删除现有的 PDF 签名。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中删除 PDF 签名
Abstract: 了解如何使用 Aspose.PDF for Java 从已签名的 PDF 中删除签名。当前的 Java 示例集涵盖按名称删除现有签名并保存更新后的文档，但未提供单独的示例来清理相关的签名字段。
---
## 删除签名

当需要从文档中删除现有数字签名时，请使用此工作流。

### 步骤

1. 创建 `PdfFileSignature` 实例并绑定已签名的 PDF。
2. 读取签名集合并选择签名名称。
3. 调用 `removeSignature` 使用该名称。
4. 保存已更新的文件并关闭 facade 对象。

### Java 示例

```java
public static void removeSignature(Path inputFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        pdfSignature.removeSignature(signatureName);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

当前的 Java 示例集未包含在删除签名后移除相关签名字段的单独方法。
