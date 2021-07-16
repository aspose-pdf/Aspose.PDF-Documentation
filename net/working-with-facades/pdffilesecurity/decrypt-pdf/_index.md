---
title: Decrypt PDF File
type: docs
weight: 20
url: /net/decrypt-pdf-file/
description: This topic explains how to Decrypt PDF File using PdfFileSecurity Class.
lastmod: "2021-06-05"
draft: false
---

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
