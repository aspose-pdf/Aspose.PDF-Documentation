---
title: Tambahkan Header dan Footer ke PDF menggunakan Python
linktitle: Tambahkan Header dan Footer ke PDF
type: docs
weight: 50
url: /python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF untuk Python melalui .NET memungkinkan Anda menambahkan header dan footer ke file PDF Anda menggunakan kelas TextStamp.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambahkan Header dan Footer ke PDF menggunakan Python",
    "alternativeHeadline": "Cara menambahkan Header dan Footer ke File PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, tambahkan header, tambahkan footer dalam pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk Python melalui .NET memungkinkan Anda menambahkan header dan footer ke file PDF Anda menggunakan kelas TextStamp."
}
</script>


**Aspose.PDF untuk Python via .NET** memungkinkan Anda menambahkan header dan footer dalam file PDF yang sudah ada. Anda dapat menambahkan gambar atau teks ke dokumen PDF. Juga, cobalah untuk menambahkan header yang berbeda dalam satu File PDF dengan Python.

## Menambahkan Teks di Header File PDF

Anda dapat menggunakan kelas [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) untuk menambahkan teks di header file PDF. Kelas TextStamp menyediakan properti yang diperlukan untuk membuat cap berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan teks di header, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode 'add_stamp' dari Page untuk menambahkan teks di header PDF.

Anda perlu mengatur properti [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) sedemikian rupa sehingga menyesuaikan teks di area header PDF Anda. Anda juga perlu mengatur 'horizontal_alignment' ke Center dan 'vertical_alignment' ke Top.

Cuplikan kode berikut menunjukkan kepada Anda bagaimana menambahkan teks di header file PDF dengan Python:

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Buat header
    textStamp = ap.TextStamp("Header Text")
    # Atur properti dari cap
    textStamp.top_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.TOP
    # Tambahkan header di semua halaman
    for page in document.pages:
        page.add_stamp(textStamp)

    # Simpan dokumen yang telah diperbarui
    document.save(output_pdf)
```

## Menambahkan Teks di Footer File PDF

Anda dapat menggunakan kelas [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) untuk menambahkan teks di footer file PDF.
 Kelas TextStamp menyediakan properti yang diperlukan untuk membuat stempel berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan teks di footer, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode 'add_stamp' dari Page untuk menambahkan teks di footer PDF.

Cuplikan kode berikut menunjukkan cara menambahkan teks di footer file PDF dengan Python:

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    # Buat footer
    textStamp = ap.TextStamp("Footer Text")
    # Atur properti stempel
    textStamp.bottom_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # Tambahkan footer di semua halaman
    for page in document.pages:
        page.add_stamp(textStamp)

    # Simpan file PDF yang diperbarui
    document.save(output_pdf)
```

## Menambahkan Gambar di Header File PDF

Anda dapat menggunakan kelas [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) untuk menambahkan gambar di header file PDF. Kelas Image Stamp menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan gambar di header, Anda perlu membuat objek Document dan objek Image Stamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode 'add_stamp' dari Page untuk menambahkan gambar di header PDF.

Cuplikan kode berikut menunjukkan cara menambahkan gambar di header file PDF dengan Python:

```python 

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Buat header
    image_stamp = ap.ImageStamp(input_image)
    # Atur properti stempel
    image_stamp.top_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.TOP
    # Tambahkan header di semua halaman
    for page in document.pages:
        page.add_stamp(image_stamp)

    # Simpan dokumen yang diperbarui
    document.save(output_pdf)
```

## Menambahkan Gambar di Footer File PDF

Anda dapat menggunakan kelas [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) untuk menambahkan gambar di footer file PDF. [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) kelas menyediakan properti yang diperlukan untuk membuat stempel berbasis gambar seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan gambar di footer, Anda perlu membuat objek Document dan objek Image Stamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode 'add_stamp' dari Page untuk menambahkan gambar di footer PDF.

Kode berikut menunjukkan cara menambahkan gambar di footer file PDF dengan Python:

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    # Buat footer
    image_stamp = ap.ImageStamp(input_image)
    # Atur properti stempel
    image_stamp.bottom_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # Tambahkan footer pada semua halaman
    for page in document.pages:
        page.add_stamp(image_stamp)

    # Simpan file PDF yang diperbarui
    document.save(output_pdf)
```

## Menambahkan Header yang Berbeda dalam Satu File PDF

Kita tahu bahwa kita dapat menambahkan TextStamp di bagian Header/Footer dokumen dengan menggunakan properti [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) atau [bottom_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties), tetapi terkadang kita mungkin memiliki kebutuhan untuk menambahkan beberapa header/footer dalam satu dokumen PDF. **Aspose.PDF for Python via .NET** menjelaskan cara melakukannya.

Untuk memenuhi kebutuhan ini, kita akan membuat objek TextStamp individual (jumlah objek tergantung pada jumlah Header/Footer yang diperlukan) dan akan menambahkannya ke dokumen PDF.
 Kami juga dapat menentukan informasi pemformatan yang berbeda untuk objek stempel individu. Dalam contoh berikut, kami telah membuat objek Dokumen dan tiga objek TextStamp dan kemudian kami menggunakan metode 'add_stamp' dari Page untuk menambahkan teks di bagian header PDF. Cuplikan kode berikut menunjukkan cara menambahkan gambar di footer file PDF dengan Aspose.PDF untuk Python:

```python

    import aspose.pdf as ap

    # Buat tiga stempel
    stamp1 = ap.TextStamp("Header 1")
    stamp2 = ap.TextStamp("Header 2")
    stamp3 = ap.TextStamp("Header 3")

    # Atur keselarasan stempel (tempatkan stempel di bagian atas halaman, sejajar secara horizontal)
    stamp1.vertical_alignment = ap.VerticalAlignment.TOP
    stamp1.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Tentukan gaya font sebagai Bold
    stamp1.text_state.font_style = ap.text.FontStyles.BOLD
    # Atur informasi warna depan teks sebagai merah
    stamp1.text_state.foreground_color = ap.Color.red
    # Tentukan ukuran font sebagai 14
    stamp1.text_state.font_size = 14

    # Sekarang kita perlu mengatur keselarasan vertikal objek stempel kedua sebagai Atas
    stamp2.vertical_alignment = ap.VerticalAlignment.TOP
    # Atur informasi keselarasan Horizontal untuk stempel sebagai Sejajar tengah
    stamp2.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Atur faktor zoom untuk objek stempel
    stamp2.zoom = 10

    # Atur pemformatan objek stempel ketiga
    # Tentukan informasi keselarasan Vertikal untuk objek stempel sebagai ATAS
    stamp3.vertical_alignment = ap.VerticalAlignment.TOP
    # Atur informasi keselarasan Horizontal untuk objek stempel sebagai Sejajar tengah
    stamp3.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Atur sudut rotasi untuk objek stempel
    stamp3.rotate_angle = 35
    # Atur warna latar belakang untuk stempel sebagai merah muda
    stamp3.text_state.background_color = ap.Color.pink
    # Ubah informasi wajah font untuk stempel ke Verdana
    stamp3.text_state.font = ap.text.FontRepository.find_font("Verdana")
    # Stempel pertama ditambahkan pada halaman pertama;
    document.pages[1].add_stamp(stamp1)
    # Stempel kedua ditambahkan pada halaman kedua;
    document.pages[2].add_stamp(stamp2)
    # Stempel ketiga ditambahkan pada halaman ketiga.
    document.pages[3].add_stamp(stamp3)

    # Simpan dokumen yang diperbarui
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Python melalui .NET Library",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
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
    "applicationCategory": "Library Manipulasi PDF untuk Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>