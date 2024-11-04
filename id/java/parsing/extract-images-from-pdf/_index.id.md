---
title: Ekstrak Gambar dari PDF 
linktitle: Ekstrak Gambar
type: docs
weight: 20
url: /java/extract-images-from-the-pdf-file/
description: Cara mengekstrak bagian gambar dari PDF menggunakan Aspose.PDF untuk Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Setiap halaman dalam dokumen PDF mengandung sumber daya (gambar, formulir, dan font). Kita dapat mengakses sumber daya ini dengan memanggil metode [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). Kelas [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) mengandung [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) dan kita dapat mendapatkan daftar gambar dengan memanggil metode [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Jadi untuk mengekstrak gambar dari halaman, kita perlu mendapatkan referensi ke halaman, kemudian ke sumber daya halaman, dan terakhir ke koleksi gambar. 

Gambar tertentu dapat kita ekstrak misalnya dengan indeks.


Indeks gambar mengembalikan objek [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
This object menyediakan metode [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) yang dapat digunakan untuk menyimpan gambar yang diekstraksi. Cuplikan kode berikut menunjukkan cara mengekstrak gambar dari file PDF.

```java
public static void Extract_Images(){
        // Jalur ke direktori dokumen.
        String _dataDir = "/home/admin1/pdf-examples/Samples/";
        String filePath = _dataDir + "ExtractImages.pdf";

        // Memuat dokumen PDF
        com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

        com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection = page.getResources().getImages();
        // Mengekstrak gambar tertentu
        com.aspose.pdf.XImage xImage = xImageCollection.get_Item(1);

        try {
            java.io.FileOutputStream outputImage = new java.io.FileOutputStream(_dataDir + "output.jpg");
            // Menyimpan gambar keluaran
            xImage.save(outputImage);
            outputImage.close();
        } catch (java.io.FileNotFoundException e) {
            // TODO: menangani pengecualian
            e.printStackTrace();
        } catch (java.io.IOException e) {
            // TODO: menangani pengecualian
            e.printStackTrace();
        }
    }
```