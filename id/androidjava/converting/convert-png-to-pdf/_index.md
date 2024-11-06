---
title: Konversi PNG ke PDF 
linktitle: Konversi PNG ke PDF
type: docs
weight: 200
url: id/androidjava/convert-png-to-pdf/
lastmod: "2021-06-05"
description: Artikel ini menunjukkan cara mengonversi PNG ke PDF dengan pustaka Aspose.PDF di aplikasi Android Anda melalui Java. Anda dapat mengonversi gambar PNG ke format PDF menggunakan langkah-langkah sederhana. 
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF untuk Android melalui Java** mendukung fitur untuk mengonversi gambar PNG ke format PDF. Periksa cuplikan kode berikut untuk menyelesaikan tugas Anda.

<abbr title="Portable Network Graphics">PNG</abbr> mengacu pada jenis format file gambar raster yang menggunakan kompresi tanpa kehilangan, yang membuatnya populer di kalangan penggunanya.

Anda dapat mengonversi gambar PNG ke PDF menggunakan langkah-langkah berikut:

1. Muat gambar PNG input
1. Baca nilai tinggi dan lebar
1. Buat dokumen baru dan tambahkan Halaman
1. Atur dimensi halaman
1. Simpan file keluaran

Selain itu, cuplikan kode di bawah ini menunjukkan cara mengonversi PNG ke PDF di aplikasi Java Anda:

```java
    public void convertPNGtoPDF () {
        // Inisialisasi objek dokumen
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.png");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
```