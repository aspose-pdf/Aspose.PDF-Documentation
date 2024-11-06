---
title: Bekerja dengan Tanda Tangan dalam File PDF
type: docs
weight: 40
url: id/java/working-with-signature-in-a-pdf-file/
description: Bagian ini menjelaskan bagaimana cara bekerja dengan Tanda Tangan dalam File PDF menggunakan kelas PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Cara Mengekstrak Informasi Tanda Tangan

Aspose.PDF untuk Java mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas PdfFileSignature. Saat ini, juga memungkinkan untuk menentukan keabsahan sertifikat tetapi kita tidak dapat mengekstrak seluruh sertifikat. Informasi yang dapat diekstrak adalah kunci publik, sidik jari, dan penerbit, dll.

Untuk mengekstrak informasi tanda tangan, kami telah memperkenalkan metode extractCertificate(..) ke kelas PdfFileSignature. Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mengekstrak sertifikat dari objek PdfFileSignature:

```java
public static void ExtractSignatureInfo() {
        String input = _dataDir + "DigitallySign.pdf";
        String certificateFileName = "extracted_cert.pfx";
        PdfFileSignature pdfFileSignature = new PdfFileSignature();
        pdfFileSignature.bindPdf(input);
        List<String> sigNames = pdfFileSignature.getSignNames();

        if (sigNames.size() > 0) {
            String sigName = sigNames.get(0);
            if (sigName != "") {
                InputStream cerStream = pdfFileSignature.extractCertificate(sigName);
                if (cerStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(_dataDir + certificateFileName);
                        cerStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                }
            }
        }
    }
```


## Mengekstrak Gambar dari Bidang Tanda Tangan (PdfFileSignature)

Aspose.PDF untuk Java mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas PdfFileSignature dan saat menandatangani dokumen, Anda juga dapat mengatur gambar untuk SignatureAppearance. Sekarang API ini juga menyediakan kemampuan untuk mengekstrak informasi tanda tangan serta gambar yang terkait dengan bidang tanda tangan.

Untuk mengekstrak informasi tanda tangan, kami telah memperkenalkan metode [extractImage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#extractImage-java.lang.String-) ke kelas PdfFileSignature. Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mengekstrak gambar dari objek PdfFileSignature:

```java
 public static void ExtractSignatureImage() {
        PdfFileSignature signature = new PdfFileSignature();
        signature.bindPdf(_dataDir + "DigitallySign.pdf");
        if (signature.containsSignature()) {
            for (String sigName : signature.getSignNames()) {
                String outFile = _dataDir + sigName + "_ExtractImages_out.jpg";
                InputStream imageStream = signature.extractImage(sigName);
                if (imageStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(outFile);
                        imageStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
```


## Menyembunyikan Lokasi dan Alasan

Fungsi Aspose.PDF memungkinkan konfigurasi yang fleksibel untuk instance tanda tangan digital. Kelas [PdfFileSignature ](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) menyediakan kemampuan untuk menandatangani file PDF. Implementasi metode Sign memungkinkan untuk menandatangani PDF dan mengirimkan objek tanda tangan tertentu ke kelas ini. Metode Sign mengandung serangkaian atribut untuk kustomisasi tanda tangan digital keluaran. Jika Anda ingin menyembunyikan beberapa atribut teks dari hasil tanda tangan, Anda dapat membiarkannya kosong. Potongan kode berikut menunjukkan cara menyembunyikan dua baris Lokasi dan Alasan dari blok tanda tangan:

```java
public static void SupressLocationReason() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Buat persegi panjang untuk lokasi tanda tangan
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // Atur tampilan tanda tangan
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // Buat salah satu dari tiga jenis tanda tangan
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "", "test01@aspose-pdf-demo.local", "", true, rect, signature);
        // Simpan file PDF keluaran
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## Fitur Kustomisasi untuk Tanda Tangan Digital

Aspose.PDF untuk Java memungkinkan fitur kustomisasi untuk tanda tangan digital. Metode Sign dari kelas SignatureCustomAppearance mengimplementasikan dengan 6 overload untuk penggunaan yang nyaman. Sebagai contoh, Anda dapat mengonfigurasi tanda tangan hasil hanya dengan instance kelas SignatureCustomAppearance dan nilai propertinya. Cuplikan kode berikut menunjukkan cara menyembunyikan keterangan "Digitally signed by" dari tanda tangan digital keluaran PDF Anda.

```java
    public static void CustomizationFeaturesForDigitalSign() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Buat persegi panjang untuk lokasi tanda tangan
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // Buat salah satu dari tiga jenis tanda tangan
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setFontSize(6);
        signatureCustomAppearance.setFontFamilyName("Times New Roman");
        signatureCustomAppearance.setDigitalSignedLabel("SIGNED BY:");
        signature.setCustomAppearance(signatureCustomAppearance);

        pdfSign.sign(1, true, rect, signature);
        // Simpan file PDF keluaran
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## Ubah Bahasa Dalam Teks Tanda Tangan Digital

Menggunakan Aspose.PDF untuk Java API, Anda dapat menandatangani file PDF menggunakan salah satu dari tiga jenis tanda tangan berikut:

- PKCS#1
- PKCS#7
- PKCS#7

Masing-masing tanda tangan yang disediakan berisi sekumpulan properti konfigurasi yang diimplementasikan untuk kenyamanan Anda (lokalisasi, format tanggal waktu, keluarga font, dll). Kelas SignatureCustomAppearance menyediakan fungsionalitas yang sesuai. Cuplikan kode berikut menunjukkan cara mengubah bahasa dalam teks tanda tangan digital:

```java
     public static void ChangeLanguageInDigitalSignText() {
        String inFile = _dataDir + "sample01.pdf";
        String outFile = _dataDir + "DigitallySign.pdf";

        PdfFileSignature pdfSign = new PdfFileSignature();

        pdfSign.bindPdf(inFile);
        // buat persegi panjang untuk lokasi tanda tangan
        java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);

        // buat salah satu dari tiga jenis tanda tangan
        PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021");
        pkcs.setReason("Pruebas Firma");
        pkcs.setContactInfo("Contacto Pruebas");
        pkcs.setLocation("Población (Provincia)");
        pkcs.setDate(new Date());
        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setDateSignedAtLabel("Fecha");
        signatureCustomAppearance.setDigitalSignedLabel("Digitalmente firmado por");
        signatureCustomAppearance.setReasonLabel("Razón");
        signatureCustomAppearance.setLocationLabel("Localización");
        signatureCustomAppearance.setFontFamilyName("Arial");
        signatureCustomAppearance.setFontSize(10);
        signatureCustomAppearance.setCulture(new Locale("es", "ES"));
        // signatureCustomAppearance.setCulture (Locale.ROOT);
        signatureCustomAppearance.setDateTimeFormat("yyyy.MM.dd HH:mm:ss");
        pkcs.setCustomAppearance(signatureCustomAppearance);
        // tandatangani file PDF
        pdfSign.sign(1, true, rect, pkcs);
        // simpan file PDF keluaran
        pdfSign.save(outFile);
    }
```