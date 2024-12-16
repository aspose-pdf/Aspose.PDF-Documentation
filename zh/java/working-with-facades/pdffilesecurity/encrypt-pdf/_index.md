---
title: 加密 PDF 文件
type: docs
weight: 10
url: /zh/java/encrypt-pdf-file/
description: 本主题解释如何使用 PdfFileSecurity 类加密 PDF 文件。
lastmod: "2021-06-05"
draft: false
---

## 使用不同的加密类型和算法加密 PDF 文件

为了加密 PDF 文件，您需要创建 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) 对象，然后调用 [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-) 方法。您可以将用户密码、所有者密码和权限传递给 [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-) 方法。您还需要将 KeySize 和 Algorithm 值传递给此方法。

以下代码片段向您展示如何加密 PDF 文件。

```java
    public static void EncryptPDFFile() {
        // 创建 PdfFileSecurity 对象
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        // 使用 256 位加密加密文件
        fileSecurity.encryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.getPrint(), KeySize.x256,
                Algorithm.AES);
        fileSecurity.save(_dataDir + "sample_encrypted.pdf");
    }
```