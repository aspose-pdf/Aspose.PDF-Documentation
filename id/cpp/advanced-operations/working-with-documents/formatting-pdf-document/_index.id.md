---
title: Memformat Dokumen PDF menggunakan C++
linktitle: Memformat Dokumen PDF
type: docs
weight: 20
url: /cpp/formatting-pdf-document/
description: Buat dan format Dokumen PDF dengan Aspose.PDF untuk C++. Gunakan potongan kode berikut untuk menyelesaikan tugas Anda.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Memformat Dokumen PDF

### Mendapatkan Jendela Dokumen dan Properti Tampilan Halaman

Topik ini membantu Anda memahami cara mendapatkan properti jendela dokumen, aplikasi penampil, dan bagaimana halaman ditampilkan. Untuk mengatur properti ini, buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Sekarang Anda dapat mengatur properti objek Document, seperti:

- CenterWindow – Memusatkan jendela dokumen di layar. Default: false.
- Direction – Urutan membaca. Ini menentukan bagaimana halaman ditata ketika ditampilkan berdampingan. Default: kiri ke kanan.
- DisplayDocTitle – Menampilkan judul dokumen di bilah judul jendela dokumen.  Default: false (judul ditampilkan).
- HideMenuBar – Sembunyikan atau tampilkan menu bar jendela dokumen. Default: false (menu bar ditampilkan).
- HideToolBar – Sembunyikan atau tampilkan toolbar jendela dokumen. Default: false (toolbar ditampilkan).
- HideWindowUI – Sembunyikan atau tampilkan elemen jendela dokumen seperti scroll bar. Default: false (elemen UI ditampilkan).
- NonFullScreenPageMode – Bagaimana dokumen ditampilkan saat tidak dalam mode layar penuh.
- PageLayout – Tata letak halaman.
- PageMode – Bagaimana dokumen ditampilkan saat pertama kali dibuka. Opsi yang tersedia adalah tampilkan thumbnail, layar penuh, tampilkan panel lampiran.

Cuplikan kode berikut menunjukkan kepada Anda cara mendapatkan properti menggunakan kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void GetDocumentWindowAndPageDisplayProperties()
{
    // String untuk nama path.
    String _dataDir("C:\\Samples\\");
    // String untuk nama file.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Dapatkan berbagai properti dokumen
    // Posisi jendela dokumen - Default: false
    Console::WriteLine(u"CenterWindow : {0}", document->get_CenterWindow());

    // Urutan membaca yang dominan; menentukan posisi halaman
    // Saat ditampilkan berdampingan - Default: L2R
    Console::WriteLine(u"Direction : {0}", document->get_Direction());

    // Apakah bilah judul jendela harus menampilkan judul dokumen
    // Jika false, bilah judul menampilkan nama file PDF - Default: false
    Console::WriteLine(u"DisplayDocTitle : {0}", document->get_DisplayDocTitle());

    // Apakah mengubah ukuran jendela dokumen agar sesuai dengan ukuran
    // Halaman pertama yang ditampilkan - Default: false
    Console::WriteLine(u"FitWindow : {0}", document->get_FitWindow());

    // Apakah menyembunyikan bilah menu aplikasi penampil - Default: false
    Console::WriteLine(u"HideMenuBar : {0}", document->get_HideMenubar());

    // Apakah menyembunyikan bilah alat aplikasi penampil - Default: false
    Console::WriteLine(u"HideToolBar : {0}", document->get_HideToolBar());

    // Apakah menyembunyikan elemen UI seperti scroll bar
    // Dan hanya menampilkan konten halaman - Default: false
    Console::WriteLine(u"HideWindowUI : {0}", document->get_HideWindowUI());

    // Mode halaman dokumen. Bagaimana menampilkan dokumen saat keluar dari mode layar penuh.
    Console::WriteLine(u"NonFullScreenPageMode : {0}", document->get_NonFullScreenPageMode());

    // Tata letak halaman yaitu halaman tunggal, satu kolom
    Console::WriteLine(u"PageLayout : {0}", document->get_PageLayout());

    // Bagaimana dokumen harus ditampilkan saat dibuka
    // Misalnya tampilkan thumbnail, layar penuh, tampilkan panel lampiran
    Console::WriteLine(u"pageMode : {0}", document->get_PageMode());
}
```
### Setel Jendela Dokumen dan Properti Tampilan Halaman

Topik ini menjelaskan cara menyetel properti jendela dokumen, aplikasi penampil, dan tampilan halaman. Untuk menyetel properti yang berbeda ini:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Setel properti dokumen yang berbeda:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

1. [Simpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) file PDF yang diperbarui menggunakan metode Save.

Properti yang tersedia adalah:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Masing-masing digunakan dan dijelaskan dalam kode di bawah ini. Berikut ini - potongan kode menunjukkan cara mengatur properti menggunakan kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void SetDocumentWindowAndPageDisplayProperties()
{
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");
    // String untuk nama file.
    String inputFileName("sample.pdf");
    String outputFileName("sample_page_display_properties.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Mengatur properti dokumen yang berbeda
    // Tentukan untuk memposisikan jendela dokumen - Default: false
    document->set_CenterWindow(true);

    // Urutan membaca yang dominan; menentukan posisi halaman
    // Ketika ditampilkan berdampingan - Default: L2R
    document->set_Direction(Direction::R2L);

    // Tentukan apakah bilah judul jendela harus menampilkan judul dokumen
    // Jika false, bilah judul menampilkan nama file PDF - Default: false
    document->set_DisplayDocTitle(true);

    // Tentukan apakah untuk mengubah ukuran jendela dokumen agar sesuai dengan ukuran
    // Halaman pertama yang ditampilkan - Default: false
    document->set_FitWindow(true);

    // Tentukan apakah untuk menyembunyikan bilah menu dari aplikasi penampil - Default: false
    document->set_HideMenubar(true);

    // Tentukan apakah untuk menyembunyikan bilah alat dari aplikasi penampil - Default: false
    document->set_HideToolBar(true);

    // Tentukan apakah untuk menyembunyikan elemen UI seperti bilah gulir
    // Dan hanya menampilkan konten halaman - Default: false
    document->set_HideWindowUI(true);

    // Mode halaman dokumen. tentukan cara menampilkan dokumen saat keluar dari mode layar penuh.
    document->set_NonFullScreenPageMode(PageMode::UseOC);

    // Tentukan tata letak halaman yaitu satu halaman, satu kolom
    document->set_PageLayout(PageLayout::TwoColumnLeft);

    // Tentukan bagaimana dokumen harus ditampilkan saat dibuka
    // Yaitu menampilkan thumbnail, layar penuh, menampilkan panel lampiran
    document->set_PageMode(PageMode::UseThumbs);

    // Simpan file PDF yang diperbarui
    document->Save(_dataDir + outputFileName);
}
```
### Menyematkan Font dalam file PDF yang sudah ada

