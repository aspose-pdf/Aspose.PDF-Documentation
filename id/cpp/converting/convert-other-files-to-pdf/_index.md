---
linktitle: Mengonversi format file lain ke PDF
type: docs
weight: 80
url: id/cpp/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: Topik ini menunjukkan kepada Anda bagaimana Aspose.PDF memungkinkan mengonversi format file lain ke dokumen PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Mengonversi EPUB ke PDF

**Aspose.PDF for C++** memungkinkan Anda dengan mudah mengonversi file EPUB ke format PDF.

<abbr title="electronic publication">EPUB</abbr> (singkatan dari electronic publication) adalah standar buku elektronik gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub. EPUB dirancang untuk konten yang dapat diatur ulang, yang berarti bahwa pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu.

EPUB juga mendukung konten tata letak tetap. Format ini dimaksudkan sebagai format tunggal yang dapat digunakan oleh penerbit dan rumah konversi secara internal, serta untuk distribusi dan penjualan. Ini menggantikan standar Open eBook. Versi EPUB 3 juga didukung oleh Book Industry Study Group (BISG), sebuah asosiasi perdagangan buku terkemuka untuk praktik terbaik standar, penelitian, informasi, dan acara, untuk pengemasan konten.

Langkah-langkah konversi:

1. Buat [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) untuk nama jalur dan nama file.
1. Buat instance dari kelas [EpubLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. Buat instance dari kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dengan menyebutkan nama file sumber dan opsi.
1. Muat dan [Simpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) file input.

Berikut cuplikan kode berikut menunjukkan cara mengonversi file EPUB ke format PDF dengan C++.

```cpp
void ConvertEPUBtoPDF()
{
    std::clog << "EPUB to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("aliceDynamic.epub");
    String outfilename("epub_test.pdf");
    auto options = MakeObject<EpubLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "EPUB to PDF convert: End" << std::endl;
}
```
{{% alert color="success" %}}
**Cobalah untuk mengonversi EPUB ke PDF secara online**

Aspose.PDF untuk C++ menyajikan aplikasi online gratis ["EPUB ke PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi EPUB ke PDF dengan Aplikasi Gratis](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Konversi Teks ke PDF

**Aspose.PDF untuk C++** mendukung fitur mengonversi teks biasa dan file teks pra-format ke format PDF.

Mengonversi teks ke PDF berarti menambahkan fragmen teks ke halaman PDF. Adapun file teks, kita berurusan dengan 2 jenis teks: pra-formatting (misalnya, 25 baris dengan 80 karakter per baris) dan teks tidak berformat (teks biasa). Bergantung pada kebutuhan kita, kita dapat mengontrol penambahan ini sendiri atau mempercayakannya kepada algoritma perpustakaan.

### Konversi file teks biasa ke PDF

Dalam hal file teks biasa, kita dapat menggunakan teknik berikut: 

1. Buat [Kelas String](https://reference.aspose.com/pdf/cpp/class/system.string) untuk nama path dan nama file.
1. Baca file teks sumber menggunakan [TextReader](https://reference.aspose.com/pdf/cpp/class/system.i_o.text_reader/.)
1. Instansiasi Objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Tambahkan [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) ke koleksi halaman dokumen.
1. Buat objek baru dari TextFragment dan berikan objek TextReader ke konstruktor-nya.
1. Tambahkan paragraf teks baru dalam koleksi paragraf dan berikan objek TextFragment.
1. Muat dan [Simpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) file input.

```cpp
void ConvertTextToPDF()
{
    std::clog << "Konversi Teks ke PDF: Mulai" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.txt");
    String outfilename("TextToPDF.pdf");

    // Baca file teks sumber
    String content = System::IO::File::ReadAllText(_dataDir + infilename);

    // Instansiasi objek Document dengan memanggil konstruktor kosongnya
    auto document = MakeObject<Document>();

    // Tambahkan halaman baru ke koleksi Pages dari Document
    auto page = document->get_Pages()->Add();

    // Buat instance dari TextFragment dan berikan teks dari objek pembaca ke konstruktor-nya sebagai argumen
    auto text = MakeObject<TextFragment>(content);

    // Tambahkan paragraf teks baru dalam koleksi paragraf dan berikan objek TextFragment
    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Simpan file PDF yang dihasilkan
    document->Save(_dataDir + outfilename);
    std::clog << "Konversi Teks ke PDF: Selesai" << std::endl;
}
```
### Mengonversi file teks yang sudah diformat ke PDF

Mengonversi teks yang sudah diformat mirip dengan teks biasa, tetapi Anda perlu melakukan beberapa tindakan tambahan seperti mengatur margin, tipe dan ukuran font. Jelas bahwa font tersebut harus monospace (misalnya Courier New).

Ikuti langkah-langkah ini untuk mengonversi teks yang sudah diformat ke PDF dengan C++:

1. Instansiasi objek Document dengan memanggil konstruktor kosongnya.
1. Atur margin kiri dan kanan untuk presentasi yang lebih baik.
1. Instansiasi objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dan tambahkan halaman baru dalam koleksi Pages.
1. Muat dan [Simpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) file gambar input.

```CPP
void ConvertPreFormattedTextToPdf()
{
    std::clog << "Performatted Text to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("rfc822.txt");
    String outfilename("TextToPDF.pdf");
    // Baca file teks sebagai array string
    auto lines = System::IO::File::ReadAllLines(_dataDir + infilename);

    // Instansiasi objek Document dengan memanggil konstruktor kosongnya
    auto document = MakeObject<Document>();

    // Tambahkan halaman baru dalam koleksi Pages pada Document
    auto page = document->get_Pages()->Add();

    // Atur margin kiri dan kanan untuk presentasi yang lebih baik
    page->get_PageInfo()->get_Margin()->set_Left(20);
    page->get_PageInfo()->get_Margin()->set_Right(10);
    page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
    page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);

    for (int index = 0; index < lines->get_Length(); index++)
    {
        // periksa apakah baris mengandung karakter "form feed"
        // lihat https://en.wikipedia.org/wiki/Page_break
        auto line = lines->idx_get(index);
        if (line.StartsWith(u"\x0c"))
        {
        if (document->get_Pages()->get_Count() > 3) break;
        page = document->get_Pages()->Add();
        // Atur margin kiri dan kanan untuk presentasi yang lebih baik
        page->get_PageInfo()->get_Margin()->set_Left(20);
        page->get_PageInfo()->get_Margin()->set_Right(10);
        page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
        page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);
        }
        else
        {
        // Buat instance TextFragment dan
        // masukkan baris ke dalam konstruktornya sebagai argumen
        auto text = MakeObject<TextFragment>(line);

        // Tambahkan paragraf teks baru dalam koleksi paragraf dan masukkan objek TextFragment
        page->get_Paragraphs()->Add(text);
        }
    }

    // Simpan file PDF hasil
    document->Save(_dataDir + outfilename);
    std::clog << "Performatted Text to PDF convert: End" << std::endl;
}
```

{{% alert color="success" %}}
**Cobalah mengonversi TEKS ke PDF secara online**

Aspose.PDF untuk C++ menghadirkan aplikasi online gratis ["Teks ke PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi TEKS ke PDF dengan Aplikasi Gratis](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

## Konversi XPS ke PDF

**Aspose.PDF untuk C++** mendukung fitur mengonversi file <abbr title="XML Paper Specification">XPS</abbr> ke format PDF. Periksa artikel ini untuk menyelesaikan tugas Anda.

Jenis file XPS terutama terkait dengan Spesifikasi Kertas XML oleh Microsoft Corporation. Spesifikasi Kertas XML (XPS), sebelumnya diberi nama kode Metro dan menggantikan konsep pemasaran Jalur Cetak Generasi Berikutnya (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dan penayangan dokumen ke dalam sistem operasi Windows-nya.

{{% alert color="primary" %}}

Format file ini pada dasarnya adalah file XML yang dikompresi yang terutama digunakan untuk distribusi dan penyimpanan. Sulit sekali untuk mengedit dan sebagian besar diimplementasikan oleh Microsoft.

{{% /alert %}}

Untuk mengonversi XPS ke PDF dengan Aspose.PDF untuk C++, kami telah memperkenalkan kelas bernama [XpsLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options) yang digunakan untuk menginisialisasi objek [LoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options). Kemudian, objek ini dilewatkan sebagai argumen selama inisialisasi objek Document dan ini membantu mesin rendering PDF untuk menentukan format input dokumen sumber.

Cuplikan kode berikut menunjukkan proses mengonversi file XPS ke format PDF dengan C++.

```cpp
void ConvertXPStoPDF()
{
    std::clog << "XPS to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.oxps");
    String outfilename("XPStoPDF.pdf");
    auto options = MakeObject<XpsLoadOptions>();
    try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
    };
    std::clog << "XPS to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Cobalah mengonversi format XPS ke PDF secara online**

Aspose.PDF untuk C++ menyajikan aplikasi gratis online ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi XPS ke PDF dengan Aplikasi Gratis](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Mengonversi XML ke PDF

Format XML digunakan untuk menyimpan data terstruktur. Ada beberapa cara untuk mengonversi <abbr title="Extensible Markup Language">XML</abbr> ke PDF di Aspose.PDF.

## Mengonversi XSL-FO ke PDF

1. Buat [Kelas String](https://reference.aspose.com/pdf/cpp/class/system.string) untuk nama jalur dan nama file.
1. Instansiasi [objek XslFoLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. Atur strategi penanganan kesalahan.
1. Instansiasi Objek [Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) file gambar input.

```cpp
void Convert_XSLFO_to_PDF()
{
    std::clog << "Konversi XSL-FO ke PDF: Mulai" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilenameXSL("c:\\samples\\employees.xslt");
    String infilenameXML("c:\\samples\\employees.xml");

     String outfilename("XMLFOtoPDF.pdf");
    // Membuat objek XslFoLoadOption
    auto options = new XslFoLoadOptions(infilenameXSL);
    // Menetapkan strategi penanganan kesalahan
    options->ParsingErrorsHandlingType = XslFoLoadOptions::ParsingErrorsHandlingTypes::ThrowExceptionImmediately;
    // Membuat objek Dokumen
    auto document = MakeObject<Document>(infilenameXML, options);
    document->Save(_dataDir + outfilename);
}
```

{{% alert color="success" %}}
**Cobalah untuk mengonversi XML ke PDF secara online**


Aspose.PDF untuk C++ menghadirkan aplikasi online gratis ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), di mana Anda dapat mencoba meneliti fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi XML ke PDF dengan Aplikasi Gratis](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}
```