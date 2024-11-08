---
title: Tambahkan Stempel Halaman PDF ke PDF
linktitle: Stempel halaman di File PDF
type: docs
weight: 30
url: /id/java/page-stamps-in-the-pdf-file/
description: Tambahkan stempel halaman ke file PDF menggunakan kelas PdfPageStamp dengan Java.
lastmod: "2021-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan Stempel Halaman dengan Java

Sebuah [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) dapat digunakan ketika Anda perlu menerapkan stempel komposit yang mengandung grafik, teks, tabel. Contoh berikut menunjukkan cara menggunakan stempel untuk membuat alat tulis seperti menggunakan Adobe InDesign, Illustrator, Microsoft Word. Misalkan kita memiliki beberapa dokumen input dan kita ingin menerapkan 2 jenis batas dengan warna biru dan plum.

```java
public static void AddPageStamp()
{
    String inputFileName = "sample-4pages.pdf";
    String outputFileName = "AddPageStamp_out.pdf";
    String pageStampFileName = "PageStamp.pdf";
    Document document = new Document(_dataDir + inputFileName);

    PdfPageStamp bluePageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 1);
    bluePageStamp.setHeight(800);
    bluePageStamp.setBackground(true);

    PdfPageStamp plumPageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 2);
    plumPageStamp.setHeight(800);
    plumPageStamp.setBackground(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document.getPages().get_Item(i).addStamp(bluePageStamp);
        else
            document.getPages().get_Item(i).addStamp(plumPageStamp);
    }

    document.save(_dataDir + outputFileName);
}
```