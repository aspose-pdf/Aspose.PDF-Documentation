---
title: Tambahkan Tanda Tangan di File PDF
type: docs
weight: 10
url: /id/net/add-signature-in-pdf/
description: Bagian ini menjelaskan cara menambahkan tanda tangan ke File PDF menggunakan kelas PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Tambahkan Tanda Tangan Digital di File PDF

Kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) memungkinkan Anda untuk menambahkan tanda tangan di file PDF.
``` Anda perlu membuat objek dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) menggunakan file PDF masukan dan keluaran. Anda juga perlu membuat objek [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) di mana Anda ingin menambahkan tanda tangan dan untuk mengatur tampilan, Anda dapat menentukan gambar menggunakan properti [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) dari objek [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Aspose.Pdf.Facades juga menyediakan berbagai jenis tanda tangan seperti PKCS#1, PKCS#7, dan PKCS#7Detached. Untuk membuat tanda tangan tipe tertentu, Anda perlu membuat objek dari kelas tertentu seperti **PKCS1**, **PKCS7** atau **PKCS7Detached** menggunakan file sertifikat dan kata sandi.

Setelah objek dari tipe tanda tangan tertentu dibuat, Anda dapat menggunakan metode [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) untuk menandatangani PDF dan meneruskan objek tanda tangan tertentu ke kelas ini. Anda juga dapat menentukan atribut lain untuk metode ini. Akhirnya, Anda perlu menyimpan PDF yang telah ditandatangani menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Cuplikan kode berikut menunjukkan cara menambahkan tanda tangan dalam file PDF.

```csharp
public static void AddPdfFileSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Buat persegi panjang untuk lokasi tanda tangan
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Atur tampilan tanda tangan
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Buat salah satu dari tiga jenis tanda tangan
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "I'm document author", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
            // Simpan file PDF keluaran
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```
Contoh kode berikut menunjukkan kemampuan untuk menandatangani dokumen dengan dua tanda tangan. Dalam contoh kami, kami meletakkan tanda tangan pertama di halaman pertama, dan tanda tangan kedua di halaman kedua. Anda dapat menentukan halaman yang Anda butuhkan.

```csharp
 public static void AddTwoSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Tanda tangan dengan tanda tangan pertama

            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Buat persegi panjang untuk lokasi tanda tangan pertama
            System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Buat objek tanda tangan pertama
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "Saya penulis dokumen", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1, signature1);
            pdfSign.Save(_dataDir + "DigitallySign.pdf");


            // Tanda tangan dengan tanda tangan kedua

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // Buat persegi panjang untuk lokasi tanda tangan kedua
            System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Buat objek tanda tangan kedua
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(2, "Saya peninjau dokumen", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect2, signature2);

            // Simpan file PDF keluaran
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

Untuk dokumen dengan formulir atau acroforms yang perlu ditandatangani, lihat contoh berikut.
Anda perlu membuat objek dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) menggunakan file PDF input dan output. Gunakan [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) untuk mengikat. Buat tanda tangan dengan kemampuan untuk menambahkan properti yang diperlukan. Dalam contoh kami, mereka adalah 'Reason' dan 'CustomAppearance'.

```csharp
 public static void AddPdfFileSignatureField()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample02.pdf");

            // Buat salah satu dari tiga jenis tanda tangan
            PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Tandatangan sebagai Penulis",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6,
                    FontFamilyName = "Calibri"
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature);
            // Simpan file PDF output
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

Jika dokumen kita memiliki dua bidang, algoritma untuk menandatanganinya mirip dengan contoh pertama.

```csharp
public static void AddPdfFileSignatureField2()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample03.pdf");

            // Buat salah satu dari tiga jenis tanda tangan
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021")
            {
                Reason = "Tandatangan sebagai Penulis",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature1);
            // Simpan file PDF keluaran
            pdfSign.Save(_dataDir + "DigitallySign.pdf");

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // Buat salah satu dari tiga jenis tanda tangan
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Tandatangan sebagai Peninjau",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature2", signature2);
            // Simpan file PDF keluaran
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```