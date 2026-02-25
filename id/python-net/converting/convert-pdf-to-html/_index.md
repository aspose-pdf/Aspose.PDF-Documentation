---
title: Konversi PDF ke HTML dalam Python
linktitle: Konversi format PDF ke HTML
type: docs
weight: 50
url: /id/python-net/convert-pdf-to-html/
lastmod: "2025-09-27"
description: Topik ini menunjukkan cara mengonversi file PDF ke format HTML dengan library Aspose.PDF untuk Python via .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cara Mengonversi PDF ke HTML dalam Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang mengonversi file PDF ke HTML menggunakan Python, khususnya melalui library Aspose.PDF untuk Python via .NET. Artikel ini menjelaskan langkah-langkah yang diperlukan untuk melakukan konversi secara programatis, menyoroti pembuatan objek `Document` dari PDF sumber dan penggunaan `HtmlSaveOptions` untuk menyimpan dokumen dalam format HTML. Artikel ini menyertakan potongan kode Python yang singkat yang menunjukkan proses konversi. Selain itu, artikel ini memperkenalkan alat daring, aplikasi "PDF ke HTML" dari Aspose.PDF, bagi pengguna untuk menjelajahi fungsi dan kualitas konversi. Artikel ini disusun untuk mencakup berbagai topik terkait, memastikan pemahaman mendalam tentang penggunaan Python untuk konversi PDF ke HTML.
---

## Konversi PDF ke HTML

**Aspose.PDF for Python via .NET** menyediakan banyak fitur untuk mengonversi berbagai format file menjadi dokumen PDF dan mengonversi file PDF ke berbagai format output. Artikel ini membahas cara mengonversi file PDF menjadi <abbr title="HyperText Markup Language">HTML</abbr>. Anda dapat menggunakan hanya beberapa baris kode Python untuk mengonversi PDF ke HTML. Anda mungkin perlu mengonversi PDF ke HTML jika ingin membuat situs web atau menambahkan konten ke forum daring. Salah satu cara mengonversi PDF ke HTML adalah dengan menggunakan Python secara programatis.

{{% alert color="success" %}}
**Coba konversi PDF ke HTML secara daring**

Aspose.PDF untuk Python mempersembahkan aplikasi daring gratis ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), di mana Anda dapat mencoba menyelidiki fungsi dan kualitasnya.

[![Aspose.PDF Konversi PDF ke HTML dengan Aplikasi Gratis](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Langkah: Konversi PDF ke HTML dalam Python

1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.
1. Simpan ke [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) dengan memanggil metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke HTML dengan menyimpan gambar di folder yang ditentukan

Fungsi ini mengonversi file PDF ke format HTML menggunakan Aspose.PDF untuk Python via .NET. Semua gambar yang diekstrak disimpan di folder tertentu alih-alih disematkan dalam file HTML.

1. Konfigurasikan opsi penyimpanan HTML.
1. Simpan sebagai HTML dengan gambar eksternal.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_all_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke HTML Multi-Halaman

Fungsi ini mengonversi file PDF menjadi HTML multi-halaman, dimana setiap halaman PDF diekspor sebagai file HTML terpisah. Hal ini membuat hasil lebih mudah dinavigasi dan mengurangi waktu pemuatan untuk PDF besar.

1. Muat PDF sumber menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan 'set split_into_pages'.
1. Simpan dokumen sebagai HTML dengan halaman yang dipisah menjadi file terpisah.
1. Tampilkan pesan konfirmasi.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke HTML dengan menyimpan gambar SVG di folder yang ditentukan

Fungsi ini mengonversi PDF ke format HTML sambil menyimpan semua gambar sebagai file SVG di folder tertentu, alih-alih menyematkannya langsung dalam HTML.

1. Muat PDF sumber menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan 'set special_folder_for_svg_images' ke folder target.
1. Simpan dokumen sebagai HTML dengan gambar SVG eksternal.
1. Tampilkan pesan konfirmasi.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke HTML dan menyimpan gambar SVG terkompresi

Potongan kode ini mengonversi PDF ke format HTML, menyimpan semua gambar sebagai file SVG di folder tertentu dan mengompresnya untuk mengurangi ukuran file.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan:
- Atur 'special_folder_for_svg_images' untuk menyimpan gambar SVG secara eksternal.
- Aktifkan 'compress_svg_graphics_if_any' untuk mengompres gambar SVG.
1. Simpan dokumen sebagai HTML dengan gambar SVG eksternal terkompresi.
1. Tampilkan pesan konfirmasi.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    save_options.compress_svg_graphics_if_any = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke HTML dengan kontrol Gambar Raster Tersemat

Potongan kode ini mengonversi PDF ke format HTML, menyematkan gambar raster sebagai latar belakang halaman PNG. Pendekatan ini mempertahankan kualitas gambar dan tata letak halaman dalam HTML.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan 'set raster_images_saving_mode' menjadi 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. Simpan dokumen sebagai HTML dengan gambar raster tersemat.
1. Cetak pesan konfirmasi.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.raster_images_saving_mode = apdf.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Mengonversi PDF ke Halaman HTML Konten Hanya Badan

Fungsi ini mengonversi PDF menjadi format HTML, menghasilkan konten 'hanya badan' tanpa tag 'html' atau 'head' tambahan, dan memisahkan output menjadi halaman terpisah.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan konfigurasikan:
- 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' untuk menghasilkan hanya konten 'body'.
- 'split_into_pages' untuk membuat file HTML terpisah untuk setiap halaman PDF.
1. Simpan dokumen sebagai HTML dengan opsi yang ditentukan.
1. Cetak pesan konfirmasi.

```python

from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.html_markup_generation_mode = apdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Mengonversi PDF ke HTML dengan Rendering Teks Transparan

Fungsi ini mengonversi PDF menjadi format HTML, merender semua teks sebagai transparan, termasuk teks berbayang, yang menjaga kesetiaan visual sambil memungkinkan styling fleksibel dalam HTML output.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan konfigurasikan:
- 'save_transparent_texts' untuk merender teks normal sebagai transparan.
- 'save_shadowed_texts_as_transparent_texts' untuk merender teks berbayang sebagai transparan.
1. Simpan dokumen sebagai HTML dengan rendering teks transparan.
1. Cetak pesan konfirmasi.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Mengonversi PDF ke HTML dengan Rendering Lapisan Dokumen

Fungsi ini mengonversi PDF menjadi format HTML, mempertahankan lapisan dokumen dengan mengubah konten yang ditandai menjadi lapisan terpisah dalam HTML output. Ini memungkinkan elemen berlapis (seperti anotasi, latar belakang, dan overlay) dirender dengan akurat.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan aktifkan 'convert_marked_content_to_layers' untuk mempertahankan lapisan.
1. Simpan dokumen sebagai HTML dengan konten berlapis.
1. Cetak pesan konfirmasi.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers  = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```


