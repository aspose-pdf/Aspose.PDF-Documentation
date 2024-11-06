---
title: Bekerja dengan Metadata File PDF
linktitle: Metadata File PDF
type: docs
weight: 140
url: id/java/pdf-file-metadata/
description: Bagian ini menjelaskan bagaimana mendapatkan informasi file PDF, bagaimana mendapatkan Metadata XMP dari file PDF, mengatur Informasi File PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mendapatkan Informasi File PDF

Untuk mendapatkan informasi spesifik file tentang file PDF, pertama dapatkan objek [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). Setelah objek [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) diperoleh, Anda dapat mendapatkan nilai dari properti individual.

Cuplikan kode berikut menunjukkan cara mengatur informasi file PDF.

```java
public class ExampleMetadata {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Metadata/";

    public static void GetPDFFileInformation() {
        // Buat dokumen PDF baru
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
        // Dapatkan informasi dokumen
        DocumentInfo docInfo = pdfDocument.getInfo();
        // Tampilkan informasi dokumen
        System.out.println("Penulis: " + docInfo.getAuthor());
        System.out.println("Tanggal Pembuatan: " + docInfo.getCreationDate());
        System.out.println("Kata Kunci: " + docInfo.getKeywords());
        System.out.println("Tanggal Modifikasi: " + docInfo.getModDate());
        System.out.println("Subjek: " + docInfo.getSubject());
        System.out.println("Judul: " + docInfo.getTitle());
    }
```


## Mengatur Informasi File PDF

Aspose.PDF untuk Java memungkinkan Anda untuk mengatur informasi spesifik file untuk PDF, informasi seperti penulis, tanggal pembuatan, subjek, dan judul.

Untuk mengatur informasi ini:

1. Buat objek [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo).
1. Atur nilai dari properti.
1. Simpan dokumen yang diperbarui menggunakan metode [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

{{% alert color="primary" %}}

Harap dicatat bahwa Anda tidak dapat mengatur nilai untuk kolom **Producer** dan **Creator**, karena Aspose.PDF untuk Java x.x.x akan ditampilkan pada kolom ini.

{{% /alert %}}

Cuplikan kode berikut menunjukkan cara mengatur informasi file PDF.

```java
 public static void SetPDFFileInformation() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Tentukan informasi dokumen
        DocumentInfo docInfo = new DocumentInfo(pdfDocument);

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(new java.util.Date());
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(new java.util.Date());
        docInfo.setSubject("Informasi PDF");
        docInfo.setTitle("Mengatur Informasi Dokumen PDF");

        // Simpan dokumen keluaran
        pdfDocument.save(_dataDir + "SetFileInfo_out.pdf");
    }
```


## Mendapatkan Metadata XMP dari File PDF

Aspose.PDF untuk Java memungkinkan Anda mengakses metadata XMP file PDF.

Untuk mendapatkan metadata file PDF,

1. Buat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan buka file PDF input.
1. Gunakan properti [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) untuk mendapatkan metadata.

Cuplikan kode berikut menunjukkan cara mendapatkan metadata dari file PDF.

```java
   public static void GetXMPMetadata() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");

        System.out.println("xmp:CreateDate: " + pdfDocument.getMetadata().get_Item("xmp:CreateDate"));
        System.out.println("xmp:Nickname: " + pdfDocument.getMetadata().get_Item("xmp:Nickname"));
        System.out.println("xmp:CustomProperty: " + pdfDocument.getMetadata().get_Item("xmp:CustomProperty"));

    }
```

## Menetapkan Metadata XMP dalam File PDF

Aspose.PDF untuk Java memungkinkan Anda menetapkan metadata dalam file PDF.
 Untuk menetapkan metadata:

1. Buat objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Tetapkan nilai metadata menggunakan properti [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--).
1. Simpan dokumen yang diperbarui menggunakan metode [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Cuplikan kode berikut menunjukkan cara menetapkan metadata dalam file PDF.

```java
    public static void SetXMPMetadata() {

        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Tetapkan properti
        pdfDocument.getMetadata().set_Item("xmp:CreateDate", new XmpValue(new java.util.Date()));
        pdfDocument.getMetadata().set_Item("xmp:Nickname", new XmpValue("Nickname"));
        pdfDocument.getMetadata().set_Item("xmp:CustomProperty", new XmpValue("Custom Value"));

        // Simpan dokumen
        pdfDocument.save(_dataDir + "SetXMPMetadata.pdf");
    }
```

## Sisipkan Metadata dengan Prefix

Beberapa pengembang perlu membuat namespace metadata baru dengan prefix. Cuplikan kode berikut menunjukkan cara menyisipkan metadata dengan prefix.

```java
    public static void InsertMetadataWithPrefix() {
        // Buka dokumen
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");
        pdfDocument.getMetadata().registerNamespaceUri("adc", "http://tempuri.org/adc/1.0");
        pdfDocument.getMetadata().set_Item("adc:format", new XmpValue("application/pdf"));
        pdfDocument.getMetadata().set_Item("adc:title", new XmpValue("judul alternatif"));        
        // Simpan dokumen
        pdfDocument.save(_dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```