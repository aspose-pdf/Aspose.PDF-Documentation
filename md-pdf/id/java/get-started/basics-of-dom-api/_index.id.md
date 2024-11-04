---
title: Dasar-dasar Aspose.PDF DOM API
linktitle: Dasar-dasar DOM API
type: docs
weight: 110
url: /java/basics-of-dom-api/
description: Aspose.PDF untuk Java juga menggunakan konsep DOM untuk merepresentasikan struktur dokumen PDF dalam bentuk objek. Di sini Anda dapat membaca deskripsi struktur ini.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Pengenalan API DOM

Document Object Model (DOM) adalah bentuk representasi dokumen terstruktur sebagai model berorientasi objek. DOM adalah standar resmi World Wide Web Consortium (W3C) untuk merepresentasikan dokumen terstruktur dengan cara yang netral terhadap platform dan bahasa.

Dengan kata sederhana, DOM adalah pohon objek yang merepresentasikan struktur dari suatu dokumen.
 Aspose.PDF untuk Java juga menggunakan ide DOM untuk merepresentasikan struktur dokumen PDF dalam bentuk objek. Namun, aspek-aspek dari DOM (seperti Elemen-elemen) dimanipulasi dalam sintaks bahasa pemrograman yang digunakan. Antarmuka publik dari DOM ditentukan dalam antarmuka pemrograman aplikasinya (API).

### Pengenalan ke Dokumen PDF

Portable Document Format (PDF) adalah standar terbuka untuk pertukaran dokumen. Dokumen PDF adalah kombinasi data teks dan biner. Jika Anda membukanya di editor teks, Anda akan melihat objek mentah yang mendefinisikan struktur dan konten dari dokumen tersebut.

Struktur logis dari file PDF bersifat hierarkis dan menentukan urutan di mana aplikasi penampil menggambar halaman dokumen dan isinya. Sebuah PDF terdiri dari empat komponen: objek, struktur file, struktur dokumen, dan aliran konten.

### Struktur Dokumen PDF

Karena struktur file PDF bersifat hierarkis, Aspose.PDF untuk Java juga mengakses elemen-elemen dengan cara yang sama. Hierarki berikut menunjukkan kepada Anda bagaimana dokumen PDF disusun secara logis dan bagaimana Aspose.PDF untuk Java DOM API membangunnya.

![Struktur Dokumen PDF](../images/structure.png)

### Mengakses Elemen Dokumen PDF

Objek Dokumen berada pada tingkat akar dari model objek. Aspose.PDF untuk Java DOM API memungkinkan Anda untuk membuat objek Dokumen dan kemudian mengakses semua objek lain dalam hierarki. Anda dapat mengakses salah satu koleksi seperti Pages atau elemen individu seperti Page, dll. DOM API menyediakan titik masuk dan keluar tunggal untuk memanipulasi dokumen PDF seperti yang ditunjukkan di bawah ini:

- Buka dokumen PDF
- Akses struktur dokumen PDF dalam gaya DOM
- Perbarui data dalam dokumen PDF
- Validasi dokumen PDF
- Ekspor dokumen PDF ke dalam format berbeda
- Akhirnya, simpan dokumen PDF yang telah diperbarui

## Cara Menggunakan Aspose.PDF Baru untuk Java API

Topik ini akan menjelaskan Aspose.PDF baru untuk Java API dan membimbing Anda untuk memulai dengan cepat dan mudah. Harap dicatat bahwa rincian mengenai penggunaan fitur tertentu bukan bagian dari artikel ini.

Aspose.PDF untuk Java terdiri dari dua bagian:

- Aspose.PDF untuk Java DOM API
- Aspose.PDF.Facades

Anda akan menemukan rincian dari masing-masing area ini di bawah.

### Aspose.PDF untuk Java DOM API

Aspose.PDF untuk Java DOM API yang baru sesuai dengan struktur dokumen PDF, yang membantu Anda bekerja dengan dokumen PDF tidak hanya pada tingkat file dan dokumen, tetapi juga pada tingkat objek. Kami telah memberikan lebih banyak fleksibilitas kepada pengembang untuk mengakses semua elemen dan objek dari dokumen PDF. Dengan menggunakan kelas-kelas dari Aspose.PDF DOM API, Anda dapat memperoleh akses program ke elemen dan pemformatan dokumen. DOM API baru ini terdiri dari berbagai namespace seperti yang diberikan di bawah ini:

### com.aspose.pdf

Namespace ini menyediakan kelas Document yang memungkinkan Anda untuk membuka dan menyimpan dokumen PDF. Kelas License juga merupakan bagian dari namespace ini. Ini juga menyediakan kelas yang terkait dengan halaman PDF, lampiran, dan penanda seperti com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, dan com.aspose.pdf.OutlineCollection dll.

#### com.aspose.pdf.text

Namespace ini menyediakan kelas yang membantu Anda bekerja dengan teks dan berbagai aspeknya, misalnya com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment dan com.aspose.pdf.TextSegmentCollection dll.

#### com.aspose.pdf.TextOptions

Namespace ini menyediakan kelas yang memungkinkan Anda untuk mengatur opsi berbeda untuk mencari, mengedit, atau mengganti teks, misalnya com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions, dan com.aspose.pdf.TextSearchOptions.
#### com.aspose.pdf.PdfAction

Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan fitur interaktif dari dokumen PDF, misalnya bekerja dengan dokumen dan tindakan lainnya. Namespace ini berisi kelas-kelas seperti com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction dan com.aspose.pdf.GoToURIAction dll.

#### com.aspose.pdf.Annotation

Annotasi adalah bagian dari fitur interaktif dokumen PDF. Kami telah mendedikasikan sebuah namespace untuk anotasi. Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan anotasi, misalnya, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation dan com.aspose.pdf.LinkAnnotation dll.

#### com.aspose.pdf.Form

Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan formulir PDF dan field formulir, misalnya com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField dan com.aspose.pdf.OptionCollection dll.

#### com.aspose.pdf.devices 

Kami dapat melakukan berbagai operasi pada dokumen PDF seperti mengonversi dokumen PDF ke berbagai format gambar.
 Namun, operasi semacam itu tidak termasuk dalam objek Dokumen dan kita tidak dapat memperluas kelas Dokumen untuk operasi semacam itu. Itu sebabnya kami telah memperkenalkan konsep Perangkat dalam API DOM yang baru.

##### com.aspose.pdf.facades

Sebelumnya untuk Aspose.PDF untuk Java t.o.o, Anda memerlukan Aspose.PDF.Kit untuk Java untuk memanipulasi file PDF yang ada. Untuk menjalankan kode Aspose.PDF.Kit lama, dapat menggunakan namespace com.aspose.pdf.facades.