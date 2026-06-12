---
title: Potong Halaman PDF dengan Python
linktitle: Memotong Halaman PDF
type: docs
weight: 70
url: /id/python-net/crop-pages/
description: Pelajari cara memotong halaman PDF dan menyesuaikan kotak crop, trim, bleed, dan media di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mengakses dan memodifikasi properti halaman dalam PDF menggunakan Python
Abstract: Artikel ini memberikan gambaran tentang cara mengakses dan memodifikasi properti halaman dalam dokumen PDF menggunakan Aspose.PDF for Python. Artikel ini menjelaskan beberapa properti halaman, termasuk media box, bleed box, trim box, art box, dan crop box, serta menjelaskan peran masing‑masing dalam mendefinisikan dimensi dan batas halaman PDF untuk keperluan pencetakan dan tampilan. Media box merupakan ukuran halaman terbesar, sementara bleed box memastikan cakupan tinta melampaui tepi halaman untuk proses pemotongan. Trim box menandakan ukuran akhir dokumen setelah pemotongan, dan art box menyelimuti konten halaman yang sebenarnya. Crop box menentukan area yang terlihat di Adobe Acrobat. Artikel ini menyertakan cuplikan kode Python yang menunjukkan cara menetapkan crop box baru, bersama dengan kotak‑kotak lainnya, untuk halaman tertentu dalam dokumen PDF. Contoh visual menggambarkan tampilan halaman sebelum dan sesudah penerapan crop, menampilkan penerapan praktis dalam memodifikasi properti‑properti tersebut.
---

## Dapatkan Properti Halaman

Setiap halaman dalam file PDF memiliki sejumlah properti, seperti lebar, tinggi, bleed-, crop-, dan trimbox. Aspose.PDF for Python memungkinkan Anda mengakses properti-properti ini.

Gunakan halaman ini ketika Anda perlu mengurangi area halaman yang terlihat, menyiapkan file untuk alur kerja cetak, atau memeriksa geometri kotak halaman dalam dokumen PDF.

- **media_box**: Media box adalah kotak halaman terbesar. Itu sesuai dengan ukuran halaman (misalnya A4, A5, US Letter, dll.) yang dipilih saat dokumen dicetak ke PostScript atau PDF. Dengan kata lain, media box menentukan ukuran fisik media tempat dokumen PDF ditampilkan atau dicetak.
- **bleed_box**: Jika dokumen memiliki bleed, PDF juga akan memiliki bleed box. Bleed adalah jumlah warna (atau karya seni) yang melampaui tepi halaman. Ini digunakan untuk memastikan bahwa ketika dokumen dicetak dan dipotong ke ukuran (\"trimmed\"), tinta akan mencapai seluruh tepi halaman. Bahkan jika halaman dipotong tidak tepat - dipotong sedikit di luar tanda potong - tidak akan muncul tepi putih pada halaman.
- **trim_box**: Trim box menunjukkan ukuran akhir dokumen setelah pencetakan dan pemangkasan.
- **art_box**: Art box adalah kotak yang digambar di sekitar konten sebenarnya dari halaman dalam dokumen Anda. Kotak halaman ini digunakan saat mengimpor dokumen PDF ke aplikasi lain.
- **crop_box**: Crop box adalah ukuran "page" dimana dokumen PDF Anda ditampilkan di Adobe Acrobat. Dalam tampilan normal, hanya konten dari crop box yang ditampilkan di Adobe Acrobat. Untuk deskripsi rinci tentang properti ini, baca spesifikasi Adobe.Pdf, khususnya 10.10.1 Page Boundaries.

Potong yang pertama [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dari PDF ke area persegi panjang tertentu menggunakan Aspose.PDF for Python. Fungsi tersebut menyesuaikan beberapa kotak halaman—`crop_box`, `trim_box`, `art_box`, dan `bleed_box`—untuk memastikan hasil visual yang konsisten. Pemotongan dapat berguna untuk menghilangkan margin yang tidak diinginkan atau memfokuskan pada wilayah tertentu dari halaman.

1. Muat PDF sebagai [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (gunakan `ap.Document()`).
1. Definisikan persegi panjang pemotongan menggunakan [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) dengan koordinat yang diinginkan (dalam poin).
1. Atur [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)'s `crop_box`, `trim_box`, `art_box`, dan `bleed_box` ke persegi panjang yang didefinisikan.
1. Simpan yang dimodifikasi [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ke file output baru.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page(input_file_name, output_file_name):
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

Potong yang pertama [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) secara dinamis berdasarkan batas gambar pertama yang ditemukan pada halaman. Dengan menggunakan [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/), skrip mengidentifikasi gambar pertama dan menyesuaikan halaman `crop_box` untuk mencocokkan dimensi gambar. Pendekatan ini berguna ketika Anda ingin fokus pada konten visual tertentu daripada koordinat yang telah ditetapkan sebelumnya.

1. Muat PDF sebagai [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Temukan gambar pada halaman pertama menggunakan [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. Periksa apakah gambar ada:
    - Jika ditemukan, atur [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) `crop_box` untuk mencocokkan gambar pertama [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
    - Jika tidak, biarkan halaman tidak berubah dan beri tahu pengguna.
1. Simpan yang dimodifikasi [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ke file output yang ditentukan.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page_by_content(input_file_name, output_file_name):
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

## Topik Halaman Terkait

- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
- [Ubah ukuran halaman PDF di Python](/pdf/id/python-net/change-page-size/)
- [Dapatkan dan atur properti halaman PDF dalam Python](/pdf/id/python-net/get-and-set-page-properties/)
- [Putar halaman PDF dalam Python](/pdf/id/python-net/rotate-pages/)