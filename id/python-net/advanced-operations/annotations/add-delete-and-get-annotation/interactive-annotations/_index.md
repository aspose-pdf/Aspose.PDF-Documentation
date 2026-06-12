---
title: Anotasi Interaktif menggunakan Python
linktitle: Anotasi Interaktif
type: docs
weight: 60
url: /id/python-net/interactive-annotations/
description: Pelajari cara menambahkan, membaca, dan menghapus anotasi tautan, serta cara membuat tombol navigasi dan cetak dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bekerja dengan anotasi PDF interaktif dan tombol di Python.
Abstract: Artikel ini menjelaskan cara bekerja dengan anotasi interaktif dalam file PDF menggunakan Aspose.PDF for Python via .NET. Ini mencakup penambahan anotasi tautan, membaca area tautan yang ada, menghapus anotasi tautan, membuat tombol navigasi halaman, dan menambahkan tombol cetak ke dokumen PDF.
---

Artikel ini menunjukkan cara bekerja dengan anotasi interaktif dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET.

Skrip contoh menunjukkan beberapa alur kerja umum:

- tambahkan anotasi tautan ke teks yang ada
- dapatkan persegi panjang anotasi tautan dari sebuah halaman
- hapus anotasi tautan
- buat tombol navigasi
- buat tombol cetak

## Anotasi Tautan

### Tambahkan Anotasi Tautan

Contoh ini mencari fragmen teks pada halaman pertama. `"file"` dan menempatkan anotasi tautan yang dapat diklik di atas area teks yang cocok. Ketika pengguna mengklik anotasi tersebut, PDF membuka alamat web yang ditentukan.

#### Muat dokumen dan temukan teks target

Buat sebuah `Document` objek dan gunakan `TextFragmentAbsorber` untuk mencari teks yang akan menjadi interaktif.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

document.pages[1].accept(text_fragment_absorber)
phone_number_fragment = text_fragment_absorber.text_fragments[1]
```

#### Buat anotasi tautan

Bangun sebuah `LinkAnnotation` menggunakan persegi panjang dari fragmen teks yang cocok dan menetapkan aksi URI padanya.

```python
link_annotation = ap.annotations.LinkAnnotation(
    document.pages[1], phone_number_fragment.rectangle
)
link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")
```

#### Tambahkan anotasi dan simpan PDF

Tambahkan anotasi ke halaman dan simpan file yang diperbarui.

```python
document.pages[1].annotations.append(link_annotation)
document.save(outfile)
```

#### Contoh lengkap

```python
def link_add(infile, outfile):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

    document.pages[1].accept(text_fragment_absorber)
    phone_number_fragment = text_fragment_absorber.text_fragments[1]

    link_annotation = ap.annotations.LinkAnnotation(
        document.pages[1], phone_number_fragment.rectangle
    )
    link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")

    document.pages[1].annotations.append(link_annotation)
    document.save(outfile)
```

### Dapatkan Anotasi Tautan

Untuk memeriksa tautan interaktif yang ada, filter koleksi anotasi pada halaman pertama dan pertahankan hanya item yang tipenya adalah `LINK`. Contoh kemudian mencetak persegi panjang untuk tiap anotasi yang cocok.

#### Muat PDF dan kumpulkan anotasi tautan

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Baca persegi panjang anotasi

Loop melalui anotasi yang difilter dan cetak koordinat setiap area tautan.

```python
for link_annotation in link_annotations:
    print(link_annotation.rect)
