---
title: Mengatur informasi file PDF - fasad
type: docs
weight: 20
url: id/java/set-pdf-information/
description: Bagian ini menjelaskan cara mengatur informasi file PDF dengan Aspose.PDF Facades menggunakan Kelas PdfFileInfo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Kelas [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) memungkinkan Anda mengatur informasi khusus file dari dokumen PDF. Anda perlu membuat objek dari kelas [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) dan kemudian menetapkan berbagai properti khusus file seperti Penulis, Judul, Kata Kunci, dan Pembuat, dll. Terakhir, simpan file PDF yang diperbarui menggunakan metode [saveNewInfo(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#saveNewInfo-java.io.OutputStream-) dari objek [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo).

Cuplikan kode berikut menunjukkan cara mengatur informasi file PDF.

```java
 public static void SetPdfInfo()
    {
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // Mengatur informasi PDF
        fileInfo.setAuthor("Aspose");
        fileInfo.setTitle ("Hello World!");
        fileInfo.setKeywords("Peace and Development");
        fileInfo.setCreator ("Aspose");
        
        // Simpan file yang diperbarui
        fileInfo.saveNewInfo(_dataDir + "SetfileInfo_out.pdf");
    }
```


## Setel Info Meta

[setMetaInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#setMetaInfo-java.lang.String-java.lang.String-) metode memungkinkan Anda untuk menambahkan informasi apapun. Dalam contoh kami, kami menambahkan sebuah bidang. Periksa cuplikan kode berikut:

```java
   public static void SetMetaInfo()
    {
        // Buat instance dari objek PdffileInfo
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "sample.pdf");
       
        // Tetapkan atribut pelanggan baru sebagai info meta
        fInfo.setMetaInfo("Reviewer", "Pengguna Aspose.PDF");

        // Simpan file yang diperbarui
        fInfo.saveNewInfo(_dataDir + "SetMetaInfo_out.pdf");

    }
```