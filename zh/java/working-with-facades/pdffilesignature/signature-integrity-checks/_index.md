---
title: 签名完整性检查
linktitle: 签名完整性检查
type: docs
weight: 70
url: /java/signature-integrity-checks/
description: 了解如何使用 PdfFileSignature 外观验证 Java 中的签名覆盖率和完整性。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中验证 PDF 签名覆盖率和完整性
Abstract: 了解如何使用 Aspose.PDF for Java 检查签名完整性。当前的Java示例集使用`verifySignature`来验证所选签名，并使用`coversWholeDocument`来确定签名是否保护整个PDF。
---
## 检查签名完整性

本文映射到 `PdfFileSignatureExamples.java` 公开的相同验证工作流程。

### 步骤

1. 使用 `PdfFileSignature` 绑定已签名的 PDF。
2. 从文档中选择签名名称。
3. 调用`verifySignature`验证签名内容。
4. 致电`coversWholeDocument`以确认文档范围内的覆盖范围。
5. 关闭门面对象。

### Java示例

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
