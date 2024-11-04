---
title: Bekerja dengan Aksi dalam PDF
linktitle: Aksi
type: docs
weight: 20
url: /cpp/actions/
description: Bagian ini menjelaskan cara menambahkan aksi ke dokumen dan bidang formulir secara programatis dengan C++.
lastmod: "2022-01-25"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Menambahkan Hyperlink dalam File PDF

Dokumen PDF adalah cara yang bagus untuk berbagi informasi. Mereka mudah dibaca, diedit, dan didistribusikan. Namun, membuat tautan dalam dokumen PDF bisa menjadi tantangan. Mari kami tunjukkan caranya.

Dimungkinkan untuk menambahkan hyperlink ke file PDF, baik untuk memungkinkan pembaca bernavigasi ke bagian lain dari PDF, atau ke konten eksternal.

Misalnya, Anda mungkin ingin menambahkan daftar isi yang dapat diklik ke ebook Anda, mengutip sumber daya luar untuk artikel Anda, atau dengan cepat mengarahkan pembaca ke halaman berbeda di situs web untuk mendapatkan informasi lebih lanjut tentang suatu subjek.

Untuk membuat hyperlink dengan beberapa klik, ikuti langkah-langkah sederhana berikut:

1. Buat objek Kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).  
1. Dapatkan Kelas [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) yang ingin Anda tambahkan tautannya.  
1. Buat objek [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) menggunakan objek Page dan [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/). Objek persegi panjang digunakan untuk menentukan lokasi pada halaman di mana tautan harus ditambahkan.  
1. Atur properti Action ke objek [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) yang menentukan lokasi URI jarak jauh.  
1. Untuk menampilkan teks hyperlink, tambahkan string teks pada lokasi yang mirip dengan tempat objek [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) ditempatkan.  
1. Untuk menambahkan teks bebas:

- Buat objek [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation). Itu juga menerima objek Halaman dan Persegi Panjang sebagai argumen, sehingga memungkinkan untuk menyediakan nilai yang sama seperti yang ditentukan terhadap konstruktor LinkAnnotation.
- Menggunakan properti Isi objek [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation), tentukan string yang harus ditampilkan dalam keluaran PDF.
- Secara opsional, atur lebar batas dari objek [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) dan FreeTextAnnotation ke 0 sehingga mereka tidak muncul dalam dokumen PDF.
- Setelah objek [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) dan [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation) telah didefinisikan, tambahkan tautan ini ke koleksi Anotasi objek [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).

- Terakhir, simpan PDF yang diperbarui menggunakan metode Simpan objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
The following code snippet shows you how to add a hyperlink to a PDF file.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddHyperlinkInPDFFile() {

String _dataDir("C:\\Samples\\");

// Buka dokumen

auto document = MakeObject<Document>(_dataDir + u"AddHyperlink.pdf");

// Buat tautan

auto page = document->get_Pages()->idx_get(1);

// Buat objek anotasi tautan

auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 100, 300, 300));

// Buat objek border untuk LinkAnnotation

auto border = MakeObject<Aspose::Pdf::Annotations::Border>(link);

// Atur nilai lebar border sebagai 0

border->set_Width(0);

// Atur border untuk LinkAnnotation

link->set_Border(border);

// Tentukan jenis tautan sebagai URI jarak jauh

link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

// Tambahkan anotasi tautan ke koleksi anotasi halaman pertama file PDF

page->get_Annotations()->Add(link);


// Buat anotasi Teks Bebas

auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::FreeTextAnnotation>(


page,


MakeObject<Rectangle>(100, 100, 300, 300),


MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(



FontRepository::FindFont(u"TimesNewRoman"), 10, Color::get_Blue()));


// String yang akan ditambahkan sebagai teks bebas

textAnnotation->set_Contents(u"Tautan ke situs web Aspose");

// Atur border untuk Anotasi Teks Bebas

textAnnotation->set_Border(border);

// Tambahkan anotasi FreeText ke koleksi anotasi halaman pertama Dokumen

page->get_Annotations()->Add(textAnnotation);


// Simpan dokumen yang diperbarui

