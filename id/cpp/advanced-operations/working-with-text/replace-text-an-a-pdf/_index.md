---
title: Ganti Teks dalam PDF menggunakan C++
linktitle: Ganti Teks dalam PDF
type: docs
weight: 40
url: /id/cpp/replace-text-in-pdf/
description: Pelajari lebih lanjut tentang berbagai cara mengganti dan menghapus teks dari PDF. Aspose.PDF memungkinkan penggantian teks di wilayah tertentu atau dengan ekspresi reguler.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Terkadang muncul tugas untuk mengoreksi atau mengganti teks dalam dokumen PDF. Mencoba melakukannya secara manual akan menjadi tugas yang menakutkan, jadi inilah solusi untuk masalah tersebut.

Sejujurnya, mengedit file PDF bukanlah tugas yang mudah. Jadi, situasi di mana Anda perlu mencari dan mengganti satu kata dengan kata lain saat mengedit file PDF, akan sangat sulit karena akan memakan waktu lama untuk melakukannya. Selain itu, Anda mungkin menghadapi banyak masalah dengan keluaran Anda, seperti pemformatan atau font yang rusak. Jika Anda ingin dengan mudah mencari dan mengganti teks dalam file PDF, kami sarankan Anda menggunakan perangkat lunak pustaka Aspose.Pdf karena ini akan menyelesaikan pekerjaan dalam hitungan menit.

Dalam artikel ini, kami akan menunjukkan kepada Anda bagaimana menemukan dan mengganti teks dalam file PDF Anda dengan sukses menggunakan Aspose.PDF untuk C++.

## Ganti Teks di semua halaman dokumen PDF

{{% alert color="primary" %}}

