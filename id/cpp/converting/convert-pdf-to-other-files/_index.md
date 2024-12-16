---
title: Konversi file PDF ke format lain
linktitle: Konversi PDF ke format lain
type: docs
weight: 90
url: /id/cpp/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF ke format file lain.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Konversi PDF ke EPUB

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke EPUB secara online**

Aspose.PDF untuk C++ menghadirkan aplikasi online gratis ["PDF ke EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), di mana Anda dapat mencoba menyelidiki fungsi dan kualitasnya bekerja.

[![Aspose.PDF Konversi PDF ke EPUB dengan Aplikasi Gratis](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> (singkatan dari Electronic Publication) adalah standar buku elektronik gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub.
EPUB dirancang untuk konten yang dapat diubah, yang berarti bahwa pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu. EPUB juga mendukung konten dengan tata letak tetap. Format ini dimaksudkan sebagai format tunggal yang dapat digunakan oleh penerbit dan rumah konversi secara internal, serta untuk distribusi dan penjualan. Ini menggantikan standar Open eBook.

Aspose.PDF untuk C++ juga mendukung fitur untuk mengonversi dokumen PDF ke format EPUB. Aspose.PDF untuk C++ memiliki kelas bernama EpubSaveOptions yang dapat digunakan sebagai argumen kedua untuk metode [`Document.Save(..)`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa), untuk menghasilkan file EPUB. Silakan coba menggunakan potongan kode berikut untuk memenuhi persyaratan ini dengan C++.

```cpp
void ConvertPDFtoEPUB()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.pdf");
    // String untuk nama file output
    String outfilename("PDFToEPUB_out.epub");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Simpan file PDF ke dalam format EPUB
    document->Save(_dataDir + outfilename, SaveFormat::Epub);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Mengonversi PDF ke LaTeX/TeX

**Aspose.PDF untuk C++** mendukung konversi PDF ke LaTeX/TeX. Format file LaTeX adalah format file teks dengan markup khusus dan digunakan dalam sistem persiapan dokumen berbasis TeX untuk typesetting berkualitas tinggi.

Untuk mengonversi file PDF ke TeX, Aspose.PDF memiliki kelas [LaTeXSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.la_te_x_save_options) yang menyediakan properti OutDirectoryPath untuk menyimpan gambar sementara selama proses konversi.

Cuplikan kode berikut menunjukkan proses mengonversi file PDF ke format TEX dengan C++.

```cpp
void ConvertPDFtoLaTeX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.pdf");
    // String untuk nama file output
    String outfilename("PDFToTeX_out.tex");

    // Membuka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi opsi simpan LaTeX
    auto saveOptions = MakeObject<LaTeXSaveOptions>();

    // Mengatur jalur direktori keluaran untuk objek opsi simpan
    saveOptions->set_OutDirectoryPath(_dataDir);

    // Menyimpan file PDF ke dalam format LaTeX
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke LaTeX/TeX secara online**

Aspose.PDF untuk C++ menghadirkan aplikasi online gratis ["PDF ke LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke LaTeX/TeX dengan Aplikasi Gratis](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Konversi PDF ke Teks

**Aspose.PDF untuk C++** mendukung konversi seluruh dokumen PDF dan halaman tunggal ke file Teks.

### Konversi seluruh dokumen PDF ke file Teks

Anda dapat mengonversi dokumen PDF ke file TXT menggunakan kelas [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/).

Cuplikan kode berikut menjelaskan cara mengekstrak teks dari semua halaman.

```cpp
void ConvertPDFDocToTXT()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.pdf");
    // String untuk nama file output
    String outfilename("input_Text_Extracted_out.txt");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();
    ta->Visit(document);
    // Simpan teks yang diekstraksi di file teks
    System::IO::File::WriteAllText(_dataDir + outfilename, ta->get_Text());
    std::clog << __func__ << ": Selesai" << std::endl;
}
```

### Konversi halaman PDF ke file teks

Anda dapat mengonversi dokumen PDF ke file TXT dengan Aspose.PDF untuk C++. Anda harus menggunakan kelas [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/) untuk menyelesaikan tugas ini.

Cuplikan kode berikut menjelaskan cara mengekstraksi teks dari halaman tertentu.

```cpp
void ConvertPDFPagestoTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample-4pages.pdf");
    // String untuk nama file output
    String outfilename("sample-4pages_out.txt");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();

    auto pages = { 1, 3, 4 };
    try {
    for (auto page : pages)
    {
    ta->Visit(document->get_Pages()->idx_get(page));
    }
    // Simpan teks yang diekstraksi ke dalam file teks
    auto text = ta->get_Text();
    System::IO::File::WriteAllText(_dataDir + outfilename, text);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Coba konversi PDF ke Teks secara online**

Aspose.PDF untuk C++ menghadirkan aplikasi online gratis ["PDF ke Teks"](https://products.aspose.app/pdf/conversion/pdf-to-txt), di mana Anda dapat mencoba menyelidiki fungsi dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke Teks dengan Aplikasi Gratis](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Konversi PDF ke XPS

**Aspose.PDF untuk C++** memberikan kemungkinan untuk mengonversi file PDF ke format <abbr title="XML Paper Specification">XPS</abbr>. Mari coba gunakan potongan kode yang disajikan untuk mengonversi file PDF ke format XPS dengan C++.

Jenis file XPS terutama diasosiasikan dengan XML Paper Specification oleh Microsoft Corporation. XML Paper Specification (XPS), sebelumnya bernama kode Metro dan menggabungkan konsep pemasaran Next Generation Print Path (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dan penayangan dokumen ke dalam sistem operasi Windows.

Untuk mengonversi file PDF ke XPS, Aspose.PDF memiliki kelas [XpsSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xps_save_options) yang digunakan sebagai argumen kedua untuk metode [Document.Save(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) untuk menghasilkan file XPS.

Potongan kode berikut menunjukkan proses mengubah file PDF ke format XPS.

```cpp
void ConvertPDFtoXPS()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.pdf");
    // String untuk nama file output
    String outfilename("PDFToXPS_out.xps");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi opsi simpan LaTex
    auto saveOptions = MakeObject<XpsSaveOptions>();

    // Simpan file PDF ke format XPS
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Coba ubah PDF ke SVG secara online**

Aspose.PDF untuk C++ mempersembahkan aplikasi gratis online ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.
{{% /alert %}}


[![Aspose.PDF Konversi PDF ke SVG dengan Aplikasi Gratis](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)