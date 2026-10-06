---
title: 签名完整性检查
linktitle: 签名完整性检查
type: docs
weight: 70
url: /zh/java/signature-integrity-checks/
description: 了解如何使用 PdfFileSignature 门面在 Java 中验证签名覆盖范围和完整性。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中验证 PDF 签名的覆盖范围和完整性
Abstract: 了解如何使用 Aspose.PDF for Java 检查签名完整性。当前的 Java 示例集使用 `verifySignature` 来验证选定的签名，并使用 `coversWholeDocument` 来确定签名是否保护了整个 PDF。
---
## 检查签名完整性

本文映射到相同的验证工作流，由 `PdfFileSignatureExamples.java`.

### 步骤

1. 将已签名的 PDF 与 `PdfFileSignature`.
2. 从文档中选择签名名称。
3. 调用 `verifySignature` 验证签名内容。
4. 调用 `coversWholeDocument` 确认整个文档的覆盖。
5. 关闭外观对象。

### Java 示例

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: " + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: " + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
