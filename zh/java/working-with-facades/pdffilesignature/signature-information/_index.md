---
title: 签名信息
linktitle: 签名信息
type: docs
weight: 60
url: /zh/java/signature-information/
description: 了解如何使用 PdfFileSignature 在 Java 中读取已签名 PDF 的签名名称和签署者详细信息。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中读取 PDF 文档的签名详细信息
Abstract: 了解如何使用 Aspose.PDF for Java 检查签名元数据。该 Java 示例读取第一个可用的签名名称，然后从已签名的 PDF 中获取签署者、日期、原因和位置。
---
## 获取签名信息

当您需要检查 PDF 的签署者以及存储了哪些签名元数据时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileSignature` 实例并绑定已签名的 PDF。
2. 读取签名集合并选择签名名称。
3. 调用签名信息访问器以获取签署人姓名、日期、原因和位置。
4. 完成后关闭 Facades 对象。

### Java 示例

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