document->Save(_dataDir + u"AddHyperlink_out.pdf");

}
```

## Membuat Hyperlink ke halaman dalam PDF yang sama

Aspose.PDF untuk C++ menyediakan fitur hebat untuk pembuatan PDF serta manipulasi. Ini juga menawarkan fitur untuk menambahkan tautan ke halaman PDF dan tautan dapat mengarah ke halaman dalam file PDF lain, URL web, tautan untuk meluncurkan Aplikasi, atau bahkan tautan ke halaman dalam file PDF yang sama. Untuk menambahkan hyperlink lokal (tautan ke halaman dalam file PDF yang sama), sebuah kelas bernama [LocalHyperlink](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.local_hyperlink) ditambahkan ke namespace Aspose.PDF dan kelas ini memiliki properti bernama TargetPageNumber, yang digunakan untuk menentukan halaman target/destinasi untuk hyperlink.

Untuk menambahkan hyperlink lokal, kita perlu membuat TextFragment sehingga tautan dapat dikaitkan dengan TextFragment. Kelas [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment) memiliki properti bernama Hyperlink yang digunakan untuk mengasosiasikan instance LocalHyperlink. Cuplikan kode berikut menunjukkan langkah-langkah untuk memenuhi persyaratan ini.

```cpp
void CreateHyperlinkToPagesInSamePDF() {

String _dataDir("C:\\Samples\\");


// Buat instance Dokumen

auto document = MakeObject<Document>();


// Tambahkan halaman ke koleksi halaman file PDF

auto page = document->get_Pages()->Add();


// Buat instance Text Fragment

auto text = MakeObject<TextFragment>(u"link page number test to page 2");


// Buat instance hyperlink lokal

auto link = MakeObject<LocalHyperlink>();


// Tetapkan halaman target untuk instance link

link->set_TargetPageNumber(2);


// Tetapkan hyperlink TextFragment

text->set_Hyperlink(link);


// Tambahkan teks ke koleksi paragraf Halaman

page->get_Paragraphs()->Add(text);


// Buat instance TextFragment baru

text = new TextFragment(u"link page number test to page 1");


// TextFragment harus ditambahkan di atas halaman baru

text->set_IsInNewPage(true);


// Buat instance hyperlink lokal lainnya

link = new LocalHyperlink();


// Tetapkan halaman target untuk hyperlink kedua

link->set_TargetPageNumber(1);


// Tetapkan link untuk TextFragment kedua

text->set_Hyperlink(link);


// Tambahkan teks ke koleksi paragraf objek halaman

page->get_Paragraphs()->Add(text);


// Simpan dokumen yang diperbarui

document->Save(_dataDir + u"CreateLocalHyperlink_out.pdf");
}
```
## Mendapatkan Tujuan Hyperlink PDF (URL)

Tautan diwakili sebagai anotasi dalam file PDF dan dapat ditambahkan, diperbarui, atau dihapus. Aspose.PDF untuk C++ juga mendukung mendapatkan tujuan (URL) dari hyperlink dalam file PDF.

Untuk mendapatkan URL tautan:

1. Buat objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Dapatkan [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) yang ingin Anda ekstrak tautannya.
1. Gunakan kelas [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) untuk mengekstrak semua objek [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) dari halaman yang ditentukan.
1. Berikan objek [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) ke metode Accept objek [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).
1. Dapatkan semua anotasi tautan yang dipilih ke dalam objek IList menggunakan properti Selected dari objek [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/).
1. Akhirnya, ekstrak Tindakan LinkAnnotation sebagai GoToURIAction.

Cuplikan kode berikut menunjukkan cara mendapatkan tujuan hyperlink (URL) dari file PDF.

```cpp
void GetPDFHyperlinkDestination() {

String _dataDir("C:\\Samples\\");


auto document = new Document(_dataDir + u"Aspose-app-list.pdf");

// Ekstrak tindakan

auto page = document->get_Pages()->idx_get(1);


auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(


MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));

page->Accept(selector);


auto list = selector->get_Selected();

// Iterasi melalui item individu di dalam daftar

if (list->get_Count() == 0)


Console::WriteLine(u"Tidak ada Hyperlink ditemukan...");

