---
title: Enkripsi File PDF
linktitle: Enkripsi File PDF
type: docs
weight: 30
url: /id/java/encrypt-pdf-file/
description: Pelajari cara mengenkripsi PDF dan mengonfigurasi izin di Java dengan facade PdfFileSecurity.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Enkripsikan file PDF dan definisikan izin pengguna di Java
Abstract: Pelajari cara mengenkripsi PDF dengan Aspose.PDF for Java. Set contoh Java mencakup enkripsi berbasis kata sandi dengan hak istimewa terbatas, enkripsi yang berfokus pada izin, dan enkripsi berbasis AES dengan ukuran kunci 256-bit.
---
## Enkripsi file PDF

Gunakan `PdfFileSecurity` ketika Anda perlu melindungi PDF dengan kata sandi dan aturan hak istimewa.

### Langkah

1. Buat sebuah `PdfFileSecurity` Instansi.
2. Mengikat PDF sumber dengan `bindPdf`.
3. Bangun sebuah `DocumentPrivilege` objek yang cocok dengan tindakan yang diizinkan.
4. Panggil yang sesuai `encryptFile` overload untuk ukuran kunci dan algoritma yang Anda butuhkan.
5. Simpan file yang diamankan dan tutup objek.

### Contoh Java

```java
public static void encryptPdfWithUserOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithPermissions(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getAllowAll();
    privilege.setAllowPrint(false);
    privilege.setAllowCopy(false);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithEncryptionAlgorithm(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x256, Algorithm.AES);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
