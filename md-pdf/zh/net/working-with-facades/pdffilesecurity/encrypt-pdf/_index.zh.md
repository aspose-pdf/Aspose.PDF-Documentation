---
title: Encrypt PDF File
type: docs
weight: 10
url: /net/encrypt-pdf-file/
description: 本主题解释了如何使用 PdfFileSecurity 类加密 PDF 文件。
lastmod: "2021-06-05"
draft: false
---

加密 PDF 文档可以保护其内容免受外部未经授权的访问，尤其是在文件共享或归档期间。

机密的 PDF 文档可以被加密并设置密码保护。只有知道密码的用户才能解密、打开和查看这些文档。

让我们看看如何使用 Aspose.PDF 库进行 PDF 加密。

## 使用不同的加密类型和算法加密 PDF 文件

为了加密 PDF 文件，您需要创建 [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 对象，然后调用 [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) 方法。 您可以将用户密码、所有者密码和权限传递给[EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile)方法。您还需要将KeySize和Algorithm值传递给该方法。

查看此类[CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm)的可能列表：

|**成员名称**|**值**|**描述**|
| :- | :- | :- |
|RC4x40|0|RC4，密钥长度为40。|
|RC4x128|1|RC4，密钥长度为128。|
|AESx128|2|AES，密钥长度为128。|
|AESx256|3|AES，密钥长度为256。|

以下代码片段向您展示了如何加密PDF文件。

```csharp
public static void EncryptPDFFile()
        {
            // 创建 PdfFileSecurity 对象
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample.pdf");
            // 使用256位加密加密文件
            fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.Print, KeySize.x256, Algorithm.AES);
            fileSecurity.Save(_dataDir + "sample_encrypted.pdf");
        }
```