```
---
title: Dasar-dasar Aspose.PDF DOM API
linktitle: Dasar-dasar DOM API
type: docs
weight: 120
url: /id/cpp/basics-of-dom-api/
description: Aspose.PDF untuk C++ juga menggunakan ide DOM untuk merepresentasikan struktur dokumen PDF dalam bentuk objek. Di sini Anda dapat membaca deskripsi struktur ini.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Pengenalan API DOM

Document Object Model (DOM) adalah bentuk representasi dokumen terstruktur sebagai model berorientasi objek. DOM adalah standar resmi World Wide Web Consortium (W3C) untuk merepresentasikan dokumen terstruktur dengan cara yang netral terhadap platform dan bahasa.

Secara sederhana, DOM adalah pohon objek yang merepresentasikan struktur dari suatu dokumen.
``` Aspose.PDF untuk C++ juga menggunakan ide DOM untuk merepresentasikan struktur dokumen PDF dalam hal objek. Namun, aspek-aspek dari DOM (seperti Elemennya) dimanipulasi dalam sintaks bahasa pemrograman yang digunakan. Antarmuka publik dari sebuah DOM ditentukan dalam antarmuka pemrograman aplikasinya (API).

### Pengenalan ke Dokumen PDF

Portable Document Format (PDF) adalah standar terbuka untuk pertukaran dokumen. Dokumen PDF adalah kombinasi dari teks dan data biner. Jika Anda membukanya di editor teks, Anda akan melihat objek mentah yang mendefinisikan struktur dan isi dokumen.

Struktur logis dari file PDF bersifat hierarkis dan menentukan urutan di mana aplikasi penampil menggambar halaman-halaman dokumen dan isinya. Sebuah PDF terdiri dari empat komponen: objek, struktur file, struktur dokumen, dan aliran konten.

### Struktur Dokumen PDF

Karena struktur dari file PDF bersifat hierarkis, Aspose.PDF untuk C++ juga mengakses elemen-elemen dengan cara yang sama. Hierarki berikut menunjukkan kepada Anda bagaimana dokumen PDF secara logis terstruktur dan bagaimana Aspose.PDF untuk C++ DOM API membangunnya.

![Struktur Dokumen PDF](../images/structure.png)

### Mengakses Elemen Dokumen PDF

Objek Document berada pada tingkat akar dari model objek. Aspose.PDF untuk C++ DOM API memungkinkan Anda untuk membuat objek Document dan kemudian mengakses semua objek lain dalam hierarki. Anda dapat mengakses salah satu koleksi seperti Pages atau elemen individu seperti Page, dll. DOM API menyediakan titik masuk dan keluar tunggal untuk memanipulasi dokumen PDF seperti yang ditunjukkan di bawah ini:

- Buka dokumen PDF
- Akses struktur dokumen PDF dalam gaya DOM
- Perbarui data dalam dokumen PDF
- Validasi dokumen PDF
- Ekspor dokumen PDF ke dalam berbagai format
- Akhirnya, simpan dokumen PDF yang telah diperbarui

## Cara Menggunakan API Aspose.PDF untuk C++ yang Baru

Topik ini akan menjelaskan API Aspose.PDF untuk C++ yang baru dan membimbing Anda untuk memulai dengan cepat dan mudah. Harap dicatat bahwa detail mengenai penggunaan fitur tertentu bukan bagian dari artikel ini.

Aspose.PDF for C++ terdiri dari dua bagian:

- Aspose.PDF for C++ DOM API
- Aspose.PDF.Facades

Anda akan menemukan detail dari masing-masing area ini di bawah.

### Aspose.PDF for C++ DOM API

Aspose.PDF for C++ DOM API sesuai dengan struktur dokumen PDF, yang membantu Anda bekerja dengan dokumen PDF tidak hanya di tingkat file dan dokumen, tetapi juga di tingkat objek. Kami telah memberikan lebih banyak fleksibilitas kepada pengembang untuk mengakses semua elemen dan objek dokumen PDF. Dengan menggunakan kelas-kelas dari Aspose.PDF DOM API, Anda dapat memperoleh akses pemrograman ke elemen dan pemformatan dokumen. DOM API baru ini terdiri dari berbagai namespace seperti yang diberikan di bawah ini:

### Aspose::Pdf Namespace Reference

Namespace ini menyediakan kelas Document yang memungkinkan Anda membuka dan menyimpan dokumen PDF.

#### Aspose::Pdf::Text Namespace Reference

Namespace ini menyediakan kelas-kelas yang membantu Anda bekerja dengan teks dan berbagai aspeknya, misalnya Font, FontCollection, FontRepository, FontSource, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment dan TextSegmentCollection dll.
#### Aspose::Pdf::Collections Namespace Reference

