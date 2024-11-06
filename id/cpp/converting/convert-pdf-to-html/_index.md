---
title: Mengonversi File PDF ke Format HTML 
linktitle: Mengonversi File PDF ke Format HTML
type: docs
weight: 50
url: id/cpp/convert-pdf-to-html/
lastmod: "2021-11-19"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan mengonversi file PDF ke format HTML dengan pustaka C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++** menyediakan banyak fitur untuk mengonversi berbagai format file menjadi dokumen PDF dan mengonversi file PDF menjadi berbagai format output. Artikel ini membahas cara mengonversi file PDF menjadi <abbr title="HyperText Markup Language">HTML</abbr>. Aspose.PDF for C++ menyediakan kemampuan untuk mengonversi file HTML menjadi format PDF menggunakan pendekatan InLineHtml. Kami telah menerima banyak permintaan untuk fungsionalitas yang mengonversi file PDF menjadi format HTML dan telah menyediakan fitur ini. Harap dicatat bahwa fitur ini juga mendukung XHTML 1.0.

**Aspose.PDF for C++** mendukung fitur untuk mengonversi file PDF menjadi HTML. Tugas utama yang dapat Anda lakukan dengan pustaka Aspose.PDF adalah sebagai berikut:

- konversi PDF ke HTML;
- membagi Output ke HTML Multi-halaman;
- menentukan Folder untuk Menyimpan File SVG;
- mengompresi Gambar SVG Selama Konversi;
- menentukan Folder Gambar;
- membuat File Selanjutnya dengan Hanya Isi Badan;
- rendering Teks transparan;
- rendering lapisan dokumen PDF.

Aspose.PDF untuk C++ menyediakan kode dua baris untuk mengubah file PDF sumber ke HTML. `SaveFormat enumeration` mengandung nilai Html yang memungkinkan Anda menyimpan file sumber ke HTML. Cuplikan kode berikut menunjukkan proses mengonversi file PDF menjadi HTML.

```cpp
void ConvertPDFtoHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Simpan output dalam format HTML
    document->Save(outfilename, SaveFormat::Html);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Coba konversi PDF ke HTML secara online**

Aspose.PDF untuk C++ menyajikan aplikasi gratis online ["PDF ke HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke HTML dengan Aplikasi Gratis](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

## Memisahkan Output ke HTML Multi-halaman

Saat mengonversi file PDF besar dengan beberapa halaman ke format HTML, output muncul sebagai satu halaman HTML. Ini bisa menjadi sangat panjang. Untuk mengontrol ukuran halaman, dimungkinkan untuk membagi output menjadi beberapa halaman selama konversi PDF ke HTML. Silakan coba gunakan cuplikan kode berikut.

```cpp
void ConvertPDFtoHTML_SplittingOutputToMultiPageHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi objek Opsi Simpan HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();
    // Tentukan untuk membagi output menjadi beberapa halaman
    htmlOptions->set_SplitIntoPages(true);

    try {
    // Simpan output dalam format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Tentukan Folder untuk Menyimpan File SVG

Selama konversi PDF ke HTML, dimungkinkan untuk menentukan folder tempat gambar SVG harus disimpan. Gunakan [`HtmlSaveOption class`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) [`SpecialFolderForSvgImages property`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#ac1bb3905c599118fb3db67fd67a5a06f) untuk menentukan direktori gambar SVG khusus. Properti ini mendapatkan atau menetapkan jalur ke direktori tempat gambar SVG harus disimpan ketika ditemukan selama konversi. Jika parameter kosong atau null, maka file SVG disimpan bersama dengan file gambar lainnya.

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringSVGfiles()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("SaveSVGFiles_out.html");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi objek Opsi Simpan HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Tentukan folder tempat gambar SVG disimpan selama konversi PDF ke HTML
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // Simpan output dalam format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Mengompres Gambar SVG Selama Konversi

Untuk mengompres gambar SVG selama konversi PDF ke HTML, silakan coba menggunakan kode berikut:

```cpp
void ConvertPDFtoHTML_CompressingSVGimages()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Memulai objek Opsi Simpan HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Tentukan folder di mana gambar SVG disimpan selama konversi PDF ke HTML
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // Simpan output dalam format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Selesai" << std::endl;
}
```

## Menentukan Folder Gambar

Kita juga dapat menentukan folder tempat gambar akan disimpan selama konversi PDF ke HTML:

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringAllImages()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi objek HTML Save Option
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Tentukan folder di mana semua gambar disimpan selama konversi PDF ke HTML
    htmlOptions->SpecialFolderForAllImages = (_dataDir + String("\\images\\"));

    // Simpan output dalam format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Selesai" << std::endl;
}
```

## Buat File Selanjutnya dengan Hanya Isi Badan

Baru-baru ini, kami diminta untuk memperkenalkan fitur di mana file PDF dikonversi ke HTML dan pengguna bisa mendapatkan hanya isi dari tag `<body>` untuk setiap halaman. Dokumen ini akan menghasilkan satu file dengan detail CSS, `<html>`, `<head>` dan semua halaman dalam file lain hanya dengan isi `<body>`.

Untuk memenuhi persyaratan ini, properti baru, HtmlMarkupGenerationMode, diperkenalkan ke kelas [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options).

Dengan cuplikan kode sederhana berikut, Anda dapat membagi output HTML menjadi halaman-halaman. Dalam halaman output, semua objek HTML harus berada persis di tempat yang seharusnya (pemrosesan dan output font, pembuatan dan output CSS, pembuatan dan output gambar), kecuali bahwa output HTML akan berisi konten yang saat ini ditempatkan di dalam tag (sekarang tag “body” akan dihilangkan). Namun, saat menggunakan pendekatan ini, tautan ke CSS menjadi tanggung jawab kode Anda, karena hal-hal seperti itu akan dihapus. Untuk tujuan ini, Anda dapat membaca CSS melalui File.ReadAllText() dan mengirimkannya melalui AJAX ke halaman web di mana itu akan diterapkan oleh jQuery.

```cpp
void ConvertPDFtoHTML_CreateSubsequentFilesWithBodyContentsOnly()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("CreateSubsequentFiles_out.html");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi objek HTML Save Option
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->set_SplitIntoPages(true);

    // Simpan output dalam format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Rendering Teks Transparan

Jika file PDF sumber/input berisi teks transparan yang ditutupi oleh gambar latar depan, maka mungkin ada masalah rendering teks. Jadi untuk mengatasi skenario seperti itu, properti [SaveShadowedTextsAsTransparentTexts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#a6269cf414eb8c252f0ba64a0baf2f9ef) dan SaveTransparentTexts dapat digunakan.

```cpp
void ConvertPDFtoHTML_TransparentTextRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("TransparentTextRendering_out.html");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi objek Opsi Simpan HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->SaveShadowedTextsAsTransparentTexts = true;
    htmlOptions->SaveTransparentTexts = true;

    // Simpan output dalam format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Perenderan lapisan dokumen PDF

Kami dapat merender lapisan dokumen PDF dalam elemen tipe lapisan terpisah selama konversi PDF ke HTML:

```cpp
void ConvertPDFtoHTML_DocumentLayersRendering()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("LayersRendering_out.html");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi objek Opsi Simpan HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Tentukan untuk merender lapisan dokumen PDF secara terpisah dalam HTML keluaran
    htmlOptions->set_ConvertMarkedContentToLayers(true);

    // Simpan keluaran dalam format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Selesai" << std::endl;
}
```