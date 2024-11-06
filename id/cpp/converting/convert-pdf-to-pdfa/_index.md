---
title: Konversi PDF ke format PDF/A
linktitle: Konversi PDF ke format PDF/A
type: docs
weight: 100
url: id/cpp/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF ke file PDF yang sesuai dengan PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF untuk C++** memungkinkan Anda untuk mengonversi file PDF ke file PDF yang sesuai dengan <abbr title="Portable Document Format / A">PDF/A</abbr>. Sebelum melakukannya, file harus divalidasi. Topik ini menjelaskan caranya.

{{% alert color="primary" %}}

Harap dicatat bahwa kami mengikuti Adobe Preflight untuk memvalidasi kepatuhan PDF/A. Semua alat di pasar memiliki "representasi" mereka sendiri tentang kepatuhan PDF/A. Silakan periksa artikel ini tentang alat validasi PDF/A untuk referensi. Kami memilih produk Adobe untuk memverifikasi bagaimana Aspose.PDF menghasilkan file PDF karena Adobe adalah pusat dari segala sesuatu yang berhubungan dengan PDF.

{{% /alert %}}

Konversi file menggunakan metode Convert dari kelas Document. Sebelum mengonversi PDF ke file yang sesuai dengan PDF/A, validasi PDF menggunakan metode Validasi. Hasil validasi disimpan dalam file XML dan kemudian hasil ini juga diteruskan ke metode Konversi. Anda juga dapat menentukan tindakan untuk elemen-elemen yang tidak dapat dikonversi menggunakan enumerasi ConvertErrorAction.
## Konversi file PDF ke PDF/A-1b

Cuplikan kode berikut menunjukkan cara mengonversi file PDF ke PDF yang sesuai dengan PDF/A-1b.

```cpp
void ConverttoPDFA_1b()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.pdf");
    // String untuk nama file log
    String logfilename("log.xml");
    // String untuk nama file output
    String outfilename("PDFToPDFA_out.pdf");

    // Buka dokumen
    auto document = new Document(_dataDir + infilename);

    // Konversi ke dokumen yang sesuai dengan PDF/A
    // Selama proses konversi, validasi juga dilakukan
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

    // Simpan dokumen keluaran
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Selesai" << std::endl;
}
```
Untuk melakukan validasi saja, gunakan baris kode berikut:

```cpp
void ConverttoPDFA_1b_Validation()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.pdf");
    // String untuk nama file log
    String logfilename("log.xml");

    // Buka dokumen
    auto document = new Document(_dataDir + infilename);

    // Konversi ke dokumen yang sesuai dengan PDF/A
    // Selama proses konversi, validasi juga dilakukan
    document->Validate(_dataDir + logfilename, PdfFormat::PDF_A_1B);
    std::clog << __func__ << ": Selesai" << std::endl;
}
```

## Mengonversi file PDF ke PDF/A-3b

Aspose.PDF untuk C++ juga mendukung fitur untuk mengonversi file PDF ke format PDF/A-3b.

```cpp
void ConverttoPDFA_3b()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.pdf");
    // String untuk nama file log
    String logfilename("log.xml");
    // String untuk nama file input
    String outfilename("PDFToPDFA3b_out.pdf");

    // Buka dokumen
    auto document = new Document(_dataDir + infilename);

    // Konversi ke dokumen yang sesuai dengan PDF/A
    // Selama proses konversi, validasi juga dilakukan
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3B, ConvertErrorAction::Delete);

    // Simpan dokumen keluaran
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Selesai" << std::endl;
}
```

## Mengkonversi file PDF ke PDF/A-2u

Aspose.PDF untuk C++ juga mendukung fitur untuk mengkonversi file PDF ke format PDF/A-2u.

```cpp
void ConverttoPDFA_2u()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.pdf");
    // String untuk nama file log
    String logfilename("log.xml");
    // String untuk nama file output
    String outfilename("PDFToPDFA3b_out.pdf");

    // Buka dokumen
    auto document = new Document(_dataDir + infilename);

    // Konversi ke dokumen yang sesuai dengan PDF/A
    // Selama proses konversi, validasi juga dilakukan
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // Simpan dokumen output
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Selesai" << std::endl;
}
```