```

#### Contoh lengkap

```python
def link_get(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        print(link_annotation.rect)
```

### Hapus Anotasi Tautan

Alur kerja ini menghapus semua anotasi tautan dari halaman pertama dan menyimpan PDF yang telah dibersihkan sebagai file baru.

#### Temukan anotasi tautan untuk dihapus

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Hapus setiap anotasi tautan

```python
for link_annotation in link_annotations:
    document.pages[1].annotations.delete(link_annotation)
```

#### Simpan dokumen yang diperbarui

```python
document.save(outfile)
```

#### Contoh lengkap

```python
def link_delete(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        document.pages[1].annotations.delete(link_annotation)

    document.save(outfile)
```

## Anotasi Widget

### Tambah Tombol Navigasi

Tombol navigasi berguna dalam PDF multi-halaman ketika Anda ingin pembaca berpindah antar halaman tanpa menggunakan antarmuka penampil. Contoh ini menambahkan `Previous Page` dan `Next Page` tombol ke setiap halaman.

#### Tentukan pengaturan tombol

Simpan keterangan tombol, posisi, dan aksi yang telah ditentukan dalam daftar konfigurasi sederhana.

```python
button_config = [
    ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
    ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
]
```

#### Muat PDF dan pastikan ada beberapa halaman

Contoh membuka dokumen sumber dan menambahkan satu halaman lagi sehingga tindakan navigasi memiliki setidaknya dua halaman untuk diproses.

```python
document = ap.Document(infile)
document.pages.add()
```

#### Buat tombol pada setiap halaman

Untuk setiap halaman, buat sebuah `ButtonField`, atur teks dan warnanya, tetapkan aksi navigasi yang telah ditentukan, dan tambahkan ke formulir.

```python
for page in document.pages:
    for name, x_pos, action in button_config:
        rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
        button = ap.forms.ButtonField(page, rect)
        button.partial_name = name
        button.value = name
        button.characteristics.border = ap.Color.red.to_rgb()
        button.characteristics.background = ap.Color.orange.to_rgb()
        button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
        document.form.add(button)
```

#### Simpan hasil

```python
document.save(outfile)
```

#### Contoh lengkap

```python
def navigation_buttons_add(infile, outfile):
    button_config = [
        ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
        ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
    ]

    document = ap.Document(infile)
    document.pages.add()

    for page in document.pages:
        for name, x_pos, action in button_config:
            rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ap.forms.ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

### Tambah Tombol Cetak

Contoh ini membuat PDF satu halaman baru dan menempatkan tombol cetak di dekat bagian atas halaman. Mengklik tombol tersebut memicu aksi cetak yang telah ditentukan dalam penampil PDF yang kompatibel.

#### Buat PDF baru dan tambahkan halaman

```python
document = ap.Document()
page = document.pages.add()
```

#### Buat dan konfigurasikan tombol

Tentukan persegi panjang tombol, buat `ButtonField`, atur caption-nya, dan lampirkan aksi cetak.

```python
rect = ap.Rectangle(72, 748, 164, 768, True)

print_button = ap.forms.ButtonField(page, rect)
print_button.alternate_name = "Print current document"
print_button.color = ap.Color.black
print_button.partial_name = "printBtn1"
print_button.value = "Print Document"
print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
    ap.annotations.PredefinedAction.FILE_PRINT
)
```

#### Atur gaya batas dan latar belakang

Contoh ini mendefinisikan batas padat dan menerapkan warna khusus agar tombol terlihat dalam dokumen.

```python
border = ap.annotations.Border(print_button)
border.style = ap.annotations.BorderStyle.SOLID
border.width = 2
print_button.border = border

print_button.characteristics.border = ap.Color.blue.to_rgb()
print_button.characteristics.background = ap.Color.light_blue.to_rgb()
```

#### Tambahkan tombol dan simpan PDF

```python
document.form.add(print_button)
document.save(outfile)
```

#### Contoh lengkap

```python
def print_button_add(infile, outfile):
    document = ap.Document()
    page = document.pages.add()

    rect = ap.Rectangle(72, 748, 164, 768, True)

    print_button = ap.forms.ButtonField(page, rect)
    print_button.alternate_name = "Print current document"
    print_button.color = ap.Color.black
    print_button.partial_name = "printBtn1"
    print_button.value = "Print Document"
    print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
        ap.annotations.PredefinedAction.FILE_PRINT
    )

    border = ap.annotations.Border(print_button)
    border.style = ap.annotations.BorderStyle.SOLID
    border.width = 2
    print_button.border = border

    print_button.characteristics.border = ap.Color.blue.to_rgb()
    print_button.characteristics.background = ap.Color.light_blue.to_rgb()

    document.form.add(print_button)
    document.save(outfile)
```

## Topik Terkait

- [Impor dan Ekspor Anotasi](/python-net/import-export-annotations/)
- [Anotasi Penandaan](/python-net/markup-annotations/)
- [Anotasi Media](/python-net/media-annotations/)
- [Anotasi Keamanan](/python-net/security-annotations/)
- [Anotasi Bentuk](/python-net/shape-annotations/)
- [Anotasi Berbasis Teks](/python-net/text-based-annotations/)
- [Anotasi Watermark](/python-net/watermark-annotations/)
