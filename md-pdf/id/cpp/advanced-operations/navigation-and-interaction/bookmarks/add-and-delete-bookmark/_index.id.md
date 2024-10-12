```
---
title: Tambahkan dan Hapus Penanda 
linktitle: Tambahkan dan Hapus Penanda 
type: docs
weight: 10
url: /cpp/add-and-delete-bookmark/
description: Topik ini menjelaskan cara menambahkan penanda ke dokumen PDF dengan pustaka C++. Anda juga dapat menghapus semua atau penanda tertentu dari dokumen PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Penanda ke Dokumen PDF

Penanda disimpan dalam koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/) dari objek Document, yang berada dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).

Untuk menambahkan penanda ke PDF:

1. Buka dokumen PDF menggunakan objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/).
1. Buat penanda dan tentukan propertinya.
1.
``` Tambahkan koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) ke koleksi Outlines.

Cuplikan kode berikut menunjukkan cara menambahkan penanda buku dalam dokumen PDF.

```cpp
void AddBookmarks() {


String _dataDir("C:\\Samples\\Bookmarks\\");

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddBookmark.pdf");


// Buat objek penanda buku

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Test Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// Tetapkan nomor halaman tujuan

pdfOutline->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Tambahkan penanda buku dalam koleksi outline dokumen.

pdfDocument->get_Outlines()->Add(pdfOutline);


// Simpan dokumen yang diperbarui

pdfDocument->Save(_dataDir + u"AddBookmark_out.pdf");
}
```

## Tambahkan Penanda Buku Anak ke Dokumen PDF

Penanda buku dapat disusun bersarang, menunjukkan hubungan hierarkis dengan penanda buku induk dan anak. Artikel ini menjelaskan cara menambahkan penanda halaman anak, yaitu penanda halaman tingkat kedua, ke dalam PDF.

Untuk menambahkan penanda halaman anak ke file PDF, pertama-tama tambahkan penanda halaman induk:

1. Buka dokumen.
1. Tambahkan penanda halaman ke [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/), mendefinisikan propertinya.
1. Tambahkan OutlineItemCollection ke koleksi objek Dokumen [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).

Penanda halaman anak dibuat sama seperti penanda halaman induk, dijelaskan di atas, tetapi ditambahkan ke koleksi Outlines dari penanda halaman induk.

Cuplikan kode berikut menunjukkan cara menambahkan penanda halaman anak ke dokumen PDF.

```cpp
void AddChildBookmark() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Buka dokumen

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddChildBookmark.pdf");


// Buat objek penanda halaman induk

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Parent Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// Buat objek penanda halaman anak

auto pdfChildOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfChildOutline->set_Title(u"Child Outline");

pdfChildOutline->set_Italic(true);

pdfChildOutline->set_Bold(true);


// Tambahkan penanda halaman anak ke koleksi penanda halaman induk

pdfOutline->Add(pdfChildOutline);

// Tambahkan penanda halaman induk ke koleksi outline dokumen.

pdfDocument->get_Outlines()->Add(pdfOutline);


// Simpan output

pdfDocument->Save(_dataDir + u"AddChildBookmark_out.pdf");
}
```
## Hapus Semua Penanda Buku dari Dokumen PDF

Semua penanda buku dalam sebuah PDF disimpan dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/). Artikel ini menjelaskan cara menghapus semua penanda buku dari file PDF.

Untuk menghapus semua penanda buku dari file PDF:

1. Panggil metode Delete dari koleksi [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).
2. Simpan file yang telah dimodifikasi menggunakan metode Save dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/).

Cuplikan kode berikut menunjukkan cara menghapus semua penanda buku dari dokumen PDF.

```cpp
void DeleteAllBookmarksFromPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Buka dokumen

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteAllBookmarks.pdf");


// Hapus semua penanda buku

pdfDocument->get_Outlines()->Delete();


// Simpan file yang diperbarui

pdfDocument->Save(_dataDir + u"DeleteAllBookmarks_out.pdf");
}
```


## Hapus Penanda Buku Tertentu dari Dokumen PDF

[Hapus Semua Lampiran dari dokumen PDF](https://docs.aspose.com/pdf/cpp/working-with-attachments/) menunjukkan cara menghapus semua lampiran dari file PDF. Juga dimungkinkan untuk hanya menghapus lampiran tertentu.

Untuk menghapus penanda buku tertentu dari file PDF:

1. Berikan judul penanda buku sebagai parameter ke metode Delete koleksi [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).
2. Kemudian simpan file yang diperbarui dengan metode Save dari objek Document.

Kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) menyediakan koleksi [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/). Metode [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection#a04f36a1f4f7c4fde3189399eb046a98b) menghapus penanda buku apa pun dengan judul yang diberikan ke metode tersebut.

Cuplikan kode berikut menunjukkan cara menghapus penanda buku tertentu dari dokumen PDF.

```cpp
void DeleteParticularBookmarkPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Buka dokumen

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteParticularBookmark.pdf");


// Hapus outline tertentu dengan Judul

pdfDocument->get_Outlines()->Delete(u"Child Outline");


// Simpan file yang diperbarui

pdfDocument->Save(_dataDir + u"DeleteParticularBookmark_out.pdf");
}
```