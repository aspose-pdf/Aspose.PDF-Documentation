```
---
title: Tambahkan Nomor Halaman ke PDF dengan C++
linktitle: Tambahkan Nomor Halaman
type: docs
weight: 100
url: id/cpp/add-page-number/
description: Aspose.PDF untuk C++ memungkinkan Anda menambahkan Cap Nomor Halaman ke file PDF Anda menggunakan kelas PageNumber Stamp.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cara Menambahkan Nomor Halaman ke PDF yang Ada

Semua dokumen harus memiliki nomor halaman di dalamnya. Nomor halaman memudahkan pembaca untuk menemukan bagian-bagian berbeda dari dokumen.
**Aspose.PDF untuk C++** memungkinkan Anda menambahkan nomor halaman dengan PageNumberStamp.

Langkah-langkah berikut dan contoh kode menggambarkan bagaimana menambahkan label penomoran halaman ke dokumen PDF yang ada menggunakan elemen halaman [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) untuk secara otomatis menambahkan nomor halaman ke PDF.

Langkah-langkah untuk Menambahkan Nomor Halaman ke Dokumen PDF yang Ada:

Untuk menambahkan cap nomor halaman, Anda perlu membuat objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dan objek [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) menggunakan properti yang diperlukan.
```

Setelah itu, Anda dapat memanggil metode [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) dari [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) untuk menambahkan cap pada PDF.

Anda juga dapat mengatur atribut font dari cap nomor halaman.

Cuplikan kode berikut menunjukkan kepada Anda cara menambahkan nomor halaman dalam file PDF.

```cpp
void AddPageNumberToPDF() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("PageNumberStamp.pdf");
    String outputFileName("PageNumberStamp_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Buat cap nomor halaman
    auto pageNumberStamp = MakeObject<PageNumberStamp>();
    //// Apakah cap tersebut adalah latar belakang
    //pageNumberStamp.Background = false;
    //pageNumberStamp.Format = "Halaman # dari " + pdfDocument.Pages.Count;
    //pageNumberStamp.BottomMargin = 10;
    //pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
    //pageNumberStamp.StartingNumber = 1;

    //// Atur properti teks
    //pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
    //pageNumberStamp.TextState.FontSize = 14.0F;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
    //pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

    // Tambahkan cap ke halaman tertentu
    document->get_Pages()->idx_get(1)->AddStamp(pageNumberStamp);

    // Simpan dokumen keluaran
    document->Save(_dataDir+ outputFileName);
}
```

## Contoh Langsung

[Tambahkan nomor halaman PDF](https://products.aspose.app/pdf/page-number) adalah aplikasi web online gratis yang memungkinkan Anda menyelidiki bagaimana fungsionalitas penambahan nomor halaman bekerja.

[![Cara menambahkan nomor halaman dalam pdf menggunakan C++](page_number.png)](https://products.aspose.app/pdf/page-number)

## Tambah/Hapus Penomoran Bates

**Penomoran Bates** (juga dikenal sebagai pencap Bates) digunakan dalam bidang hukum, medis, dan bisnis untuk menempatkan angka pengenal dan/atau tanda tanggal/waktu pada gambar dan dokumen saat dipindai atau diproses, misalnya, selama tahap penemuan persiapan persidangan atau mengidentifikasi tanda terima bisnis. Proses ini menyediakan identifikasi, perlindungan, dan penomoran berurutan otomatis dari gambar atau dokumen.

Aspose.PDF saat ini memiliki dukungan terbatas untuk Penomoran Bates. Fungsionalitas ini akan diperbarui sesuai permintaan pelanggan.

### Cara menghapus penomoran Bates

```cpp
void WorkingWithPages::RemoveBatesNubmering()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("BatesNumbering.pdf");
    String outputFileName("BatesNumbering_out.pdf");
    String customSubtype("BatesN");
    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    for (auto page : document->get_Pages())
    {
        auto coll = page->get_Artifacts();
        for (auto batesNum : coll)
        {
        if (batesNum->get_CustomSubtype() == customSubtype)
            page->get_Artifacts()->Delete(batesNum);
        }
    }

    // Simpan dokumen keluaran
    document->Save(_dataDir + outputFileName);
}
```