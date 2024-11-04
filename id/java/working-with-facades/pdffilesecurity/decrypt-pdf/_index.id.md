---
title: Dekripsi File PDF
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: Topik ini menjelaskan cara Mendekripsi File PDF menggunakan Kelas PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Dekripsi File PDF menggunakan Kata Sandi Pemilik

{{% alert color="primary" %}}
Coba online <br>
Anda dapat mencoba membuka kunci dokumen menggunakan Aspose.PDF dan mendapatkan hasilnya secara online di tautan ini:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Untuk mendekripsi file PDF, Anda perlu membuat objek [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) dan kemudian memanggil metode [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-). Anda juga perlu memberikan kata sandi pemilik ke metode [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-). Cuplikan kode berikut menunjukkan cara mendekripsi file PDF.

```java
    public static void DecryptPDFFile() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // Buat objek PdfFileSecurity
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            // Dekripsi dokumen PDF
            fileSecurity.decryptFile("User_P@ssw0rd");
            fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
        }
    }
```