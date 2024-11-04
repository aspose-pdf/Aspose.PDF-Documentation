---
title: Dasar-dasar API Aspose.PDF DOM
linktitle: Dasar-dasar API DOM
type: docs
weight: 10
url: /androidjava/basics-of-dom-api/
description: Aspose.PDF untuk Android melalui Java juga menggunakan ide DOM untuk merepresentasikan struktur dokumen PDF dalam bentuk objek. Di sini Anda dapat membaca deskripsi struktur ini.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Pengantar API DOM

Document Object Model (DOM) adalah bentuk representasi dokumen terstruktur sebagai model berorientasi objek. DOM adalah standar resmi World Wide Web Consortium (W3C) untuk merepresentasikan dokumen terstruktur dengan cara yang netral terhadap platform dan bahasa.

Dalam kata sederhana, DOM adalah pohon objek yang merepresentasikan struktur dari beberapa dokumen.
 Aspose.PDF untuk Android melalui Java juga menggunakan ide DOM untuk merepresentasikan struktur dokumen PDF dalam bentuk objek. Namun, aspek-aspek DOM (seperti Elemennya) dimanipulasi dalam sintaksis bahasa pemrograman yang digunakan. Antarmuka publik dari DOM ditentukan dalam antarmuka pemrograman aplikasi (API) nya.

### Pengenalan ke Dokumen PDF

Portable Document Format (PDF) adalah standar terbuka untuk pertukaran dokumen. Dokumen PDF adalah kombinasi dari teks dan data biner. Jika Anda membukanya dalam editor teks, Anda akan melihat objek mentah yang mendefinisikan struktur dan isi dokumen.

Struktur logis dari file PDF bersifat hierarkis dan menentukan urutan di mana aplikasi tampilan menggambar halaman dokumen dan isinya. Sebuah PDF terdiri dari empat komponen: objek, struktur file, struktur dokumen dan aliran konten.

### Struktur Dokumen PDF

Karena struktur file PDF bersifat hierarkis, Aspose.PDF untuk Java juga mengakses elemen-elemen dengan cara yang sama. Hierarki berikut menunjukkan kepada Anda bagaimana dokumen PDF disusun secara logis dan bagaimana Aspose.PDF untuk Java DOM API membangunnya.

![Struktur Dokumen PDF](https://docs.aspose.com/pdf/java/images/structure.png)

### Mengakses Elemen Dokumen PDF

Objek Dokumen berada di tingkat akar dari model objek. Aspose.PDF untuk Android melalui Java DOM API memungkinkan Anda untuk membuat objek Dokumen dan kemudian mengakses semua objek lain dalam hierarki. Anda dapat mengakses salah satu koleksi seperti Halaman atau elemen individu seperti Halaman, dll. DOM API menyediakan titik masuk dan keluar tunggal untuk memanipulasi dokumen PDF seperti yang ditunjukkan di bawah ini:

- Buka dokumen PDF
- Akses struktur dokumen PDF dalam gaya DOM
- Perbarui data dalam dokumen PDF
- Validasi dokumen PDF
- Ekspor dokumen PDF ke dalam berbagai format
- Akhirnya, simpan dokumen PDF yang diperbarui

## Cara Menggunakan Aspose.PDF Baru untuk Android melalui Java API

Topik ini akan menjelaskan Aspose.PDF baru untuk Android melalui Java API dan membimbing Anda untuk memulai dengan cepat dan mudah. Silakan dicatat bahwa rincian mengenai penggunaan fitur tertentu bukan bagian dari artikel ini.

Aspose.PDF untuk Android melalui Java terdiri dari dua bagian:

- Aspose.PDF untuk Android melalui Java DOM API
- Aspose.PDF.Facades

Anda akan menemukan rincian dari masing-masing area ini di bawah.

### Aspose.PDF untuk Android melalui Java DOM API

Aspose.PDF baru untuk Android melalui Java DOM API sesuai dengan struktur dokumen PDF, yang membantu Anda bekerja dengan dokumen PDF tidak hanya pada tingkat file dan dokumen, tetapi juga pada tingkat objek. Kami telah memberikan fleksibilitas lebih kepada pengembang untuk mengakses semua elemen dan objek dari dokumen PDF. Dengan menggunakan kelas-kelas dari Aspose.PDF DOM API, Anda dapat mengakses elemen dokumen dan pemformatan secara programatis. DOM API baru ini terdiri dari berbagai namespace seperti yang diberikan di bawah ini:

### com.aspose.pdf

Namespace ini menyediakan kelas Document yang memungkinkan Anda untuk membuka dan menyimpan dokumen PDF. Kelas License juga merupakan bagian dari namespace ini. Ini juga menyediakan kelas-kelas yang terkait dengan halaman PDF, lampiran, dan penanda buku seperti com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, dan com.aspose.pdf.OutlineCollection dll.

#### com.aspose.pdf.text

Namespace ini menyediakan kelas-kelas yang membantu Anda bekerja dengan teks dan berbagai aspeknya, misalnya com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment dan com.aspose.pdf.TextSegmentCollection dll.

#### com.aspose.pdf.TextOptions

Namespace ini menyediakan kelas-kelas yang memungkinkan Anda untuk mengatur berbagai opsi untuk mencari, mengedit, atau mengganti teks, misalnya com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions, dan com.aspose.pdf.TextSearchOptions.
#### com.aspose.pdf.PdfAction

Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan fitur interaktif dari dokumen PDF, misalnya bekerja dengan dokumen dan aksi lainnya. Namespace ini berisi kelas-kelas seperti com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction dan com.aspose.pdf.GoToURIAction dll.

#### com.aspose.pdf.Annotation

Anotasi adalah bagian dari fitur interaktif dokumen PDF. Kami telah mendedikasikan namespace untuk anotasi. Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan anotasi, misalnya, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation dan com.aspose.pdf.LinkAnnotation dll.

#### com.aspose.pdf.Form

Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan formulir PDF dan bidang formulir, misalnya com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField dan com.aspose.pdf.OptionCollection dll.

#### com.aspose.pdf.devices 

Kami dapat melakukan berbagai operasi pada dokumen PDF seperti mengonversi dokumen PDF ke berbagai format gambar.
 Namun, operasi semacam itu tidak termasuk dalam objek Dokumen dan kami tidak dapat memperluas kelas Dokumen untuk operasi semacam itu. Itulah mengapa kami memperkenalkan konsep Perangkat dalam API DOM baru.

##### com.aspose.pdf.facades

Sebelumnya pada Aspose.PDF untuk Java t.o.o, Anda memerlukan Aspose.PDF.Kit untuk Java untuk memanipulasi file PDF yang ada. Untuk menjalankan kode Aspose.PDF.Kit lama, dapat menggunakan namespace com.aspose.pdf.facades.