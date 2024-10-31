---
title: Mengonversi BMP ke PDF 
linktitle: Mengonversi BMP ke PDF
type: docs
weight: 220
url: /androidjava/convert-bmp-to-pdf/
lastmod: "2021-06-05"
description: Anda dapat dengan mudah mengonversi file bitmap BMP ke PDF yang digunakan untuk menyimpan gambar bitmap digital secara terpisah dari perangkat tampilan menggunakan Aspose.PDF untuk Android melalui Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Gambar BMP adalah file dengan ekstensi .BMP yang mewakili file Gambar Bitmap yang digunakan untuk menyimpan gambar digital bitmap. Gambar-gambar ini independen dari adapter grafis dan juga disebut format file bitmap independen perangkat (DIB).
Anda dapat mengonversi BMP ke PDF dengan API Aspose.PDF untuk Java. Oleh karena itu, Anda dapat mengikuti langkah-langkah berikut untuk mengonversi gambar BMP:

1. Inisialisasi Dokumen baru
1. Muat file gambar BMP contoh
1. Akhirnya, simpan file PDF keluaran

Jadi cuplikan kode berikut mengikuti langkah-langkah ini dan menunjukkan cara mengonversi BMP ke PDF menggunakan Java:

```java
public void convertBMPtoPDF () {
        // Inisialisasi objek dokumen
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.bmp");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Muat file gambar BMP contoh
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "BMP-to-PDF.pdf");

        // Simpan dokumen keluaran
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```