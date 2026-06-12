---
title: Ubah Ukuran Halaman PDF dengan Python
linktitle: Mengubah Ukuran Halaman
type: docs
weight: 40
url: /id/python-net/change-page-size/
description: Pelajari cara membaca dan mengubah dimensi halaman PDF dengan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mengubah Ukuran Halaman menggunakan Python
Abstract: Artikel ini menunjukkan cara membaca dan memodifikasi dimensi halaman PDF menggunakan Aspose.PDF. Contoh Get Page Size mengambil lebar dan tinggi dari halaman PDF tertentu, memungkinkan pengguna untuk memeriksa tata letak halaman, memvalidasi format, atau menganalisis struktur dokumen. Contoh Set Page Size menunjukkan cara mengubah dimensi halaman—seperti mengonversi halaman pertama ke ukuran A4—sementara juga menampilkan properti kotak (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) sebelum dan sesudah modifikasi.
---

Aspose.PDF for Python via .NET memungkinkan Anda mengubah ukuran halaman PDF dengan baris kode sederhana. Topik ini menunjukkan cara memperbarui dimensi halaman menggunakan [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dan [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API.

Gunakan panduan ini ketika Anda perlu mengubah ukuran halaman PDF yang ada, menormalkan dimensi dokumen, atau memeriksa pengaturan kotak halaman dalam Python.

{{% alert color="primary" %}}

Harap dicatat bahwa properti tinggi dan lebar menggunakan poin sebagai satuan dasar, di mana 1 inch = 72 poin dan 1 cm = 1/2.54 inch = 0.3937 inch = 28.3 poin.

{{% /alert %}}

## Atur Ukuran Halaman PDF menjadi A4

Contoh ini memperbarui ukuran halaman pertama dalam dokumen PDF ke dimensi standar A4. Ini juga mencetak dimensi kotak halaman (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) sebelum dan sesudah mengubah ukuran sehingga Anda dapat memverifikasi perubahan.

Potongan kode berikut menunjukkan cara mengubah dimensi halaman PDF ke ukuran A4:

1. Akses yang pertama [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dari [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Tampilkan ukuran kotak halaman sebelum modifikasi (CropBox, TrimBox, ArtBox, BleedBox, MediaBox).
1. Terapkan dimensi A4 (597.6 × 842.4 poin) menggunakan API halaman.
1. Tampilkan ukuran kotak halaman yang diperbarui.
1. Simpan yang telah dimodifikasi [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ke jalur output yang ditentukan.

```python
import aspose.pdf as ap

def set_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in) and in Aspose.Pdf, 1 inch = 72 points
    # So A4 dimensions in points will be (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## Dapatkan Ukuran Halaman PDF

Potongan kode ini membaca PDF dan mengambil dimensi (lebar dan tinggi) dari halaman pertama. Itu menggunakan [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API untuk mengekstrak batas halaman [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) dan mencetak ukurannya ke konsol. Ini berguna untuk memeriksa tata letak halaman, memverifikasi format, atau menyiapkan dokumen untuk pemrosesan lebih lanjut.

1. Muat PDF sebagai [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Akses yang pertama [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Dapatkan persegi pembatas halaman menggunakan `get_page_rect()`.
1. Ekstrak nilai lebar dan tinggi.
1. Cetak dimensi halaman.

```python
import aspose.pdf as ap

def get_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Get particular page
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### Dapatkan Ukuran Halaman PDF Sebelum dan Sesudah Rotasi

Dapatkan dimensi halaman PDF sebelum dan sesudah menerapkan rotasi 90°. Ini mendemonstrasikan bagaimana rotasi memengaruhi lebar dan tinggi serta cara menggunakannya. `get_page_rect()` dengan atau tanpa pertimbangan rotasi.

1. Buka PDF sebagai [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Akses yang pertama [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Terapkan rotasi 90° menggunakan `page.rotate = ap.Rotation.ON90` (lihat [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) enum).
1. Ambil persegi panjang halaman tanpa rotasi menggunakan `get_page_rect(False)` dan cetak lebar serta tinggi-nya.
1. Ambil persegi halaman dengan mempertimbangkan rotasi menggunakan `get_page_rect(True)` dan cetak lebar serta tinggi-nya.
1. Bandingkan bagaimana dimensi berubah karena rotasi.

```python
import aspose.pdf as ap

def get_page_size_rotation(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

## Topik Halaman Terkait

- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
- [Potong halaman PDF dengan Python](/pdf/id/python-net/crop-pages/)
- [Dapatkan dan atur properti halaman PDF dengan Python](/pdf/id/python-net/get-and-set-page-properties/)
- [Putar halaman PDF dengan Python](/pdf/id/python-net/rotate-pages/)