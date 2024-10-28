---
title: Enkripsi Berkas PDF
type: docs
weight: 10
url: /java/encrypt-pdf-file/
description: Topik ini menjelaskan cara Mengenkripsi Berkas PDF menggunakan Kelas PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Enkripsi Berkas PDF menggunakan Berbagai Jenis dan Algoritma Enkripsi

Untuk mengenkripsi sebuah berkas PDF, Anda perlu membuat objek [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) dan kemudian memanggil metode [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-). Anda dapat mengoper kata sandi pengguna, kata sandi pemilik, dan hak istimewa ke metode [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-). Anda juga perlu mengoper nilai KeySize dan Algoritma ke metode ini.

Cuplikan kode berikut menunjukkan kepada Anda bagaimana mengenkripsi berkas PDF.

```java
    public static void EncryptPDFFile() {
        // Buat objek PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        // Enkripsi berkas menggunakan enkripsi 256-bit
        fileSecurity.encryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.getPrint(), KeySize.x256,
                Algorithm.AES);
        fileSecurity.save(_dataDir + "sample_encrypted.pdf");
    }
```