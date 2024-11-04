---
title: Optimalkan, Kompres atau Kurangi Ukuran PDF di Python
linktitle: Optimalkan PDF
type: docs
weight: 30
url: /python-net/optimize-pdf/
keywords: "optimalkan pdf python"
description: Optimalkan file PDF, perkecil semua gambar, kurangi ukuran PDF, Hapus penyematan font, Hapus objek yang tidak digunakan dengan Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimalkan PDF menggunakan Python",
    "alternativeHeadline": "Cara mengoptimalkan PDF dengan Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, optimalkan pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Optimalkan file PDF, perkecil semua gambar, kurangi ukuran PDF, Hapus penyematan font, Hapus objek yang tidak digunakan dengan Python."
}
</script>


Sebuah dokumen PDF kadang-kadang dapat berisi data tambahan. Mengurangi ukuran file PDF akan membantu Anda mengoptimalkan transfer jaringan dan penyimpanan. Ini sangat berguna untuk dipublikasikan di halaman web, dibagikan di jejaring sosial, dikirim melalui e-mail, atau diarsipkan dalam penyimpanan. Kita dapat menggunakan beberapa teknik untuk mengoptimalkan PDF:

- Optimalkan konten halaman untuk penelusuran online
- Kecilkan atau kompres semua gambar
- Aktifkan penggunaan ulang konten halaman
- Gabungkan aliran duplikat
- Hapus penyematan font
- Hapus objek yang tidak digunakan
- Hapus bidang formulir pelipatan
- Hapus atau lipat anotasi

{{% alert color="primary" %}}

Penjelasan terperinci tentang metode optimasi dapat ditemukan di halaman Tinjauan Metode Optimasi.

{{% /alert %}}

## Optimalkan Dokumen PDF untuk Web

Optimasi, atau linearisasi untuk Web, merujuk pada proses membuat file PDF cocok untuk penelusuran online menggunakan peramban web. Untuk mengoptimalkan file untuk tampilan web:

