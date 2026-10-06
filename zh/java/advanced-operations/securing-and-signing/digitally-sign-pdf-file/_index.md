---
title: 在 Java 中添加数字签名或对 PDF 进行数字签署
linktitle: 对 PDF 进行数字签名
type: docs
weight: 10
url: /zh/java/digitally-sign-pdf-file/
description: 了解如何使用 Aspose.PDF 在 Java 中对 PDF 文档进行数字签名和认证。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 对 PDF 文件进行数字签名
Abstract: 本指南介绍如何使用 Aspose.PDF for Java 对 PDF 文档进行数字签名。它涵盖了使用证书对象签名、使用基础证书参数签名，以及使用 DocMDP 签名对文档进行认证以控制签名后允许的更改。
---
Aspose.PDF for Java 支持通过多种签名流程 `PdfFileSignature`。

## 使用证书对象对 PDF 进行签名

1. 创建 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 对象并绑定源 PDF 文档。
1. 创建 [PKCS7](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) 签名对象并配置签名选项。
1. 通过以下方式对 PDF 文档应用签名 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/)。
1. 保存更新后的 PDF 文档。

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
```

这种方法构建了一个 `PKCS7` 首先是签名对象，然后将其应用于第 1 页。

## 使用基本证书参数对 PDF 进行签名

1. 创建 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 对象并绑定源 PDF 文档。
1. 配置签名示例所需的证书参数。
1. 通过以下方式对 PDF 文档应用签名 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/)。
1. 保存更新后的 PDF 文档。

```java
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

## 使用 DocMDP 对 PDF 进行认证

当您需要认证级别的限制时，请使用文档修改检测与防止签名：

1. 创建 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 对象并绑定源 PDF 文档。
1. 创建 [DocMDPSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) 对象并配置 [DocMDPAccessPermissions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/) 签名选项。
1. 应用认证签名并保存更新后的 PDF 文档。

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com",
                "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
