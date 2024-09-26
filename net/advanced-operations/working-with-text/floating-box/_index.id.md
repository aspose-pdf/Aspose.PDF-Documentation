---
title: Menggunakan FloatingBox untuk generasi teks
linktitle: Menggunakan FloatingBox
type: docs
weight: 30
url: /net/floating-box/
description: Halaman ini menjelaskan cara memformat teks di dalam kotak mengambang.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Fitur ini juga bekerja di pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Dasar-dasar penggunaan alat FloatingBox

Alat Floating Box adalah alat khusus untuk menempatkan teks dan konten lainnya di halaman PDF. Fitur utamanya adalah pemotongan teks ketika tumpang tindih dengan ukuran FloatingBox.

```cs
Document document = new Document();
Page page = document.Pages.Add();
var box = new FloatingBox(400, 30)
{
    Border = new BorderInfo(BorderSide.All, 1.5f, Color.DarkGreen),
    IsNeedRepeating = false,
};
var text = LoremNET.Lorem.Paragraph(20, 6);
box.Paragraphs.Add(new TextFragment(text));
page.Paragraphs.Add(box);
```  

Pada contoh di atas, kita membuat FloatingBox dengan lebar 400 pt dan tinggi 30 pt.
Juga, dalam contoh ini, lebih banyak teks sengaja dibuat daripada yang bisa muat dalam ukuran yang diberikan.
Akibatnya, teks dipotong.

![Image 1](image01.png)

Properti `IsNeedRepeating` dengan nilai `false` membatasi teks dengan 1 halaman.

Jika kita atur properti ini ke `true` teks akan mengalir ke halaman berikutnya di posisi yang sama.

![Image 2](image02.png)

## Fitur lanjutan dari FloatingBox

### Dukungan multi-kolom

#### Tata letak multi-kolom (kasus sederhana)

`FloatingBox` mendukung tata letak multi-kolom. Untuk membuat tata letak seperti itu, Anda harus menentukan nilai-nilai dari properti ColumnInfo.

* `ColumnWidths` adalah string dengan enumerasi lebar dalam pt.
* `ColumnSpacing` adalah string dengan lebar celah antar kolom.
* `ColumnCount` adalah jumlah kolom.

```cs
Document document = new Document();
Page page = document.Pages.Add();
page.PageInfo.Margin = new MarginInfo(36, 18, 36, 18);
var columnCount = 3;
var spacing = 10;
var width = page.PageInfo.Width 
    - page.PageInfo.Margin.Left 
    - page.PageInfo.Margin.Right 
    - (columnCount - 1) * spacing;
var columnWidth = width / 3;
var box = new FloatingBox()
{
    IsNeedRepeating = true
};
box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
box.ColumnInfo.ColumnSpacing = "{spacing}";
box.ColumnInfo.ColumnCount = columnCount;
var paragraphs = LoremNET.Lorem.Paragraphs(20, 8, 20);
foreach (var paragraph in paragraphs)
{
    box.Paragraphs.Add(new TextFragment(paragraph));
}

page.Paragraphs.Add(box);

document.Save("sample.pdf");
```
Kami menggunakan pustaka tambahan LoremNET dalam contoh di atas dan membuat 20 paragraf. Paragraf-paragraf ini dibagi menjadi tiga kolom dan mengisi halaman berikutnya sampai teks habis.

#### Tata letak multi-kolom dengan permulaan kolom yang dipaksakan

Kami akan melakukan hal yang sama dengan contoh berikut seperti contoh sebelumnya. Perbedaannya adalah kami membuat 3 paragraf. Kami dapat memaksa FloatingBox untuk merender setiap paragraf dalam kolom baru. Untuk melakukan itu, kita perlu mengatur `IsFirstParagraphInColumn` ketika menambahkan teks ke objek FloatingBox.

```cs
Document document = new Document();
Page page = document.Pages.Add();
page.PageInfo.Margin = new MarginInfo(36, 18, 36, 18);
var columnCount = 3;
var spacing = 10;
var width = page.PageInfo.Width 
    - page.PageInfo.Margin.Left 
    - page.PageInfo.Margin.Right 
    - (columnCount - 1) * spacing;
var columnWidth = width / 3;
var box = new FloatingBox()
{
    IsNeedRepeating = true
};
box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
box.ColumnInfo.ColumnSpacing = "{spacing}";
box.ColumnInfo.ColumnCount = 3;

var paragraphs = LoremNET.Lorem.Paragraphs(20, 8, 3);
foreach (var paragraph in paragraphs)
{
    var text = new TextFragment(paragraph)
    {
        IsFirstParagraphInColumn = true
    };
    box.Paragraphs.Add(text);
}

page.Paragraphs.Add(box);

document.Save("sample.pdf");
```
### Dukungan Latar Belakang

Anda dapat mengatur warna latar belakang yang diinginkan dengan menggunakan properti `BackgroundColor`.

```cs
// Inisialisasi objek dokumen
Document document = new Document();
Page page = document.Pages.Add();
var box = new FloatingBox(400, 60)
{
    IsNeedRepeating = false,
    BackgroundColor = Color.LightGreen,
};
var text = LoremNET.Lorem.Paragraph(20, 6);
box.Paragraphs.Add(new TextFragment(text));
page.Paragraphs.Add(box);
```

### Dukungan Offset

FloatingBox dapat dipindahkan ke lokasi lain dengan mengatur nilai `Top` dan `Left`.

```cs
Document document = new Document();
Page page = document.Pages.Add();

var box = new FloatingBox()
{
    Top = -45,
    Left = 15,
    Border = new BorderInfo(BorderSide.All, 1.5f, Color.DarkGreen)
};
var text = LoremNET.Lorem.Paragraph(20, 6);
box.Paragraphs.Add(new TextFragment(text));

page.Paragraphs.Add(new TextFragment(LoremNET.Lorem.Paragraph(20, 6)));
page.Paragraphs.Add(box);            
page.Paragraphs.Add(new TextFragment(LoremNET.Lorem.Paragraph(20, 6)));
```