Namespace ini menyediakan kelas AsposeHashDictionary.

#### Aspose::Pdf::CommonData Namespace Reference

#### Aspose::Pdf::Diagnostics Namespace Reference

#### Aspose::Pdf::Drawing Namespace Reference

Namespace ini menyediakan kelas: Curve, Circle, Arc, Rectangle, Graph dan lain-lain, untuk menambahkan elemen grafis ke file PDF Anda.

#### Aspose::Pdf::Engine Namespace Reference

Namespace ini menyediakan kelas Addressing, Interactive, Security, CommonData, IO, Presentation.

#### Aspose::Pdf::GroupProcessor Namespace Reference

Namespace ini menyediakan kelas: ExtractorFactory - merepresentasikan pabrik untuk membuat objek IPdfTypeExtractor, IDocumentPageTextExtractor, IDocumentTextExtractor, kelas IPdfTypeExtractor - merepresentasikan antarmuka untuk berinteraksi dengan extractor.

#### Aspose::Pdf::Interchange Namespace Reference

#### Aspose::Pdf::LogicalStructure Namespace Reference

Namespace ini menyediakan kelas: AnnotationElement, AttributeOwnerStandard, CaptionElement, DocumentElement, FormElement, GroupingElement, ILSTextElement, PrivateElement, WarichuWTElement, dan lain-lain.

#### Aspose::Pdf::Operators Namespace Reference

Namespace ini menyediakan kelas dari operator berikut: BasicSetColorAndPatternOperator, BlockTextOperator, SetCharWidthBoundingBox, SetColorStroke, SetHorizontalTextScaling, SetTextRenderingMode, TextShowOperator, dan lain-lain.

#### Aspose::Pdf::Optimization Namespace Reference

Namespace ini menyediakan dua kelas - ImageCompressionOptions dan OptimizationOptions.

#### Aspose::Pdf::PageModel Namespace Reference

#### Aspose::Pdf::PdfAOptionClasses Namespace Reference

Namespace ini menyediakan dua kelas: FontEmbeddingOptions - Standar PDF/A mengharuskan, bahwa semua font harus disematkan ke dalam dokumen. Kelas ini mencakup flag untuk kasus ketika tidak mungkin menyematkan beberapa font karena font tersebut tidak ada di PC tujuan. ToUnicodeProcessingRules - Kelas ini menjelaskan aturan yang dapat digunakan untuk memecahkan kesalahan Adobe Preflight "Text cannot be mapped to Unicode".

#### Aspose::Pdf::Sanitization Namespace Reference

Namespace ini menyediakan dua kelas: Details_SanitizationException dan IRecovery.

#### Aspose::Pdf::Tagged Namespace Reference

Namespace ini menyediakan kelas Details_TaggedException - Mewakili pengecualian untuk konten TaggedPDF dari dokumen. ITaggedContent - Mewakili antarmuka untuk bekerja dengan konten TaggedPdf dari dokumen? dan TaggedPdfExceptionCode.

#### Aspose::Pdf::Validation Namespace Reference

#### Aspose::Pdf::XfaConverter Namespace Reference

Namespace ini menyediakan kelas XfaParserOptions - kelas untuk menangani enkapsulasi data terkait.

#### Aspose::Pdf::Annotations Namespace Reference

Anotasi adalah bagian dari fitur interaktif dokumen PDF. Kami telah menyediakan namespace khusus untuk anotasi. Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan anotasi, misalnya, Annotation, AnnotationCollection, CircleAnnotation dan LinkAnnotation dll.

#### Aspose::Pdf::Forms Namespace Reference

Namespace ini berisi kelas-kelas yang membantu Anda bekerja dengan formulir PDF dan bidang formulir, misalnya Form, Field, TextBoxField dan OptionCollection dll.

#### Aspose::Pdf::Devices Namespace Reference

We dapat melakukan berbagai operasi pada dokumen PDF seperti mengkonversi dokumen PDF ke berbagai format gambar. Namun, operasi semacam itu tidak termasuk dalam objek Dokumen dan kita tidak dapat memperluas kelas Dokumen untuk operasi semacam itu. Itulah mengapa kami telah memperkenalkan konsep Perangkat dalam API DOM baru.

##### Aspose::Pdf::Facades Namespace Reference

Anda dapat menggunakan namespace Aspose.PDF.Facades. Namespace ini menyediakan kelas-kelas AutoFiller - mewakili kelas untuk menerima data dari basis data atau sumber data lainnya. Bookmark, Form, Stamp, PdfConverter dan lebih banyak kelas.