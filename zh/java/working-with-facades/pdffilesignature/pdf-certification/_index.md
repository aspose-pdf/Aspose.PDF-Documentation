---
title: PDF认证
linktitle: PDF认证
type: docs
weight: 30
url: /java/pdf-certification/
description: 了解如何使用 PdfFileSignature 和 DocMDPSignature 在 Java 中验证 PDF 文档。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 中的 DocMDP 权限验证 PDF 文档
Abstract: 了解如何使用 Aspose.PDF for Java 验证 PDF 文档。 Java 示例使用 PdfFileSignature 以及 DocMDPSignature 和 DocMDPAccessPermissions 来验证文档的表单填写和签名，同时限制其他类型的修改。
---
## 认证 PDF 文档

当文档应保持可信但仍允许在签名后进行定义的更改类别时，请使用认证。

### 步骤

1. 创建`PdfFileSignature`实例并绑定源PDF。
2. 使用证书和证书密码构建`PKCS7`签名对象。
3. 使用所需的 `DocMDPAccessPermissions` 值将该签名封装在 `DocMDPSignature` 中。
4. 使用目标页面、签名元数据、可见矩形和 MDP 签名调用 `certify`。
5. 保存经过认证的 PDF 并关闭外观对象。

### Java示例

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
