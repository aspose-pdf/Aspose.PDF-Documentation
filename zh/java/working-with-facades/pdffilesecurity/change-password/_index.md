---
title: 更改 PDF 文件的密码
type: docs
weight: 40
url: zh/java/change-password/
description: 本主题讲解如何使用 PdfFileSecurity 类更改 PDF 文件的密码。
lastmod: "2021-06-05"
draft: false
---

## 更改 PDF 文件的密码

为了更改 PDF 文件的密码，您需要创建 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) 对象，然后调用 [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-) 方法。您需要将现有的所有者密码和新的用户及所有者密码传递给 [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-) 方法。

以下代码片段演示了如何更改 PDF 文件的密码。

```java
    public static void ChangePassword() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // 创建 PdfFileSecurity 对象
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.changePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.getPrint(),
                    KeySize.x256);
            fileSecurity.save(_dataDir + "sample_encrtypted1.pdf");
        }
    }
```