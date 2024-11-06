---
title: Simpan Dokumen PDF menggunakan C++
linktitle: Simpan
type: docs
weight: 30
url: id/cpp/save-pdf-document/
description: Pelajari cara menyimpan file PDF dengan pustaka Aspose.PDF untuk C++.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Simpan dokumen PDF ke sistem file

Anda dapat menyimpan dokumen PDF yang dibuat atau dimanipulasi ke sistem file menggunakan metode Save dari kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void SaveDocument()
{
    // String untuk nama path
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);
    // lakukan beberapa manipulasi, misalnya tambahkan halaman kosong baru
    document->get_Pages()->Add();
    document->Save(_dataDir + modifiedFileName);
}
```

## Simpan dokumen PDF ke stream

Anda juga dapat menyimpan dokumen PDF yang dibuat atau dimanipulasi ke stream dengan menggunakan overload dari metode Save.

```cpp
void SaveDocumentStream()
{
    // String untuk nama path
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);

    // lakukan beberapa manipulasi, misalnya tambahkan halaman kosong baru
    document->get_Pages()->Add();

    auto fileStream = System::IO::File::OpenWrite(_dataDir + modifiedFileName);
    document->Save(fileStream);
}
```

## Simpan format PDF/A atau PDF/X

PDF/A adalah versi standar ISO dari Portable Document Format (PDF) untuk digunakan dalam pengarsipan dan pelestarian jangka panjang dokumen elektronik. PDF/A berbeda dari PDF karena melarang fitur yang tidak cocok untuk pengarsipan jangka panjang, seperti penghubungan font (berlawanan dengan penyematan font) dan enkripsi. Persyaratan ISO untuk penampil PDF/A mencakup pedoman manajemen warna, dukungan font yang disematkan, dan antarmuka pengguna untuk membaca anotasi yang disematkan.

PDF/X adalah subset dari standar ISO PDF. Tujuan dari PDF/X adalah untuk memfasilitasi pertukaran grafis, dan oleh karena itu memiliki serangkaian persyaratan terkait pencetakan yang tidak berlaku untuk file PDF standar.

Dalam kedua kasus, metode Save digunakan untuk menyimpan dokumen, sementara dokumen harus dipersiapkan menggunakan [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_format_conversion_options).

```cpp
void SaveDocumentAsPDFx()
{
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file
    String infilename("SimpleResume.pdf");
    String outfilename("SimpleResume_A3U.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    auto options = new PdfFormatConversionOptions(Aspose::Pdf::PdfFormat::PDF_A_3U);
    try
    {
        document->Convert(options);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what();
    }

    document->Save(_dataDir + outfilename);
}
```