---
title: Dasar-dasar Aspose.PDF DOM API
linktitle: Dasar-dasar DOM API
type: docs
weight: 140
url: id/net/basics-of-dom-api/
description: Aspose.PDF untuk .NET juga menggunakan ide DOM untuk merepresentasikan struktur dokumen PDF dalam bentuk objek.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Pengenalan ke DOM API

Model Objek Dokumen (DOM) adalah bentuk representasi dokumen terstruktur sebagai model berorientasi objek. DOM adalah standar resmi Konsorsium World Wide Web (W3C) untuk merepresentasikan dokumen terstruktur secara netral platform dan bahasa.

Dengan kata sederhana, DOM adalah pohon objek yang merepresentasikan struktur dari suatu dokumen.
Dengan kata sederhana, DOM adalah pohon objek yang merepresentasikan struktur dari suatu dokumen.

### Pengenalan Dokumen PDF

Portable Document Format (PDF) adalah standar terbuka untuk pertukaran dokumen. Sebuah dokumen PDF merupakan kombinasi dari teks dan data biner. Jika Anda membukanya dengan editor teks, Anda akan melihat objek mentah yang mendefinisikan struktur dan isi dari dokumen tersebut.

Struktur logis dari file PDF bersifat hierarkis dan menentukan urutan dimana aplikasi penampil menggambar halaman dokumen dan isi mereka. PDF terdiri dari empat komponen: objek, struktur file, struktur dokumen, dan aliran konten.

### Struktur Dokumen PDF

Karena struktur file PDF bersifat hierarkis, Aspose.PDF untuk .NET juga mengakses elemen dengan cara yang sama. Hierarki berikut menunjukkan bagaimana dokumen PDF secara logis terstruktur dan bagaimana Aspose.PDF untuk .NET DOM API membangunnya.

![Struktur Dokumen PDF](../images/structure.png)

### Mengakses Elemen Dokumen PDF

Objek Dokumen berada di tingkat akar dari model objek.
Objek Dokumen berada pada level akar dari model objek.

- Buka dokumen PDF
- Akses struktur dokumen PDF dalam gaya DOM
- Perbarui data dalam dokumen PDF
- Validasi dokumen PDF
- Ekspor dokumen PDF ke berbagai format
- Akhirnya, simpan dokumen PDF yang telah diperbarui

## Cara Menggunakan API Aspose.PDF untuk .NET yang Baru

Topik ini akan menjelaskan API Aspose.PDF untuk .NET yang baru dan memandu Anda untuk memulai dengan cepat dan mudah. Harap dicatat bahwa detail mengenai penggunaan fitur tertentu tidak merupakan bagian dari artikel ini.

Aspose.PDF untuk .NET terdiri dari dua bagian:

- Aspose.PDF untuk .NET DOM API
- Aspose.PDF.Facades (dulu Aspose.PDF.Kit untuk .NET)
Anda akan menemukan detail dari masing-masing area di bawah ini.

### Aspose.PDF untuk .NET DOM API

API DOM Aspose.PDF untuk .NET sesuai dengan struktur dokumen PDF, yang membantu Anda bekerja dengan dokumen PDF tidak hanya pada level file dan dokumen, tetapi juga pada level objek.
API DOM Aspose.PDF untuk .NET sesuai dengan struktur dokumen PDF, yang membantu Anda bekerja dengan dokumen PDF tidak hanya pada tingkat file dan dokumen, tetapi juga pada tingkat objek.

### Aspose.PDF

Namespace ini menyediakan kelas Document yang memungkinkan Anda membuka dan menyimpan dokumen PDF. Kelas License juga merupakan bagian dari namespace ini. Ini juga menyediakan kelas terkait halaman PDF, lampiran, dan bookmark seperti Page, PageCollection, FileSpecification, EmbeddedFileCollection, OutlineItemCollection, dan OutlineCollection dll.

#### Aspose.Text

Namespace ini menyediakan kelas yang membantu Anda bekerja dengan teks dan berbagai aspeknya, misalnya Font, FontCollection, FontRepository, FontStyles, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment dan TextSegmentCollection dll.

#### Aspose.Text.TextOptions

Namespace ini menyediakan kelas yang memungkinkan Anda mengatur berbagai opsi untuk mencari, mengedit atau mengganti teks, misalnya TextEditOptions, TextReplaceOptions dan TextSearchOptions.
Namespace ini menyediakan kelas yang memungkinkan Anda untuk mengatur berbagai opsi untuk pencarian, pengeditan, atau penggantian teks, misalnya TextEditOptions, TextReplaceOptions, dan TextSearchOptions.

#### Aspose.InteractiveFeatures

Namespace ini berisi kelas yang membantu Anda bekerja dengan fitur interaktif dari dokumen PDF, misalnya bekerja dengan dokumen dan tindakan lainnya. Namespace ini berisi kelas seperti GoToAction, GoToRemoteAction, dan GoToURIAction dll.

#### Aspose.InteractiveFeatures.Annotations

Annotasi adalah bagian dari fitur interaktif dokumen PDF. Kami telah mendefinisikan sebuah namespace untuk anotasi. Namespace ini berisi kelas yang membantu Anda bekerja dengan anotasi, misalnya, Annotation, AnnotationCollection, CircleAnnotation, dan LinkAnnotation dll.

#### Aspose.InteractiveFeatures.Forms

Namespace ini berisi kelas yang membantu Anda bekerja dengan formulir PDF dan bidang formulir, misalnya Form, Field, TextBoxField, dan OptionCollection dll.

#### Aspose.PDF.Devices

Kita dapat melakukan berbagai operasi pada dokumen PDF seperti mengonversi dokumen PDF ke berbagai format gambar.
Kita dapat melakukan berbagai operasi pada dokumen PDF seperti mengonversi dokumen PDF ke berbagai format gambar.

##### Aspose.PDF.Facades

Sebelum Aspose.PDF untuk .NET, Anda memerlukan Aspose.PDF.Kit untuk .NET untuk memanipulasi file PDF yang ada. Untuk menjalankan kode Aspose.PDF.Kit lama, Anda dapat menggunakan ruang nama Aspose.PDF.Facades.
