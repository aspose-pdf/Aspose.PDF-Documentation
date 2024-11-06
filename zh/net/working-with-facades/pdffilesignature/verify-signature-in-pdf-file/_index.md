---
title: 验证PDF文件中的签名
type: docs
weight: 30
url: zh/net/verify-signature-in-pdf/
description: 本节解释如何使用PdfFileSignature类验证PDF文件中的签名。
lastmod: "2021-06-05"
draft: false
---

## 验证PDF文件是否使用签名签署

要验证PDF文件是否使用[特定签名](/pdf/net/working-with-signature-in-a-pdf-file/)，可以使用[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)类的VerifySigned方法。此方法需要签名名称，如果PDF使用该签名名称签署，则返回true。也可以在不验证具体签名的情况下验证[PDF是否已签署](/pdf/net/working-with-signature-in-a-pdf-file/)。

### 验证PDF是否使用给定签名签署

以下代码片段展示了如何验证PDF是否使用给定签名签署。

```csharp
public static void IsPdfSigned()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.ContainsSignature())
                Console.WriteLine("Document Signed");
            pdfSign.Close();
        }
```

### 验证 PDF 是否已签名

要在不提供签名名称的情况下确定文件是否已签名，请使用以下代码。

```csharp
 public static void IsPdfSignedWithGivenSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySigned("Signature1"))
            {
                Console.WriteLine("PDF 已签名");
            }
            //if (pdfSign.VerifySigned("Signature2"))
            //{
            //    Console.WriteLine("PDF 已签名");
            //}
        }
```

## 验证签名是否有效

[VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) 方法在 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类中允许您验证特定签名。 这方法需要签名名称作为输入，如果签名有效，则返回true。以下代码片段展示了如何验证签名。

```csharp
public static void IsPdfSignatureValid()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySignature("Signature1"))
            {
                Console.WriteLine("Signature Verified");
            }
        }
```