---
title: 签署 PDF 文档
linktitle: 签署 PDF 文档
type: docs
weight: 10
url: /java/pdf-signing/
description: 了解如何使用 PdfFileSignature 外观在 Java 中签署 PDF 文档。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 中的数字签名对 PDF 文档进行签名
Abstract: 了解如何使用 Aspose.PDF for Java 签署 PDF 文档。 Java 示例集涵盖使用配置的证书路径和密码进行签名，以及使用显式 PKCS7 签名对象进行签名，其中包括签名元数据（例如原因、联系信息、位置和权限）。
---
## 签署 PDF 文档

当您需要将可见的数字签名应用于 PDF 时，请使用`PdfFileSignature`。

### 步骤

1. 创建`PdfFileSignature`实例并绑定源PDF。
2. 通过`setCertificate` 或创建`PKCS7` 对象加载证书。
3. 使用目标页面、可见性设置、签名矩形和签名数据调用`sign`。
4. 保存签名的 PDF 并关闭外观对象。

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
