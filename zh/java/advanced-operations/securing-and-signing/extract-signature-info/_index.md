---
title: 用Java从PDF中提取签名信息
linktitle: 从签名中提取详细信息
type: docs
weight: 20
url: /java/extract-image-and-signature-information/
description: 了解如何使用 Java 从 PDF 文件中提取证书和数字签名详细信息。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 从签名 PDF 中提取签名详细信息和证书数据
Abstract: 本文介绍如何使用 Aspose.PDF for Java 检查 PDF 文档中的数字签名。了解如何读取签名者详细信息、验证签名、检查签名是否覆盖整个文档、提取嵌入的签名证书以及删除现有签名。
---
使用 `PdfFileSignature` 检查和管理 PDF 文档中已存在的签名。

## 读取签名信息

1. 创建 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 外观并绑定源 PDF 文档。
1. 访问文档签名名称并配置示例所需的签名检查流程。
1. 从 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 外观读取并验证签名信息。
1. 读取返回的值或继续执行下一个处理步骤。

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

## 验证签名

1. 创建 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 外观并绑定源 PDF 文档。
1. 访问文档签名名称并配置示例所需的验证流程。
1. 从 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 外观读取并验证签名信息。

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: "
                + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: "
                + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```

## 提取签名证书

1. 创建 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 外观并绑定源 PDF 文档。
1. 访问证书提取所需的文档签名名称。
1. 写入提取的输出或检查 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) 外观返回的值。

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
