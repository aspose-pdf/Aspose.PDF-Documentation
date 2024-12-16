---
title: Decrypt PDF File
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: Discover how to decrypt PDF files using Aspose.PDF in Java and remove password protection to gain access to the content.
lastmod: "2021-06-05"
draft: false
---

## Decrypt PDF File using Owner Password

{{% alert color="primary" %}}
Try online <br>
You can try to unlock document using Aspose.PDF and get the results online at this link:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

In order to decrypt a PDF file, you need to create [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) object and then call the [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) method. You also need to pass the owner password to [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) method. The following code snippet shows you how to decrypt PDF file.

```java
    public static void DecryptPDFFile() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // Create PdfFileSecurity object
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            // Decrypt PDF document
            fileSecurity.decryptFile("User_P@ssw0rd");
            fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
        }
    }
```