Pembaca PDF mendukung [inti dari 14 font](https://en.wikipedia.org/wiki/PDF#Text) sehingga dokumen dapat ditampilkan dengan cara yang sama terlepas dari platform tempat dokumen ditampilkan. Ketika PDF berisi font yang bukan salah satu dari 14 font inti, sematkan font ke file PDF untuk menghindari penggantian font.

Aspose.PDF untuk C++ mendukung penyematan font dalam file PDF yang sudah ada. Anda dapat menyematkan font lengkap atau subset dari font tersebut. Untuk menyematkan font, buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Kemudian gunakan kelas [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.font) untuk menyematkan font ke dalam file PDF. Untuk menyematkan font penuh, gunakan properti IsEmbeded dari kelas Font; untuk menggunakan subset dari font, gunakan properti IsSubset.

{{% alert color="primary" %}}

Subset font hanya menyematkan karakter yang digunakan dan berguna ketika font digunakan untuk kalimat pendek atau slogan, misalnya ketika font perusahaan digunakan untuk logo, tetapi tidak untuk teks badan. Menggunakan subset mengurangi ukuran file dari output PDF. Namun, jika font kustom digunakan untuk teks isi, sematkan secara keseluruhan.

{{% /alert %}}

Cuplikan kode berikut menunjukkan cara menyematkan font dalam file PDF.

### Menyematkan Font Tipe Standar 1

Ada dokumen PDF yang menggunakan font dari set khusus yang disebut "Font Tipe Standar 1". Set ini mencakup 14 font dan penyematan jenis font ini memerlukan penggunaan bendera khusus yaitu [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a8f1a88eef22e05ee9ee22a79db9cb9f6).

Berikut adalah cuplikan kode yang dapat digunakan untuk mendapatkan dokumen dengan semua font disematkan termasuk Font Tipe Standar 1:

```cpp
void EmbeddingStandardType1Fonts()
{

    // String untuk nama path.
    String _dataDir("C:\\Samples\\");
    // String untuk nama file.
    String inputFileName("sample.pdf");
    String outputFileName("embedded-fonts-updated_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Set properti EmbedStandardFonts dari dokumen
    document->set_EmbedStandardFonts(true);
    for (auto page : document->get_Pages())
    {
        auto fonts = page->get_Resources()->get_Fonts();
        if (fonts != nullptr)
        {
            for (auto pageFont : fonts)
            {
                // Periksa apakah font sudah disematkan
                if (!pageFont->get_IsEmbedded())
                {
                    pageFont->set_IsEmbedded(true);
                }
            }
        }
    }
    document->Save(_dataDir + outputFileName);
}
```
### Menyematkan Font saat membuat PDF

Jika Anda perlu menggunakan font lain selain dari 14 core fonts yang didukung oleh Adobe Reader, Anda harus menyematkan deskripsi font saat membuat file Pdf. Jika informasi font tidak disematkan, Adobe Reader akan mengambilnya dari Sistem Operasi jika terinstal di sistem, atau akan membangun font pengganti sesuai dengan deskriptor font dalam Pdf.

>Harap dicatat bahwa font yang disematkan harus diinstal di mesin host yaitu dalam kasus kode berikut, font 'Univers Condensed' terinstal di sistem.

Kami menggunakan properti IsEmbedded dari kelas Font untuk menyematkan informasi font ke dalam file Pdf. Menyetel nilai properti ini ke 'True' akan menyematkan seluruh file font ke dalam Pdf, dengan mengetahui fakta bahwa ini akan meningkatkan ukuran file Pdf. Berikut adalah cuplikan kode yang dapat digunakan untuk menyematkan informasi font ke dalam Pdf.

```cpp
void EmbeddingFontsWhileCreatingPDF()
{
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");
    // String untuk nama file.
    String inputFileName("sample.pdf");
    String outputFileName("EmbedFontWhileDocCreation_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Buat bagian dalam objek Pdf
    auto page = document->get_Pages()->Add();

    auto fragment = MakeObject<TextFragment>("");
    auto segment = MakeObject <TextSegment>(u"This is a sample text using Custom font.");

    auto ts = MakeObject<TextState>();

    ts->set_Font(FontRepository::FindFont(u"Arial"));
    ts->get_Font()->set_IsEmbedded(true);
    segment->set_TextState(ts);
    fragment->get_Segments()->Add(segment);
    page->get_Paragraphs()->Add(fragment);

    // Simpan Dokumen PDF
    document->Save(_dataDir);
}
```

### Atur Nama Font Default saat Menyimpan PDF

Ketika dokumen PDF mengandung font yang tidak tersedia di dalam dokumen itu sendiri dan pada perangkat, API mengganti font tersebut dengan font default. Ketika font tersedia (terpasang pada perangkat atau tertanam dalam dokumen), PDF keluaran harus memiliki font yang sama (tidak boleh diganti dengan font default). Nilai font default harus berisi nama font (bukan jalur ke file font). Apose.PDF untuk C++ mengimplementasikan fitur untuk mengatur nama font default saat menyimpan dokumen sebagai PDF. Cuplikan kode berikut dapat digunakan untuk mengatur font default:

```cpp
void SetDefaultFontNameWhileSavingPDF()
{
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");
    // String untuk nama file.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);

    auto pdfSaveOptions = MakeObject<PdfSaveOptions>();

    // Tentukan Nama Font Default
    pdfSaveOptions->set_DefaultFontName(newName);
    document->Save(_dataDir + outputFileName, pdfSaveOptions);
}
```

### Dapatkan Semua Font dari Dokumen PDF

Jika Anda ingin mendapatkan semua font dari dokumen PDF, Anda dapat menggunakan metode [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a2e22a508e8baef176dfc34734cf0def9).GetAllFonts() yang disediakan dalam kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Silakan cek cuplikan kode berikut untuk mendapatkan semua font dari dokumen PDF yang ada:

```cpp
void GetAllFontsFromPDFdocument()
{
    // String untuk nama path.
    String _dataDir("C:\\Samples\\");
    // String untuk nama file.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);
    auto fonts = document->get_FontUtilities()->GetAllFonts();
    for (auto font : fonts)
    {
        std::cerr << font->get_FontName() << std::endl;
    }
}
```

### Dapatkan Peringatan untuk Penggantian Font

Aspose.PDF untuk C++ menyediakan metode untuk mendapatkan notifikasi tentang penggantian font untuk menangani kasus penggantian font. Potongan kode di bawah ini menunjukkan cara menggunakan fungsionalitas yang sesuai.

```cpp
void GetWarningsForFontSubstitution()
{
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    document->FontSubstitution = Aspose::Pdf::Document::FontSubstitutionHandler(OnFontSubstitution);
}
```

Metode [OnFontSubstitution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac776d8736d430532bdaa530a36eb51a0) terdaftar di bawah ini.

```cpp
void OnFontSubstitution(Aspose::Pdf::Text::Font &font, Aspose::Pdf::Text::Font& newFont) {
    std::cout << "Peringatan: Font " << font.get_FontName() 
            << " diganti dengan font lain -> " 
            << newFont.get_FontName() << std::endl;
}
```

### Tingkatkan Penyematan Font menggunakan FontSubsetStrategy

Fitur untuk menyematkan font sebagai subset dapat dicapai dengan menggunakan properti IsSubset, tetapi terkadang Anda ingin mengurangi set font yang sepenuhnya disematkan ke hanya subset yang digunakan dalam dokumen. [Aspose.Pdf.Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) memiliki properti [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.i_document_font_utilities/) yang mencakup metode SubsetFonts(FontSubsetStrategy subsetStrategy). Dalam metode SubsetFonts(), parameter subsetStrategy membantu untuk menyetel strategi subset. FontSubsetStrategy mendukung dua varian subset font berikut.

- SubsetAllFonts - Ini akan membuat subset semua font yang digunakan dalam dokumen.
- SubsetEmbeddedFontsOnly - Ini akan membuat subset hanya font yang sepenuhnya disematkan ke dalam dokumen.

Cuplikan kode berikut menunjukkan cara mengatur FontSubsetStrategy:

```cpp
void ImproveFontsEmbeddingUsingFontSubsetStrategy()
{
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String inputFileName("sample.pdf");
    // String untuk nama file.
    String outputFileName("sample_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    // Semua font akan disematkan sebagai subset ke dalam dokumen dalam kasus SubsetAllFonts.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetAllFonts);
    // Subset font akan disematkan untuk font yang sepenuhnya disematkan tetapi font yang tidak disematkan ke dalam dokumen tidak akan terpengaruh.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetEmbeddedFontsOnly);
    document->Save(_dataDir + outputFileName);
}
```
### Get-Set Faktor Zoom dari File PDF

Kadang-kadang, Anda ingin mengatur faktor zoom dari dokumen PDF. Dengan Aspose.PDF untuk C++, Anda dapat mengatur nilai faktor zoom dengan metode [set_OpenAction(…)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#abb5c84979077034d06a673409b666e21) dari kelas Document.

Properti Destination dari kelas [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action/) memungkinkan Anda untuk mendapatkan nilai zoom yang terkait dengan file PDF. Demikian pula, ini dapat digunakan untuk mengatur faktor zoom dari file.

#### Mengatur Faktor Zoom

Cuplikan kode berikut menunjukkan cara mengatur faktor zoom dari file PDF.

```cpp
void SetZoomFactor() {
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String inputFileName("sample.pdf");
    // String untuk nama file.
    String outputFileName("Zoomed_pdf_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 0, 0, .5));

    document->set_OpenAction(action);
    // Simpan dokumen
    document->Save(_dataDir + outputFileName);
}
```

#### Get Zoom Factor

Dapatkan faktor zoom di file PDF Anda menggunakan Aspose.PDF untuk C++.

Cuplikan kode berikut menunjukkan cara mendapatkan faktor zoom file PDF:

```cpp
void GetZoomFactor() 
{
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Buat objek GoToAction
    auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(document->get_OpenAction());

    // Dapatkan faktor Zoom dari file PDF
    auto zoom = System::DynamicCast<Aspose::Pdf::Annotations::XYZExplicitDestination>(action->get_Destination());
    Console::WriteLine(zoom->get_Zoom()); // Nilai zoom Dokumen;
}
```

### Setting Print Dialog Preset Properties

Aspose.PDF untuk C++ memungkinkan pengaturan properti Print Dialog Preset dari dokumen PDF. Itu memungkinkan Anda untuk mengubah properti DuplexMode untuk dokumen PDF yang secara default diatur ke simplex. Ini dapat dicapai menggunakan dua metodologi berbeda seperti yang ditunjukkan di bawah ini.

```cpp
void SettingPrintDialogPresetProperties()
{
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");
    // String untuk nama file.
    String outputFileName("SettingPrintDialogPresetProperties.pdf");

    auto document = MakeObject<Document>();
    document->get_Pages()->Add();
    document->set_Duplex(PrintDuplex::DuplexFlipLongEdge);
    document->Save(_dataDir + outputFileName);
}
```

### Mengatur Properti Preset Dialog Cetak menggunakan Editor Konten PDF

```cpp
void SettingPrintDialogPresetPropertiesUsingContentEditor() {
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String inputFileName("sample.pdf");
    String outputFileName("SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto contentEditor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    contentEditor->BindPdf(outputFileName);
    if ((contentEditor->GetViewerPreference() & Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge) > 0)
    {
    std::cout << "File ini memiliki duplex flip short edge" << std::endl;
    }

    contentEditor->ChangeViewerPreference(Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge);
    contentEditor->Save(_dataDir + outputFileName);
}
```