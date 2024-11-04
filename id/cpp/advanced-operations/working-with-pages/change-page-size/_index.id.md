---
title: Change PDF Page Size Programmatically 
linktitle: Change PDF Page Size
type: docs
weight: 40
url: /cpp/change-page-size/
description: Ubah Ukuran Halaman dari file PDF Anda menggunakan pustaka C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF adalah format cetak tata letak statis, itulah sebabnya format ini telah menjadi tersebar luas dalam kehidupan bisnis.

Namun, Anda mungkin memiliki tugas ketika Anda perlu mengubah ukuran dokumen PDF Anda karena ukuran halaman lebih besar dari ukuran kertas. Tapi bagaimana?

Jangan khawatir. Di halaman ini, Anda akan menemukan cara untuk menyelesaikan tugas Anda.

Tapi pertama-tama, mari kita ingat bahwa ada Seri Ukuran Halaman.

Ada dua seri ukuran halaman yang banyak diadopsi di dunia.
Tentu saja, ada banyak format, tetapi ada yang paling umum digunakan.
Yang pertama adalah Ukuran Kertas ISO. 
Series A4 digunakan untuk Pencetakan Standar dan Alat Tulis. Kertas ukuran Letter digunakan untuk Poster, Papan Dinding, dll. Amerika Serikat, Kanada, dan sebagian Meksiko mengadopsi Seri Ukuran Halaman kedua dan mereka saat ini adalah satu-satunya negara industri di mana ukuran kertas standar ISO belum banyak digunakan.

Sekarang mari kita lihat bagaimana Aspose.PDF memandu Anda mengubah ukuran halaman menggunakan pustaka C++.

## Ubah Ukuran Halaman PDF

Aspose.PDF untuk C++ memungkinkan Anda mengubah ukuran halaman PDF dengan baris kode sederhana dalam aplikasi C++ Anda. Topik ini menjelaskan cara memperbarui/mengubah dimensi (ukuran) halaman dari file PDF yang ada.

Kelas [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) berisi metode SetPageSize(...) yang memungkinkan Anda mengatur ukuran halaman. Cuplikan kode di bawah ini memperbarui dimensi halaman dalam beberapa langkah mudah:

1. Muat file PDF sumber.
1. Dapatkan halaman-halaman ke dalam objek [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. Dapatkan halaman tertentu.
1.
``` Panggil metode SetPageSize(..) untuk memperbarui dimensinya.
1. Panggil metode Save(..) dari kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) untuk menghasilkan file PDF dengan dimensi halaman yang diperbarui.

Cuplikan kode berikut menunjukkan cara mengubah dimensi halaman PDF menjadi ukuran A4.

```cpp
void ChangePageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");
    String outputFileName("UpdateDimensions_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Dapatkan halaman tertentu
    auto pdfPage = document->get_Pages()->idx_get(1);

    // Atur ukuran halaman sebagai A4 (11.7 x 8.3 in) dan di Aspose.Pdf, 1 inci = 72 poin
    // Jadi dimensi A4 dalam poin akan menjadi (842.4, 597.6)
    pdfPage->SetPageSize(597.6, 842.4);
    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outputFileName);
}
```

## Dapatkan Ukuran Halaman PDF

Anda dapat membaca ukuran halaman PDF dari file PDF yang ada menggunakan Aspose.PDF untuk C++. Contoh kode berikut menunjukkan cara membaca dimensi halaman PDF menggunakan C++.

```cpp
void GetPDFPageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Dapatkan halaman tertentu
    auto page = document->get_Pages()->idx_get(1);

    // Dapatkan informasi tinggi dan lebar halaman
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());
    // Putar halaman pada sudut 90 derajat
    page->set_Rotate(Rotation::on90);
    // Dapatkan informasi tinggi dan lebar halaman
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());

}
```