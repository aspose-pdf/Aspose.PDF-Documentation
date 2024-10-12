---
title: Tambahkan Cap Halaman PDF di PDF
linktitle: Cap halaman di File PDF
type: docs
weight: 30
url: /cpp/page-stamps-in-the-pdf-file/
description: Tambahkan cap halaman ke file PDF menggunakan kelas PdfPageStamp dengan C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Cap Halaman dengan C++

[PdfPageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_page_stamp) dapat digunakan ketika Anda perlu menerapkan cap gabungan yang berisi grafik, teks, tabel. Contoh berikut menunjukkan cara menggunakan cap untuk membuat alat tulis seperti menggunakan Adobe InDesign, Illustrator, Microsoft Word. Misalkan kita memiliki beberapa dokumen input dan kita ingin menerapkan 2 jenis batas dengan warna biru dan plum.

```cpp
void AddPageStamp()
{
    String _dataDir("C:\\Samples\\");

    String inputFileName ("sample-4pages.pdf");
    String outputFileName ("AddPageStamp_out.pdf");
    String pageStampFileName ("PageStamp.pdf");
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto bluePageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 1);
    bluePageStamp->set_Height(800);
    bluePageStamp->set_Background(true);

    auto plumPageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 2);
    plumPageStamp->set_Height(800);
    plumPageStamp->set_Background(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document->get_Pages()->idx_get(i)->AddStamp(bluePageStamp);
        else
            document->get_Pages()->idx_get(i)->AddStamp(plumPageStamp);
    }

    document->Save(_dataDir + outputFileName);
}
```