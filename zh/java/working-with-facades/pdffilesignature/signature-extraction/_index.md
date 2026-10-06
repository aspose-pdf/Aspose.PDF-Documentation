---
title: 签名提取
linktitle: 签名提取
type: docs
weight: 50
url: /zh/java/signature-extraction/
description: 了解如何在 Java 中使用 PdfFileSignature 从已签名的 PDF 中提取签名证书。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中从 PDF 提取签名证书
Abstract: 了解如何使用 Aspose.PDF for Java 提取与 PDF 签名关联的证书。当前的 Java 示例集包括将证书提取到输出流，但不包含单独的签名图像提取示例。
---
## 提取签名证书

当您需要保存现有签名关联的证书时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileSignature` 实例并绑定已签名的 PDF。
2. 选择要检查的签名名称。
3. 调用 `extractCertificate` 打开证书流。
4. 将证书字节复制到输出文件。
5. 关闭流资源和 Facades 对象。

### Java 示例

```java
public static void extractSignatureCertificate(Path inputFile, Path outputFile) throws Exception {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        try (InputStream inputStream = pdfSignature.extractCertificate(signatureName);
             OutputStream outputStream = Files.newOutputStream(outputFile)) {
            inputStream.transferTo(outputStream);
        }
    } finally {
        pdfSignature.close();
    }
}
```

当前 `PdfFileSignatureExamples.java` 该类未包含用于提取已呈现的签名图像的专用 Java 示例。
