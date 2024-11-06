---
title: Tambahkan Cap Teks di PDF melalui Python
linktitle: Cap Teks dalam Berkas PDF
type: docs
weight: 20
url: id/python-net/text-stamps-in-the-pdf-file/
description: Tambahkan cap teks ke dokumen PDF menggunakan kelas TextStamp dengan pustaka Aspose.PDF untuk Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambahkan Cap Teks di PDF Python",
    "alternativeHeadline": "Tambahkan Cap Teks di PDF Python",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, pembuatan dokumen",
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
    "url": "/python-net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2023-04-04",
    "description": "Tambahkan cap teks ke dokumen PDF menggunakan kelas TextStamp dengan pustaka Aspose.PDF untuk Python."
}
</script>


## Tambahkan Cap Teks dengan Python

Anda dapat menggunakan kelas [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) untuk menambahkan cap teks dalam file PDF. Kelas [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) menyediakan properti yang diperlukan untuk membuat cap berbasis teks seperti ukuran font, gaya font, dan warna font, dll. Untuk menambahkan cap teks, Anda perlu membuat objek Document dan objek TextStamp menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) dari Page untuk menambahkan cap dalam PDF. Cuplikan kode berikut menunjukkan cara menambahkan cap teks dalam file PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Buat cap teks
    text_stamp = ap.TextStamp("Sample Stamp")
    # Atur apakah cap adalah latar belakang
    text_stamp.background = True
    # Atur asal
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Putar cap
    text_stamp.rotate = ap.Rotation.ON90
    # Atur properti teks
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.aqua
    # Tambahkan cap ke halaman tertentu
    document.pages[1].add_stamp(text_stamp)

    # Simpan dokumen keluaran
    document.save(output_pdf)
```


## Mendefinisikan penyelarasan untuk objek TextStamp

Menambahkan watermark ke dokumen PDF adalah salah satu fitur yang sering diminta dan Aspose.PDF untuk Python sepenuhnya mampu menambahkan watermark Gambar serta Teks. Kami memiliki kelas bernama [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) yang menyediakan fitur untuk menambahkan cap teks ke file PDF. Baru-baru ini ada kebutuhan untuk mendukung fitur untuk menentukan penyelarasan teks saat menggunakan objek TextStamp. Jadi untuk memenuhi kebutuhan ini, kami telah memperkenalkan properti [text_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) dalam kelas [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/). Dengan menggunakan properti ini, kita dapat menentukan penyelarasan teks [horizontal_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties).

Cuplikan kode berikut menunjukkan contoh tentang cara memuat dokumen PDF yang ada dan menambahkan TextStamp ke atasnya.

```python

    import aspose.pdf as ap

    # Membuat objek Document dengan file input
    doc = ap.Document(input_pdf)
    # Membuat objek FormattedText dengan string contoh
    text = ap.facades.FormattedText("This")
    # Menambahkan baris teks baru ke FormattedText
    text.add_new_line_text("is sample")
    text.add_new_line_text("Center Aligned")
    text.add_new_line_text("TextStamp")
    text.add_new_line_text("Object")
    # Membuat objek TextStamp menggunakan FormattedText
    stamp = ap.TextStamp(text)
    # Menentukan Penyelarasan Horizontal dari cap teks sebagai rata tengah
    stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Menentukan Penyelarasan Vertikal dari cap teks sebagai rata tengah
    stamp.vertical_alignment = ap.VerticalAlignment.CENTER
    # Menentukan Penyelarasan Teks Horizontal dari TextStamp sebagai rata tengah
    stamp.text_alignment = ap.HorizontalAlignment.CENTER
    # Mengatur margin atas untuk objek stamp
    stamp.top_margin = 20
    # Menambahkan objek stamp ke halaman pertama dokumen
    doc.pages[1].add_stamp(stamp)

    # Menyimpan dokumen yang diperbarui
    doc.save(output_pdf)
```


## Mengisi Teks Stroke sebagai Stempel dalam File PDF

Kami telah mengimplementasikan pengaturan mode rendering untuk skenario penambahan dan pengeditan teks. Untuk merender teks stroke, silakan buat objek TextState untuk mentransfer properti lanjutan. Atur warna untuk stroke. Setelah itu, atur mode rendering teks. Langkah selanjutnya adalah mengikat TextState, dan menambahkan Stempel.

Cuplikan kode berikut menunjukkan penambahan Teks Stroke Isi:

```python

    import aspose.pdf as ap

    # Buat objek TextState untuk mentransfer properti lanjutan
    ts = ap.text.TextState()
    # Atur warna untuk stroke
    ts.stroking_color = ap.Color.gray
    # Atur mode rendering teks
    ts.rendering_mode = ap.text.TextRenderingMode.STROKE_TEXT
    # Memuat dokumen PDF input
    file_stamp = ap.facades.PdfFileStamp(ap.Document(input_pdf))

    stamp = ap.facades.Stamp()
    stamp.bind_logo(
        ap.facades.FormattedText(
            "PAID IN FULL",
            ap.facades.FontColor(100, 100, 100),
            ap.facades.FontStyle.TIMES_ROMAN,
            ap.facades.EncodingType.WINANSI,
            True,
            78.0,
        )
    )

    # Mengikat TextState
    stamp.bind_text_state(ts)
    # Atur asal X,Y
    stamp.set_origin(100, 100)
    stamp.opacity = 5
    stamp.blending_space = ap.facades.BlendingColorSpace.DEVICE_RGB
    stamp.rotation = 45.0
    stamp.is_background = False
    # Tambahkan Stempel
    file_stamp.add_stamp(stamp)
    file_stamp.save(output_pdf)
    file_stamp.close()
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