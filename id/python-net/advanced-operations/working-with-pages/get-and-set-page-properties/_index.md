---
title: Dapatkan dan Atur Properti Halaman PDF dengan Python
linktitle: Mendapatkan dan Mengatur Properti Halaman
type: docs
weight: 90
url: /id/python-net/get-and-set-page-properties/
description: Pelajari cara memeriksa dan memperbarui properti halaman PDF seperti ukuran, jumlah, dan informasi warna dengan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mendapatkan dan Mengatur Properti Halaman menggunakan Python
Abstract: Artikel ini membahas kemampuan Aspose.PDF for Python via .NET, dengan fokus pada membaca dan mengatur properti halaman dalam file PDF menggunakan Python. Artikel ini mencakup berbagai fungsionalitas termasuk menentukan jumlah halaman dalam sebuah PDF, mengakses dan memodifikasi properti halaman, serta menangani informasi warna. Untuk mendapatkan jumlah halaman, kelas `Document` dan koleksi `PageCollection` digunakan, dengan potongan kode yang menunjukkan cara mengambil jumlah halaman, bahkan tanpa menyimpan dokumen. Artikel ini menjelaskan berbagai properti halaman seperti MediaBox, BleedBox, TrimBox, ArtBox, dan CropBox, serta menyediakan contoh kode untuk mengakses properti tersebut. Selain itu, dibahas cara mengambil halaman tertentu dari PDF dan menyimpannya sebagai dokumen terpisah, serta menentukan jenis warna setiap halaman. Contoh-contoh tersebut diimplementasikan dalam Python, menggambarkan aplikasi praktis dari fitur-fitur ini.
---

Aspose.PDF for Python via .NET memungkinkan Anda membaca dan mengatur properti halaman dalam file PDF di aplikasi Python Anda. Bagian ini menunjukkan cara memperoleh jumlah halaman dalam file PDF, mendapatkan informasi tentang properti halaman PDF seperti warna, dan mengatur properti halaman. Contoh-contoh menggunakan [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) API dan ditulis dalam Python.

Gunakan panduan ini ketika Anda perlu memeriksa metadata halaman, menentukan jumlah halaman, atau memperbarui karakteristik tingkat halaman sebagai bagian dari analisis dokumen atau tugas normalisasi.

## Dapatkan Jumlah Halaman dalam File PDF

Saat bekerja dengan dokumen, Anda sering ingin mengetahui berapa banyak halaman yang mereka miliki. Dengan Aspose.PDF ini tidak memerlukan lebih dari dua baris kode.

Untuk mendapatkan jumlah halaman dalam file PDF:

1. Buka file PDF menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class.
1. Kemudian gunakan [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) properti Count koleksi (dari objek Document) untuk mendapatkan total jumlah halaman dalam dokumen.

