---
title: Dasar-dasar API DOM Aspose.PDF
linktitle: Dasar-dasar API DOM
type: docs
weight: 10
url: /id/androidjava/basics-of-dom-api/
description: Aspose.PDF for Android via Java juga menggunakan konsep DOM untuk merepresentasikan struktur dokumen PDF dalam bentuk objek. Di sini Anda dapat membaca deskripsi struktur ini.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Pengenalan API DOM

Model Objek Dokumen (DOM) adalah sebuah bentuk representasi dokumen terstruktur sebagai model berorientasi objek. DOM adalah standar resmi World Wide Web Consortium (W3C) untuk merepresentasikan dokumen terstruktur secara netral platform dan bahasa.

Dalam kata sederhana, DOM adalah pohon objek yang merepresentasikan struktur suatu dokumen. Aspose.PDF for Android via Java juga menggunakan konsep DOM untuk merepresentasikan struktur dokumen PDF dalam bentuk objek. Namun, aspek-aspek DOM (seperti Elements) dimanipulasi melalui sintaks bahasa pemrograman yang digunakan. Antarmuka publik sebuah DOM ditentukan dalam application programming interface (API)-nya.

### Pendahuluan Dokumen PDF

Portable Document Format (PDF) adalah standar terbuka untuk pertukaran dokumen. Dokumen PDF merupakan kombinasi teks dan data biner. Jika Anda membukanya di editor teks, Anda akan melihat objek mentah yang mendefinisikan struktur dan isi dokumen.

Struktur logis sebuah file PDF bersifat hierarkis dan menentukan urutan di mana aplikasi penampil menggambar halaman dokumen dan isinya. PDF terdiri dari empat komponen: objek, struktur file, struktur dokumen, dan aliran konten.

### Struktur Dokumen PDF

Karena struktur file PDF bersifat hierarkis, Aspose.PDF for Java juga mengakses elemen dengan cara yang sama. Hierarki berikut menunjukkan bagaimana dokumen PDF terstruktur secara logis dan bagaimana Aspose.PDF for Java DOM API menyusunnya.

![Struktur Dokumen PDF](https://docs.aspose.com/pdf/java/images/structure.png)

### Mengakses Elemen Dokumen PDF

Objek Document berada pada tingkat akar dari model objek. API DOM Aspose.PDF for Android via Java memungkinkan Anda membuat objek Document dan kemudian mengakses semua objek lain dalam hierarki. Anda dapat mengakses koleksi seperti Pages atau elemen individual seperti Page, dll. API DOM menyediakan titik masuk dan keluar tunggal untuk memanipulasi dokumen PDF seperti yang ditunjukkan di bawah ini:

- Buka dokumen PDF
- Akses struktur dokumen PDF dengan gaya DOM
- Perbarui data dalam dokumen PDF
- Validasi dokumen PDF
- Ekspor dokumen PDF ke format yang berbeda
- Terakhir, simpan dokumen PDF yang diperbarui

## Cara Menggunakan Aspose.PDF Baru untuk Android melalui API Java

Topik ini akan menjelaskan Aspose.PDF baru untuk Android melalui API Java dan membimbing Anda untuk memulai dengan cepat dan mudah. Harap dicatat bahwa detail mengenai penggunaan fitur tertentu bukanlah bagian dari artikel ini.

Aspose.PDF untuk Android melalui Java terdiri dari dua bagian:

- Aspose.PDF untuk Android melalui API DOM Java
- Aspose.PDF.Facades 

Anda akan menemukan detail masing‑masing area ini di bawah.

### Aspose.PDF untuk Android melalui API DOM Java

API DOM Java Aspose.PDF untuk Android yang baru sesuai dengan struktur dokumen PDF, yang membantu Anda bekerja dengan dokumen PDF tidak hanya pada tingkat file dan dokumen, tetapi juga pada tingkat objek. Kami telah memberikan fleksibilitas lebih kepada para pengembang untuk mengakses semua elemen dan objek dari dokumen PDF. Dengan menggunakan kelas‑kelas API DOM Aspose.PDF, Anda dapat memperoleh akses programatik ke elemen dokumen dan pemormatannya. API DOM baru ini terdiri dari berbagai namespace seperti yang diberikan di bawah ini:

### com.aspose.pdf

Namespace ini menyediakan kelas Document yang memungkinkan Anda membuka dan menyimpan dokumen PDF. Kelas License juga merupakan bagian dari namespace ini. Selain itu, namespace ini menyediakan kelas‑kelas yang terkait dengan halaman PDF, lampiran, dan bookmark seperti com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, dan com.aspose.pdf.OutlineCollection, dll.

#### com.aspose.pdf.text

Namespace ini menyediakan kelas-kelas yang membantu Anda bekerja dengan teks dan berbagai aspeknya, misalnya com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment, dan com.aspose.pdf.TextSegmentCollection, dll.

#### com.aspose.pdf.TextOptions

Namespace ini menyediakan kelas-kelas yang memungkinkan Anda mengatur berbagai opsi untuk mencari, menyunting, atau mengganti teks, misalnya com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions, dan com.aspose.pdf.TextSearchOptions.

#### com.aspose.pdf.PdfAction

Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan fitur interaktif dari dokumen PDF, misalnya bekerja dengan dokumen dan aksi-aksi lainnya. Namespace ini berisi kelas seperti com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction, dan com.aspose.pdf.GoToURIAction, dll.

#### com.aspose.pdf.Annotation

Anotasi adalah bagian dari fitur interaktif dokumen PDF. Kami telah menyediakan namespace khusus untuk anotasi. Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan anotasi, misalnya, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation dan com.aspose.pdf.LinkAnnotation, dll.

#### com.aspose.pdf.Form

Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan formulir PDF dan bidang formulir, misalnya com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField dan com.aspose.pdf.OptionCollection, dll.

#### com.aspose.pdf.devices 

Kami dapat melakukan berbagai operasi pada dokumen PDF seperti mengonversi dokumen PDF ke berbagai format gambar. Namun, operasi tersebut tidak termasuk dalam objek Document dan kami tidak dapat memperluas kelas Document untuk operasi tersebut. Karena itu kami memperkenalkan konsep Device dalam API DOM baru.

##### com.aspose.pdf.facades

Sebelum Aspose.PDF for Java t.o.o, Anda memerlukan Aspose.PDF.Kit untuk Java untuk memanipulasi file PDF yang ada. Untuk mengeksekusi kode Aspose.PDF.Kit lama, dapat menggunakan namespace com.aspose.pdf.facades.

