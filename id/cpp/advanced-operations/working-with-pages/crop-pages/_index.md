---
title: Memotong Halaman PDF secara Pemrograman C++
linktitle: Memotong Halaman
type: docs
weight: 80
url: id/cpp/crop-pages/
description: Anda dapat mendapatkan properti halaman, seperti lebar, tinggi, bleed-, crop-, dan trimbox menggunakan Aspose.PDF untuk C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mendapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop-, dan trimbox. Aspose.PDF memungkinkan Anda mengakses properti ini.

- **Media box**: Media box adalah kotak halaman terbesar. Ini sesuai dengan ukuran halaman (misalnya A4, A5, US Letter, dll.) yang dipilih ketika dokumen dicetak ke PostScript atau PDF. Dengan kata lain, media box menentukan ukuran fisik media di mana dokumen PDF ditampilkan atau dicetak.
- **Bleed box**: Jika dokumen memiliki bleed, PDF juga akan memiliki bleed box. Bleed adalah jumlah warna (atau karya seni) yang meluas melampaui tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong sesuai ukuran ("trimmed"), tinta akan mencapai tepi halaman. Bahkan jika halaman dipotong sedikit melenceng dari tanda potong, tidak akan ada tepi putih yang muncul di halaman.
- **Trim box**: Trim box menunjukkan ukuran akhir dari dokumen setelah dicetak dan dipotong.
- **Art box**: Art box adalah kotak yang digambar di sekitar konten aktual dari halaman-halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF dalam aplikasi lain.
- **Crop box**: Crop box adalah ukuran "halaman" di mana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya konten dari crop box yang ditampilkan di Adobe Acrobat. Untuk deskripsi rinci tentang properti ini, baca spesifikasi Adobe.Pdf, terutama 10.10.1 Page Boundaries.
- **Page.Rect**: perpotongan (umumnya persegi panjang yang terlihat) dari MediaBox dan DropBox. Gambar di bawah ini menggambarkan properti-properti ini.  
Untuk detail lebih lanjut, silakan kunjungi [halaman ini](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

Cuplikan di bawah ini menunjukkan cara memotong halaman:

```cpp
void CropPagesPDF()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("crop_page.pdf");
    String outputFileName("crop_page_out.pdf");

    // Buka dokumen sumber
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    Console::WriteLine(document->get_Pages()->idx_get(1)->get_CropBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_TrimBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_ArtBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_BleedBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_MediaBox());

    // Buat Rectagle Kotak baru
    auto newBox = MakeObject<Rectangle>(200, 220, 2170, 1520);
    document->get_Pages()->idx_get(1)->set_CropBox(newBox);
    document->get_Pages()->idx_get(1)->set_TrimBox(newBox);
    document->get_Pages()->idx_get(1)->set_ArtBox (newBox);
    document->get_Pages()->idx_get(1)->set_BleedBox (newBox);

    // Simpan dokumen yang telah diperbarui
    document->Save(_dataDir + outputFileName);
}
```
In this example we used a sample file [here](crop_page.pdf). Awalnya halaman kami terlihat seperti yang ditunjukkan pada Gambar 1.
![Figure 1. Cropped Page](crop_page.png)

Setelah perubahan, halaman akan terlihat seperti Gambar 2.
![Figure 2. Cropped Page](crop_page2.png)