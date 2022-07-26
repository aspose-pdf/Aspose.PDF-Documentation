---
title: Control Exception PDF File
type: docs
weight: 30
url: /java/control-exception/
description: This topic explains how control exception on PDF File using PdfFileSecurity Class Class.
lastmod: "2021-06-05"
draft: false
---

[PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) class allows you to control exceptions. To do this, you need to set [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) to false or true. If you set the operation to false, the result of [decryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) will return true or false depending on the correctness of the password. 

If you set [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) to true, then you can get the result of the operation using the try-catch operator.

```java
    public static void ControlExceptionPDFFile() {
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
        fileSecurity.setAllowExceptions(false);
        // Decrypt PDF document

        if (!fileSecurity.decryptFile("IncorrectPassword")) {
            System.out.println("Something wrong...");
            System.out.println("Last exception: " + fileSecurity.getLastException().getMessage());
        }
        fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
    }
```