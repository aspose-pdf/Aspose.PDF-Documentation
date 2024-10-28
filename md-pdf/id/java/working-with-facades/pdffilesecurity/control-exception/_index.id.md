---
title: Kontrol Pengecualian File PDF
type: docs
weight: 30
url: /java/control-exception/
description: Topik ini menjelaskan bagaimana mengontrol pengecualian pada File PDF menggunakan Kelas PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

Kelas [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) memungkinkan Anda untuk mengontrol pengecualian. Untuk melakukan ini, Anda perlu mengatur [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) ke false atau true. Jika Anda mengatur operasi ke false, hasil dari [decryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) akan mengembalikan true atau false tergantung pada kebenaran kata sandi.

Jika Anda mengatur [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) ke true, maka Anda dapat mendapatkan hasil operasi menggunakan operator try-catch.

```java
    public static void ControlExceptionPDFFile() {
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
        fileSecurity.setAllowExceptions(false);
        // Dekripsi dokumen PDF

        if (!fileSecurity.decryptFile("IncorrectPassword")) {
            System.out.println("Ada yang salah...");
            System.out.println("Pengecualian terakhir: " + fileSecurity.getLastException().getMessage());
        }
        fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
    }
```