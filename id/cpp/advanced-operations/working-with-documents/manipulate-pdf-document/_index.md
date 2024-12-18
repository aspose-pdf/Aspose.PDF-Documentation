```
title: Manipulasi Dokumen PDF
linktitle: Manipulasi Dokumen PDF
type: docs
weight: 30
url: /id/cpp/manipulate-pdf-document/
lastmod: "2021-11-11"
description: Bagian ini menjelaskan tentang validasi Dokumen PDF untuk Standar PDF A, cara bekerja dengan TOC, cara mengatur tanggal kedaluwarsa PDF, dan cara menentukan Progres dari pembuatan file PDF.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Validasi Dokumen PDF untuk Standar PDF A (A 1A dan A 1B)

Untuk memvalidasi dokumen PDF agar sesuai dengan kompatibilitas PDF/A-1a atau PDF/A-1b, gunakan kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) metode [Validate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aa1ac4565b320807c718c44eeee7cda8c). Metode ini memungkinkan Anda untuk menentukan nama file di mana hasil akan disimpan dan jenis validasi yang diperlukan [PdfFormat](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ac83739fd7c818167c2fdc4dd554de763) enumerasi: PDF_A_1A atau PDF_A_1B.

{{% alert color="primary" %}}
```

Format XML keluaran adalah format Aspose khusus. XML berisi koleksi tag dengan nama Problem; setiap tag berisi detail dari masalah tertentu. Atribut ObjectID pada tag Problem mewakili ID dari objek tertentu yang terkait dengan masalah ini. Atribut Clause mewakili aturan yang sesuai dalam spesifikasi PDF.

{{% /alert %}}

Cuplikan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1A.

```cpp
void ExampleValidate01() {
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1A.xml");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Validasi PDF untuk PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1A);
}
```

Cuplikan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1B.

```cpp
void ExampleValidate02() {
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1B.xml");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Validasi PDF untuk PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1B);
}
```

## Bekerja dengan TOC

### Tambahkan TOC ke PDF yang Ada

API Aspose.PDF memungkinkan Anda untuk menambahkan daftar isi baik saat membuat PDF, atau ke file yang sudah ada.

Untuk menambahkan TOC ke file PDF yang sudah ada, gunakan kelas [Heading](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.heading) dalam namespace Aspose.Pdf. Namespace Aspose.Pdf memungkinkan Anda untuk membuat dan memanipulasi file PDF yang sudah ada. Untuk menambahkan TOC ke PDF yang sudah ada, gunakan namespace Aspose.Pdf.

Cuplikan kode berikut menunjukkan cara membuat daftar isi di dalam file PDF yang sudah ada.

```cpp
void ExampleToc01() {
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file
    String inputFileName("AddTOC.pdf");
    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Dapatkan akses ke halaman pertama file PDF
    auto tocPage = document->get_Pages()->Insert(1);

    // Buat objek untuk merepresentasikan informasi TOC
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Tetapkan judul untuk TOC
    tocInfo->set_Title(title);
    tocPage->set_TocInfo(tocInfo);

    // Buat objek string yang akan digunakan sebagai elemen TOC
    auto titles = MakeArray<String>(4);
    titles->SetValue(u"First page", 0);
    titles->SetValue(u"Second page", 1);
    titles->SetValue(u"Third page", 2);
    titles->SetValue(u"Fourth page", 3);

    for (int i = 0; i < 2; i++)
    {
        // Buat objek Heading
        auto heading2 = MakeObject<Heading>(1);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);

        // Tentukan halaman tujuan untuk objek heading

        heading2->set_DestinationPage(document->get_Pages()->idx_get(i + 2));

        // Halaman tujuan
        heading2->set_Top(document->get_Pages()->idx_get(i + 2)->get_Rect()->get_Height());

        // Koordinat tujuan
        segment2->set_Text(titles[i]);

        // Tambahkan heading ke halaman yang berisi TOC
        tocPage->get_Paragraphs()->Add(heading2);
    }

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outputFileName);
}
```

### Mengatur TabLeaderType yang Berbeda untuk Level TOC yang Berbeda

