---
title: Mendapatkan dan Menetapkan Properti Halaman menggunakan Python
linktitle: Mendapatkan dan Menetapkan Properti Halaman
type: docs
weight: 90
url: /id/python-net/get-and-set-page-properties/
description: Bagian ini menunjukkan cara mendapatkan jumlah halaman dalam file PDF, mendapatkan informasi tentang properti halaman PDF seperti warna, dan mengatur properti halaman.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mendapatkan dan Menetapkan Properti Halaman menggunakan Python
Abstract: Artikel ini membahas kemampuan Aspose.PDF untuk Python via .NET, berfokus pada membaca dan mengatur properti halaman dalam file PDF menggunakan Python. Artikel ini mencakup berbagai fungsi termasuk menentukan jumlah halaman dalam PDF, mengakses dan memodifikasi properti halaman, serta menangani informasi warna. Untuk mendapatkan jumlah halaman, kelas `Document` dan koleksi `PageCollection` digunakan, dengan potongan kode yang mendemonstrasikan cara mengambil jumlah halaman, bahkan tanpa menyimpan dokumen. Artikel ini menjelaskan berbagai properti halaman seperti MediaBox, BleedBox, TrimBox, ArtBox, dan CropBox, serta menyediakan contoh kode untuk mengakses properti tersebut. Selain itu, artikel ini membahas cara mengambil halaman tertentu dari PDF dan menyimpannya sebagai dokumen terpisah, serta menentukan tipe warna setiap halaman. Contoh-contoh tersebut diimplementasikan dalam Python, menggambarkan penerapan praktis fitur-fitur ini.
---

Aspose.PDF untuk Python via .NET memungkinkan Anda membaca dan mengatur properti halaman dalam file PDF di aplikasi Python Anda. Bagian ini menunjukkan cara mendapatkan jumlah halaman dalam file PDF, mendapatkan informasi tentang properti halaman PDF seperti warna, dan mengatur properti halaman. Contoh-contohnya menggunakan API [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) dan ditulis dalam Python.

## Dapatkan Jumlah Halaman dalam File PDF

Saat bekerja dengan dokumen, Anda sering ingin mengetahui berapa banyak halaman yang mereka miliki. Dengan Aspose.PDF ini tidak memerlukan lebih dari dua baris kode.

Untuk mendapatkan jumlah halaman dalam file PDF:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Kemudian gunakan properti Count pada koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (dari objek Document) untuk mendapatkan total jumlah halaman dalam dokumen.

Potongan kode berikut menunjukkan cara mendapatkan jumlah halaman file PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count(input_file_name):
    """
    Get the total number of pages in a PDF document.
    Args:
        input_file_name (str): Path to the input PDF file.
    Returns:
        None: Prints the page count to console.
    Example:
        get_page_count("example.pdf")
        # Output: Page Count: 10
    """
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### Dapatkan jumlah halaman tanpa menyimpan dokumen

Kadang-kadang kami menghasilkan file PDF secara dinamis dan selama pembuatan file PDF, kami mungkin menemukan kebutuhan (misalnya membuat Daftar Isi) untuk mendapatkan jumlah halaman file PDF tanpa menyimpan file ke sistem atau stream. Oleh karena itu, untuk memenuhi kebutuhan ini, sebuah metode [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) telah diperkenalkan dalam kelas Document. Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mendapatkan jumlah halaman tanpa menyimpan dokumen.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count_without_saving(input_file_name):
    """
    Get the page count of a PDF document after adding content without saving the file.

    This function opens an existing PDF document, adds a new page with 300 text fragments,
    processes the paragraphs to ensure accurate page counting, and prints the total number
    of pages in the document. The document is not saved to disk.

    Args:
        input_file_name (str): Path to the input PDF file to be processed.

    Returns:
        None: This function prints the page count but does not return a value.

    Example:
        >>> get_page_count_without_saving("sample.pdf")
        Number of pages in document = 2
    """
    # Instantiate Document instance
    document = ap.Document(input_file_name)
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

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop-, dan trimbox. Aspose.PDF memungkinkan Anda mengakses properti-properti ini.

