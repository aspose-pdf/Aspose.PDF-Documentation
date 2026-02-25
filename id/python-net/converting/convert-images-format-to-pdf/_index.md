---
title: Konversi berbagai format Gambar ke PDF dalam Python
linktitle: Konversi Gambar ke PDF
type: docs
weight: 60
url: /id/python-net/convert-images-format-to-pdf/
lastmod: "2025-09-01"
description: Konversi berbagai format gambar seperti BMP, CGM, DICOM, PNG, TIFF, EMF, dan SVG ke PDF menggunakan Python.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cara Mengonversi Gambar ke PDF dalam Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang mengonversi berbagai format gambar ke PDF menggunakan Python, khususnya dengan memanfaatkan pustaka Aspose.PDF untuk Python melalui .NET. Artikel ini mencakup berbagai format gambar termasuk BMP, CGM, DICOM, EMF, GIF, PNG, SVG, dan TIFF. Setiap bagian menjelaskan langkah-langkah yang diperlukan untuk melakukan konversi, menyertakan cuplikan kode untuk mengilustrasikan prosesnya. Misalnya, mengonversi BMP ke PDF melibatkan pembuatan dokumen PDF baru, mendefinisikan penempatan gambar, menyisipkan gambar, dan menyimpan dokumen. Demikian pula, untuk format seperti CGM, DICOM, dan lainnya, opsi pemuatan khusus dan langkah pemrosesan dijabarkan. Artikel ini juga menyoroti keunggulan menggunakan Aspose.PDF untuk tugas tersebut, seperti dukungan terhadap berbagai metode enkoding dan kemampuan memproses gambar satu frame maupun multi-frame.
---

## Konversi Gambar Python ke PDF

**Aspose.PDF for Python via .NET** memungkinkan Anda mengonversi berbagai format gambar ke file PDF. Perpustakaan kami menunjukkan cuplikan kode untuk mengonversi format gambar paling populer, seperti - BMP, CGM, DICOM, EMF, JPG, PNG, SVG, dan format TIFF.

## Konversi BMP ke PDF

Konversi file BMP ke dokumen PDF menggunakan perpustakaan **Aspose.PDF for Python via .NET**.

<abbr title="Bitmap Image File">BMP</abbr> gambar adalah File yang memiliki ekstensi. BMP mewakili file Gambar Bitmap yang digunakan untuk menyimpan gambar digital bitmap. Gambar ini independen dari adaptor grafis dan juga disebut format file bitmap tidak tergantung perangkat (DIB).

Anda dapat mengonversi BMP ke file PDF dengan API Aspose.PDF untuk Python via .NET. Oleh karena itu, Anda dapat mengikuti langkah-langkah berikut untuk mengonversi gambar BMP:

Langkah-langkah untuk Mengonversi BMP ke PDF dalam Python:

1. Buat dokumen PDF kosong.
1. Buat halaman yang Anda butuhkan, misalnya kami membuat A4, tetapi Anda dapat menentukan format Anda sendiri.
1. Tempatkan gambar (dari infile) di dalam halaman menggunakan persegi panjang yang didefinisikan.
1. Simpan dokumen sebagai PDF.

Jadi cuplikan kode berikut mengikuti langkah-langkah ini dan menunjukkan cara mengonversi BMP ke PDF menggunakan Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba konversi BMP ke PDF secara online**

