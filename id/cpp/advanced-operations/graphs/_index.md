---
title: Bekerja dengan Grafik dalam PDF
linktitle: Bekerja dengan Grafik
type: docs
weight: 70
url: /id/cpp/graphs/
description: Artikel ini menjelaskan apa itu Grafik, bagaimana cara membuat objek persegi panjang yang terisi, bagaimana cara menambahkan teks di dalam objek grafik, bagaimana cara menambahkan objek garis ke PDF, dan lain-lain.
lastmod: "2021-12-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Apa itu Grafik

Menambahkan grafik ke dokumen PDF adalah tugas yang sangat umum bagi pengembang saat bekerja dengan Adobe Acrobat Writer atau aplikasi pemrosesan PDF lainnya. Ada banyak jenis grafik yang dapat digunakan dalam aplikasi PDF.
[Aspose.PDF untuk C++](/pdf/id/cpp/) juga mendukung penambahan grafik ke dokumen PDF. Untuk tujuan ini, kelas Graph disediakan. Grafik adalah elemen tingkat paragraf dan dapat ditambahkan ke koleksi Paragraf dalam suatu instansi Halaman. Sebuah instansi Grafik berisi koleksi Bentuk.

Jenis-jenis bentuk berikut didukung oleh kelas [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph):

- [Busur](/pdf/id/cpp/add-arc/) - kadang-kadang juga disebut bendera adalah pasangan berurutan dari simpul yang berdekatan, tetapi kadang-kadang juga disebut garis terarah.
- [Circle](/pdf/id/cpp/add-circle/) - menampilkan data menggunakan lingkaran yang dibagi menjadi sektor. Kami menggunakan grafik lingkaran (juga disebut diagram pai) untuk menunjukkan bagaimana data mewakili bagian dari satu keseluruhan atau satu kelompok.  
- [Curve](/pdf/id/cpp/add-curve/) - adalah gabungan terhubung dari garis-garis proyektif, setiap garis bertemu dengan tiga lainnya di titik-titik ganda biasa.  
- [Line](/pdf/id/cpp/add-line) - grafik garis digunakan untuk menampilkan data kontinu dan dapat berguna dalam memprediksi peristiwa di masa depan ketika mereka menunjukkan tren seiring waktu.  
- [Rectangle](/pdf/id/cpp/add-rectangle/) - adalah salah satu dari banyak bentuk dasar yang akan Anda lihat dalam grafik, dapat sangat berguna dalam membantu Anda menyelesaikan masalah.  
- [Ellipse](/pdf/id/cpp/add-ellipse/) - adalah sekumpulan titik pada bidang, membentuk bentuk oval melengkung.  

Detail di atas juga digambarkan dalam gambar di bawah ini:

![Figures in Graphs](graph.png)