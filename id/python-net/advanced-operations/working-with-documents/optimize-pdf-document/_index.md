---
title: Optimalkan, Kompres atau Kurangi Ukuran PDF dengan Python
linktitle: Optimalkan PDF
type: docs
weight: 30
url: /id/python-net/optimize-pdf/
description: Pelajari cara mengoptimalkan dokumen PDF dengan Python untuk meningkatkan kinerja web dan mengurangi ukuran file menggunakan Aspose.PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Kompres halaman PDF menggunakan Python
Abstract: Artikel ini memberikan panduan komprehensif tentang mengoptimalkan file PDF untuk mengurangi ukuran mereka dan meningkatkan kinerja di berbagai platform, seperti halaman web, email, dan sistem penyimpanan. Teknik optimasi meliputi pengurangan ukuran gambar, penghapusan sumber daya yang tidak terpakai, dan unembedding font. Metode spesifik untuk mengoptimalkan PDF untuk web dan mengurangi ukuran file secara keseluruhan dibahas, menggunakan metode `Optimize` dan `OptimizeResources` dalam Aspose.PDF untuk Python. Kustomisasi strategi optimasi dimungkinkan melalui `OptimizationOptions`, memungkinkan tindakan terarah seperti mengompresi gambar, menghapus objek dan stream yang tidak terpakai, menghubungkan stream duplikat, dan unembedding font. Strategi tambahan mencakup meratakan anotasi, menghapus bidang formulir, dan mengkonversi file PDF dari RGB ke skala abu-abu untuk lebih mengurangi ukuran. Artikel ini juga menyoroti penggunaan kompresi FlateDecode untuk optimasi gambar, memastikan manajemen file PDF yang efektif sambil mempertahankan kualitas dan fungsionalitas.
---

Dokumen PDF kadang-kadang dapat berisi data tambahan. Mengurangi ukuran file PDF akan membantu Anda mengoptimalkan transfer jaringan dan penyimpanan. Hal ini sangat berguna untuk publikasi di halaman web, berbagi di jejaring sosial, mengirim via email, atau mengarsipkan dalam penyimpanan. Kita dapat menggunakan beberapa teknik untuk mengoptimalkan PDF:

- Optimalkan konten halaman untuk penelusuran daring
- Perkecil atau kompres semua gambar
- Aktifkan penggunaan kembali konten halaman
- Gabungkan stream duplikat
- Lepaskan font yang ter-embed
- Hapus objek yang tidak terpakai
- Hapus bidang formulir yang diratakan
- Hapus atau ratakan anotasi

{{% alert color="primary" %}}

Penjelasan detail tentang metode optimasi dapat ditemukan di halaman Ikhtisar Metode Optimasi.

{{% /alert %}}

## Optimalkan Dokumen PDF untuk Web

Optimasi, atau linearisasi untuk Web, mengacu pada proses membuat file PDF cocok untuk penelusuran daring menggunakan peramban web. Untuk mengoptimalkan file agar ditampilkan di web:

1. Buka dokumen input dalam objek [Dokumen](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Gunakan metode [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) .
1. Simpan dokumen yang dioptimalkan menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) .

Cuplikan kode berikut menunjukkan cara mengoptimalkan dokumen PDF untuk web.

```python

    import aspose.pdf as ap

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    document.optimize()
    document.save(path_outfile)
```

## Kurangi Ukuran PDF

Metode [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) memungkinkan Anda mengurangi ukuran dokumen dengan membersihkan informasi yang tidak diperlukan. Secara default, metode ini bekerja sebagai berikut:

- Sumber daya yang tidak digunakan pada halaman dokumen dihapus
- Sumber daya yang sama digabungkan menjadi satu objek
- Objek yang tidak terpakai dihapus