Aspose mempersembahkan aplikasi gratis daring ["BMP ke PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), dimana Anda dapat mencoba menyelidiki fungsi dan kualitasnya.

[![Aspose.PDF Konversi BMP ke PDF menggunakan Aplikasi Gratis](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Konversi CGM ke PDF

Konversi CGM (Computer Graphics Metafile) menjadi PDF (atau format lain yang didukung) menggunakan Aspose.PDF untuk Python via .NET.

<abbr title="Computer Graphics Metafile">CGM</abbr> adalah ekstensi file untuk format Computer Graphics Metafile yang umum digunakan dalam CAD (computer-aided design) dan aplikasi grafik presentasi. CGM adalah format grafik vektor yang mendukung tiga metode enkoding berbeda: biner (terbaik untuk kecepatan baca program), berbasis karakter (menghasilkan ukuran file terkecil dan memungkinkan transfer data lebih cepat) atau enkoding teks jelas (memungkinkan pengguna membaca dan mengubah file dengan editor teks).

Lihat cuplikan kode berikut untuk mengonversi file CGM ke format PDF.

Langkah-langkah untuk Mengonversi CGM ke PDF dalam Python:

1. Tentukan Jalur File
1. Atur Opsi Muat untuk CGM.
1. Konversi CGM ke PDF
1. Cetak Pesan Konversi

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = apdf.CgmLoadOptions()

    # Open PDF document
    document = apdf.Document(path_infile, options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Konversi DICOM ke PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> adalah standar industri medis untuk pembuatan, penyimpanan, transmisi, dan visualisasi gambar medis digital serta dokumen pasien yang diperiksa.

**Aspose.PDF for Python** memungkinkan Anda mengonversi gambar DICOM dan SVG, tetapi karena alasan teknis dalam menambahkan gambar Anda harus menentukan jenis file yang akan ditambahkan ke PDF.

Cuplikan kode berikut menunjukkan cara mengonversi file DICOM ke format PDF dengan Aspose.PDF. Anda harus memuat gambar DICOM, menempatkan gambar pada halaman dalam file PDF, dan menyimpan output sebagai PDF. Kami menggunakan perpustakaan tambahan pydicom untuk mengatur dimensi gambar ini. Jika Anda ingin memposisikan gambar pada halaman, Anda dapat melewati cuplikan kode ini.

1. Inisialisasi 'ap.Document()' baru dan tambahkan halaman
1. Sisipkan Gambar DICOM. Buat apdf.Image(), atur tipenya ke DICOM, dan berikan jalur file.
1. Sesuaikan Ukuran Halaman. Sesuaikan dimensi halaman PDF dengan ukuran gambar DICOM, hilangkan margin.
1. Tambahkan gambar ke halaman, simpan dokumen ke file output.

1. Muat file DICOM.
1. Ekstrak dimensi gambar.
1. Cetak ukuran gambar.
1. Buat dokumen PDF baru.
1. Siapkan gambar DICOM untuk PDF.
1. Atur ukuran halaman PDF dan margin.
1. Tambahkan gambar ke halaman.
1. Simpan PDF.
1. Cetak Pesan Konversi.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    # Load the DICOM file
    dicom_file = pydicom.dcmread(path_infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = apdf.Document()
    page = document.pages.add()
    image = apdf.Image()
    image.file_type = apdf.ImageFileType.DICOM
    image.file = path_infile

    # Set page dimensions

    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba konversi DICOM ke PDF secara daring**

Aspose mempersembahkan aplikasi gratis daring ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi DICOM ke PDF menggunakan Aplikasi Gratis](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Konversi EMF ke PDF

<abbr title="Enhanced metafile format">EMF</abbr> menyimpan gambar grafis secara independen terhadap perangkat. Metafile EMF terdiri dari record dengan panjang variabel dalam urutan kronologis yang dapat menampilkan gambar yang disimpan setelah diparsing pada perangkat output mana pun.

Potongan kode berikut menunjukkan cara mengonversi EMF ke PDF dengan Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(path_infile, rectangle)

    # Save the file into PDF format
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba konversi EMF ke PDF secara daring**

Aspose mempersembahkan aplikasi gratis daring ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi EMF ke PDF menggunakan Aplikasi Gratis](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Konversi GIF ke PDF

Konversikan file GIF ke dokumen PDF menggunakan perpustakaan **Aspose.PDF for Python via .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> dapat menyimpan data terkompresi tanpa kehilangan kualitas dalam format tidak lebih dari 256 warna. Format GIF yang independen perangkat dikembangkan pada 1987 (GIF87a) oleh CompuServe untuk mentransmisikan gambar bitmap melalui jaringan.

Jadi potongan kode berikut mengikuti langkah-langkah ini dan menunjukkan cara mengonversi BMP ke PDF menggunakan Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba konversi GIF ke PDF secara daring**

Aspose mempersembahkan aplikasi gratis daring ["GIF to PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi GIF ke PDF menggunakan Aplikasi Gratis](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Konversi PNG ke PDF

**Aspose.PDF for Python via .NET** mendukung fitur untuk mengonversi gambar PNG ke format PDF. Lihat potongan kode berikut untuk mewujudkan tugas Anda.

<abbr title="Portable Network Graphics">PNG</abbr> merujuk pada jenis format file gambar raster yang menggunakan kompresi lossless, yang membuatnya populer di kalangan penggunanya.

Anda dapat mengonversi gambar PNG ke PDF menggunakan langkah-langkah berikut:

1. Buat Dokumen PDF Baru.
1. Tentukan Penempatan Gambar.
1. Simpan PDF.
1. Cetak Pesan Konversi.

Selain itu, potongan kode di bawah ini menunjukkan cara mengonversi PNG ke PDF dengan Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba konversi PNG ke PDF secara daring**

Aspose mempersembahkan aplikasi gratis daring ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PNG ke PDF menggunakan Aplikasi Gratis](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Konversi SVG ke PDF

**Aspose.PDF for Python via .NET** menjelaskan cara mengonversi gambar SVG ke format PDF dan cara mendapatkan dimensi file SVG sumber.

Scalable Vector Graphics (SVG) adalah sekumpulan spesifikasi format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak 1999.

<abbr title="Scalable Vector Graphics">SVG</abbr> gambar dan perilakunya didefinisikan dalam file teks XML. Ini berarti mereka dapat dicari, diindeks, diprogram, dan jika diperlukan, dikompres. Sebagai file XML, gambar SVG dapat dibuat dan diedit dengan editor teks apa saja, namun seringkali lebih nyaman membuatnya dengan program menggambar seperti Inkscape.

{{% alert color="success" %}}
**Coba konversi format SVG ke PDF secara daring**

Aspose.PDF for Python via .NET mempersembahkan aplikasi gratis daring ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi SVG ke PDF dengan Aplikasi Gratis](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

Cuplikan kode berikut menunjukkan proses mengonversi file SVG ke format PDF dengan Aspose.PDF untuk Python.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = apdf.SvgLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Konversi TIFF ke PDF

**Aspose.PDF** format file didukung, baik itu gambar TIFF satu frame atau multi-frame. Artinya Anda dapat mengonversi gambar TIFF ke PDF.

TIFF atau TIF, Tagged Image File Format, mewakili gambar raster yang ditujukan untuk penggunaan pada berbagai perangkat yang mematuhi standar format file ini. Gambar TIFF dapat berisi beberapa frame dengan gambar yang berbeda. Format file Aspose.PDF juga didukung, baik itu gambar TIFF satu frame atau multi-frame.

Anda dapat mengonversi TIFF ke PDF dengan cara yang sama seperti format file raster lainnya:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Konversi CDR ke PDF

Cuplikan kode berikut menunjukkan cara memuat file CorelDRAW (CDR) dan menyimpannya sebagai PDF menggunakan 'CdrLoadOptions' di Aspose.PDF untuk Python via .NET.

1. Buat 'CdrLoadOptions()' untuk mengonfigurasi cara file CDR harus dimuat.
1. Inisialisasi objek Document dengan file CDR dan opsi pemuatan.
1. Simpan dokumen sebagai PDF.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = apdf.CdrLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Konversi JPEG ke PDF

Contoh ini menunjukkan cara mengonversi JPEG ke file PDF menggunakan Aspose.PDF untuk Python via .NET.

1. Buat dokumen PDF baru.
1. Tambahkan halaman baru.
1. Tentukan persegi penempatan (ukuran A4: 595x842 poin).
1. Sisipkan gambar ke dalam halaman.
1. Simpan PDF.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

