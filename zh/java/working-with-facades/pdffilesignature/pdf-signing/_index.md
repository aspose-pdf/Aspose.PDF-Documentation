---
title: 签署 PDF 文档
linktitle: 签署 PDF 文档
type: docs
weight: 10
url: /zh/java/pdf-signing/
description: 了解如何在 Java 中使用 PdfFileSignature 类签署 PDF 文档。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中使用数字签名签署 PDF 文档
Abstract: 了解如何使用 Aspose.PDF for Java 签署 PDF 文档。Java 示例集涵盖使用配置的证书路径和密码进行签署，以及使用显式的 PKCS7 签名对象进行签署，该对象包含签名元数据，如原因、联系信息、位置和授权机构。
---
## 签署 PDF 文档

当需要在 PDF 上应用可见的数字签名时，使用 `PdfFileSignature`。

### 步骤

1. 创建一个 `PdfFileSignature` 实例并绑定源 PDF。
2. 通过以下方式加载证书 `setCertificate` 或通过创建一个 `PKCS7` 对象。
3. 调用 `sign` 带有目标页面、可见性设置、签名矩形和签名数据。
4. 保存已签名的 PDF 并关闭 Facades 对象。

### Java 示例

```java
public static void signPdfWithCertificateObject(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.sign(1, false, signatureRectangle(), createPkcs7(certificateFile, "Document approval"));
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}

public static void signPdfWithBasicParameters(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.setCertificate(certificateFile.toString(), CERTIFICATE_PASSWORD);
        pdfSignature.sign(1, "Document approval", "qa@example.com", "New York, USA", false, signatureRectangle());
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
