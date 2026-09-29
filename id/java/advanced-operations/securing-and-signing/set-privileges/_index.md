---
title: Enkripsi dan Dekripsi File PDF dalam Java
linktitle: Enkripsi dan Dekripsi File PDF
type: docs
weight: 70
url: /id/java/set-privileges-encrypt-and-decrypt-pdf-file/
description: Pelajari cara mengatur hak istimewa PDF, mengenkripsi file, mendekripsi PDF yang dilindungi, dan mengubah kata sandi dalam Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur izin PDF dan kelola enkripsi dalam Java
Abstract: Artikel ini menjelaskan cara mengamankan file PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup enkripsi dokumen dengan kata sandi pengguna dan pemilik, penerapan batasan izin, dekripsi file, mengubah kata sandi, dan pengaturan hak istimewa dengan atau tanpa metode aman dari pengecualian.
---
Aspose.PDF for Java mengekspos operasi keamanan PDF melalui `PdfFileSecurity` fasad.

## Enkripsi PDF dengan kata sandi pengguna dan pemilik

1. Buat dan ikat [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) fasad ke dokumen PDF sumber.
1. Konfigurasikan [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) dan [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) properti yang diperlukan oleh contoh.
1. Simpan dokumen PDF yang diperbarui melalui [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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
```

## Enkripsi PDF dengan algoritma tertentu

`encryptPdfWithEncryptionAlgorithm` menggunakan `KeySize.x256` bersama dengan `Algorithm.AES` untuk menerapkan pengaturan enkripsi yang lebih kuat.

## Dekripsi PDF yang dilindungi

1. Buat dan ikat [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) fasad ke dokumen PDF sumber.
1. Dekripsi dokumen yang dilindungi dengan kata sandi pemilik.
1. Simpan dokumen PDF yang diperbarui melalui [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

Set contoh juga mencakup `tryDecryptPdfWithoutException`, yang mengembalikan `false` alih-alih melempar ketika dekripsi gagal.

## Ubah kata sandi dan atur ulang keamanan

Itu `PdfFileSecurityExamples` kelas menunjukkan:

- `changeUserAndOwnerPassword` untuk mengganti kedua kata sandi.
- `changePasswordAndResetSecurity` untuk mengubah kata sandi dan menerapkan kembali hak istimewa dalam satu langkah.
- `tryChangePasswordWithoutException` untuk alur perubahan kata sandi yang tidak melempar pengecualian.

## Atur hak istimewa dokumen

Untuk membatasi tindakan seperti mencetak dan menyalin:

1. Buat dan ikat [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) fasad ke dokumen PDF sumber.
1. Atur yang diperlukan [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) izin atau opsi enkripsi.
1. Atur properti yang diperlukan oleh contoh.
1. Simpan dokumen PDF yang diperbarui melalui [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void setPdfPrivilegesWithPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    privilege.setAllowCopy(false);
    fileSecurity.setPrivilege("user_password", "owner_password", privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
