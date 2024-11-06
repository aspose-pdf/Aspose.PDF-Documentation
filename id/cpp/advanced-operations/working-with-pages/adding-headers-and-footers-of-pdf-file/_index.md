---
title: Tambahkan Header dan Footer ke PDF
linktitle: Tambahkan Header dan Footer ke PDF
type: docs
weight: 70
url: id/cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF untuk C++ memungkinkan Anda menambahkan header dan footer ke file PDF Anda menggunakan kelas TextStamp.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF untuk C++** memungkinkan Anda menambahkan header dan footer di file PDF yang sudah ada. Anda dapat menambahkan gambar atau teks ke dokumen PDF. Juga, coba tambahkan header yang berbeda dalam satu file PDF dengan C++.

## Menambahkan Teks di Header File PDF

Anda dapat menggunakan kelas [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) untuk menambahkan teks di header file PDF. TextStamp class menyediakan properti yang diperlukan untuk membuat stempel berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan teks di header, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan teks di header PDF.

Anda perlu mengatur properti TopMargin sedemikian rupa sehingga menyesuaikan teks di area header PDF Anda. Anda juga perlu mengatur HorizontalAlignment ke Center dan VerticalAlignment ke Top.

Cuplikan kode berikut menunjukkan kepada Anda bagaimana menambahkan teks di header file PDF dengan C++.

```cpp
void AddingTextInHeaderOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinHeader.pdf");
    String outputFileName("TextinHeader_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create header
    auto textStamp = MakeObject<TextStamp>(u"Header Text");

    // Set properties of the stamp
    textStamp->set_TopMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // Add header on all pages
    for(auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```
## Menambahkan Teks di Footer File PDF

Anda dapat menggunakan kelas TextStamp untuk menambahkan teks di footer file PDF. Kelas TextStamp menyediakan properti yang diperlukan untuk membuat stempel berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan teks di footer, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan teks di footer PDF.

{{% alert color="primary" %}}

Anda perlu mengatur properti Bottom Margin sedemikian rupa sehingga menyesuaikan teks di area footer PDF Anda. Anda juga perlu mengatur HorizontalAlignment ke Center dan VerticalAlignment ke Bottom

{{% /alert %}}

Cuplikan kode berikut menunjukkan cara menambahkan teks di footer file PDF dengan C++.

```cpp
void AddingTextInFooterOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinFooter.pdf");
    String outputFileName("TextinFooter_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Buat footer
    auto textStamp = MakeObject<TextStamp>(u"Teks Footer");

    // Atur properti stempel
    textStamp->set_BottomMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Bottom);

    // Tambahkan footer di semua halaman
    for (auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outputFileName);
}
```

## Menambahkan Gambar di Header File PDF

Anda dapat menggunakan kelas [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) untuk menambahkan gambar di header file PDF. Kelas Image Stamp menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan gambar di header, Anda perlu membuat objek Document dan objek Image Stamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan gambar di header file PDF.

Cuplikan kode berikut menunjukkan cara menambahkan gambar di header file PDF dengan C++.

```cpp
void AddingImageInHeaderOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinHeader.pdf");
    String outputFileName("ImageinHeader_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Buat header
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // Atur properti dari stempel
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment (VerticalAlignment::Top);

    // Tambahkan header pada semua halaman
    for(auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outputFileName);
}
```

## Menambahkan Gambar di Footer File PDF

Anda dapat menggunakan kelas Image Stamp untuk menambahkan gambar di footer file PDF. Kelas Image Stamp menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan gambar di footer, Anda perlu membuat objek Document dan objek Image Stamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode AddStamp dari Page untuk menambahkan gambar di footer PDF.

