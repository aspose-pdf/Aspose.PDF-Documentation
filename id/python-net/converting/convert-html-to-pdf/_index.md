---
title: Konversi HTML ke PDF dalam Python
linktitle: Konversi file HTML ke PDF
type: docs
weight: 40
url: /id/python-net/convert-html-to-pdf/
lastmod: "2025-09-27"
description: Pelajari cara mengkonversi konten HTML menjadi dokumen PDF menggunakan Aspose.PDF untuk Python via .NET
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cara mengkonversi HTML ke PDF menggunakan Aspose.PDF untuk Python
Abstract: Aspose.PDF untuk Python via .NET menawarkan solusi kuat untuk membuat file PDF dari halaman web dan kode HTML mentah dalam aplikasi. Artikel ini memberikan panduan tentang mengkonversi HTML ke PDF menggunakan Python, menjelaskan penggunaan Aspose.PDF untuk Python, sebuah API manipulasi PDF yang memungkinkan konversi mulus dokumen HTML ke format PDF. Proses konversi dapat disesuaikan sesuai kebutuhan. Artikel ini menyertakan contoh kode Python yang menunjukkan proses konversi, yang melibatkan pembuatan instance kelas HtmlLoadOptions, menginisialisasi objek Document, dan menyimpan dokumen PDF output menggunakan metode Document.Save(). Selain itu, Aspose menyediakan alat online untuk mengkonversi HTML ke PDF, memungkinkan pengguna mengeksplorasi fungsionalitas dan kualitas proses konversi.
---

## Konversi HTML ke PDF dengan Python

**Aspose.PDF for Python** adalah API manipulasi PDF yang memungkinkan Anda mengkonversi dokumen HTML yang ada ke PDF secara mulus. Proses mengkonversi HTML ke PDF dapat disesuaikan secara fleksibel.

## Konversi HTML ke PDF

Contoh kode Python berikut menunjukkan cara mengkonversi dokumen HTML ke PDF.

1. Buat sebuah instance dari kelas [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
1. Inisialisasi objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Simpan dokumen PDF output dengan memanggil metode **document.save()**.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba konversi HTML ke PDF secara online**

Aspose mempersembahkan aplikasi gratis online ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), dimana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF HTML ke PDF menggunakan Aplikasi Gratis](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Konversi HTML ke PDF menggunakan tipe media

Contoh ini menunjukkan cara mengkonversi file HTML ke PDF menggunakan Aspose.PDF untuk Python via .NET dengan opsi rendering spesifik.

1. Buat sebuah instance dari kelas [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/). Properti 'html_media_type' menerapkan aturan CSS yang ditujukan untuk tampilan di layar. Properti 'html_media_type' dapat memiliki beberapa nilai. Anda dapat mengaturnya menjadi HtmlMediaType.SCREEN atau HtmlMediaType.PRINT.
1. Muat HTML ke dalam ap.Document menggunakan opsi pemuatan.
1. Simpan dokumen sebagai PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.html_media_type = ap.HtmlMediaType.SCREEN
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Konversi HTML ke PDF dengan Aturan CSS Page Prioritas

Beberapa dokumen mungkin berisi pengaturan tata letak yang menggunakan [the Page rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@page), yang dapat menyebabkan ambiguitas saat menghasilkan tata letak. Anda dapat mengontrol prioritas menggunakan properti 'is_priority_css_page_rule'. Jika properti ini diatur ke 'True', aturan CSS akan diterapkan terlebih dahulu.

1. Buat sebuah instance dari kelas [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
1. Setel 'is_priority_css_page_rule = False' untuk menonaktifkan prioritas aturan CSS @page, memungkinkan gaya lain memiliki prioritas.
1. Muat HTML ke dalam ap.Document dengan opsi yang telah dikonfigurasi.
1. Simpan dokumen sebagai PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    # load_options.is_priority_css_page_rule = False
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Konversi HTML ke PDF dengan Font Tersemat

Contoh ini menunjukkan cara mengkonversi file HTML ke PDF sambil menyematkan font. Jika Anda memerlukan dokumen PDF dengan Font Tersemat, Anda harus mengatur 'is_embed_fonts' ke True.

1. Buat 'HtmlLoadOptions()' untuk mengkonfigurasi konversi HTML ke PDF.
1. Setel 'is_embed_fonts = True' untuk memastikan semua font yang digunakan dalam HTML disematkan langsung ke dalam PDF, menjaga kesetiaan visual.
1. Muat HTML ke dalam ap.Document dengan opsi ini.
1. Simpan dokumen sebagai PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.is_embed_fonts = True
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Render Konten pada Satu Halaman selama konversi HTML ke PDF

Contoh ini mendemonstrasikan cara mengkonversi file HTML menjadi PDF satu halaman menggunakan Aspose.PDF untuk Python.
Anda dapat menampilkan semua konten pada satu halaman menggunakan properti 'is_render_to_single_page'.

1. Buat sebuah instance dari 'HtmlLoadOptions()' untuk mengkonfigurasi proses konversi.
1. Aktifkan 'is_render_to_single_page' untuk merender seluruh konten HTML ke dalam satu halaman PDF kontinu.
1. Muat dokumen dengan opsi yang dikonfigurasi ke dalam 'ap.Document'.
1. Simpan hasil sebagai file PDF.

```python
    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = ap.HtmlLoadOptions()
    options.is_render_to_single_page = True

    doc = ap.Document(path_infile, options)
    doc.save(path_outfile)
```

## Konversi MHTML ke PDF

Contoh ini menunjukkan cara mengubah file MHT (MHTML) menjadi dokumen PDF menggunakan Aspose.PDF untuk Python dengan dimensi halaman tertentu.

1. Buat instance ap.MhtLoadOptions() untuk mengonfigurasi pemrosesan file MHT.
1. Atur berbagai parameter, seperti ukuran halaman.
1. Inisialisasi dokumen dengan file input dan opsi pemuatan yang telah dikonfigurasi.
1. Simpan dokumen hasil sebagai PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    load_options = ap.MhtLoadOptions()
    load_options.page_info.width = 842
    load_options.page_info.height= 1191
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