Aspose.PDF untuk C++ juga memungkinkan pengaturan TabLeaderType yang berbeda untuk level TOC yang berbeda. Anda perlu mengatur properti LineDash dari FormatArray dengan nilai yang sesuai dari TabLeaderType. Selanjutnya, Anda dapat menambahkan bagian daftar ke koleksi bagian dari dokumen Pdf. Setelah itu, buat bagian dalam dokumen Pdf dan simpan file PDF.

```cpp
void ExampleToc02() {
    // String untuk nama path.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto tocPage = document->get_Pages()->Add();
    auto tocInfo = MakeObject<TocInfo>();

    //atur LeaderType
    tocInfo->set_LineDash(TabLeaderType::Solid);

    // Buat objek untuk merepresentasikan informasi TOC
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Atur judul untuk TOC
    tocInfo->set_Title(title);

    //Tambahkan bagian daftar ke koleksi bagian dari dokumen Pdf
    tocPage->set_TocInfo(tocInfo);

    //Definisikan format dari daftar empat level dengan mengatur margin kiri
    //dan
    //pengaturan format teks dari setiap level

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Left(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(0)->set_LineDash(TabLeaderType::Dot);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(10);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(1)->set_LineDash(TabLeaderType::None);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Left(20);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->set_LineDash(TabLeaderType::Solid);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    //Buat bagian dalam dokumen Pdf
    auto page = document->get_Pages()->Add();

    //Tambahkan empat judul dalam bagian
    for (int Level = 1; Level <= 4; Level++)
    {
    auto heading2 = MakeObject<Heading>(Level);
    auto segment2 = MakeObject<TextSegment>();

    heading2->get_Segments()->Add(segment2);
    heading2->set_IsAutoSequence(true);
    heading2->set_TocPage(tocPage);
    segment2->set_Text(u"Sample Heading" + Level);
    heading2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial Unicode MS"));

    //Tambahkan judul ke dalam Daftar Isi.
    heading2->set_IsInList(true);
    page->get_Paragraphs()->Add(heading2);
    }

    // simpan Pdf
    document->Save(_dataDir + outputFileName);
}
```

### Sembunyikan Nomor Halaman di TOC

