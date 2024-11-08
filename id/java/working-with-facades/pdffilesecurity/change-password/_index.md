---
title: Ubah Kata Sandi File PDF
type: docs
weight: 40
url: /id/java/change-password/
description: Topik ini menjelaskan cara mengubah kata sandi pada File PDF menggunakan Kelas PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Ubah Kata Sandi File PDF

Untuk mengubah kata sandi file PDF, Anda perlu membuat objek [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) dan kemudian memanggil metode [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-). Anda perlu memasukkan kata sandi pemilik yang ada dan kata sandi pengguna serta pemilik baru ke metode [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-).

Cuplikan kode berikut menunjukkan cara mengubah kata sandi file PDF.

```java
    public static void ChangePassword() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // Buat objek PdfFileSecurity
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.changePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.getPrint(),
                    KeySize.x256);
            fileSecurity.save(_dataDir + "sample_encrtypted1.pdf");
        }
    }
```