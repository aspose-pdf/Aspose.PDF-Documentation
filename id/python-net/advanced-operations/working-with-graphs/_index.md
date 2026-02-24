---
title: Bekerja dengan Grafik di PDF menggunakan Python
linktitle: Bekerja dengan Grafik
type: docs
weight: 70
url: /id/python-net/working-with-graphs/
description: Artikel ini menjelaskan apa itu Graf, cara membuat objek persegi panjang terisi, dan fungsi lainnya
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan Grafik ke PDF menggunakan Python
Abstract: Artikel ini membahas integrasi grafik ke dalam dokumen PDF, sebuah kebutuhan umum bagi pengembang yang menggunakan Adobe Acrobat Writer atau alat pemrosesan PDF serupa. Artikel ini memperkenalkan kelas Graph dalam Aspose.PDF for Python via .NET, yang mempermudah tugas ini dengan memungkinkan penambahan berbagai jenis bentuk ke dokumen PDF. Kelas Graph adalah elemen tingkat paragraf yang dapat ditambahkan ke koleksi Paragraphs dalam sebuah instance Page dan mendukung kumpulan bentuk, termasuk Arc, Circle, Curve, Line, Rectangle, dan Ellipse. Setiap bentuk memiliki tujuan unik, seperti Arc yang mewakili kedekatan, Circle yang menggambarkan bagian data, Curve yang menggambarkan garis terhubung, Line yang menampilkan tren data kontinu, Rectangle yang menyelesaikan masalah spasial, dan Ellipse yang membentuk bentuk oval. Artikel ini juga menyediakan representasi visual dari bentuk-bentuk tersebut untuk membantu pemahaman.
---

## Apa itu Graf

Menambahkan grafik ke dokumen PDF adalah tugas yang sangat umum bagi pengembang saat bekerja dengan Adobe Acrobat Writer atau aplikasi pemrosesan PDF lainnya. Ada banyak jenis grafik yang dapat digunakan dalam aplikasi PDF.
[Aspose.PDF for Python via .NET](/pdf/python-net/) juga mendukung penambahan grafik ke dokumen PDF. Untuk tujuan ini, kelas Graph disediakan. Graph adalah elemen tingkat paragraf dan dapat ditambahkan ke koleksi Paragraphs dalam sebuah instance Page. Sebuah instance Graph berisi kumpulan Shapes.

Jenis-jenis bentuk berikut didukung oleh kelas [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/):

- [Arc](/pdf/python-net/add-arc/) - kadang disebut flag, merupakan pasangan terurut dari vertex berdekatan, tetapi kadang juga disebut garis berarah.
- [Circle](/pdf/python-net/add-circle/) - menampilkan data menggunakan lingkaran yang dibagi menjadi sektor. Kami menggunakan grafik lingkaran (juga disebut diagram lingkaran) untuk menunjukkan bagaimana data mewakili bagian dari satu keseluruhan atau satu grup.
- [Curve](/pdf/python-net/add-curve/) - adalah gabungan terhubung dari garis proyektif, setiap garis bertemu tiga lainnya pada titik ganda biasa.
- [Line](/pdf/python-net/add-line) - grafik garis digunakan untuk menampilkan data kontinu dan dapat berguna dalam memprediksi peristiwa masa depan ketika mereka menunjukkan tren seiring waktu.
- [Rectangle](/pdf/python-net/add-rectangle/) - adalah salah satu dari banyak bentuk dasar yang akan Anda temui dalam grafik, sangat berguna untuk membantu Anda menyelesaikan suatu masalah.
- [Ellipse](/pdf/python-net/add-ellipse/) - adalah sekumpulan titik pada bidang, membentuk bentuk oval yang melengkung.

Detail di atas juga ditampilkan dalam gambar di bawah ini:

![Gambar dalam Grafik](graphs.png)


