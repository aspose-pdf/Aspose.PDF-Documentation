---
title: Ekstrak Gambar dari PDF
linktitle: Ekstrak Gambar
type: docs
weight: 20
url: /id/androidjava/extract-images-from-the-pdf-file/
description: Cara mengekstrak bagian gambar dari PDF menggunakan Aspose.PDF for Android via Java
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Setiap halaman dalam dokumen PDF berisi sumber daya (gambar, formulir, dan font). Kita dapat mengakses sumber daya ini dengan memanggil [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) metode. Kelas [Sumber daya](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) mengandung [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) dan kita dapat memperoleh daftar gambar dengan memanggil [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) metode.

Dengan demikian, untuk mengekstrak gambar dari halaman, kita perlu mendapatkan referensi ke halaman, selanjutnya ke sumber daya halaman, dan terakhir ke koleksi gambar.
Gambar tertentu yang dapat kita ekstrak, misalnya dengan indeks.

Indeks gambar mengembalikan sebuah [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) objek.
Objek ini menyediakan sebuah [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) metode yang dapat digunakan untuk menyimpan gambar yang diekstrak. Potongan kode berikut menunjukkan cara mengekstrak gambar dari file PDF.

 ```java
 public void extractImage () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.Page page=document.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
        // Extract a particular image
        com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
        File file=new File(fileStorage, "extracted-image.jpeg");
        try {
            java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
            // Save output image
            xImage.save(outputImage, ImageType.getJpeg());
            outputImage.close();
        } catch (java.io.IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.
          }
```

