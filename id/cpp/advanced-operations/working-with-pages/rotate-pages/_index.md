---
title: Memutar Halaman PDF Menggunakan C++
linktitle: Memutar Halaman PDF
type: docs
weight: 50
url: /id/cpp/rotate-pages/
description: Topik ini menjelaskan cara memutar orientasi halaman dalam file PDF yang sudah ada secara terprogram dengan C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Topik ini menjelaskan cara memperbarui atau mengubah orientasi halaman dari halaman dalam file PDF yang sudah ada secara terprogram dengan C++.

## Mengubah Orientasi Halaman

Aspose.PDF untuk C++ memungkinkan Anda untuk mengubah orientasi halaman dari landscape ke portrait dan sebaliknya. Untuk mengubah orientasi halaman, atur MediaBox halaman menggunakan potongan kode berikut. Anda juga dapat mengubah orientasi halaman dengan mengatur sudut rotasi menggunakan metode Rotate().

```cpp
void ChangePageOrientation() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Membuka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {

        auto r = page->get_MediaBox();
        double newHeight = r->get_Width();
        double newWidth = r->get_Height();
        double newLLX = r->get_LLX();

        // Kita harus memindahkan halaman ke atas untuk mengkompensasi perubahan ukuran halaman
        // (tepi bawah halaman adalah 0,0 dan informasi biasanya ditempatkan dari
        // Bagian atas halaman. Itulah mengapa kita memindahkan tepi bawah ke atas pada perbedaan antara
        // Tinggi lama dan baru.

        double newLLY = r->get_LLY() + (r->get_Height() - newHeight);
        page->set_MediaBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
        // Terkadang kita juga perlu mengatur CropBox (jika diatur dalam file asli)
        page->set_CropBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

        // Mengatur sudut rotasi halaman
        page->set_Rotate(Rotation::on90);
    }

    // Menyimpan file output
    document->Save(_dataDir + outputFileName);
}
```

## Menyesuaikan Konten Halaman dengan Orientasi Halaman Baru

Harap dicatat bahwa saat menggunakan potongan kode di atas, beberapa konten dokumen mungkin terpotong karena tinggi halaman berkurang. Untuk menghindari ini, tingkatkan lebar secara proporsional dan biarkan tinggi tetap. Contoh perhitungan:

```cpp
void FittingPageContentToNewPageOrientation()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {
        auto r = page->get_MediaBox();
        // Tinggi baru sama
        double newHeight = r->get_Height();
        // Lebar baru diperluas secara proporsional untuk membuat orientasi lanskap
        // (kami berasumsi bahwa orientasi sebelumnya adalah potret)
        double newWidth = r->get_Height() * r->get_Height() / r->get_Width();

        // ...

    }
}
```

Selain pendekatan di atas, pertimbangkan untuk menggunakan facade PdfPageEditor yang dapat menerapkan zoom pada konten halaman.

```cpp
void ZoomPageContent()
{

    String _dataDir("C:\\Samples\\");
    String inputFileName("ZoomToPageContents.pdf");
    String outputFileName("ZoomToPageContents_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Dapatkan wilayah persegi panjang dari halaman pertama PDF
    auto rect = document->get_Pages()->idx_get(1)->get_Rect();

    // Instansiasi objek PdfPageEditor
    auto ppe = MakeObject<Aspose::Pdf::Facades::PdfPageEditor>();
    // Ikat PDF sumber
    ppe->BindPdf(_dataDir + inputFileName);
    // Atur koefisien zoom
    ppe->set_Zoom ((float)(rect->get_Width() / rect->get_Height()));
    // Perbarui ukuran halaman
    ppe->set_PageSize(MakeObject<PageSize>((float)rect->get_Height(), (float)rect->get_Width()));

    // Simpan file keluaran
    document->Save(_dataDir + outputFileName);
}
```