Jika Anda ingin menyembunyikan nomor halaman bersama dengan judul di daftar isi, Anda dapat menggunakan properti [IsShowPageNumbers](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info#ada10e841699bba062dcd0b440c26b832) dari Kelas [TOCInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info) sebagai false.

Silakan periksa potongan kode berikut untuk menyembunyikan nomor halaman di daftar isi:

```cpp
void ExampleToc03() {
    // String untuk nama jalur.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto tocPage = document->get_Pages()->Add();

    // Buat objek untuk merepresentasikan informasi TOC
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Daftar Isi");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Atur judul untuk TOC
    tocInfo->set_Title(title);

    //Tambahkan bagian daftar ke koleksi bagian dari dokumen Pdf  
    tocPage->set_TocInfo(tocInfo);

    tocInfo->set_IsShowPageNumbers(false);

    //Definisikan format dari empat level daftar dengan mengatur margin kiri dan
    //pengaturan format teks dari setiap level

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_Underline(true);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    auto page = document->get_Pages()->Add();
    //Tambahkan empat judul di bagian tersebut
    for (int Level = 1; Level != 5; Level++)
    {
        auto heading2 = MakeObject<Heading>(Level);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);
        heading2->set_IsAutoSequence(true);
        segment2->set_Text(u"ini adalah judul dari level " + Level);
        heading2->set_IsInList(true);
        page->get_Paragraphs()->Add(heading2);
    }
    // simpan Pdf
    document->Save(_dataDir + outputFileName);
}
```

## Cara mengatur tanggal kedaluwarsa PDF

Kami menerapkan hak akses pada file PDF sehingga sekelompok pengguna tertentu dapat mengakses fitur/objek tertentu dari dokumen PDF. Untuk membatasi akses file PDF, biasanya kami menerapkan enkripsi dan kami mungkin memiliki persyaratan untuk mengatur kedaluwarsa file PDF, sehingga pengguna yang mengakses/melihat dokumen mendapatkan pemberitahuan yang valid mengenai kedaluwarsa file PDF.

Untuk mencapai persyaratan yang disebutkan di atas, kami dapat menggunakan objek [JavascriptAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.javascript_action/). Silakan periksa cuplikan kode berikut.

```cpp
void SetPDFexpiryDate() {

    // String untuk nama path.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file. 
    String outputFileName("SetExpiryDate_out.pdf");

    // Instansiasi objek Document
    auto document = MakeObject<Document>();

    // Tambahkan halaman ke koleksi halaman file PDF
    document->get_Pages()->Add();

    // Tambahkan potongan teks ke koleksi paragraf dari objek halaman
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(new TextFragment(u"Hello World..."));

    String javascriptCode(u"var year=2017;");
    javascriptCode += u"var month=5;";
    javascriptCode += u"today = new Date(); today = new Date(today.getFullYear(), today.getMonth());";
    javascriptCode += u"expiry = new Date(year, month);";
    javascriptCode += u"if (today.getTime() > expiry.getTime())";
    javascriptCode += u"app.alert('The file is expired. You need a new one.');";

    // Buat objek JavaScript untuk mengatur tanggal kedaluwarsa PDF
    auto javaScript = MakeObject<Aspose::Pdf::Annotations::JavascriptAction>(javascriptCode);

    // Atur JavaScript sebagai tindakan pembukaan PDF
    document->set_OpenAction(javaScript);

    // Simpan Dokumen PDF
    document->Save(_dataDir + outputFileName);
}
```

## Menentukan Kemajuan Pembuatan File PDF

Seorang pelanggan meminta kami untuk menambahkan fitur yang memungkinkan pengembang menentukan kemajuan pembuatan file PDF. Berikut adalah tanggapan terhadap permintaan tersebut.

Bidang [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb) dari kelas [DocSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) memungkinkan Anda untuk menentukan bagaimana pembuatan PDF berjalan.

Cuplikan kode di bawah ini menunjukkan cara menggunakan [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb).

```cpp
using ProgressHandler = System::MulticastDelegate<void(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo>)>;
void ConversionProgressCallback(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    String eventType;
    switch (eventInfo->EventType)
    {
    case ProgressEventType::ResultPageCreated:
        eventType = u"ResultPageCreated";
        break;
    case ProgressEventType::ResultPageSaved:
        eventType = u"ResultPageSaved";
        break;
    case ProgressEventType::SourcePageAnalysed:
        eventType = u"SourcePageAnalysed";
        break;
    case ProgressEventType::TotalProgress:
        eventType = u"TotalProgress";
        break;
    }
    Console::WriteLine(String::Format(u"Jenis kejadian: {0}, Nilai: {1}, Nilai Maksimal: {2}", 
        eventType, eventInfo->Value, eventInfo->MaxValue));
}
```

```cpp
void DetermineProgressOfPDFfileGeneration() {
    // String untuk nama path.
    String _dataDir("C:\\Samples\\");

    // String untuk nama file.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Buka dokumen
    auto saveOptions = MakeObject<DocSaveOptions>();

    saveOptions->CustomProgressHandler = ProgressHandler(ConversionProgressCallback);

    document->Save(_dataDir + outputFileName, saveOptions);
}
```

## Ratakan PDF yang Dapat Diisi di C++

Dokumen PDF sering kali menyertakan formulir dengan widget interaktif yang dapat diisi seperti tombol radio, kotak centang, kotak teks, daftar, dll. Untuk membuatnya tidak dapat diedit untuk berbagai tujuan aplikasi, kita perlu meratakan file PDF tersebut.
Aspose.PDF untuk C++ menyediakan fungsi untuk meratakan PDF Anda di C++ hanya dengan beberapa baris kode:

```cpp
void FlattenFillablePDF() {
    // String untuk nama path.
    String _dataDir("C:\\Samples\\");
    // String untuk nama file.
    String inputFileName("sample-form.pdf");
    String outputFileName("FlattenForms_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Ratakan PDF yang Dapat Diisi
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for (auto item : document->get_Form()->get_Fields())
        item->Flatten();
    }

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outputFileName);
}
```