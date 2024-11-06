---
title: Ekstrak Teks SuperScript dan SubScript dari PDF
linktitle: Ekstrak SuperScript dan SubScript
type: docs
weight: 30
url: id/net/extract-superscripts-subscripts-from-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstrak teks SuperScript dan SubScript dari PDF menggunakan Aspose.PDF di C#.
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Teks SuperScript dan SubScript

Mengekstrak teks dari dokumen PDF adalah hal yang umum. Namun, dalam teks tersebut, ketika diekstrak, **SuperScript dan SubScript** yang terkandung di dalamnya, yang khas untuk dokumen teknis dan artikel, mungkin tidak ditampilkan. SubScript atau SuperScript adalah karakter, angka, atau huruf yang ditempatkan di bawah atau di atas garis teks reguler. Biasanya lebih kecil dari teks lainnya.

**SubScript dan SuperScript** paling sering digunakan dalam rumus, ekspresi matematika, dan spesifikasi senyawa kimia.
**SubScripts dan SuperScripts** sering digunakan dalam rumus, ekspresi matematika, dan spesifikasi senyawa kimia.
Dalam salah satu rilis terbaru, pustaka **Aspose.PDF for .NET** menambahkan dukungan untuk mengekstrak teks SuperScripts dan SubScripts dari PDF.

Gunakan kelas **TextFragmentAbsorber** dan Anda sudah dapat melakukan apa saja dengan teks yang ditemukan, yaitu, Anda dapat menggunakan seluruh teks. Coba potongan kode berikut:

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            writer.WriteLine(absorber.Text);
        }
```

Atau gunakan **TextFragments** secara terpisah dan lakukan berbagai manipulasi dengan mereka, misalnya, urutkan berdasarkan koordinat atau ukuran.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).
Potongan kode berikut ini juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                writer.Write(textFragment.Text);
            }
        }
```