### Memahami Properti Halaman: Perbedaan antara ArtBox, BleedBox, CropBox, MediaBox, TrimBox, dan properti Rect

- **Media box**: Media box adalah kotak halaman terbesar. Itu sesuai dengan ukuran halaman (misalnya A4, A5, US Letter, dll.) yang dipilih saat dokumen dicetak ke PostScript atau PDF. Dengan kata lain, media box menentukan ukuran fisik media tempat dokumen PDF ditampilkan atau dicetak.
- **Bleed box**: Jika dokumen memiliki bleed, PDF juga akan memiliki bleed box. Bleed adalah jumlah warna (atau karya seni) yang melampaui tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong sesuai ukuran (“trimmed”), tinta akan mencapai seluruh tepi halaman. Bahkan jika halaman dipotong tidak tepat - dipotong sedikit di luar tanda pemotongan - tidak akan muncul tepi putih pada halaman.
- **Trim box**: Trim box menunjukkan ukuran akhir dokumen setelah pencetakan dan pemotongan.
- **Art box**: Art box adalah kotak yang digambar di sekitar isi sebenarnya dari halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF ke aplikasi lain.
- **Crop box**: Crop box adalah ukuran “halaman” dimana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya isi dari crop box yang ditampilkan di Adobe Acrobat.
Untuk deskripsi terperinci tentang properti ini, bacalah spesifikasi Adobe.Pdf, khususnya 10.10.1 Batas Halaman.
-- **Page.Rect**: irisan (biasanya persegi panjang yang terlihat) dari MediaBox dan DropBox (`Page.rect`). Lihat tipe [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) untuk properti persegi panjang. Gambar di bawah ini mengilustrasikan properti-properti ini.

Untuk detail lebih lanjut, silakan kunjungi [halaman ini](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Mengakses Properti Halaman

Kelas [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) menyediakan semua properti yang terkait dengan halaman PDF tertentu. Semua halaman file PDF terkandung dalam koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Dari situ, dimungkinkan untuk mengakses objek `Page` individual menggunakan indeksnya, atau mengulang koleksi untuk mendapatkan semua halaman. Setelah sebuah halaman individual diakses, kita dapat mengambil propertinya. Potongan kode berikut menunjukkan cara mendapatkan properti halaman (API `Page`).

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_properties(input_file_name):
    """
    Retrieves and displays various page properties for the first page of a PDF document.

    Args:
        input_file_name (str): Path to the PDF file to analyze.
    """
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
        "Rect": page.rect
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}")

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## Menentukan Warna Halaman

Kelas [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) menyediakan properti yang terkait dengan halaman tertentu dalam dokumen PDF, termasuk jenis warna - RGB, hitam putih, skala abu-abu, atau tidak terdefinisi - yang digunakan halaman tersebut.

Semua halaman file PDF terkandung dalam koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/). Properti [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) menentukan warna elemen pada halaman. Untuk mendapatkan atau menentukan informasi warna untuk halaman PDF tertentu, gunakan properti [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) dari objek [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

Potongan kode berikut menunjukkan cara mengiterasi setiap halaman file PDF untuk mendapatkan informasi warna.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_color_type(input_file_name):
    """
    Analyzes and prints the color type information for each page in a PDF document.

    This function opens a PDF file and iterates through all pages to determine
    the color type of each page (black and white, grayscale, RGB, or undefined).
    The results are printed to the console with human-readable descriptions.

    Args:
        input_file_name (str): Path to the PDF file to analyze.

    Returns:
        None: This function prints results directly to console and doesn't return a value.

    Example:
        >>> get_page_color_type("sample.pdf")
        Page # 1 is RGB.
        Page # 2 is Gray Scale.
        Page # 3 is Black and white.

    Note:
        Requires the aspose.pdf library (imported as ap) to be installed and available.
        The PDF file must be accessible at the specified path.
    """
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
            ap.ColorType.UNDEFINED: "undefined"
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```


