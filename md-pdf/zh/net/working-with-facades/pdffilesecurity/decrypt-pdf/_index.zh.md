---
title: 解密 PDF 文件
type: docs
weight: 20
url: /net/decrypt-pdf-file/
description: 本主题解释如何使用 PdfFileSecurity 类解密 PDF 文件。
lastmod: "2021-06-05"
draft: false
---

用密码或证书加密的 PDF 文档必须解锁后才能对其执行其他操作。如果尝试对加密的 PDF 文档进行操作，将抛出异常。解锁加密的 PDF 后，可以对其执行一个或多个操作。

## 使用所有者密码解密 PDF 文件

{{% alert color="primary" %}}
在线尝试 <br>
您可以尝试使用 Aspose.PDF 解锁文档，并通过此链接在线获取结果：
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

为了解密 PDF 文件，您需要创建 [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 对象，然后调用 [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) 方法。 你还需要将拥有者密码传递给[DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile)方法。以下代码片段向您展示了如何解密PDF文件。

```csharp
    public static void DecryptPDFFile()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // 创建PdfFileSecurity对象
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                // 解密PDF文档
                fileSecurity.DecryptFile("P@ssw0rd");
                fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
            }
        }
```