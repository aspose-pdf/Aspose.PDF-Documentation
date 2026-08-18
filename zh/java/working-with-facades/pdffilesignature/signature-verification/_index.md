---
title: 签名验证
linktitle: 签名验证
type: docs
weight: 90
url: /java/signature-verification/
description: 了解如何使用 PdfFileSignature 外观在 Java 中验证 PDF 签名。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中验证 PDF 签名
Abstract: 了解如何使用 Aspose.PDF for Java 验证 PDF 签名。 Java 示例选择第一个可用的签名，验证该签名，并检查它是否覆盖整个文档。
---
## 验证 PDF 签名

当您需要对现有签名 PDF 进行快速验证时，请使用此工作流程。

### 步骤

1. 创建`PdfFileSignature`实例并绑定签名的PDF。
2. 选择您要检查的签名名称。
3. 调用`verifySignature`来验证签名。
4. 致电`coversWholeDocument`以检查覆盖范围。
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
