---
title: Ekstrak Teks Dari Stempel menggunakan C#
type: docs
weight: 60
url: /id/net/extract-text-from-stamps/
description: Pelajari cara menggunakan fitur khusus dari Aspose.PDF untuk .NET - ekstraksi teks dari anotasi stempel
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak Teks dari Anotasi Stempel

Aspose.PDF untuk NET memungkinkan Anda untuk mengekstrak teks dari anotasi stempel. Untuk mengekstrak teks dari Anotasi Stempel dalam PDF, langkah-langkah berikut dapat digunakan.

1. Buat objek kelas `Document`
1. Dapatkan `Annotation` yang diinginkan dari daftar anotasi halaman
1. Definisikan objek baru dari kelas `TextAbsorber`
1. Gunakan metode kunjungan TextAbsorber untuk mendapatkan Teks

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```csharp
public static void ExtractText()
{
   Document document = new Document(_dataDir + "ExtractStampText.pdf");
   Annotation item = document.Pages[1].Annotations[1];
   if (item is StampAnnotation annot) {
         TextAbsorber ta = new TextAbsorber();
         XForm ap = annot.Appearance["N"];
         ta.Visit(ap);
         Console.WriteLine(ta.Text);
   }
}
```

