---
title: Dasar-dasar Aspose.PDF DOM API
linktitle: Dasar-dasar DOM API
type: docs
weight: 110
url: zh/python-java/basics-of-dom-api/
description: Aspose.PDF untuk Java juga menggunakan ide DOM untuk merepresentasikan struktur dokumen PDF dalam bentuk objek. Di sini Anda dapat membaca deskripsi struktur ini.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Pengenalan ke DOM API

Document Object Model (DOM) adalah bentuk representasi dokumen terstruktur sebagai model berorientasi objek. DOM adalah standar resmi World Wide Web Consortium (W3C) untuk merepresentasikan dokumen terstruktur dengan cara yang netral platform dan bahasa.

Secara sederhana, DOM adalah pohon objek yang merepresentasikan struktur suatu dokumen.
 Aspose.PDF untuk Java juga menggunakan konsep DOM untuk merepresentasikan struktur dokumen PDF dalam bentuk objek. Namun, aspek-aspek DOM (seperti Elemennya) dimanipulasi dalam sintaks bahasa pemrograman yang digunakan. Antarmuka publik dari DOM ditentukan dalam antarmuka pemrograman aplikasi (API) nya.

### Pengenalan ke Dokumen PDF

Portable Document Format (PDF) adalah standar terbuka untuk pertukaran dokumen. Dokumen PDF adalah kombinasi dari teks dan data biner. Jika Anda membukanya di editor teks, Anda akan melihat objek mentah yang mendefinisikan struktur dan isi dari dokumen.

Struktur logis dari file PDF adalah hierarkis dan menentukan urutan di mana aplikasi penampil menggambar halaman dokumen dan isinya. Sebuah PDF terdiri dari empat komponen: objek, struktur file, struktur dokumen, dan aliran konten.

### Struktur Dokumen PDF

Karena struktur file PDF adalah hierarkis, Aspose.PDF untuk Java juga mengakses elemen-elemen dengan cara yang sama. Hierarki berikut menunjukkan kepada Anda bagaimana dokumen PDF disusun secara logis dan bagaimana Aspose.PDF untuk Java DOM API membangunnya.

![Struktur Dokumen PDF](../images/structure.png)

### Mengakses Elemen Dokumen PDF

Objek Dokumen berada pada tingkat akar dari model objek. Aspose.PDF untuk Java DOM API memungkinkan Anda membuat objek Dokumen dan kemudian mengakses semua objek lain dalam hierarki. Anda dapat mengakses salah satu koleksi seperti Pages atau elemen individu seperti Page, dll. DOM API menyediakan titik masuk dan keluar tunggal untuk memanipulasi dokumen PDF seperti yang ditunjukkan di bawah ini:

- Buka dokumen PDF
- Akses struktur dokumen PDF dalam gaya DOM
- Perbarui data dalam dokumen PDF
- Validasi dokumen PDF
- Ekspor dokumen PDF ke berbagai format
- Terakhir, simpan dokumen PDF yang telah diperbarui

## Cara Menggunakan Aspose.PDF untuk Java API Baru

Topik ini akan menjelaskan Aspose.PDF untuk Java API yang baru dan memandu Anda untuk memulai dengan cepat dan mudah. Silakan perhatikan bahwa detail mengenai penggunaan fitur tertentu tidak termasuk dalam artikel ini.

Aspose.PDF untuk Java terdiri dari dua bagian:

- Aspose.PDF untuk Java DOM API
- Aspose.PDF.Facades

Anda akan menemukan rincian masing-masing area di bawah ini.

### Aspose.PDF untuk Java DOM API

Aspose.PDF untuk Java DOM API yang baru sesuai dengan struktur dokumen PDF, yang membantu Anda bekerja dengan dokumen PDF tidak hanya pada tingkat file dan dokumen, tetapi juga pada tingkat objek. Kami telah memberikan lebih banyak fleksibilitas kepada pengembang untuk mengakses semua elemen dan objek dari dokumen PDF. Dengan menggunakan kelas-kelas Aspose.PDF DOM API, Anda dapat memperoleh akses programatis ke elemen dan pemformatan dokumen. DOM API baru ini terdiri dari berbagai namespace seperti yang diberikan di bawah ini:

### com.aspose.pdf

Namespace ini menyediakan kelas Document yang memungkinkan Anda untuk membuka dan menyimpan dokumen PDF. Kelas License juga merupakan bagian dari namespace ini. Ini juga menyediakan kelas yang terkait dengan halaman PDF, lampiran, dan penanda buku seperti com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, dan com.aspose.pdf.OutlineCollection dll.

#### com.aspose.pdf.text

Namespace ini menyediakan kelas yang membantu Anda bekerja dengan teks dan berbagai aspeknya, misalnya com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment dan com.aspose.pdf.TextSegmentCollection dll.

#### com.aspose.pdf.TextOptions

Namespace ini menyediakan kelas yang memungkinkan Anda untuk mengatur opsi yang berbeda untuk mencari, mengedit atau mengganti teks, misalnya com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions, dan com.aspose.pdf.TextSearchOptions.
#### com.aspose.pdf.PdfAction

Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan fitur interaktif dari dokumen PDF, misalnya bekerja dengan dokumen dan aksi lainnya. Namespace ini berisi kelas-kelas seperti com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction dan com.aspose.pdf.GoToURIAction dll.

#### com.aspose.pdf.Annotation

Anotasi adalah bagian dari fitur interaktif dokumen PDF. Kami telah menyediakan namespace untuk anotasi. Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan anotasi, misalnya, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation dan com.aspose.pdf.LinkAnnotation dll.

#### com.aspose.pdf.Form

Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan formulir PDF dan bidang formulir, misalnya com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField dan com.aspose.pdf.OptionCollection dll.

#### com.aspose.pdf.devices

Kami dapat melakukan berbagai operasi pada dokumen PDF seperti mengonversi dokumen PDF ke berbagai format gambar.
 Namun, operasi semacam itu tidak termasuk dalam objek Dokumen dan kita tidak dapat memperluas kelas Dokumen untuk operasi semacam itu. Itulah mengapa kami memperkenalkan konsep Perangkat dalam API DOM yang baru.

##### com.aspose.pdf.facades

Sebelumnya, untuk Aspose.PDF for Java, Anda memerlukan Aspose.PDF.Kit for Java untuk memanipulasi file PDF yang ada. Untuk menjalankan kode Aspose.PDF.Kit lama, dapat menggunakan namespace com.aspose.pdf.facades.