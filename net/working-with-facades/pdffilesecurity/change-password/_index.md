---
title: Change Password of PDF File
type: docs
weight: 40
url: /net/change-password/
description: This topic explains how change-password on PDF File using PdfFileSecurity Class.
lastmod: "2021-06-05"
draft: false
---

## Change Password of a PDF File

In order to change password of a PDF file, you need to create [PdfFileSecurity](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) object and then call the [ChangePassword](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2) method. You need to pass existing owner password and new user and owner passwords to the [ChangePassword](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2) method.

{{% alert color="primary" %}}

- The **User password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it's not correct, the document will not open.
- The **Owner password**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

{{% /alert %}}

The following code snippet shows you how to change passwords of a PDF file.

```csharp
public static void ChangePassword()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Create PdfFileSecurity object
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.Print, KeySize.x256);
                fileSecurity.Save(_dataDir + "sample_encrtypted1.pdf");
            }
        }
```

