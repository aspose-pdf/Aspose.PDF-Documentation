---
title: Temukan apakah PDF berisi gambar atau teks
linktitle: Periksa keberadaan teks dan gambar
type: docs
weight: 40
url: /net/find-whether-pdf-file-contains-images-or-text-only/
description: Topik ini menjelaskan cara menemukan apakah file PDF hanya berisi gambar atau teks dengan Kelas PdfExtractor.
lastmod: "2021-06-05"
draft: false
---

## Latar Belakang

File PDF dapat berisi teks dan gambar. Terkadang, pengguna mungkin perlu mencari tahu apakah file PDF hanya berisi teks, atau hanya berisi gambar. Kita juga dapat menemukan apakah file tersebut berisi keduanya atau tidak sama sekali.

{{% alert color="primary" %}}

Cuplikan kode berikut menunjukkan kepada Anda cara memenuhi kebutuhan ini.

{{% /alert %}}

```csharp
 public static void CheckIfPdfContainsTextOrImages()
{
    // Membuat objek memoryStream untuk menyimpan teks yang diekstraksi dari Dokumen
    MemoryStream ms = new MemoryStream();
    // Membuat objek PdfExtractor
    PdfExtractor extractor = new PdfExtractor();

    // Menghubungkan dokumen PDF input ke extractor
    extractor.BindPdf(_dataDir + "FilledForm.pdf");
    // Mengekstraksi teks dari dokumen PDF input
    extractor.ExtractText();
    // Menyimpan teks yang diekstraksi ke file teks
    extractor.GetText(ms);
    // Memeriksa apakah panjang MemoryStream lebih besar atau sama dengan 1

    bool containsText = ms.Length >= 1;

    // Mengekstraksi gambar dari dokumen PDF input
    extractor.ExtractImage();

    // Memanggil metode HasNextImage dalam loop while. Ketika gambar selesai, loop akan keluar
    bool containsImage = extractor.HasNextImage();

    // Sekarang mencari tahu apakah PDF ini hanya teks atau hanya gambar

    if (containsText && !containsImage)
        Console.WriteLine("PDF hanya berisi teks");
    else if (!containsText && containsImage)
        Console.WriteLine("PDF hanya berisi gambar");
    else if (containsText && containsImage)
        Console.WriteLine("PDF berisi teks dan gambar");
    else if (!containsText && !containsImage)
        Console.WriteLine("PDF tidak berisi teks maupun gambar");
}
```