---
title: 更改PDF文件的密码
type: docs
weight: 40
url: /net/change-password/
description: 本主题解释如何使用PdfFileSecurity类更改PDF文件上的密码。
lastmod: "2021-06-05"
draft: false
---

## 更改PDF文件的密码

为了更改PDF文件的密码，您需要创建一个[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity)对象，然后调用[ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2)方法。您需要将现有的所有者密码和新的用户及所有者密码传递给[ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2)方法。

{{% alert color="primary" %}}

- **用户密码**，如果设置，是您打开PDF时需要提供的。Acrobat/Reader会提示用户输入用户密码。如果不正确，文档将不会打开。
- **所有者密码**，如果设置，控制权限，例如打印、编辑、提取、评论等。 Acrobat/Reader 将根据权限设置禁用这些功能。如果您想设置/更改权限，Acrobat 将需要此密码。

{{% /alert %}}

以下代码片段向您展示如何更改 PDF 文件的密码。

```csharp
public static void ChangePassword()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // 创建 PdfFileSecurity 对象
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.Print, KeySize.x256);
                fileSecurity.Save(_dataDir + "sample_encrtypted1.pdf");
            }
        }
```