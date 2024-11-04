---
title: Konversi JPG ke PDF 
linktitle: Konversi JPG ke PDF 
type: docs
weight: 190
url: /androidjava/convert-jpg-to-pdf/
lastmod: "2021-06-05"
description: Pelajari cara mudah mengonversi gambar JPG ke file PDF. Juga, Anda dapat mengonversi gambar ke PDF dengan tinggi dan lebar halaman yang sama.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Tidak perlu bertanya-tanya bagaimana cara mengonversi JPG ke PDF, karena Apose.PDF untuk Android melalui pustaka Java memiliki solusi terbaik.

Anda dapat dengan sangat mudah mengonversi gambar JPG ke PDF dengan Aspose.PDF untuk Android melalui Java dengan mengikuti langkah-langkah berikut:

1. Inisialisasi objek dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Muat gambar JPG dan tambahkan ke paragraf
1. Simpan PDF keluaran

Cuplikan kode di bawah ini menunjukkan cara mengonversi Gambar JPG ke PDF:

```java
public void convertJPEGtoPDF () {
        // Inisialisasi objek dokumen
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.jpg");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Muat file gambar JPEG contoh
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

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