Cuplikan di bawah ini adalah contoh. Namun, perlu dicatat bahwa metode ini tidak dapat menjamin pengurangan ukuran dokumen.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(output_pdf)
```

## Manajemen Strategi Optimasi

Kita juga dapat menyesuaikan strategi optimasi. Saat ini, metode [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) menggunakan 5 teknik. Teknik-teknik ini dapat diterapkan menggunakan metode OptimizeResources() dengan parameter [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) .

### Memperkecil atau Mengompresi Semua Gambar

Kita memiliki dua cara untuk bekerja dengan gambar: mengurangi kualitas gambar dan/atau mengubah resolusinya. Dalam hal apapun, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) harus diterapkan. Pada contoh berikut, kami memperkecil gambar dengan mengurangi ImageQuality menjadi 50.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Menghapus Objek yang Tidak Terpakai

Dokumen PDF kadang-kadang berisi objek PDF yang tidak direferensikan oleh objek lain dalam dokumen. Hal ini dapat terjadi, misalnya, ketika sebuah halaman dihapus dari pohon halaman dokumen tetapi objek halaman itu sendiri tidak dihapus. Menghapus objek-objek ini tidak membuat dokumen menjadi tidak valid melainkan memperkecilnya.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedObject option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Menghapus Stream yang Tidak Terpakai

Terkadang dokumen berisi stream sumber daya yang tidak terpakai. Stream ini bukan “objek tidak terpakai” karena mereka direferensikan dari kamus sumber daya halaman. Oleh karena itu, mereka tidak dihapus dengan metode “hapus objek tidak terpakai”. Namun stream ini tidak pernah digunakan dalam konten halaman. Hal ini dapat terjadi ketika sebuah gambar telah dihapus dari halaman tetapi tidak dari sumber daya halaman. Selain itu, situasi ini sering terjadi ketika halaman diekstrak dari dokumen dan halaman dokumen memiliki sumber daya “bersama”, yaitu objek Resources yang sama. Konten halaman dianalisis untuk menentukan apakah stream sumber daya digunakan atau tidak. Stream yang tidak terpakai dihapus. Kadang-kadang ini mengurangi ukuran dokumen. Penggunaan teknik ini serupa dengan langkah sebelumnya:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Menghubungkan Stream Duplikat

Beberapa dokumen dapat berisi beberapa stream sumber daya yang identik (seperti gambar, misalnya). Hal ini dapat terjadi, misalnya ketika sebuah dokumen digabungkan dengan dirinya sendiri. Dokumen output berisi dua salinan independen dari stream sumber daya yang sama. Kami menganalisis semua stream sumber daya dan membandingkannya. Jika stream duplikat, mereka digabungkan, sehingga hanya satu salinan yang tersisa. Referensi diubah secara tepat, dan salinan objek dihapus. Dalam beberapa kasus, ini membantu mengurangi ukuran dokumen.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set LinkDuplicateStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Menghapus Embedding Font

Jika dokumen menggunakan font yang di-embed, itu berarti semua data font disimpan dalam dokumen. Keuntungannya adalah dokumen dapat dilihat terlepas dari apakah font tersebut terpasang di mesin pengguna atau tidak. Namun, embedding font membuat dokumen menjadi lebih besar. Metode unembed font menghapus semua font yang di-embed. Dengan demikian, ukuran dokumen berkurang tetapi dokumen itu sendiri mungkin menjadi tidak dapat dibaca jika font yang tepat tidak terpasang.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set UnembedFonts  option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Sumber daya optimasi menerapkan metode-metode ini pada dokumen. Jika salah satu metode ini diterapkan, ukuran dokumen kemungkinan besar akan berkurang. Jika tidak ada metode yang diterapkan, ukuran dokumen tidak akan berubah, yang jelas.

## Cara Tambahan untuk Mengurangi Ukuran Dokumen PDF

### Menghapus atau Meratakan Anotasi

Anotasi dapat dihapus ketika tidak diperlukan. Jika diperlukan tetapi tidak memerlukan penyuntingan tambahan, anotasi dapat diratakan. Kedua teknik ini akan mengurangi ukuran file.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(output_pdf)
```

### Menghapus Field Formulir

Jika dokumen PDF berisi AcroForms, kita dapat mencoba mengurangi ukuran file dengan meratakan field formulir.

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```

### Mengonversi PDF dari ruang warna RGB ke skala abu-abu

Sebuah file PDF terdiri dari Teks, Gambar, Lampiran, Anotasi, Grafik, dan objek lainnya. Anda mungkin menemukan kebutuhan untuk mengonversi PDF dari ruang warna RGB ke skala abu-abu agar proses pencetakan file PDF tersebut menjadi lebih cepat. Selain itu, ketika file dikonversi ke skala abu-abu, ukuran dokumen juga berkurang, namun hal ini dapat menyebabkan penurunan kualitas dokumen. Fitur ini saat ini didukung oleh fitur Pre-Flight pada Adobe Acrobat, tetapi dalam konteks otomasi Office, Aspose.PDF adalah solusi utama untuk memberikan kemampuan tersebut dalam manipulasi dokumen. Untuk mencapai kebutuhan ini, potongan kode berikut dapat digunakan.

```python

    import aspose.pdf as ap

    # Load source PDF file
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(output_pdf)
```

### Kompresi FlateDecode

Aspose.PDF untuk Python via .NET menyediakan dukungan kompresi FlateDecode untuk fungsi Optimisasi PDF. Potongan kode di bawah ini menunjukkan cara menggunakan opsi dalam Optimisasi untuk menyimpan gambar dengan **FlateDecode** kompresi:

```python

    import aspose.pdf as ap

    # Open Document
    doc = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(output_pdf)
```


