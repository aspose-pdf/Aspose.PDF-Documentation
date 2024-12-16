---
title: Dapatkan, Perbarui dan Kembangkan Penanda 
linktitle: Dapatkan, Perbarui dan Kembangkan Penanda
type: docs
weight: 20
url: /id/cpp/get-update-and-expand-bookmark/
description: Aspose.PDF untuk pustaka C++ memungkinkan Anda mendapatkan? memperbarui dalam file PDF dengan kami.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dapatkan Penanda

Koleksi [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) berisi semua penanda dari file PDF. Artikel ini menjelaskan cara mendapatkan penanda dari sebuah file PDF, dan bagaimana mengetahui halaman mana penanda tertentu berada.

Untuk mendapatkan penanda, lakukan loop melalui koleksi [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) dan dapatkan setiap penanda dalam OutlineItemCollection. The OutlineItemCollection menyediakan akses ke semua atribut penanda buku. Potongan kode berikut menunjukkan cara mendapatkan penanda buku dari file PDF.

```cpp
void GettingBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// Buka dokumen

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Loop melalui semua penanda buku

for (auto outlineItem : pdfDocument->get_Outlines()) {


Console::WriteLine(u"Judul :- " + outlineItem->get_Title());


Console::WriteLine(u"Apakah Miring :- " + outlineItem->get_Italic());


Console::WriteLine(u"Apakah Tebal :- " + outlineItem->get_Bold());


Console::WriteLine(u"Warna :- {0}", outlineItem->get_Color());

}
}
```

## Mendapatkan Nomor Halaman Penanda Buku

Setelah Anda menambahkan penanda buku, Anda dapat mengetahui halaman mana penanda buku tersebut dengan mendapatkan PageNumber tujuan yang terkait dengan objek Bookmark.

```cpp
void GettingBookmarksPageNumber() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Buat PdfBookmarkEditor

auto bookmarkEditor = MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();

// Buka file PDF

bookmarkEditor->BindPdf(_dataDir + u"UpdateBookmarks.pdf");

// Ekstrak penanda buku

auto bookmarks = bookmarkEditor->ExtractBookmarks();

for (auto bookmark : bookmarks) {


String strLevelSeprator("");


for (int i = 1; i < bookmark->get_Level(); i++) {



strLevelSeprator += u"---- ";


}


Console::WriteLine(u"Judul :- " + strLevelSeprator + bookmark->get_Title());


Console::WriteLine(u"Nomor Halaman :- " + strLevelSeprator + bookmark->get_PageNumber());


Console::WriteLine(u"Tindakan Halaman :- " + strLevelSeprator + bookmark->get_Action());

}
}
```
## Memperbarui Penanda Buku dalam Dokumen PDF

Untuk memperbarui penanda buku dalam berkas PDF, pertama, dapatkan penanda buku tertentu dari koleksi OutlineColletion objek Dokumen dengan menentukan indeks penanda buku. Setelah Anda mendapatkan penanda buku ke dalam objek [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection), Anda dapat memperbarui properti-propertinya dan kemudian menyimpan berkas PDF yang diperbarui menggunakan metode Save. Cuplikan kode berikut menunjukkan cara memperbarui penanda buku dalam dokumen PDF.

```cpp
void UpdateBookmarksInPDFDocument() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// Buka dokumen

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Dapatkan objek penanda buku

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);


// Perbarui objek penanda buku

pdfOutline->set_Title(u"Updated Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);

// Tetapkan halaman target sebagai 2

pdfOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Simpan keluaran

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## Memperbarui Penanda Buku Anak dalam Dokumen PDF

Untuk memperbarui penanda buku anak:

1. Ambil penanda buku anak yang ingin Anda perbarui dari file PDF dengan terlebih dahulu mendapatkan penanda buku induk dan kemudian penanda buku anak menggunakan nilai indeks yang sesuai.
1. Simpan file PDF yang diperbarui menggunakan metode Save.

{{% alert color="primary" %}}

Dapatkan penanda buku dari koleksi OutlineCollection objek Dokumen dengan menentukan indeks penanda buku, dan kemudian dapatkan penanda buku anak dengan menentukan indeks dari penanda buku induk ini.

{{% /alert %}}

Cuplikan kode berikut menunjukkan kepada Anda cara memperbarui penanda buku anak dalam dokumen PDF.

```cpp
void UpdateChildBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Buka dokumen

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Dapatkan objek penanda buku

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);

// Dapatkan objek penanda buku anak

auto childOutline = pdfOutline->idx_get(1);


// Perbarui objek penanda buku

childOutline->set_Title(u"Updated Outline");

childOutline->set_Italic(true);

childOutline->set_Bold(true);

// Tetapkan halaman target sebagai 2

childOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Simpan keluaran

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## Penanda Buku yang Diperluas saat Melihat Dokumen

Penanda buku disimpan dalam koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) objek Dokumen, yang berada dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection). Namun, kita mungkin memiliki kebutuhan untuk memperluas semua penanda buku saat melihat file PDF.

Untuk memenuhi kebutuhan ini, kita dapat mengatur status terbuka untuk setiap item garis besar/penanda buku sebagai Terbuka. Cuplikan kode berikut menunjukkan cara mengatur status terbuka untuk setiap penanda buku agar diperluas dalam dokumen PDF.

```cpp
void ExpandedBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

auto doc = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// atur mode tampilan halaman yaitu tampilkan thumbnail, layar penuh, tampilkan panel lampiran

doc->set_PageMode(PageMode::UseOutlines);

// cetak jumlah total Penanda Buku dalam file PDF

Console::WriteLine(doc->get_Outlines()->get_Count());

// telusuri setiap item Outline dalam koleksi outline file PDF

for (int counter = 1; counter <= doc->get_Outlines()->get_Count(); counter++) {

// atur status terbuka untuk item outline

doc->get_Outlines()->idx_get(counter)->set_Open(true);

}

// simpan file PDF

doc->Save(_dataDir + u"Bookmarks_Expanded.pdf");
}
```