---
title: Mengonversi PDF/A ke format PDF 
linktitle: Mengonversi PDF/A ke format PDF
type: docs
weight: 110
url: /cpp/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF/A ke dokumen PDF dengan pustaka C++. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Mengonversi dokumen PDF/A ke PDF

Mengonversi dokumen PDF/A ke PDF berarti menghapus pembatasan <abbr title="Portable Document Format Archive
">PDF/A</abbr> dari dokumen asli. Kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) memiliki metode 'RemovePdfaCompliance' untuk menghapus informasi kepatuhan PDF dari file input/sumber.
Setelah [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) file input.

```cpp
void ConvertPDFAtoPDF()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);

    // Remove PDF/A compliance information
    document->RemovePdfaCompliance();

    // Save updated document
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```

Dokumen ini juga menghapus jika Anda membuat perubahan apa pun di dalam dokumen (misalnya, menambahkan halaman). Dalam contoh berikut, dokumen keluaran kehilangan kepatuhan PDF/A setelah penambahan halaman.

```cpp
void ConvertPDFAtoPDFAdvanced()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    // Menambahkan halaman baru (kosong) menghapus informasi kepatuhan PDF/A.

    document->get_Pages()->Add();
    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```