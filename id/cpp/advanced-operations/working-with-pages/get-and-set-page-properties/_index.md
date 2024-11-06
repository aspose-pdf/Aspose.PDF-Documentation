---
title: Dapatkan dan Atur Properti Halaman
type: docs
weight: 20
url: id/cpp/get-and-set-page-properties/
description: Anda dapat mendapatkan dan mengatur properti halaman dari file PDF Anda menggunakan pustaka C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF untuk C++** memungkinkan Anda membaca dan mengatur properti halaman dalam file PDF di aplikasi C++ Anda. Bagian ini menunjukkan cara mendapatkan jumlah halaman dalam file PDF, mendapatkan informasi tentang properti halaman PDF seperti warna dan mengatur properti halaman, mendapatkan halaman tertentu dari file PDF dan lain-lain.

## Dapatkan Jumlah Halaman dalam File PDF

Saat bekerja dengan dokumen, Anda sering ingin mengetahui berapa banyak halaman yang mereka miliki. Dengan Aspose.PDF ini hanya membutuhkan tidak lebih dari dua baris kode.

Untuk mendapatkan jumlah halaman dalam file PDF:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Gunakan properti Count dari koleksi [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) (dari objek Document) untuk mendapatkan jumlah total halaman dalam dokumen.

Cuplikan kode berikut menunjukkan cara mendapatkan jumlah halaman dari file PDF.

```cpp
void GetNumberOfPages() {
    // Buka dokumen
    String _dataDir("C:\\Samples\\");
    String srcFileName("GetNumberofPages.pdf");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);

    // Dapatkan jumlah halaman
    std::cout << "Jumlah Halaman : " << srcDocument->get_Pages()->get_Count() << std::endl;
}
```

### Dapatkan jumlah halaman tanpa menyimpan dokumen

Terkadang kita membuat file PDF secara langsung dan selama pembuatan file PDF, kita mungkin menemui kebutuhan (membuat Daftar Isi dll.) untuk mendapatkan jumlah halaman file PDF tanpa menyimpan file tersebut ke sistem atau aliran. So untuk memenuhi persyaratan ini, sebuah metode [ProcessParagraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a1773e7b6a887eaddd602073e29939a6f) telah diperkenalkan dalam kelas Document. Silakan lihat cuplikan kode berikut yang menunjukkan langkah-langkah untuk mendapatkan jumlah halaman tanpa menyimpan dokumen.

```cpp
void GetPageCountWithoutSavingTheDocument() {
    // Buat instance Document
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->Add();
    // Buat instance loop
    for (int i = 0; i < 300; i++)
        // Tambahkan TextFragment ke koleksi paragraf dari objek halaman
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Pengujian jumlah halaman"));
    // Proses paragraf dalam file PDF untuk mendapatkan jumlah halaman yang akurat
    document->ProcessParagraphs();
    // Cetak jumlah halaman dalam dokumen
    std::cout << "Jumlah halaman dalam dokumen = " << document->get_Pages()->get_Count();
}
```

## Dapatkan Properti Halaman
### Mengakses Properti Halaman

Kelas [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) menyediakan semua properti terkait dengan halaman PDF tertentu. Semua halaman dari file PDF terkandung dalam koleksi [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Dari situ, dimungkinkan untuk mengakses objek Page individu menggunakan indeks mereka, atau melakukan iterasi melalui koleksi, menggunakan loop foreach, untuk mendapatkan semua halaman. Setelah halaman individu diakses, kita dapat memperoleh propertinya. Potongan kode berikut menunjukkan cara mendapatkan properti halaman.

```cpp
void AccessingPageProperties() {

    String _dataDir("C:\\Samples\\");
    String pdfDocument("GetProperties.pdf");

    // Membuka dokumen
    auto document = MakeObject<Document>(_dataDir + pdfDocument);

    // Mendapatkan halaman tertentu
    auto pdfPage = document->get_Pages()->idx_get(1);
    // Mendapatkan properti halaman
    Console::WriteLine(u"ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_ArtBox()->get_Height(), pdfPage->get_ArtBox()->get_Width(),
        pdfPage->get_ArtBox()->get_LLX(), pdfPage->get_ArtBox()->get_LLY(),
        pdfPage->get_ArtBox()->get_URX(), pdfPage->get_ArtBox()->get_URY());

    Console::WriteLine(u"->get_BleedBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_BleedBox()->get_Height(), pdfPage->get_BleedBox()->get_Width(),
        pdfPage->get_BleedBox()->get_LLX(), pdfPage->get_BleedBox()->get_LLY(),
        pdfPage->get_BleedBox()->get_URX(), pdfPage->get_BleedBox()->get_URY());

    Console::WriteLine(u"get_CropBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_CropBox()->get_Height(), pdfPage->get_CropBox()->get_Width(),
        pdfPage->get_CropBox()->get_LLX(), pdfPage->get_CropBox()->get_LLY(),
        pdfPage->get_CropBox()->get_URX(), pdfPage->get_CropBox()->get_URY());

    Console::WriteLine(u"get_MediaBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_MediaBox()->get_Height(), pdfPage->get_MediaBox()->get_Width(),
        pdfPage->get_MediaBox()->get_LLX(), pdfPage->get_MediaBox()->get_LLY(),
        pdfPage->get_MediaBox()->get_URX(), pdfPage->get_MediaBox()->get_URY());

    Console::WriteLine(u"get_TrimBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_TrimBox()->get_Height(), pdfPage->get_TrimBox()->get_Width(),
        pdfPage->get_TrimBox()->get_LLX(), pdfPage->get_TrimBox()->get_LLY(),
        pdfPage->get_TrimBox()->get_URX(), pdfPage->get_TrimBox()->get_URY());

    Console::WriteLine(u"Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_Rect()->get_Height(), pdfPage->get_Rect()->get_Width(),
        pdfPage->get_Rect()->get_LLX(), pdfPage->get_Rect()->get_LLY(),
        pdfPage->get_Rect()->get_URX(), pdfPage->get_Rect()->get_URY());

    Console::WriteLine(u"Page Number : {0}", pdfPage->get_Number());
    Console::WriteLine(u"Rotate : {0}", pdfPage->get_Rotate());
}
```