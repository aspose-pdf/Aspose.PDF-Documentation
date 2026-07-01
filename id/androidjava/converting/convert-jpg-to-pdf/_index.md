---
title: Konversi JPG ke PDF
linktitle: Konversi JPG ke PDF
type: docs
weight: 190
url: /id/androidjava/convert-jpg-to-pdf/
lastmod: "2026-07-01"
description: Pelajari cara mudah mengonversi gambar JPG ke file PDF. Selain itu, Anda dapat mengonversi gambar ke PDF dengan tinggi dan lebar halaman yang sama.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Tidak perlu bertanya-tanya bagaimana mengonversi JPG ke PDF, karena pustaka Apose.PDF for Android via Java adalah keputusan terbaik.

Anda dapat dengan sangat mudah mengonversi gambar JPG ke PDF dengan Aspose.PDF for Android via Java dengan mengikuti langkah-langkah berikut:

1. Inisialisasi objek dari [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) kelas
1. Muat gambar JPG dan tambahkan ke paragraf
1. Simpan PDF output

Potongan kode di bawah ini menunjukkan cara mengonversi Gambar JPG ke PDF:

```java
public void convertJPEGtoPDF () {
        // Initialize document object
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

        // Load sample JPEG image file
        image.setImageStream(inputStream);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "JPEG-to-PDF.pdf");

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
