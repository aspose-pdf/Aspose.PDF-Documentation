---
title: Extract Chart objects from PDF document (facades)
type: docs
weight: 20
url: /id/java/extract-chart-objects/
description: Bagian ini menjelaskan cara mengekstrak objek grafik dari PDF dengan Aspose.PDF Facades menggunakan Kelas PdfExtractor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract Chart objects from PDF document (facades)

PDF memungkinkan untuk mengelompokkan konten halaman ke dalam elemen yang disebut **Marked Content**. Adobe Acrobat menampilkannya sebagai "wadah". Objek Grafik ditempatkan dalam objek semacam itu. Kami telah memperkenalkan metode baru extractMarkedContentAsImages() dalam kelas PdfExtractor untuk mengekstrak objek-objek ini. Metode ini merender setiap **Marked Content** menjadi gambar terpisah. Harap dicatat bahwa semua grafik tidak sepenuhnya ditempatkan ke dalam satu wadah. Karena itu, beberapa grafik akan disimpan ke dalam gambar terpisah berdasarkan bagian.

Harap dicatat bahwa pengelompokan konten yang benar ke dalam wadah adalah tanggung jawab perancang dokumen PDF.
 Jika Anda ingin mendapatkan grafik dengan header atau objek lainnya, Anda harus mengedit/membuat dokumen PDF di mana seluruh grafik ditempatkan dalam satu wadah.

```java

 //Buka dokumen

Document document = new Document("sample.pdf");

//instansiasi PdfExtractor

PdfExtractor pdfExtractor = new PdfExtractor();

//Ekstrak objek Grafik sebagai gambar di folder

pdfExtractor.extractMarkedContentAsImages(document.getPages().get_Item(1), "C:/Temp/Charts_page_1");

document.close();
```