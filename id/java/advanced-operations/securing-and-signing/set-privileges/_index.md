---
title: "Mengenkripsi dan mendekripsi file PDF dalam Java"
linktitle: "Mengenkripsi dan mendekripsi file PDF"
type: docs
weight: 70
url: /id/java/set-privileges-encrypt-and-decrypt-pdf-file/
description: Pelajari cara mengatur hak istimewa PDF, mengenkripsi file, mendekripsi PDF yang dilindungi, dan mengubah kata sandi dalam Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengatur izin PDF dan mengelola enkripsi dalam Java"
Abstract: Artikel ini menjelaskan cara mengamankan file PDF menggunakan Aspose.PDF for Java. Artikel ini mencakup enkripsi dokumen dengan kata sandi pengguna dan pemilik, penerapan batasan izin, dekripsi file, mengubah kata sandi, dan pengaturan hak istimewa dengan atau tanpa metode aman dari pengecualian.
---
Aspose.PDF for Java mengekspos operasi keamanan PDF melalui fasad `PdfFileSecurity`.

## Mengenkripsi PDF dengan kata sandi pengguna dan pemilik

1. Buat dan ikat fasad [`PdfFileSecurity`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) ke dokumen PDF sumber.
1. Konfigurasikan properti [`DocumentPrivilege`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) dan [`KeySize`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) yang diperlukan oleh contoh.
1. Simpan dokumen PDF yang diperbarui melalui [`PdfFileSecurity`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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

## Mengenkripsi PDF dengan algoritma tertentu

`encryptPdfWithEncryptionAlgorithm` menggunakan `KeySize.x256` bersama dengan `Algorithm.AES` untuk menerapkan pengaturan enkripsi yang lebih kuat.

## Mendekripsi PDF yang dilindungi

1. Buat dan ikat fasad [`PdfFileSecurity`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) ke dokumen PDF sumber.
1. Dekripsi dokumen yang dilindungi dengan kata sandi pemilik.
1. Simpan dokumen PDF yang diperbarui melalui [`PdfFileSecurity`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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

## Mengubah kata sandi dan mengatur ulang keamanan

Itu kelas `PdfFileSecurityExamples` menunjukkan:

- `changeUserAndOwnerPassword` untuk mengganti kedua kata sandi.
- `changePasswordAndResetSecurity` untuk mengubah kata sandi dan menerapkan kembali hak istimewa dalam satu langkah.
- `tryChangePasswordWithoutException` untuk alur perubahan kata sandi yang tidak melempar pengecualian.

## Mengatur hak istimewa dokumen

Untuk membatasi tindakan seperti mencetak dan menyalin:

1. Buat dan ikat fasad [`PdfFileSecurity`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) ke dokumen PDF sumber.
1. Atur yang diperlukan [`DocumentPrivilege`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) izin atau opsi enkripsi.
1. Atur properti yang diperlukan oleh contoh.
1. Simpan dokumen PDF yang diperbarui melalui [`PdfFileSecurity`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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
