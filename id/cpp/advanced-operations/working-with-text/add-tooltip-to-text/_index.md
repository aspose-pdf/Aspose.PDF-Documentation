---
title: Tooltip PDF menggunakan C++
linktitle: Tooltip PDF
type: docs
weight: 20
url: id/cpp/pdf-tooltip/
description: Pelajari cara menambahkan tooltip ke fragmen teks dalam PDF menggunakan C++ dan Aspose.PDF
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Tooltip ke Teks yang Dicari dengan Menambahkan Tombol Tak Terlihat

Artikel ini menunjukkan cara menambahkan tooltip ke teks pada dokumen PDF yang ada dalam C++. Aspose.PDF mendukung untuk membuat tooltip dengan menambahkan tombol tak terlihat di atas teks yang dicari dari file PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void AddTooltipToSearchedText() {

    String _dataDir("C:\\Samples\\");

    // String untuk nama file keluaran
    String outputFileName("Tooltip_out.pdf");

    // Buat dokumen contoh dengan teks
    auto document = MakeObject<Document>();
    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Pindahkan kursor mouse ke sini untuk menampilkan tooltip"));

    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(MakeObject<TextFragment>("Pindahkan kursor mouse ke sini untuk menampilkan tooltip yang sangat panjang"));

    document->Save(outputFileName);

    // Buka dokumen dengan teks
    auto document = MakeObject<Document>(outputFileName);
    // Buat objek TextAbsorber untuk menemukan semua frasa yang cocok dengan ekspresi reguler
    auto absorber = MakeObject<TextFragmentAbsorber>("Pindahkan kursor mouse ke sini untuk menampilkan tooltip");
    // Terima absorber untuk halaman dokumen
    document->get_Pages()->Accept(absorber);

    // Dapatkan fragmen teks yang diekstraksi
    auto textFragments = absorber->get_TextFragments();

    // Loop melalui fragmen
    for(auto fragment : textFragments)
    {
        // Buat tombol tak terlihat pada posisi fragmen teks
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // Nilai AlternateName akan ditampilkan sebagai tooltip oleh aplikasi penampil
        field->set_AlternateName (u"Tooltip untuk teks.");
        // Tambahkan field tombol ke dokumen
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // Selanjutnya akan menjadi contoh tooltip yang sangat panjang
    absorber = MakeObject<TextFragmentAbsorber>("Pindahkan kursor mouse ke sini untuk menampilkan tooltip yang sangat panjang");
    document->get_Pages()->Accept(absorber);
    textFragments = absorber->get_TextFragments();

    for(auto fragment : textFragments)
    {
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // Tetapkan teks yang sangat panjang
        field->set_AlternateName(String("Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna\
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
            ullamco laboris nisi ut aliquip ex ea commodo consequat.\
            Duis aute irure dolor in reprehenderit in voluptate velit\
            esse cillum dolore eu fugiat nulla pariatur. Excepteur sint\
            occaecat cupidatat non proident, sunt in culpa qui officia\
            deserunt mollit anim id est laborum."));
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // Simpan dokumen
    document->Save(outputFileName);

}
```

## Membuat Blok Teks Tersembunyi dan Menampilkannya saat Mouse Over

Aspose.PDF untuk C++ mengimplementasikan fungsi tindakan sembunyi, yang memungkinkan Anda untuk menampilkan/menyembunyikan bidang teks (atau jenis anotasi lainnya) saat memasuki/keluar dari mouse di atas beberapa tombol tak terlihat. Untuk melakukan ini, gunakan kelas Aspose.Pdf.Annotations.HideAction untuk menetapkan tindakan sembunyi/tampilkan ke blok teks. Gunakan cuplikan kode berikut untuk menampilkan/menyembunyikan blok teks pada input/output mouse.

Perhatikan juga bahwa tindakan PDF pada dokumen berfungsi dengan baik dalam pembaca masing-masing (seperti Adobe Reader), tetapi tidak memberikan jaminan untuk pembaca PDF lainnya (seperti plug-in peramban web). Kami melakukan investigasi singkat dan menemukan:

- Semua implementasi tindakan sembunyi dalam dokumen PDF berfungsi dengan baik di Internet Explorer v.11.0.
- Semua implementasi tindakan sembunyi juga berfungsi di Opera v.12.14, tetapi kami menemukan beberapa penundaan respons pada pembukaan dokumen pertama kali.

- Hanya implementasi yang menggunakan konstruktor HideAction yang menerima nama bidang yang berfungsi jika Google Chrome v.61.0 menjelajahi dokumen; Silakan gunakan konstruktor yang sesuai jika browsing di Google Chrome signifikan:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```cpp
void CreateHiddenTextBlock() {

    String _dataDir("C:\\Samples\\");

    // String untuk nama file output
    String outputFileName("TextBlock_HideShow_MouseOverOut_out.pdf");

    // Buat dokumen contoh dengan teks
    auto document = MakeObject<Document>();

    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Gerakkan kursor mouse ke sini untuk menampilkan teks mengambang"));
    document->Save(outputFileName);

    // Buka dokumen dengan teks
    auto document = MakeObject<Document>(outputFileName);

    // Buat objek TextAbsorber untuk menemukan semua frasa yang cocok dengan ekspresi reguler
    auto absorber = MakeObject<TextFragmentAbsorber>("Gerakkan kursor mouse ke sini untuk menampilkan teks mengambang");
    // Terima absorber untuk halaman dokumen
    document->get_Pages()->Accept(absorber);
    // Dapatkan fragmen teks pertama yang diekstraksi
    auto textFragments = absorber->get_TextFragments();
    auto fragment = textFragments->idx_get(1);

    // Buat bidang teks tersembunyi untuk teks mengambang dalam persegi panjang halaman yang ditentukan
    auto floatingField = MakeObject<Aspose::Pdf::Forms::TextBoxField>(fragment->get_Page(), MakeObject<Rectangle>(100, 700, 220, 740));
    // Setel teks yang akan ditampilkan sebagai nilai bidang
    floatingField->set_Value(u"Ini adalah \"bidang teks mengambang\".");
    // Kami merekomendasikan untuk membuat bidang 'readonly' untuk skenario ini
    floatingField->set_ReadOnly(true);
    // Setel bendera 'hidden' untuk membuat bidang tidak terlihat saat dokumen dibuka
    floatingField->set_Flags(floatingField->get_Flags() | Aspose::Pdf::Annotations::AnnotationFlags::Hidden);

    // Menetapkan nama bidang unik tidak perlu tetapi diizinkan
    floatingField->set_PartialName (u"FloatingField_1");

    // Menetapkan karakteristik penampilan bidang tidak perlu tetapi membuatnya lebih baik
    floatingField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>("Helv", 10, Color::get_Blue()));
    floatingField->get_Characteristics()->set_Background (System::Drawing::Color::get_LightBlue());
    floatingField->get_Characteristics()->set_Border (System::Drawing::Color::get_DarkBlue());
    floatingField->set_Border(MakeObject<Aspose::Pdf::Annotations::Border>(floatingField));
    floatingField->get_Border()->set_Width (1);
    floatingField->set_Multiline (true);

    // Tambahkan bidang teks ke dokumen
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(floatingField));

    // Buat tombol tak terlihat di posisi fragmen teks
    auto buttonField = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
    // Buat aksi sembunyi baru untuk bidang (anotasi) yang ditentukan dan bendera tidak terlihat.
    // (Anda juga dapat merujuk bidang mengambang dengan nama jika Anda telah menentukannya di atas.)
    // Tambahkan aksi saat mouse masuk/keluar pada bidang tombol tak terlihat
    buttonField->get_Actions()->set_OnEnter(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField, false));
    buttonField->get_Actions()->set_OnExit(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField));

    // Tambahkan bidang tombol ke dokumen
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(buttonField));

    // Simpan dokumen
    document->Save(outputFileName);
}
```