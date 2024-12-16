---
title: Convert TIFF to PDF 
linktitle: Convert TIFF to PDF
type: docs
weight: 210
url: /id/androidjava/convert-tiff-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF untuk Android melalui Java memungkinkan mengonversi gambar TIFF multi-halaman atau multi-frame ke aplikasi PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF untuk Android melalui Java** mendukung format file, baik itu gambar <abbr title="Tag Image File Format">TIFF</abbr> frame tunggal atau multi-frame. Ini berarti bahwa Anda dapat mengonversi gambar TIFF ke PDF dalam aplikasi Java Anda.

TIFF atau TIF, Tagged Image File Format, mewakili gambar raster yang dimaksudkan untuk digunakan pada berbagai perangkat yang sesuai dengan standar format file ini.
 TIFF gambar dapat berisi beberapa frame dengan gambar yang berbeda. Format file Aspose.PDF juga didukung, baik itu gambar TIFF dengan satu frame atau multi-frame. Jadi, Anda dapat mengonversi gambar TIFF ke PDF dalam aplikasi Java Anda. Oleh karena itu, kita akan mempertimbangkan contoh konversi gambar TIFF multi-halaman ke dokumen PDF multi-halaman dengan langkah-langkah di bawah ini:

1. Membuat instance dari kelas Document
1. Memuat gambar TIFF input
1. Mendapatkan FrameDimension dari frame
1. Menambahkan halaman baru untuk setiap frame
1. Akhirnya, menyimpan gambar ke halaman PDF

Selain itu, cuplikan kode berikut menunjukkan cara mengonversi gambar TIFF multi-halaman atau multi-frame ke PDF:

```java
 public void convertTIFFtoPDF () {
        // Inisialisasi objek dokumen
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.tiff");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Memuat file gambar TIFF sampel
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

        // Menyimpan dokumen output
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```