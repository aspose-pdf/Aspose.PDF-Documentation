---
title: "Melindungi file PDF di Java"
linktitle: "Mengenkripsi dan mendekripsi file PDF"
type: docs
weight: 70
url: /id/java/protect-pdf-file/
description: Pelajari cara mengenkripsi file PDF, mendekripsi dokumen yang dilindungi, mengubah kata sandi, dan memeriksa perlindungan kata sandi di Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengatur izin PDF dan mengelola enkripsi di Java"
Abstract: Artikel ini menjelaskan cara melindungi file PDF dalam Java menggunakan Aspose.PDF. Artikel ini mencakup penerapan kata sandi pengguna dan pemilik, pengaturan hak istimewa dokumen, enkripsi dan dekripsi file PDF, mengubah kata sandi, serta memeriksa kata sandi kandidat untuk dokumen yang terenkripsi.
---
Aspose.PDF for Java menyediakan beberapa API untuk mengamankan file PDF dengan kata sandi dan izin.

## Melindungi dokumen PDF dalam Java

Contoh-contoh di `ProtectDocumentExamples.java` demonstrasikan cara:

1. Terapkan enkripsi ke sebuah [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dengan kata sandi pengguna dan pemilik.
1. Batasi izin dengan [`DocumentPrivilege`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. Pilih satu [`CryptoAlgorithm`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) untuk yang dilindungi [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Dekripsi yang dilindungi [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Ubah kata sandi yang ada pada [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Uji kata sandi kandidat dengan [`PdfFileInfo`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) dan [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

## Mengenkripsi PDF dengan hak istimewa terbatas

```java
public static void encryptPassword(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    try {
        DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
        documentPrivilege.setAllowScreenReaders(true);

        document.encrypt(
                USER_PASSWORD,
                OWNER_PASSWORD,
                documentPrivilege,
                CryptoAlgorithm.AESx128,
                false);
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## Mengenkripsi file PDF

```java
public static void encryptPdfFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    try {
        document.encrypt(
                USER_PASSWORD,
                OWNER_PASSWORD,
                DocumentPrivilege.getAllowAll(),
                CryptoAlgorithm.RC4x128,
                false);
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## Mendekripsi PDF yang dilindungi

```java
public static void decryptPdfFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString(), USER_PASSWORD);
    try {
        document.decrypt();
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## Mengubah kata sandi

```java
public static void changePassword(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString(), OWNER_PASSWORD);
    try {
        document.changePasswords(OWNER_PASSWORD, "newuser", "newowner");
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## Menentukan kata sandi yang benar dari daftar

```java
public static void determineCorrectPasswordFromList(Path inputFile) {
    try (PdfFileInfo info = new PdfFileInfo(inputFile.toString())) {
        System.out.println("File is password protected: " + info.isEncrypted());
    }
    String[] passwords = {"test", "test1", "test2", "test3", USER_PASSWORD};
    for (String password : passwords) {
        try {
            Document document = new Document(inputFile.toString(), password);
            try {
                int pageCount = document.getPages().size();
                if (pageCount > 0) {
                    System.out.println("Password '" + password + "' is correct. Pages: " + pageCount);
                }
            } finally {
                document.close();
            }
        } catch (InvalidPasswordException ex) {
            System.out.println("Wrong password: " + password);
        }
    }
}
```
