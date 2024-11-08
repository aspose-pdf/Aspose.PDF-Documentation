---
title: 验证 PDF 文件中的签名
type: docs
weight: 30
url: /zh/java/verify-signature-in-pdf/
description: 本节解释如何使用 PdfFileSignature 类处理 PDF 文件中的签名。
lastmod: "2021-06-05"
draft: false
---

## 验证 PDF 文件是否使用签名签署

要验证 PDF 文件是否使用 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) 类的 VerifySigned 方法签署。此方法需要签名名称，如果 PDF 使用该签名名称签署，则返回 true。也可以在不验证使用哪个签名签署的情况下，验证 [PDF 已签名](/pdf/zh/java/working-with-signature-in-a-pdf-file/)。

### 验证 PDF 是否使用给定签名签署

以下代码片段演示了如何验证 PDF 是否使用给定签名签署。

```java
    public static void IsPdfSigned() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.containsSignature())
            System.out.println("Document Signed");

        pdfSign.close();
    }
```


### 验证 PDF 是否已签名

要确定文件是否已签名，而不提供签名名称，请使用以下代码。

```java
    public static void IsPdfSignedWithGivenSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySigned("Signature1")) {
            System.out.println("PDF 已签名");
        }
    }
```

## 验证签名是否有效

[VerifySignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#verifySignature-java.lang.String-) 方法是 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) 类的一部分，允许您验证特定签名。此方法需要签名名称作为输入，如果签名有效，则返回 true。以下代码片段展示了如何验证签名。

```java
    public static void IsPdfSignatureValid() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySignature("Signature1")) {
            System.out.println("签名已验证");
        }
    }
```