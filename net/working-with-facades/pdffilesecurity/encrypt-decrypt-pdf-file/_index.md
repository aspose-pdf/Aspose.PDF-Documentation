---
title: Encrypt and decrypt using PdfFileSecurity
type: docs
weight: 10
url: /net/encrypt-decrypt-on-pdf-file/
description: This topic explains how to Encrypt, Decrypt and Set Privileges on PDF File using PdfFileSecurity Class.
lastmod: "2021-12-17"
---

## Encrypt PDF File using Different Encryption Types and Algorithms

In order to encrypt a PDF file, you need to create [PdfFileSecurity](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) object and then call the [EncryptFile](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) method. You can pass user password, owner password and privileges to [EncryptFile](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) method. You also need to pass KeySize and Algorithm values to this method.

{{% alert color="primary" %}}

- The **User password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it's not correct, the document will not open.
- The **Owner password**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

{{% /alert %}}

The following code snippet shows you how to encrypt PDF file.

```csharp
public static void EncryptPDFFile()
{
    // Create PdfFileSecurity object
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    // Encrypt file using 256-bit encryption
    fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.Print, KeySize.x256, Algorithm.AES);
    fileSecurity.Save(_dataDir + "sample_encrypted.pdf");
}
```

## Decrypt PDF File using Owner Password

{{% alert color="primary" %}}
Try online <br>
You can try to unlock document using Aspose.PDF and get the results online at this link:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

In order to decrypt a PDF file, you need to create [PdfFileSecurity](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) object and then call the [DecryptFile](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) method. You also need to pass the owner password to [DecryptFile](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) method. The following code snippet shows you how to decrypt PDF file.

```csharp
public static void DecryptPDFFile()
{
    PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
    // Create PdfFileSecurity object
    if (pdfFileInfo.IsEncrypted)
    {
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
        // Decrypt PDF document
        fileSecurity.DecryptFile("P@ssw0rd");
        fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
    }
}
```

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
