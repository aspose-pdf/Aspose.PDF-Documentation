---
title: 签名提取
linktitle: 签名提取
type: docs
weight: 50
url: /java/signature-extraction/
description: 了解如何使用 PdfFileSignature 从 Java 中签名的 PDF 中提取签名证书。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 用Java从PDF中提取签名证书
Abstract: 了解如何使用 Aspose.PDF for Java 提取与 PDF 签名关联的证书。当前的 Java 示例集包括将证书提取到输出流，但不包括单独的签名图像提取示例。
---
## 提取签名证书

当您需要保存与现有签名关联的证书时，请使用此工作流程。

### 步骤

1. 创建`PdfFileSignature`实例并绑定签名的PDF。
2. 选择要检查的签名名称。
3. 调用`extractCertificate`打开证书流。
4. 将证书字节复制到输出文件。
5. 关闭流资源和外观对象。

### Java示例

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

当前的`PdfFileSignatureExamples.java` 类不包含用于提取渲染的签名图像的专用Java 示例。
