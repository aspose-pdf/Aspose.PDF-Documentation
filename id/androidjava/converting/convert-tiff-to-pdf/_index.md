---
title: Konversi TIFF ke PDF
linktitle: Konversi TIFF ke PDF
type: docs
weight: 210
url: /id/androidjava/convert-tiff-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java memungkinkan mengonversi gambar TIFF multi-halaman atau multi-frame ke aplikasi PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** format file didukung, baik itu satu frame maupun multi-frame <abbr title="Tag Image File Format">TIFF</abbr> gambar. Itu berarti Anda dapat mengonversi gambar TIFF ke PDF dalam aplikasi Java Anda.

TIFF atau TIF, Tagged Image File Format, mewakili gambar raster yang dimaksudkan untuk penggunaan pada berbagai perangkat yang mematuhi standar format file ini. Gambar TIFF dapat berisi beberapa frame dengan gambar yang berbeda. Format file Aspose.PDF juga didukung, baik itu frame tunggal maupun TIFF multi-frame. Jadi Anda dapat mengonversi gambar TIFF ke PDF dalam aplikasi Java Anda. Oleh karena itu, kami akan mempertimbangkan contoh mengonversi gambar TIFF multi-halaman ke dokumen PDF multi-halaman dengan langkah-langkah berikut:

1. Instansiasi sebuah instance dari kelas Document
1. Muat gambar TIFF input
1. Dapatkan FrameDimension dari frame-frame
1. Tambah halaman baru untuk setiap frame
1. Akhirnya, simpan gambar ke halaman PDF

Selain itu, potongan kode berikut menunjukkan cara mengonversi gambar TIFF multi-halaman atau multi-frame ke PDF:

```java
 public void convertTIFFtoPDF () {
        // Initialize document object
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

        // Load sample TIFF image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "TIFF-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

