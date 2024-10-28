---
title: Cara menandatangani PDF secara digital
linktitle: Tanda tangan digital PDF
type: docs
weight: 10
url: /java/digitally-sign-pdf-file/
description: Menandatangani dokumen PDF secara digital menggunakan Java. Memverifikasi, atau memvalidasi tanda tangan digital PDF dengan aplikasi berbasis Java dengan PDF Library. Anda dapat mengesahkan file PDF dengan Sertifikat PKCS1.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Saat menandatangani dokumen PDF menggunakan tanda tangan, Anda pada dasarnya mengonfirmasi bahwa isinya harus tetap "sebagaimana adanya". Akibatnya, setiap perubahan yang dilakukan setelahnya membatalkan tanda tangan dan dengan demikian, Anda tahu jika dokumen telah diubah. Mengesahkan dokumen terlebih dahulu, memungkinkan Anda menentukan perubahan yang dapat dilakukan pengguna pada dokumen tanpa membatalkan sertifikasi.

Dengan kata lain, dokumen tersebut masih dianggap mempertahankan integritasnya dan penerima masih dapat mempercayai dokumen tersebut. Untuk detail lebih lanjut, silakan kunjungi Mengesahkan dan menandatangani PDF.

Untuk memenuhi persyaratan yang disebutkan di atas, perubahan API publik berikut telah dilakukan.

isCertified(…) metode ditambahkan ke kelas PdfFileSignature.

## Tandatangani PDF dengan tanda tangan digital

```java
public class ExampleDigitallySign {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void SignDocument() {
        String inFile = _dataDir + "DigitallySign.pdf";
        String outFile = _dataDir + "DigitallySign_out.pdf";
        Document document = new Document(inFile);

        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Pa$$w0rd2020"); // Gunakan objek PKCS7/PKCS7Detached
        signature.sign(1, true, new java.awt.Rectangle(300, 100, 400, 200), pkcs);
        // Simpan file PDF keluaran
        signature.save(outFile);
    }
```

## Tambahkan cap waktu ke tanda tangan digital

Aspose.PDF untuk Java mendukung penandatanganan PDF secara digital dengan server cap waktu atau layanan Web.

Untuk memenuhi persyaratan ini, kelas [TimestampSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf/TimestampSettings) telah ditambahkan ke namespace Aspose.PDF. Silakan lihat potongan kode berikut yang mendapatkan timestamp dan menambahkannya ke dokumen PDF:

```java
    public static void SignWithTimeStampServer() {
        Document document = new Document(_dataDir + "SimpleResume.pdf");
        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Start2020");
        TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", ""); // User/Password dapat
                                                                                                    // diabaikan
        pkcs.setTimestampSettings(timestampSettings);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 200, 100);
        // Buat salah satu dari tiga jenis tanda tangan
        signature.sign(1, "Alasan Tanda Tangan", "Kontak", "Lokasi", true, rect, pkcs);
        // Simpan file PDF keluaran
        signature.save(_dataDir + "DigitallySignWithTimeStamp_out.pdf");
    }
```