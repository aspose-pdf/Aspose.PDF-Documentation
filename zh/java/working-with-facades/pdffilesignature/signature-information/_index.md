---
title: 签名信息
linktitle: 签名信息
type: docs
weight: 60
url: /java/signature-information/
description: 了解如何使用 PdfFileSignature 从 Java 中签名的 PDF 中读取签名名称和签名者详细信息。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 从 PDF 文档中读取签名详细信息
Abstract: 了解如何使用 Aspose.PDF for Java 检查签名元数据。 Java 示例读取第一个可用的签名名称，然后从签名的 PDF 中检索签名者、日期、原因和位置。
---
## 获取签名信息

当您需要检查谁签署了 PDF 以及存储了哪些签名元数据时，请使用此工作流程。

### 步骤

1. 创建`PdfFileSignature`实例并绑定签名的PDF。
2. 阅读签名集并选择签名名称。
3. 调用签名信息访问器以获取签名者姓名、日期、原因和位置。
4. 完成后关闭外观对象。

### Java示例

```java
public static void getSignatureInformation(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature Names: " + pdfSignature.getSignNames());
        System.out.println("Signer: " + pdfSignature.getSignerName(signatureName));
        System.out.println("Date: " + pdfSignature.getDateTime(signatureName));
        System.out.println("Reason: " + pdfSignature.getReason(signatureName));
        System.out.println("Location: " + pdfSignature.getLocation(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