Anda dapat mencoba menemukan dan mengganti teks dalam dokumen menggunakan Aspose.PDF dan mendapatkan hasilnya secara online di [tautan ini](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Untuk mengganti teks di semua halaman dokumen PDF, pertama-tama Anda perlu menggunakan TextFragmentAbsorber untuk menemukan frasa tertentu yang ingin Anda ganti. Setelah itu, Anda perlu melalui semua TextFragments untuk mengganti teks dan mengubah atribut lainnya. Setelah Anda selesai melakukannya, Anda hanya perlu menyimpan PDF keluaran menggunakan metode Save dari objek Document. Cuplikan kode berikut menunjukkan kepada Anda cara mengganti teks di semua halaman dokumen PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextOnAllPages() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Buat objek TextAbsorber untuk menemukan semua instance dari frasa pencarian input
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("Web");

    // Terima absorber untuk halaman pertama dokumen
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Dapatkan fragmen teks yang diekstrak ke dalam koleksi
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop melalui fragmen
    for (auto textFragment : textFragmentCollection) {
        // Perbarui teks dan properti lainnya
        textFragment->set_Text(u"World Wide Web");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Simpan file PDF yang diperbarui
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Ganti Teks di wilayah halaman tertentu

Untuk mengganti teks di wilayah halaman tertentu, pertama-tama kita perlu membuat objek TextFragmentAbsorber, tentukan wilayah halaman menggunakan properti TextSearchOptions.Rectangle dan kemudian iterasi melalui semua TextFragments untuk mengganti teks. Setelah operasi ini selesai, kita hanya perlu menyimpan PDF keluaran menggunakan metode Save dari objek Document. Potongan kode berikut menunjukkan cara mengganti teks di semua halaman dokumen PDF.

```cpp
void ReplaceTextInParticularRegion() {

    String _dataDir("C:\\Samples\\");

    // muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // buat objek TextFragment Absorber
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // cari teks dalam batas halaman
    textFragmentAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);

    // tentukan wilayah halaman untuk Opsi Pencarian Teks
    textFragmentAbsorber->get_TextSearchOptions()->set_Rectangle(new Rectangle(100, 700, 400, 770));

    // cari teks dari halaman pertama file PDF
    document->get_Pages()->idx_get(1)->Accept(textFragmentAbsorber);

    // iterasi melalui setiap TextFragment
    for (auto tf : textFragmentAbsorber->get_TextFragments()) {
        // ganti teks dengan "---"
        tf->set_Text(u"---");
    }

    // Simpan file PDF yang telah diperbarui
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Ganti Teks Berdasarkan Ekspresi Reguler

Jika Anda ingin mengganti beberapa frasa berdasarkan ekspresi reguler, Anda pertama-tama perlu menemukan semua frasa yang sesuai dengan ekspresi reguler tersebut menggunakan TextFragmentAbsorber. Anda harus mengoper ekspresi reguler sebagai parameter ke konstruktor TextFragmentAbsorber. Anda juga perlu membuat objek TextSearchOptions yang menentukan apakah ekspresi reguler digunakan atau tidak. Setelah Anda mendapatkan frasa yang cocok dalam TextFragments, Anda perlu melalui semuanya dan memperbaruinya sesuai kebutuhan. Terakhir, Anda perlu menyimpan PDF yang diperbarui menggunakan metode Save dari objek Document. Cuplikan kode berikut menunjukkan cara mengganti teks berdasarkan ekspresi reguler.

```cpp
void ReplaceTextWithRegularExpression() {

    String _dataDir("C:\\Samples\\");

    // muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"Sample.pdf");
    // Buat objek TextAbsorber untuk menemukan semua contoh frasa pencarian input
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("\\d{4}-\\d{4}");
    // seperti 1999-2000

    // Atur opsi pencarian teks untuk menentukan penggunaan ekspresi reguler
    auto textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Terima absorber untuk halaman pertama dokumen
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Dapatkan fragmen teks yang diekstraksi ke dalam koleksi
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop melalui fragmen
    for (auto textFragment : textFragmentCollection) {
        // Perbarui teks dan properti lainnya
        textFragment->set_Text(u"ABCD-EFGH");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }

    // Simpan file PDF yang diperbarui
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Ganti font dalam file PDF yang sudah ada

Aspose.PDF untuk C++ mendukung kemampuan untuk mengganti teks dalam dokumen PDF. Namun, terkadang Anda memiliki kebutuhan untuk hanya mengganti font yang digunakan di dalam dokumen PDF. Jadi, alih-alih mengganti teks, hanya font yang digunakan yang diganti. Salah satu overload dari konstruktor TextFragmentAbsorber menerima objek TextEditOptions sebagai argumen dan kita dapat menggunakan nilai RemoveUnusedFonts dari enumerasi TextEditOptions.FontReplace untuk memenuhi kebutuhan kita. Cuplikan kode berikut menunjukkan cara mengganti font di dalam dokumen PDF.

Dalam cuplikan kode berikut, Anda akan melihat bagaimana menggunakan font non-Inggris saat mengganti teks:

```cpp
void UseNonEnglishFontWhenReplacingText() {

    String _dataDir("C:\\Samples\\");

    // Instansiasi objek Dokumen
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Mari ubah setiap kata "PDF" menjadi beberapa teks Jepang dengan font spesifik
    // MSGothic yang mungkin terinstal di OS
    // Juga, mungkin font lain yang mendukung hieroglif
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // Buat instance dari opsi Pencarian Teks
    auto searchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(searchOptions);

    // Terima penyerap untuk semua halaman dokumen
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Dapatkan fragmen teks yang diekstraksi ke dalam koleksi
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop melalui fragmen
    for (auto textFragment : textFragmentCollection) {
        // Perbarui teks dan properti lainnya
        textFragment->set_Text(u"ファイル");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TakaoMincho"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Simpan dokumen yang telah diperbarui
    document->Save(_dataDir + u"Japanese_Text.pdf");
}
```

## Penggantian Teks harus secara otomatis mengatur ulang Konten Halaman

Aspose.PDF untuk C++ mendukung pencarian dan penggantian teks dalam file PDF. Namun, baru-baru ini, beberapa klien mengalami masalah saat mengganti teks, di mana TextFragment tertentu diganti dengan konten yang lebih kecil dan beberapa spasi ekstra ditampilkan dalam PDF yang dihasilkan, atau jika TextFragment diganti dengan string yang lebih panjang, maka kata-kata bertumpang tindih dengan konten halaman yang ada. Oleh karena itu, diperlukan untuk memperkenalkan mekanisme yang, setelah mengganti teks di dalam dokumen PDF, mengatur ulang kontennya.

Untuk melayani skenario yang disebutkan di atas, Aspose.PDF untuk C++ telah ditingkatkan sehingga masalah seperti itu tidak terjadi saat mengganti teks dalam file PDF. Cuplikan kode berikut menunjukkan cara mengganti teks dalam file PDF dan konten halaman harus diatur ulang secara otomatis.

```cpp
void RearrangeContent() {
    String _dataDir("C:\\Samples\\");

    // Buat objek Document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Buat objek TextFragment Absorber dengan ekspresi reguler
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("[PDF,Web]");

    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Anda juga dapat menentukan opsi ReplaceAdjustment.WholeWordsHyphenation untuk
    // membungkus teks pada baris berikutnya atau saat ini jika baris saat ini menjadi terlalu panjang atau
    // pendek setelah penggantian:
    //textFragmentAbsorber->get_TextReplaceOptions()->set_ReplaceAdjustmentAction(TextReplaceOptions::ReplaceAdjustment::WholeWordsHyphenation);

    // Terima absorber untuk semua halaman dokumen
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Dapatkan fragmen teks yang diekstrak ke dalam koleksi
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Ganti setiap TextFragment
    for (auto textFragment : textFragmentCollection) {
        // Atur font fragmen teks yang diganti
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        // Atur ukuran font
        textFragment->get_TextState()->set_FontSize(10);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
        // Ganti teks dengan string yang lebih besar dari placeholder
        textFragment->set_Text(u"This is a larger string for the testing of this feature");
    }
    // Simpan PDF hasil
    document->Save(_dataDir + u"RearrangeContentsUsingTextReplacement_out.pdf");
}
```

## Rendering Replaceable Symbols during PDF creation

Simbol yang dapat diganti adalah simbol khusus dalam string teks yang dapat diganti dengan konten yang sesuai saat waktu berjalan. Simbol yang dapat diganti saat ini didukung oleh Model Objek Dokumen baru dari namespace Aspose.PDF adalah `$P`, `$p`, `\n`, `\r`. `$p` dan `$P` digunakan untuk menangani penomoran halaman saat waktu berjalan. `$p` diganti dengan nomor halaman tempat kelas Paragraf saat ini berada. `$P` diganti dengan jumlah total halaman dalam dokumen. Ketika menambahkan `TextFragment` ke koleksi paragraf dari dokumen PDF, itu tidak mendukung pemisahan baris di dalam teks. Namun untuk menambahkan teks dengan pemisahan baris, silakan gunakan `TextFragment` dengan `TextParagraph`:

- gunakan "\r\n" atau Environment.NewLine dalam TextFragment daripada "\n" tunggal;
- buat objek TextParagraph. Ini akan menambahkan teks dengan pemisahan baris;
- tambahkan TextFragment dengan TextParagraph.AppendLine;
- tambahkan TextParagraph dengan TextBuilder.AppendParagraph.

## Simbol yang Dapat Diganti di Area Header/Footer

Simbol yang dapat diganti juga dapat ditempatkan di bagian header/footer dari file PDF. Tinjau cuplikan kode berikut untuk melihat cara menambahkan simbol yang dapat diganti ke bagian footer.

```csharp
void ReplaceableSymbolsInHeaderFooterArea() {

    auto document = MakeObject<Document>();
    auto page = doc.getPages().add();

    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Top(90);
    marginInfo->set_Bottom(50);
    marginInfo->set_Left(50);
    marginInfo->set_Right(50);

    // Tetapkan instance marginInfo ke properti Margin dari PageInfo
    page.getPageInfo()->set_Margin(marginInfo);

    auto hfFirst = MakeObject<HeaderFooter>();
    page->set_Header(hfFirst);
    hfFirst->get_Margin()->set_Left(50);
    hfFirst->get_Margin()->set_Right(50);

    // Instansiasi paragraf teks yang akan menyimpan konten untuk ditampilkan sebagai header
    auto t1 = MakeObject<TextFragment>("judul laporan");
    t1->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t1->get_TextState()->set_FontSize(16);
    t1->get_TextState()->set_ForegroundColor(Color::get_Black());
    t1->get_TextState()->set_FontStyle(FontStyles::Bold);
    t1->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t1->get_TextState()->set_LineSpacing(5.0f);
    hfFirst->get_Paragraphs()->Add(t1);

    auto t2 = MakeObject<TextFragment>("Nama_Laporan");
    t2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t2->get_TextState()->set_ForegroundColor(Color::get_Black());
    t2->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t2->get_TextState()->set_LineSpacing(5.0f);
    t2->get_TextState()->set_FontSize(12);
    hfFirst->get_Paragraphs()->Add(t2);

    // Buat objek HeaderFooter untuk bagian tersebut
    auto hfFoot = MakeObject<HeaderFooter>();

    // Tetapkan objek HeaderFooter ke footer ganjil & genap
    page->set_Footer(hfFoot);
    hfFoot->get_Margin()->set_Left(50);
    hfFoot->get_Margin()->set_Right(50);

    // Tambahkan paragraf teks yang berisi nomor halaman saat ini dari total jumlah halaman
    auto t3 = MakeObject<TextFragment>("Dihasilkan pada tanggal uji");
    auto t4 = MakeObject<TextFragment>("nama laporan ");
    auto t5 = MakeObject<TextFragment>("Halaman $p dari $P");

    // Instansiasi objek tabel
    auto tab2 = MakeObject<Table>();

    // Tambahkan tabel dalam koleksi paragraf dari bagian yang diinginkan
    hfFoot->get_Paragraphs()->Add(tab2);

    // Tetapkan lebar kolom dari tabel
    tab2->set_ColumnWidths(u"165 172 165");

    // Buat baris dalam tabel dan kemudian sel dalam baris
    auto row3 = tab2->get_Rows()->Add();

    row3->get_Cells()->Add();
    row3->get_Cells()->Add();
    row3->get_Cells()->Add();

    // Tetapkan perataan vertikal teks sebagai perataan tengah
    row3->get_Cells()->idx_get(0)->set_Alignment(HorizontalAlignment::Left);
    row3->get_Cells()->idx_get(1)->set_Alignment(HorizontalAlignment::Center);
    row3->get_Cells()->idx_get(2)->set_Alignment(HorizontalAlignment::Right);

    row3->get_Cells()->idx_get(0)->get_Paragraphs()->Add(t3);
    row3->get_Cells()->idx_get(1)->get_Paragraphs()->Add(t4);
    row3->get_Cells()->idx_get(2)->get_Paragraphs()->Add(t5);

    auto table = MakeObject<Table>();

    table->set_ColumnWidths(u"33% 33% 34%");
    table->set_DefaultCellPadding(new MarginInfo());
    table->get_DefaultCellPadding()->set_Top(10);
    table->get_DefaultCellPadding()->set_Bottom(10);

    // Tambahkan tabel dalam koleksi paragraf dari bagian yang diinginkan
    page.getParagraphs().add(table);

    // Tetapkan batas sel default menggunakan objek BorderInfo
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));

    // Tetapkan batas tabel menggunakan objek BorderInfo yang disesuaikan lainnya
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.0f));

    table->set_RepeatingRowsCount(1);

    // Buat baris dalam tabel dan kemudian sel dalam baris
    auto row1 = table->get_Rows()->Add();

    row1->get_Cells()->Add(u"kol1");
    row1->get_Cells()->Add(u"kol2");
    row1->get_Cells()->Add(u"kol3");

    String CRLF ("\r\n");

    for (int i = 0; i <= 10; i++) {
        auto row = table->get_Rows()->Add();
        row->set_IsRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            SharedPtr<Cell> c1;
            if (c == 2)
                c1 = row->get_Cells()->Add(
                    u"Aspose.Total untuk C++ adalah kompilasi dari setiap komponen Java yang ditawarkan oleh Aspose. Ini dikompilasi pada"
                    + CRLF
                    + u"setiap hari untuk memastikan berisi versi terbaru dari setiap komponen Java kami. "
                    + CRLF
                    + u"setiap hari untuk memastikan berisi versi terbaru dari setiap komponen Java kami. "
                    + CRLF
                    + u"Dengan menggunakan Aspose.Total untuk C++ pengembang dapat membuat berbagai macam aplikasi.");
            else
                c1 = row->get_Cells()->Add(u"item1" + c);
            c1->set_Margin(new MarginInfo());
            c1->get_Margin()->set_Left(30);
            c1->get_Margin()->set_Top(10);
            c1->get_Margin()->set_Bottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```

## Hapus Semua Teks dari Dokumen PDF

### Hapus Semua Teks menggunakan Operator

Dalam beberapa operasi teks, Anda perlu menghapus semua teks dari dokumen PDF, dan untuk itu, Anda biasanya perlu mengatur teks yang ditemukan sebagai nilai string kosong. Faktanya adalah bahwa mengubah teks untuk satu set fragmen teks menyebabkan sejumlah operasi untuk memeriksa dan menyesuaikan posisi teks. Mereka diperlukan dalam skrip pengeditan teks. Kesulitannya terletak pada kenyataan bahwa Anda tidak dapat menentukan berapa banyak potongan teks yang akan dihapus dalam skrip di mana mereka diproses dalam loop.

Oleh karena itu, kami menyarankan menggunakan pendekatan yang berbeda untuk skenario menghapus semua teks dari halaman PDF.

Cuplikan kode berikut menunjukkan cara menyelesaikan tugas ini dengan cepat.

```cpp
void RemoveAllTextUsingOperators() {

    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Loop melalui semua halaman Dokumen PDF
    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        auto page = document->get_Pages()->idx_get(i);
        auto operatorSelector = MakeObject<OperatorSelector>(MakeObject<Aspose::Pdf::Operators::TextShowOperator>());
        // Pilih semua teks di halaman
        page->get_Contents()->Accept(operatorSelector);
        // Hapus semua teks
        page->get_Contents()->Delete(operatorSelector->get_Selected());
    }
    // Simpan dokumen
    document->Save(_dataDir + u"RemoveAllText_out.pdf");
}
```