## Mengkonversi file PDF ke PDF/A-3u

Aspose.PDF untuk C++ juga mendukung fitur untuk mengkonversi file PDF ke format PDF/A-3u.

```cpp
void ConverttoPDFA_3u()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.pdf");
    // String untuk nama file log
    String logfilename("log.xml");
    // String untuk nama file output
    String outfilename("PDFToPDFA3b_out.pdf");

    // Buka dokumen
    auto document = new Document(_dataDir + infilename);

    // Konversi ke dokumen sesuai PDF/A
    // Selama proses konversi, validasi juga dilakukan
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // Simpan dokumen output
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Selesai" << std::endl;
}
```

## Tambahkan Lampiran ke file PDF/A

Jika Anda memiliki kebutuhan untuk melampirkan file ke format kepatuhan PDF/A, maka kami merekomendasikan menggunakan nilai PDF_A_3A dari enumerasi Aspose.PDF.PdfFormat.

PDF/A_3a adalah format yang menyediakan fitur untuk melampirkan format file apapun sebagai lampiran ke file sesuai PDF/A.

```cpp
void ConverttoPDFA_AddAttachment()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.pdf");
    // String untuk nama file log
    String logfilename("log.xml");
    // String untuk nama file output
    String outfilename("PDFToPDFA3b_out.pdf");

    // Buka dokumen
    auto document = new Document(_dataDir + infilename);

    // Siapkan file baru untuk ditambahkan sebagai lampiran
    auto fileSpecification = MakeObject<FileSpecification>(_dataDir + String("aspose-logo.jpg"), String("File Gambar Besar"));
    // Tambahkan lampiran ke koleksi lampiran dokumen
    document->get_EmbeddedFiles()->Add(fileSpecification);

    // Konversi ke dokumen sesuai PDF/A
    // Selama proses konversi, validasi juga dilakukan
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3A, ConvertErrorAction::Delete);

    // Simpan dokumen output
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Selesai" << std::endl;
}
```

## Gantikan font yang hilang dengan font alternatif

Sesuai standar PDFA, font harus disematkan dalam dokumen PDFA. Namun, jika font tidak disematkan dalam dokumen sumber atau tidak ada di mesin maka PDFA gagal validasi. Dalam hal ini, kami memiliki persyaratan untuk mengganti font yang hilang dengan beberapa font alternatif dari mesin. Kita dapat menggantikan font yang hilang menggunakan metode SimpleFontSubsituation seperti berikut selama konversi PDF ke PDFA.

```cpp
void ConverttoPDFA_ReplaceFont()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file input
    String infilename("sample.pdf");
    // String untuk nama file log
    String logfilename("log.xml");
    // String untuk nama file input
    String outfilename("PDFToPDFA3b_out.pdf");

    // Buka dokumen
    auto document = new Document(_dataDir + infilename);

    System::SharedPtr<Aspose::Pdf::Text::Font> originalFont;
    try
    {
        originalFont = FontRepository::FindFont(String("AgencyFB"));
    }
    catch (Exception)
    {
        // Font tidak ada di mesin tujuan
        auto substitutions = FontRepository::get_Substitutions();
        auto substitution = MakeObject<SimpleFontSubstitution>(String("AgencyFB"), String("Helvetica"));
        substitutions->Add(substitution);
    }

    // Konversi ke dokumen yang sesuai PDF/A
    try {
        // Selama proses konversi, validasi juga dilakukan
        document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

        // Simpan dokumen keluaran
        document->Save(_dataDir + outfilename);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Selesai" << std::endl;
}
```

{{% alert color="primary" %}}
**Cobalah mengonversi PDF ke PDF/A secara online**

Aspose.PDF untuk C++ menghadirkan aplikasi online gratis ["PDF ke PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke PDF/A dengan Aplikasi Gratis](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}