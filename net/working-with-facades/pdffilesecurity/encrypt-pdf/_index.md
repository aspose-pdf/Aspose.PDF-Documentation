---
title: Encrypt PDF File
type: docs
weight: 10
url: /net/encrypt-pdf-file/
description: This topic explains how to Encrypt PDF File using PdfFileSecurity Class.
lastmod: "2021-06-05"
draft: false
---

## Encrypt PDF File using Different Encryption Types and Algorithms

In order to encrypt a PDF file, you need to create [PdfFileSecurity](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) object and then call the [EncryptFile](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) method. You can pass user password, owner password and privileges to [EncryptFile](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) method. You also need to pass KeySize and Algorithm values to this method.

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