else {


// Loop melalui semua penanda buku


for (auto annot : list) {



auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);



if (la != nullptr) {




auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());




// Cetak URL tujuan




Console::WriteLine(u"Tujuan: " + action->get_URI());



}


}

} // end else
}
```
## Dapatkan Teks Hyperlink

Sebuah hyperlink memiliki dua bagian: teks yang ditampilkan dalam dokumen, dan URL tujuan. Dalam beberapa kasus, yang kita butuhkan adalah teks, bukan URL.

Teks dan anotasi/aksi dalam file PDF diwakili oleh entitas yang berbeda. Teks pada halaman hanyalah sekumpulan kata dan karakter, sementara anotasi membawa beberapa interaktivitas seperti yang ada dalam hyperlink.

Untuk menemukan konten URL, Anda perlu bekerja dengan anotasi dan teks. Objek [Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) tidak memiliki teks itu sendiri tetapi berada di bawah teks pada halaman. Jadi untuk mendapatkan teksnya, Annotation memberikan batasan URL, sementara objek Text memberikan konten URL. Silakan lihat potongan kode berikut.

```cpp
  void GetHyperlinkText() {

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"aspose-app-list.pdf");

// Ekstrak aksi

auto page = document->get_Pages()->idx_get(1);


for (auto annot : page->get_Annotations()) {


auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);


if (la != nullptr) {



// Cetak URL dari setiap Link Annotation



auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());



Console::WriteLine(u"URI: " + action->get_URI());




auto absorber = MakeObject<TextAbsorber>();



absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);



absorber->get_TextSearchOptions()->set_Rectangle(annot->get_Rect());



page->Accept(absorber);



String extractedText = absorber->get_Text();



// Cetak teks yang terkait dengan hyperlink



Console::WriteLine(extractedText);


}

}
}
```

## Hapus Aksi Buka Dokumen dari File PDF

[Bagaimana Menentukan Halaman PDF saat Melihat Dokumen](#how-to-specify-pdf-page-when-viewing-document) menjelaskan cara mengatur agar dokumen terbuka pada halaman yang berbeda dari halaman pertama. Saat menggabungkan beberapa dokumen, dan satu atau lebih memiliki aksi GoTo yang diatur, Anda mungkin ingin menghapusnya. Misalnya, jika menggabungkan dua dokumen dan dokumen kedua memiliki aksi GoTo yang membawa Anda ke halaman kedua, dokumen keluaran akan terbuka di halaman kedua dari dokumen kedua, bukan halaman pertama dari dokumen gabungan. Untuk menghindari perilaku ini, hapus perintah aksi buka.

Untuk menghapus aksi buka:

1. Atur properti [OpenAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a24b876bb6bee957feac48ac8031dc28e) dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) menjadi null.
1. Simpan PDF yang telah diperbarui menggunakan metode Save dari objek Document.

Cuplikan kode berikut menunjukkan cara menghapus aksi buka dokumen dari file PDF.

```cpp
void RemoveDocumentOpenActionFromPDFFile()
{

String _dataDir("C:\\Samples\\");

// Buka dokumen

auto document = new Document(_dataDir + u"RemoveOpenAction.pdf");

// Hapus aksi pembukaan dokumen

document->set_OpenAction(nullptr);


// Simpan dokumen yang diperbarui

document->Save(_dataDir + u"RemoveOpenAction_out.pdf");
}
```

## Cara Menentukan Halaman PDF ketika Melihat Dokumen {#how-to-specify-pdf-page-when-viewing-document}

Ketika melihat file PDF di penampil PDF seperti Adobe Reader, file biasanya terbuka pada halaman pertama. Namun, dimungkinkan untuk mengatur file agar terbuka pada halaman yang berbeda.

Kelas 'XYZExplicitDestination' memungkinkan Anda untuk menentukan halaman dalam file PDF yang ingin Anda buka. Ketika memberikan nilai objek GoToAction ke properti OpenAction kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), dokumen terbuka pada halaman yang ditentukan terhadap objek XYZExplicitDestination. Cuplikan kode berikut menunjukkan cara menentukan halaman sebagai aksi pembukaan dokumen.

```cpp
void HowToSpecifyPDFPageWhenViewingDocument()
{

String _dataDir("C:\\Samples\\");

// Muat file PDF

auto document = new Document(_dataDir + u"SpecifyPageWhenViewing.pdf");

// Dapatkan instance dari halaman kedua dokumen

auto page2 = document->get_Pages()->idx_get(2);

// Buat variabel untuk mengatur faktor zoom dari halaman target

double zoom = 1;

// Buat instance GoToAction

auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(page2);

// Pergi ke halaman 2

action->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(page2, 0, page2->get_Rect()->get_Height(), zoom));

// Atur aksi pembukaan dokumen

document->set_OpenAction(action);

// Simpan dokumen yang diperbarui

document->Save(_dataDir + u"goto2page_out.pdf");
}
```