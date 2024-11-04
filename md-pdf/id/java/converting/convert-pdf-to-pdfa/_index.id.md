---
title: Convert PDF ke format PDF/A
linktitle: Convert PDF ke format PDF/A
type: docs
weight: 100
url: /java/convert-pdf-to-pdfa/
lastmod: "2021-11-19"
description: Topik ini menunjukkan kepada Anda bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF ke file PDF yang sesuai dengan PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF untuk Java** memungkinkan Anda untuk mengonversi file PDF ke file PDF yang sesuai dengan PDF/A. Sebelum melakukan itu, file harus divalidasi. Artikel ini menjelaskan caranya.

Harap dicatat bahwa kami mengikuti Adobe Preflight untuk memvalidasi kepatuhan PDF/A. Semua alat di pasaran memiliki "representasi" mereka sendiri tentang kepatuhan PDF/A. Silakan periksa artikel ini tentang [alat validasi PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) sebagai referensi. Kami memilih produk Adobe untuk memverifikasi bagaimana Aspose.PDF menghasilkan file PDF karena Adobe berada di pusat segala sesuatu yang berhubungan dengan PDF.

Sebelum mengonversi PDF ke file yang sesuai dengan PDF/A, validasi PDF menggunakan metode validasi.
 Hasil validasi disimpan dalam file XML dan kemudian hasil ini juga diteruskan ke metode konversi. Anda juga dapat menentukan tindakan untuk elemen yang tidak dapat dikonversi menggunakan enumerasi [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

## Konversi PDF ke PDF/A_1b

Cuplikan kode berikut menunjukkan cara mengonversi file PDF ke PDF yang sesuai dengan PDF/A-1b.

```java
// Buka dokumen
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Konversi ke dokumen yang sesuai dengan PDF/A
// Selama proses konversi, validasi juga dilakukan
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

// Simpan dokumen keluaran
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

Untuk melakukan validasi saja, gunakan baris kode berikut:

```java
// Buka dokumen
Document document = new Document(DATA_DIR + "ValidatePDFAStandard.pdf");

// Validasi PDF untuk PDF/A-1a
if (document.validate(DATA_DIR + "validation-result-A1A.xml", PdfFormat.PDF_A_1B)) {
    System.out.println("Valid");
} else {
    System.out.println("Tidak valid");
}
document.close();
```

## Konversi PDF ke PDF/A_3b

Dari [Aspose.PDF for Java 9.3.0](https://downloads.aspose.com/pdf/java), API juga mendukung konversi file PDF ke format PDF/A_3b.

```java
// Buka dokumen
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Konversi ke dokumen yang sesuai dengan PDF/A
// Selama proses konversi, validasi juga dilakukan
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

// Simpan dokumen keluaran
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

## Konversi PDF ke PDF/A_3a

Dari [Aspose.PDF for Java 10.6.0](https://downloads.aspose.com/pdf/java), API juga mendukung konversi file PDF ke format PDF/A_3a.

```java
// Buka dokumen
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Konversi ke dokumen yang sesuai dengan PDF/A
// Selama proses konversi, validasi juga dilakukan
document.convert("file.log", PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

// Simpan dokumen keluaran
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```


## Konversi PDF ke PDF/A_2a

Mulai rilis [Aspose.PDF for Java 10.2.0](https://downloads.aspose.com/pdf/java), API menawarkan fitur untuk mengonversi file PDF ke format PDF/A3.

```java
    public static void ConvertPDFtoPDFa2a() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Konversi ke dokumen yang sesuai dengan PDF/A
        // Selama proses konversi, validasi juga dilakukan
        pdfDocument.convert("file.log", PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Simpan dokumen keluaran
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## Konversi PDF ke PDF/A_3U

Mulai rilis Aspose.PDF for Java 17.2.0, API menawarkan fitur untuk mengonversi file PDF ke format PDF/A_3U.

```java
    public static void ConvertPDFtoPDFa3u() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Konversi ke dokumen yang sesuai dengan PDF/A
        // Selama proses konversi, validasi juga dilakukan
        pdfDocument.convert("file.log", PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Simpan dokumen keluaran
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```


## Buat PDF/A-3 dan lampirkan file XML

Aspose.PDF untuk Java menawarkan fitur untuk mengonversi file PDF ke format PDF/A dan juga mendukung kemampuan menambahkan file sebagai lampiran ke dokumen PDF. Jika Anda memiliki persyaratan untuk melampirkan file ke format kepatuhan PDF/A, maka kami merekomendasikan menggunakan nilai PDF_A_3A dari enumerasi com.aspose.pdf.PdfFormat, PDF/A_3a adalah format yang menyediakan fitur untuk melampirkan format file apa pun sebagai lampiran ke file yang sesuai dengan PDF/A. Namun, setelah file dilampirkan, Anda harus mengonversinya kembali ke format Pdf-3a, untuk memperbaiki metadata. Silakan lihat potongan kode berikut.

```java
    public static void ConvertPDFtoPDFa3u_attachXML() {
        Document doc = new Document();
        // tambahkan halaman ke file PDF
        doc.getPages().add();
        // muat file XML
        FileSpecification fileSpecification = new FileSpecification(_dataDir + "attachment.xml", "Contoh file xml");
        // Tambahkan lampiran ke koleksi lampiran dokumen
        doc.getEmbeddedFiles().add(fileSpecification);
        // lakukan konversi PDF/A_3a
        doc.convert(_dataDir + "log.xml", PdfFormat.PDF_A_3A/* atau PDF_A_3B */, ConvertErrorAction.Delete);
        // simpan file PDF akhir
        doc.save(_dataDir + "attached_PDFA_3A.pdf");
    }
```


{{% alert color="primary" %}}
**Cobalah mengonversi PDF ke PDF/A secara online**

Aspose.PDF untuk Java menghadirkan aplikasi gratis online ["PDF ke PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF PDF ke PDF/A dengan Aplikasi Gratis](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}