1. Buka dokumen input dalam objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Gunakan metode [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. Simpan dokumen yang telah dioptimalkan menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Cuplikan kode berikut menunjukkan cara mengoptimalkan dokumen PDF untuk web.

```python 

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Optimalkan untuk web
    document.optimize()

    # Simpan dokumen keluaran
    document.save(output_pdf)
```

## Kurangi Ukuran PDF

Metode [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) memungkinkan Anda untuk mengurangi ukuran dokumen dengan menghilangkan informasi yang tidak diperlukan. Secara default, metode ini bekerja sebagai berikut:

- Sumber daya yang tidak digunakan pada halaman dokumen dihapus
- Sumber daya yang sama digabungkan menjadi satu objek

- Objek yang tidak digunakan dihapus

The snippet below is an example. Note, though, that this method cannot guarantee document shrinking.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    # Optimalkan dokumen PDF. Namun, perlu dicatat bahwa metode ini tidak dapat menjamin pengecilan dokumen
    document.optimize_resources()
    # Simpan dokumen yang diperbarui
    document.save(output_pdf)
```

## Manajemen Strategi Optimasi

Kita juga dapat menyesuaikan strategi optimasi. Saat ini, metode [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) menggunakan 5 teknik. Teknik-teknik ini dapat diterapkan menggunakan metode OptimizeResources() dengan parameter [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/).

### Mengecilkan atau Mengompresi Semua Gambar

Kita memiliki dua cara untuk bekerja dengan gambar: mengurangi kualitas gambar dan/atau mengubah resolusinya.
 Dalam hal apapun, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) harus diterapkan. Dalam contoh berikut, kita mengecilkan gambar dengan mengurangi ImageQuality menjadi 50.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    # Inisialisasi OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Atur opsi CompressImages
    optimizeOptions.image_compression_options.compress_images = True
    # Atur opsi ImageQuality
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimalkan dokumen PDF menggunakan OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Simpan dokumen yang diperbarui
    document.save(output_pdf)
```

### Menghapus Objek yang Tidak Digunakan

Dokumen PDF terkadang berisi objek PDF yang tidak dirujuk dari objek lain dalam dokumen. Ini dapat terjadi, misalnya, ketika sebuah halaman dihapus dari pohon halaman dokumen tetapi objek halaman itu sendiri tidak dihapus. Menghapus objek-objek ini tidak membuat dokumen menjadi tidak valid, melainkan mengecilkannya.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    # Atur opsi RemoveUsedObject
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimalkan dokumen PDF menggunakan OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Simpan dokumen yang telah diperbarui
    document.save(output_pdf)
```

### Menghapus Stream yang Tidak Digunakan

Kadang-kadang dokumen berisi stream sumber daya yang tidak digunakan. These streams are not “unused objects” karena mereka direferensikan dari kamus sumber halaman. Oleh karena itu, mereka tidak dihapus dengan metode “remove unused objects”. Tetapi stream ini tidak pernah digunakan dengan konten halaman. Ini mungkin terjadi dalam kasus ketika sebuah gambar telah dihapus dari halaman tetapi tidak dari sumber halaman. Juga, situasi ini sering terjadi ketika halaman diekstraksi dari dokumen dan halaman dokumen memiliki sumber daya “umum”, yaitu, objek Sumber Daya yang sama. Konten halaman dianalisis untuk menentukan apakah stream sumber daya digunakan atau tidak. Stream yang tidak digunakan dihapus. Ini kadang-kadang mengurangi ukuran dokumen. Penggunaan teknik ini mirip dengan langkah sebelumnya:

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    # Atur opsi RemoveUsedStreams
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimalkan dokumen PDF menggunakan OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Simpan dokumen yang diperbarui
    document.save(output_pdf)
```

### Menghubungkan Stream Duplikat

Beberapa dokumen dapat berisi beberapa aliran sumber daya yang identik (seperti gambar, misalnya). Ini dapat terjadi, misalnya ketika sebuah dokumen digabungkan dengan dirinya sendiri. Dokumen keluaran berisi dua salinan independen dari aliran sumber daya yang sama. Kami menganalisis semua aliran sumber daya dan membandingkannya. Jika aliran tersebut diduplikasi, mereka digabungkan, yaitu, hanya satu salinan yang tersisa. Referensi diubah sesuai, dan salinan objek dihapus. Dalam beberapa kasus, ini membantu mengurangi ukuran dokumen.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    # Atur opsi LinkDuplcateStreams
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Optimalkan dokumen PDF menggunakan OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Simpan dokumen yang diperbarui
    document.save(output_pdf)
```

### Menghapus Penyematan Font

Jika dokumen menggunakan font yang disematkan, itu berarti bahwa semua data font disimpan dalam dokumen.
 Keuntungannya adalah dokumen dapat dilihat terlepas dari apakah font diinstal pada mesin pengguna atau tidak. Namun, menyematkan font membuat dokumen menjadi lebih besar. Metode unembed fonts menghapus semua font yang disematkan. Dengan demikian, ukuran dokumen berkurang tetapi dokumen itu sendiri mungkin menjadi tidak terbaca jika font yang benar tidak diinstal.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    # Setel opsi UnembedFonts
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Optimalkan dokumen PDF menggunakan OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Simpan dokumen yang diperbarui
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Ukuran file asli: {}. Ukuran file yang dikurangi: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Sumber daya optimasi menerapkan metode ini ke dokumen. Jika salah satu dari metode ini diterapkan, ukuran dokumen kemungkinan besar akan berkurang. Jika tidak ada metode ini yang diterapkan, ukuran dokumen tidak akan berubah yang mana sudah jelas.

## Cara Tambahan untuk Mengurangi Ukuran Dokumen PDF

### Menghapus atau Meratakan Anotasi

Anotasi dapat dihapus ketika tidak diperlukan. Ketika diperlukan tetapi tidak memerlukan pengeditan tambahan, dapat diratakan. Kedua teknik ini akan mengurangi ukuran file.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    # Ratakan anotasi
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Simpan dokumen yang diperbarui
    document.save(output_pdf)
```

### Menghapus Bidang Formulir

Jika dokumen PDF berisi AcroForms, kita dapat mencoba mengurangi ukuran file dengan meratakan bidang formulir.

```python

    import aspose.pdf as ap

    # Muat formulir PDF sumber
    doc = ap.Document(input_pdf)

    # Ratakan Formulir
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Simpan dokumen yang diperbarui
    doc.save(output_pdf)
```

### Mengonversi PDF dari ruang warna RGB ke skala abu-abu

File PDF terdiri dari Teks, Gambar, Lampiran, Anotasi, Grafik, dan objek lainnya. Anda mungkin memiliki kebutuhan untuk mengonversi PDF dari ruang warna RGB ke skala abu-abu agar lebih cepat saat mencetak file PDF tersebut. Selain itu, ketika file dikonversi ke skala abu-abu, ukuran dokumen juga berkurang, tetapi hal ini juga dapat menyebabkan penurunan kualitas dokumen. Fitur ini saat ini didukung oleh fitur Pre-Flight dari Adobe Acrobat, tetapi ketika berbicara tentang otomatisasi Office, Aspose.PDF adalah solusi terbaik untuk menyediakan kemudahan manipulasi dokumen semacam itu. Untuk memenuhi kebutuhan ini, cuplikan kode berikut dapat digunakan.

```python

    import aspose.pdf as ap

    # Muat file PDF sumber
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Konversi gambar ruang warna RGB ke ruang warna skala abu-abu
        strategy.convert(page)

    # Simpan file hasil
    document.save(output_pdf)
```


### FlateDecode Compression

Aspose.PDF untuk Python via .NET menyediakan dukungan untuk kompresi FlateDecode untuk fungsionalitas Optimasi PDF. Cuplikan kode berikut di bawah ini menunjukkan cara menggunakan opsi dalam Optimasi untuk menyimpan gambar dengan kompresi **FlateDecode**:

```python

    import aspose.pdf as ap

    # Buka Dokumen
    doc = ap.Document(input_pdf)
    # Inisialisasi OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # Untuk mengoptimalkan gambar menggunakan Kompresi FlateDecode, atur opsi optimasi ke Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Atur Opsi Optimasi
    doc.optimize_resources(optimizationOptions)
    # Simpan Dokumen
    doc.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>