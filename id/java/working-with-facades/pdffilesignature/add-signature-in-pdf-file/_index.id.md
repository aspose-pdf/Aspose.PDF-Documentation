---
title: Tambahkan Tanda Tangan di File PDF
type: docs
weight: 10
url: /java/add-signature-in-pdf/
description: Bagian ini menjelaskan cara bekerja dengan Tanda Tangan dalam File PDF menggunakan kelas PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Tambahkan Tanda Tangan Digital di File PDF (facades)

Kelas [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) memungkinkan Anda untuk menambahkan tanda tangan di file PDF. Anda perlu membuat objek dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) menggunakan file PDF input dan output. Anda juga perlu membuat objek Rectangle di mana Anda ingin menambahkan tanda tangan dan untuk mengatur tampilan, Anda dapat menentukan gambar menggunakan properti setSignatureAppearance dari objek [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature).

Aspose.Pdf.Facades juga menyediakan berbagai jenis tanda tangan seperti PKCS#1, PKCS#7, dan PKCS#7Detached.
 Untuk membuat tanda tangan dari jenis tertentu, Anda perlu membuat objek dari kelas tertentu seperti PKCS1, PKCS7, atau PKCS7Detached menggunakan file sertifikat dan kata sandi.

Setelah objek dari jenis tanda tangan tertentu dibuat, Anda dapat menggunakan metode sign dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) untuk menandatangani PDF dan meneruskan objek tanda tangan tertentu ke kelas ini. Anda juga dapat menentukan atribut lain untuk metode ini. Terakhir, Anda perlu menyimpan PDF yang telah ditandatangani menggunakan metode save dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature). Cuplikan kode berikut menunjukkan cara menambahkan tanda tangan pada file PDF.

```java
public static void AddPdfFileSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Buat persegi panjang untuk lokasi tanda tangan
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);
        // Atur tampilan tanda tangan
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // Buat salah satu dari tiga jenis tanda tangan
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "Saya penulis dokumen", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect,
                signature);
        // Simpan file PDF keluaran
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

Contoh kode berikut menunjukkan kemampuan untuk menandatangani dokumen dengan dua tanda tangan. Dalam contoh kami, kami meletakkan tanda tangan pertama pada halaman pertama, dan yang kedua pada halaman kedua. Anda dapat menentukan halaman yang Anda butuhkan.

```java
    public static void AddTwoSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        // Tandatangani dengan tanda tangan pertama

        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Buat persegi panjang untuk lokasi tanda tangan pertama
        java.awt.Rectangle rect1 = new java.awt.Rectangle(10, 10, 300, 50);

        // Buat objek tanda tangan pertama
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "Saya adalah penulis dokumen", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1,
                signature1);
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        // Tandatangani dengan tanda tangan kedua

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // Buat persegi panjang untuk lokasi tanda tangan kedua
        java.awt.Rectangle rect2 = new java.awt.Rectangle(10, 10, 300, 50);

        // Buat objek tanda tangan kedua
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(2, "Saya adalah peninjau dokumen", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true,
                rect2, signature2);

        // Simpan file PDF keluaran
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


Untuk dokumen dengan formulir atau acroforms yang perlu ditandatangani, lihat contoh berikut.
Anda perlu membuat objek dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) menggunakan file PDF input dan output. Gunakan bindPdf untuk mengikat. Buat tanda tangan dengan kemampuan untuk menambahkan properti yang diperlukan. Dalam contoh kami, mereka adalah 'Reason' dan 'CustomAppearance'.

```java
  public static void AddPdfFileSignatureField() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample02.pdf");

        // Buat salah satu dari tiga jenis tanda tangan
        PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature.setReason("Tanda tangan sebagai Penulis");

        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        // PKCS#1
        pdfSign.sign("Signature1", signature);
        // Simpan file PDF keluaran
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


Jika dokumen kami memiliki dua bidang, algoritma untuk menandatanganinya mirip dengan contoh pertama.

```java
   public static void AddPdfFileSignatureField2() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample03.pdf");

        // Buat salah satu dari tiga jenis tanda tangan
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021");
        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature1.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        signature1.setReason("Tanda tangan sebagai Penulis"); // PKCS#1
        pdfSign.sign("Signature1", signature1);

        // Simpan file PDF keluaran
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // Buat salah satu dari tiga jenis tanda tangan
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature2.setReason("Tanda tangan sebagai Peninjau"); // PKCS#1
        signature2.setCustomAppearance(sca);
        pdfSign.sign("Signature2", signature2);
        // Simpan file PDF keluaran
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```