---
title: Konversi PDF ke Microsoft PowerPoint dalam C++
linktitle: Konversi PDF ke PowerPoint
type: docs
weight: 30
url: /cpp/convert-pdf-to-powerpoint/
description: Aspose.PDF memungkinkan Anda untuk mengkonversi PDF ke format PowerPoint menggunakan C++. Ada kemungkinan untuk mengkonversi PDF ke PPTX dengan Slide sebagai Gambar.
lastmod: "2021-11-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Ikhtisar

Artikel ini menjelaskan cara **mengkonversi PDF ke format PowerPoint menggunakan C++**. Ini mencakup topik-topik berikut.

_Format_: **PPTX**
- [C++ PDF ke PPTX](#cpp-pdf-to-pptx)
- [C++ Konversi PDF ke PPTX](#cpp-pdf-to-pptx)
- [C++ Cara mengkonversi file PDF ke PPTX](#cpp-pdf-to-pptx)

_Format_: **Format Microsoft PowerPoint PPTX**
- [C++ PDF ke PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Konversi PDF ke PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Cara mengkonversi file PDF ke PowerPoint](#cpp-pdf-to-powerpoint-pptx)

Topik lain yang dibahas dalam artikel ini.
- [Lihat Juga](#see-also)

## Konversi PDF ke PowerPoint C++

**Aspose.PDF untuk C++** memungkinkan Anda melacak kemajuan konversi PDF ke PPTX.
```

Selama konversi PDF ke <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, teks dirender sebagai Teks di mana Anda dapat memilih/memperbaruinya. Harap dicatat bahwa untuk mengonversi file PDF ke format PPTX, Aspose.PDF menyediakan kelas bernama [`PptxSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). Objek dari kelas PptxSaveOptions diteruskan sebagai argumen kedua ke metode [`Document.Save(..) method`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa). Potongan kode berikut menunjukkan proses untuk mengonversi file PDF ke format PPTX.

## Konversi sederhana PDF ke PPTX dengan Aspose.PDF untuk C++

Untuk mengonversi PDF ke PPTX, Aspose.PDF untuk C++ menyarankan untuk menggunakan langkah-langkah kode berikut.

<a name="cpp-pdf-to-pptx" id="cpp-pdf-to-pptx"><strong>Langkah-langkah: Mengonversi PDF ke PPTX dalam C++</strong></a> | <a name="cpp-pdf-to-powerpoint-pptx" id="cpp-pdf-to-powerpoint-pptx"><strong>Langkah-langkah: Mengonversi PDF ke format PowerPoint PPTX dalam C++</strong></a>

1. Buat instance dari kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
2. Buat instance dari kelas [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options).
3. Gunakan metode **Save** dari objek **Document** untuk _menyimpan PDF sebagai PPTX_.

```cpp
void ConvertPDFtoPPTX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Simpan keluaran dalam format PPTX
    document->Save(_dataDir + outfilename, SaveFormat::Pptx);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Konversi PDF ke PPTX dengan Slide sebagai Gambar

Jika Anda perlu mengonversi PDF yang dapat dicari menjadi PPTX sebagai gambar daripada teks yang dapat dipilih, Aspose.PDF menyediakan fitur tersebut melalui kelas [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). Untuk mencapai ini, atur properti [SlidesAsImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#aeca0659ae24ea7cdeb171d941440dcb2) dari kelas [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) menjadi 'true' seperti yang ditunjukkan dalam contoh kode berikut.

```cpp
void ConvertPDFtoPPTX_SlidesAsImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    pptxOptions->set_SlidesAsImages(true);

    // Simpan keluaran dalam format PPTX
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Detail Kemajuan Konversi PPTX

Aspose.PDF untuk C++ memungkinkan Anda melacak kemajuan konversi PDF ke PPTX. The [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) class menyediakan properti [CustomProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#ac9ad606c4b4d7249c5f299fd8d766474) yang dapat ditentukan ke metode khusus untuk melacak kemajuan konversi seperti yang ditunjukkan dalam contoh kode berikut.

```cpp
void ConvertPDFtoPPTX_ProgressDetailConversion()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    //pptxOptions->set_SlidesAsImages(true);
    //Tentukan Custom Progress Handler
    pptxOptions->set_CustomProgressHandler(ShowProgressOnConsole);

    // Simpan output dalam format PPTX
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Selesai" << std::endl;
}
```
Berikut adalah metode khusus untuk menampilkan konversi kemajuan.

```cpp
void ShowProgressOnConsole(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    switch (eventInfo->EventType)
    {
    case ProgressEventType::TotalProgress:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Kemajuan konversi : " << eventInfo->Value << std::endl;
    break;
    case ProgressEventType::ResultPageCreated:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Halaman hasil " << eventInfo->Value << " dari " << eventInfo->MaxValue << " tata letak dibuat." << std::endl;
    break;
    case ProgressEventType::ResultPageSaved:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Halaman hasil " << eventInfo->Value << " dari " << eventInfo->MaxValue << " diekspor." << std::endl;
    break;
    case ProgressEventType::SourcePageAnalysed:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Halaman sumber " << eventInfo->Value << " dari " << eventInfo->MaxValue << " dianalisis." << std::endl;
    break;
    default:
    break;
    }
}
```

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke PowerPoint secara online**

Aspose.PDF untuk C++ menyajikan aplikasi online gratis ["PDF ke PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke PPTX dengan Aplikasi Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Lihat Juga

Artikel ini juga mencakup topik-topik ini. Kode-kodenya sama seperti di atas.

_Format_: **PowerPoint**
- [C++ PDF ke Kode PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF ke API PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF ke PowerPoint Secara Programatis](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF ke Perpustakaan PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Simpan PDF sebagai PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Hasilkan PowerPoint dari PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Buat PowerPoint dari PDF](#cpp-pdf-to-powerpoint-pptx)

- [C++ Konverter PDF ke PowerPoint](#cpp-pdf-to-powerpoint-pptx)

_Format_: **Microsoft PowerPoint PPTX format**
- [C++ PDF ke PowerPoint PPTX Kode](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF ke PowerPoint PPTX API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF ke PowerPoint PPTX Secara Program](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF ke PowerPoint PPTX Perpustakaan](#cpp-pdf-to-powerpoint-pptx)
- [C++ Simpan PDF sebagai PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)
- [C++ Hasilkan PowerPoint PPTX dari PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Buat PowerPoint PPTX dari PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF ke PowerPoint PPTX Konverter](#cpp-pdf-to-powerpoint-pptx)

_Format_: **PPTX**
- [C++ PDF ke PPTX Kode](#cpp-pdf-to-pptx)
- [C++ PDF ke PPTX API](#cpp-pdf-to-pptx)
- [C++ PDF ke PPTX Secara Program](#cpp-pdf-to-pptx)
- [C++ PDF ke PPTX Perpustakaan](#cpp-pdf-to-pptx)
- [C++ Simpan PDF sebagai PPTX](#cpp-pdf-to-pptx)
- [C++ Hasilkan PPTX dari PDF](#cpp-pdf-to-pptx)
- [C++ Buat PPTX dari PDF](#cpp-pdf-to-pptx)
- [C++ PDF ke PPTX Konverter](#cpp-pdf-to-pptx)