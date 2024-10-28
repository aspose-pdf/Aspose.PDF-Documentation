```
---
title: Ekstrak Lampiran dari File PDF
type: docs
weight: 10
url: /net/extract-attachments/
description: Bagian ini menjelaskan tentang mengekstraksi lampiran dari pdf dengan kelas PdfExtractor.
lastmod: "2021-06-05"
---

Salah satu kategori utama di bawah kemampuan ekstraksi dari [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) adalah ekstraksi lampiran.
``` Kategori ini menyediakan serangkaian metode, yang tidak hanya membantu mengekstrak lampiran tetapi juga menyediakan metode yang dapat memberikan informasi terkait lampiran yaitu metode [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) dan [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) masing-masing menyediakan informasi lampiran dan nama lampiran. Untuk mengekstrak dan kemudian mendapatkan lampiran, kita menggunakan metode [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) dan [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment).

Cuplikan kode berikut menunjukkan kepada Anda cara menggunakan metode PdfExtractor:

```csharp
public static void ExtractAttachments()
{
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample-attach.pdf");

    // Ekstrak lampiran
    pdfExtractor.ExtractAttachment();

    // Dapatkan nama lampiran
    if (pdfExtractor.GetAttachNames().Count > 0)
    {
         Console.WriteLine("Mengekstrak dan menyimpan...");
         // Dapatkan lampiran yang diekstrak
         pdfExtractor.GetAttachment(_dataDir);
    }
}
```