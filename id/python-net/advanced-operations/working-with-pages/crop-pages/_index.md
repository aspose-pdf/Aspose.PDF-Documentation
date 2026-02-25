---
title: Memotong Halaman PDF menggunakan Python
linktitle: Memotong Halaman PDF
type: docs
weight: 70
url: /id/python-net/crop-pages/
description: Anda dapat mengubah properti halaman, seperti lebar, tinggi, Bleed-, Crop- dan Trimbox menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mengakses dan memodifikasi properti halaman dalam PDF menggunakan Python
Abstract: Artikel ini memberikan gambaran tentang cara mengakses dan memodifikasi properti halaman dalam dokumen PDF menggunakan Aspose.PDF untuk Python. Artikel ini menjelaskan beberapa properti halaman, termasuk media box, bleed box, trim box, art box, dan crop box, serta peran masing‑masing dalam menentukan dimensi dan batas halaman PDF untuk keperluan pencetakan dan tampilan. Media box mewakili ukuran halaman terbesar, sementara bleed box memastikan tinta menutupi area di luar tepi halaman untuk pemotongan. Trim box menandai ukuran akhir dokumen setelah dipotong, dan art box mengelilingi konten halaman yang sebenarnya. Crop box mendefinisikan area yang terlihat di Adobe Acrobat. Artikel ini menyertakan potongan kode Python yang memperlihatkan cara mengatur crop box baru, bersama dengan box lainnya, untuk halaman tertentu dalam dokumen PDF. Contoh visual menggambarkan tampilan halaman sebelum dan sesudah menerapkan pemotongan, menampilkan penerapan praktis dari modifikasi properti ini.
---

## Dapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop-, dan trimbox. Aspose.PDF untuk Python memungkinkan Anda mengakses properti‑properti ini.

- **media_box**: Media box adalah kotak halaman terbesar. Itu sesuai dengan ukuran halaman (misalnya A4, A5, US Letter, dll.) yang dipilih ketika dokumen dicetak ke PostScript atau PDF. Dengan kata lain, media box menentukan ukuran fisik media tempat dokumen PDF ditampilkan atau dicetak.
- **bleed_box**: Jika dokumen memiliki bleed, PDF juga akan memiliki bleed box. Bleed adalah jumlah warna (atau ilustrasi) yang melampaui tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong ke ukuran ("trimmed"), tinta akan mencapai seluruh tepi halaman. Bahkan jika halaman dipotong tidak tepat - dipotong sedikit di luar tanda trim - tidak akan muncul tepi putih pada halaman.
- **trim_box**: Trim box menunjukkan ukuran akhir dokumen setelah pencetakan dan pemotongan.
- **art_box**: Art box adalah kotak yang digambar di sekitar konten aktual halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF ke aplikasi lain.
- **crop_box**: Crop box adalah ukuran "halaman" tempat dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya isi crop box yang ditampilkan di Adobe Acrobat. Untuk deskripsi detail tentang properti ini, baca spesifikasi Adobe.Pdf, khususnya 10.10.1 Page Boundaries.

Potong halaman pertama [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) PDF ke area persegi panjang tertentu menggunakan Aspose.PDF untuk Python. Fungsi ini menyesuaikan beberapa kotak halaman—`crop_box`, `trim_box`, `art_box`, dan `bleed_box`—untuk memastikan hasil visual yang konsisten. Pemotongan dapat berguna untuk menghilangkan margin yang tidak diinginkan atau memfokuskan pada wilayah tertentu dari halaman.

1. Muat PDF sebagai [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (gunakan `ap.Document()`).
1. Tentukan persegi panjang pemotongan menggunakan [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) dengan koordinat yang diinginkan (dalam poin).
1. Atur `crop_box`, `trim_box`, `art_box`, dan `bleed_box` pada [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) sesuai dengan persegi panjang yang telah ditentukan.
1. Simpan [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) yang telah dimodifikasi ke file output baru.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to a specified rectangular area.
    This function loads a PDF document, defines a new rectangular boundary,
    and applies this boundary to multiple box types (crop, trim, art, and bleed)
    of the first page. The modified document is then saved to a new file.
    Args:
        input_file_name (str): Path to the input PDF file to be cropped.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Note:
        The cropping rectangle is set to coordinates (200, 220, 2170, 1520)
        which defines the visible area of the page. All box types are set
        to the same dimensions to ensure consistent cropping behavior.
    """
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

Dalam contoh ini kami menggunakan file contoh [di sini](crop_page.pdf). Awalnya halaman kami terlihat seperti yang ditunjukkan pada Gambar 1.
![Gambar 1. Halaman Dipotong](crop_page.png)

Setelah perubahan, halaman akan terlihat seperti Gambar 2.
![Gambar 2. Halaman Dipotong](crop_page2.png)

## Potong Halaman PDF Berdasarkan Konten Gambar Pertama

Potong halaman pertama [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) secara dinamis berdasarkan batas gambar pertama yang ditemukan pada halaman. Dengan menggunakan [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/), skrip mengidentifikasi gambar pertama dan menyesuaikan `crop_box` halaman agar sesuai dengan dimensi gambar tersebut. Pendekatan ini berguna ketika Anda ingin memfokuskan pada konten visual tertentu daripada koordinat yang telah ditentukan sebelumnya.

1. Muat PDF sebagai [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Temukan gambar pada halaman pertama menggunakan [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. Periksa apakah gambar ada:
- Jika ditemukan, atur `crop_box` pada [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) agar sesuai dengan [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) gambar pertama.
- Jika tidak, biarkan halaman tetap tidak berubah dan beri tahu pengguna.
1. Simpan [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) yang telah dimodifikasi ke file output yang ditentukan.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page_by_content(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to the bounds of the first image found on that page.
    This function opens a PDF document, locates the first image on the first page,
    and sets the page's crop box to match the image's rectangle dimensions. If no
    images are found, the page remains unchanged.
    Args:
        input_file_name (str): Path to the input PDF file to be processed.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Raises:
        Exception: May raise exceptions related to file I/O operations or PDF processing
                  if the input file is invalid, corrupted, or inaccessible.
    Note:
        - Only processes the first page of the document
        - Uses the first image found on the page for cropping dimensions
        - If no images are found, prints a message and saves the document unchanged
        - Requires the aspose.pdf library (imported as 'ap')
    """
    document = ap.Document(input_file_name)
    # Find first image on first page using ImagePlacementAbsorber
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        first_image = absorber.image_placements[1]
        document.pages[1].crop_box = first_image.rectangle
    else:
        print("No images found on the first page")
    document.save(output_file_name)
```
