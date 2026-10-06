---
title: PDF 认证
linktitle: PDF 认证
type: docs
weight: 30
url: /zh/java/pdf-certification/
description: 了解如何使用 PdfFileSignature 和 DocMDPSignature 在 Java 中对 PDF 文档进行认证。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中使用 DocMDP 权限对 PDF 文档进行认证
Abstract: 了解如何使用 Aspose.PDF for Java 对 PDF 文档进行认证。此 Java 示例使用 PdfFileSignature 与 DocMDPSignature 和 DocMDPAccessPermissions 相结合，对文档进行认证，以便允许填写表单和签名，同时限制其他类型的修改。
---
## 认证 PDF 文档

当文档需要保持可信任但在签名后仍允许特定类别的更改时，请使用认证。

### 步骤

1. 创建一个 `PdfFileSignature` 实例并绑定源 PDF。
2. 构建一个 `PKCS7` 带有证书和证书密码的签名对象。
3. 将该签名包装在一个 `DocMDPSignature` 带有必需的 `DocMDPAccessPermissions` 值。
4. 呼叫 `certify` 包含目标页面、签名元数据、可见矩形和 MDP 签名。
5. 保存已签署的 PDF 并关闭 Facades 对象。

### Java 示例

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com", "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