Anda perlu mengatur properti [BottomMargin](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.stamp#aeab91949cf3eb473018b31a74fed7173) sedemikian rupa sehingga menyesuaikan gambar di area footer PDF Anda. Anda juga perlu mengatur [HorizontalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#aefec9c0bf30ee5e6fb2640e69aed6cd9) ke `Center` dan [VerticalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ad4956d03096fc515eaa34319a6bf636a) ke `Bottom`.

Cuplikan kode berikut menunjukkan kepada Anda bagaimana cara menambahkan gambar di footer file PDF dengan C++.

```cpp
void AddingImageInFooterOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinFooter.pdf");
    String outputFileName("ImageinFooter_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create header
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // Set properties of the stamp
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // Add header on all pages
    for (auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```

## Menambahkan Header yang Berbeda dalam Satu File PDF

Kita tahu bahwa kita dapat menambahkan TextStamp di bagian Header/Footer dokumen dengan menggunakan properti TopMargin atau Bottom Margin, tetapi terkadang kita mungkin memiliki kebutuhan untuk menambahkan beberapa header/footer dalam satu dokumen PDF. **Aspose.PDF untuk C++** menjelaskan cara melakukan ini.

Untuk memenuhi persyaratan ini, kita akan membuat objek TextStamp individu (jumlah objek tergantung pada jumlah Header/Footer yang diperlukan) dan akan menambahkannya ke dokumen PDF. Kita juga dapat menentukan informasi pemformatan yang berbeda untuk setiap objek cap. Dalam contoh berikut, kita telah membuat objek Document dan tiga objek TextStamp dan kemudian kita menggunakan metode [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) dari Page untuk menambahkan teks di bagian header dari PDF. Cuplikan kode berikut menunjukkan cara menambahkan gambar di footer dari file PDF dengan Aspose.PDF untuk C++.

```cpp
void AddingDifferentHeadersInOnePDFFile()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("multiheader.pdf");
    String outputFileName("multiheader_out.pdf");

    // Buka dokumen sumber
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Buat tiga cap
    auto stamp1 = MakeObject<TextStamp>("Header 1");
    auto stamp2 = MakeObject<TextStamp>("Header 2");
    auto stamp3 = MakeObject<TextStamp>("Header 3");

    // Setel penempatan cap (letakkan cap di bagian atas halaman, terpusat secara horizontal)
    stamp1->set_VerticalAlignment(VerticalAlignment::Top);
    stamp1->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Tentukan gaya font sebagai Bold
    stamp1->get_TextState()->set_FontStyle(FontStyles::Bold);
    // Setel informasi warna depan teks sebagai merah
    stamp1->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Tentukan ukuran font sebagai 14
    stamp1->get_TextState()->set_FontSize(14);

    // Sekarang kita perlu mengatur penempatan vertikal dari objek cap kedua sebagai Atas
    stamp2->set_VerticalAlignment(VerticalAlignment::Top);
    // Setel informasi penempatan horizontal untuk cap sebagai Terpusat
    stamp2->set_HorizontalAlignment (HorizontalAlignment::Center);
    // Setel faktor zoom untuk objek cap
    stamp2->set_Zoom(10);

    // Setel pemformatan dari objek cap ketiga
    // Tentukan informasi penempatan vertikal untuk objek cap sebagai Atas
    stamp3->set_VerticalAlignment(VerticalAlignment::Top);
    // Setel informasi penempatan horizontal untuk objek cap sebagai Terpusat
    stamp3->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Setel sudut rotasi untuk objek cap
    stamp3->set_RotateAngle(35);
    // Setel pink sebagai warna latar belakang untuk cap
    stamp3->get_TextState()->set_BackgroundColor(Color::get_Pink());
    // Ubah informasi wajah font untuk cap menjadi Verdana
    stamp3->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));

    // Cap pertama ditambahkan pada halaman pertama;
    document->get_Pages()->idx_get(1)->AddStamp(stamp1);
    // Cap kedua ditambahkan pada halaman kedua;
    document->get_Pages()->idx_get(2)->AddStamp(stamp2);
    // Cap ketiga ditambahkan pada halaman ketiga.
    document->get_Pages()->idx_get(3)->AddStamp(stamp3);

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outputFileName);
}
```