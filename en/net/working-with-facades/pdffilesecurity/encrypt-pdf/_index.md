---
title: Encrypt PDF File
type: docs
weight: 10
url: /net/encrypt-pdf-file/
description: This topic explains how to Encrypt PDF File using PdfFileSecurity Class.
lastmod: "2021-06-05"
draft: false
---

Encrypting a PDF document protects its content from unauthorized access from outside, especially during file sharing or archiving.

Confidential PDF documents can be encrypted and password protected. Only user who know the password will be able to decrypt, open and view these documents.

Let's take a look at how PDF encryption works with Aspose.PDF library.

## Encrypt PDF File using Different Encryption Types and Algorithms

In order to encrypt a PDF file, you need to create [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) object and then call the [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) method. You can pass user password, owner password and privileges to [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) method. You also need to pass KeySize and Algorithm values to this method. 

Review a possible list of such [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm): 

|**Member name**|**Value**|**Description**|
| :- | :- | :- |
|RC4x40|0|RC4 with key length 40.|
|RC4x128|1|RC4 with key length 128.|
|AESx128|2|AES with key length 128.|
|AESx256|3|AES with key length 256.|

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

