---
title: Ekstrak Gambar dari PDF 
linktitle: Ekstrak Gambar
type: docs
weight: 20
url: id/androidjava/extract-images-from-the-pdf-file/
description: Cara mengekstrak bagian dari gambar dari PDF menggunakan Aspose.PDF untuk Android via Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Setiap halaman dalam dokumen PDF mengandung sumber daya (gambar, formulir dan font). Kita dapat mengakses sumber daya ini dengan memanggil metode [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). Kelas [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) mengandung [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) dan kita dapat mendapatkan daftar gambar dengan memanggil metode [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Jadi untuk mengekstrak gambar dari halaman, kita perlu mendapatkan referensi ke halaman, kemudian ke sumber daya halaman dan terakhir ke koleksi gambar.

Gambar tertentu dapat kita ekstrak, misalnya dengan indeks.

The image's index returns an [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) object.  
Objek ini menyediakan metode [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) yang dapat digunakan untuk menyimpan gambar yang diekstraksi. Cuplikan kode berikut menunjukkan cara mengekstraksi gambar dari file PDF.

```java
public void extractImage () {
       // Buka dokumen
       try {
           document=new Document(inputStream);
       } catch (Exception e) {
           resultMessage.setText(e.getMessage());
           return;
       }

       com.aspose.pdf.Page page=document.getPages().get_Item(1);
       com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
       // Ekstrak gambar tertentu
       com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
       File file=new File(fileStorage, "extracted-image.jpeg");
       try {
           java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
           // Simpan gambar output
           xImage.save(outputImage, ImageType.getJpeg());
           outputImage.close();
       } catch (java.io.IOException e) {
           resultMessage.setText(e.getMessage());
           return;
       }
       resultMessage.
         }
```