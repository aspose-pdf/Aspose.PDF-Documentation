---
title: Encrypt PDF File
type: docs
weight: 10
url: /java/encrypt-pdf-file/
description: This topic explains how to Encrypt PDF File using PdfFileSecurity Class.
lastmod: "2021-06-05"
draft: false
---

## Encrypt PDF File using Different Encryption Types and Algorithms

In order to encrypt a PDF file, you need to create [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) object and then call the [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-) method. You can pass user password, owner password and privileges to [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-) method. You also need to pass KeySize and Algorithm values to this method.

The following code snippet shows you how to encrypt PDF file.

```java
    public static void EncryptPDFFile() {
        // Create PdfFileSecurity object
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        // Encrypt file using 256-bit encryption
        fileSecurity.encryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.getPrint(), KeySize.x256,
                Algorithm.AES);
        fileSecurity.save(_dataDir + "sample_encrypted.pdf");
    }
```