Cuplikan kode berikut menunjukkan cara mendapatkan jumlah halaman dari file PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count(input_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### Dapatkan jumlah halaman tanpa menyimpan dokumen

Kadang-kadang kami menghasilkan file PDF secara instan dan selama pembuatan file PDF, kami mungkin menemukan kebutuhan (membuat Daftar Isi dll.) untuk memperoleh jumlah halaman file PDF tanpa menyimpan file ke sistem atau aliran. Jadi untuk memenuhi kebutuhan ini, sebuah metode [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) telah diperkenalkan dalam kelas Document. Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mendapatkan jumlah halaman tanpa menyimpan dokumen.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count_without_saving(input_file_name):
    # Instantiate Document instance
    document = ap.Document()
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create loop instance
    for _ in range(0, 300):
        # Add TextFragment to paragraphs collection of page object
        page.paragraphs.add(ap.text.TextFragment("Pages count test"))
    # Process the paragraphs in PDF file to get accurate page count
    document.process_paragraphs()
    # Print number of pages in document
    print("Number of pages in document =", str(len(document.pages)))
```

## Dapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop-, dan trimbox. Aspose.PDF memungkinkan Anda mengakses properti tersebut.

### Memahami Properti Halaman: Perbedaan antara Artbox, BleedBox, CropBox, MediaBox, TrimBox, dan properti Rect

- **Media box**: Media box adalah kotak halaman terbesar. Itu sesuai dengan ukuran halaman (misalnya A4, A5, US Letter, dll.) yang dipilih ketika dokumen dicetak ke PostScript atau PDF. Dengan kata lain, media box menentukan ukuran fisik media tempat dokumen PDF ditampilkan atau dicetak.
- **Bleed box**: Jika dokumen memiliki bleed, PDF juga akan memiliki bleed box. Bleed adalah jumlah warna (atau karya seni) yang melampaui tepi halaman. Ini digunakan untuk memastikan bahwa saat dokumen dicetak dan dipotong ke ukuran (“trimmed”), tinta akan mencapai seluruh tepi halaman. Bahkan jika halaman dipotong tidak tepat - dipotong sedikit di luar tanda pemotongan - tidak akan muncul tepi putih pada halaman.
- **Trim box**: Trim box menunjukkan ukuran akhir dokumen setelah pencetakan dan pemotongan.
- **Art box**: Art box adalah kotak yang digambar di sekitar konten sebenarnya dari halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF ke dalam aplikasi lain.
- **Crop box**: Crop box adalah ukuran “halaman” di mana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya isi dari crop box yang ditampilkan di Adobe Acrobat.
  Untuk deskripsi mendetail tentang properti ini, baca spesifikasi Adobe.Pdf, khususnya 10.10.1 Page Boundaries.
-- **Page.Rect**: perpotongan (biasanya persegi panjang yang terlihat) dari MediaBox dan DropBox (`Page.rect`). Lihat [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) tipe untuk properti persegi panjang. Gambar di bawah ini mengilustrasikan properti tersebut.

Untuk detail lebih lanjut, silakan kunjungi [halaman ini](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Mengakses Properti Halaman

The [Halaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) kelas menyediakan semua properti yang terkait dengan halaman PDF tertentu. Semua halaman file PDF terkandung dalam the of the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) koleksi.

Dari sana, dimungkinkan untuk mengakses baik individu `Page` objek menggunakan indeks mereka, atau iterasi melalui koleksi untuk mendapatkan semua halaman. Begitu sebuah halaman individu diakses, kita dapat mengambil propertinya. Potongan kode berikut menunjukkan cara mendapatkan properti halaman (the `Page` API).

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_properties(input_file_name):
    # Open document
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Get page properties
    boxes = {
        "ArtBox": page.art_box,
        "BleedBox": page.bleed_box,
        "CropBox": page.crop_box,
        "MediaBox": page.media_box,
        "TrimBox": page.trim_box,
        "Rect": page.rect,
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(
            f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}"
        )

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## Tentukan Warna Halaman

The [Halaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) kelas menyediakan properti yang terkait dengan halaman tertentu dalam dokumen PDF, termasuk jenis warna - RGB, hitam putih, skala abu-abu atau tidak terdefinisi - yang digunakan halaman.

Semua halaman file PDF terkandung dalam [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) koleksi. The [warna_jenis](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) properti menentukan warna elemen pada halaman. Untuk mendapatkan atau menentukan informasi warna untuk halaman PDF tertentu, gunakan [Halaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objek [warna_jenis](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) properti.

Potongan kode berikut menunjukkan cara mengiterasi setiap halaman file PDF untuk mendapatkan informasi warna.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_color_type(input_file_name):
    # Open source PDF file
    document = ap.Document(input_file_name)
    # Iterate through all the page of PDF file
    for page_number in range(1, len(document.pages) + 1):
        # Get the color type information for particular PDF page
        page_color_type = document.pages[page_number].color_type
        color_type_map = {
            ap.ColorType.BLACK_AND_WHITE: "Black and white",
            ap.ColorType.GRAYSCALE: "Gray Scale",
            ap.ColorType.RGB: "RGB",
            ap.ColorType.UNDEFINED: "undefined",
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```

## Topik Halaman Terkait

- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
- [Ubah ukuran halaman PDF dalam Python](/pdf/id/python-net/change-page-size/)
- [Memotong halaman PDF di Python](/pdf/id/python-net/crop-pages/)
- [Putar halaman PDF di Python](/pdf/id/python-net/rotate-pages/)