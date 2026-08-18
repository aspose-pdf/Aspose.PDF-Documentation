---
title: 签名管理
linktitle: 签名管理
type: docs
weight: 80
url: /java/signature-management/
description: 了解如何使用 PdfFileSignature 外观在 Java 中删除现有的 PDF 签名。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在Java中删除PDF签名
Abstract: 了解如何使用 Aspose.PDF for Java 从已签名的 PDF 中删除签名。当前的 Java 示例集涵盖按名称删除现有签名并保存更新的文档。它不包括用于清理关联签名字段的单独示例。
---
## 删除签名

当应从文档中删除现有数字签名时，请使用此工作流程。

### 步骤

1. 创建`PdfFileSignature`实例并绑定签名的PDF。
2. 阅读签名集并选择签名名称。
3. 使用该名称调用 `removeSignature`。
4. 保存更新的文件并关闭外观对象。

### Java示例

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

当前的 Java 示例集不包含在删除签名后删除关联签名字段的单独方法。
