---
title: PDF Tooltip menggunakan Python
linktitle: PDF Tooltip
type: docs
weight: 20
url: /python-net/pdf-tooltip/
description: Pelajari cara menambahkan tooltip ke fragmen teks dalam PDF menggunakan Python dan Aspose.PDF
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip menggunakan Python",
    "alternativeHeadline": "Tambahkan PDF Tooltip ke Teks",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, tambahkan pdf tooltip",
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
    "url": "/python-net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/pdf-tooltip/"
    },
    "dateModified": "2024-02-04",
    "description": "Pelajari cara menambahkan tooltip ke fragmen teks dalam PDF menggunakan Python dan Aspose.PDF"
}
</script>


## Tambahkan Tooltip ke Teks yang Dicari dengan Menambahkan Tombol Tak Terlihat

Kode ini menunjukkan cara menambahkan tooltip ke fragmen teks tertentu dalam dokumen PDF menggunakan Aspose.PDF. Tooltip ditampilkan ketika kursor mouse melayang di atas teks yang sesuai.

Cuplikan kode berikut akan menunjukkan cara mencapai fungsi ini:

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("Gerakkan kursor mouse di sini untuk menampilkan tooltip")
    )
    document.pages[1].paragraphs.add(
        ap.text.TextFragment(
            "Gerakkan kursor mouse di sini untuk menampilkan tooltip yang sangat panjang"
        )
    )
    document.save(output_pdf)

    # Buka dokumen dengan teks
    document = ap.Document(output_pdf)
    # Buat objek TextAbsorber untuk menemukan semua frasa yang cocok dengan ekspresi reguler
    absorber = ap.text.TextFragmentAbsorber(
        "Gerakkan kursor mouse di sini untuk menampilkan tooltip"
    )
    # Terima absorber untuk halaman dokumen
    document.pages.accept(absorber)
    # Dapatkan fragmen teks yang diekstraksi
    text_fragments = absorber.text_fragments

    # Loop melalui fragmen
    for fragment in text_fragments:
        # Buat tombol tak terlihat pada posisi fragmen teks
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # nilai alternate_name akan ditampilkan sebagai tooltip oleh aplikasi penampil
        field.alternate_name = "Tooltip untuk teks."
        # Tambahkan field tombol ke dokumen
        document.form.add(field)

    # Selanjutnya akan menjadi contoh tooltip yang sangat panjang
    absorber = ap.text.TextFragmentAbsorber(
        "Gerakkan kursor mouse di sini untuk menampilkan tooltip yang sangat panjang"
    )
    document.pages.accept(absorber)
    text_fragments = absorber.text_fragments

    for fragment in text_fragments:
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # Set teks yang sangat panjang
        field.alternate_name = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
            " sed do eiusmod tempor incididunt ut labore et dolore magna"
            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
            " ullamco laboris nisi ut aliquip ex ea commodo consequat."
            " Duis aute irure dolor in reprehenderit in voluptate velit"
            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
            " occaecat cupidatat non proident, sunt in culpa qui officia"
            " deserunt mollit anim id est laborum."
        )
        document.form.add(field)

    # Simpan dokumen
    document.save(output_pdf)
```


## Membuat Blok Teks Tersembunyi dan Menampilkannya saat Mouse Diarahkan

Cuplikan kode Python ini menunjukkan cara menambahkan teks melayang ke dokumen PDF, yang muncul ketika kursor mouse diarahkan ke area tertentu.

Pertama, dokumen PDF baru dibuat, dan sebuah paragraf yang berisi teks "Arahkan kursor mouse di sini untuk menampilkan teks melayang" ditambahkan ke dalamnya. Dokumen tersebut kemudian disimpan.

Selanjutnya, dokumen yang telah disimpan dibuka kembali, dan objek TextAbsorber dibuat untuk menemukan fragmen teks yang sebelumnya ditambahkan. Fragmen teks ini kemudian digunakan untuk menentukan posisi dan karakteristik dari bidang teks melayang.

Sebuah objek TextBoxField dibuat untuk mewakili bidang teks melayang, dan propertinya seperti posisi, nilai, status baca-saja, dan visibilitas diatur sesuai. Selain itu, sebuah nama unik dan karakteristik tampilan diberikan pada bidang tersebut.

Bidang teks melayang ditambahkan ke dalam form dokumen, dan bidang tombol tak terlihat dibuat di posisi fragmen teks asli.
 HideAction events ditugaskan ke bidang tombol, menentukan bahwa bidang teks mengambang harus muncul ketika kursor mouse memasuki sekitarnya dan menghilang ketika kursor keluar.

Akhirnya, bidang tombol ditambahkan ke formulir dokumen, dan dokumen yang dimodifikasi disimpan.

Cuplikan kode ini menyediakan metode untuk membuat elemen teks mengambang interaktif dalam dokumen PDF menggunakan Aspose.PDF untuk Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("Gerakkan kursor mouse di sini untuk menampilkan teks mengambang")
    )
    document.save(output_pdf)

    # Buka dokumen dengan teks
    document = ap.Document(output_pdf)
    # Buat objek TextAbsorber untuk menemukan semua frasa yang cocok dengan ekspresi reguler
    absorber = ap.text.TextFragmentAbsorber(
        "Gerakkan kursor mouse di sini untuk menampilkan teks mengambang"
    )
    # Terima absorber untuk halaman dokumen
    document.pages.accept(absorber)
    # Dapatkan fragmen teks pertama yang diekstraksi
    text_fragments = absorber.text_fragments
    fragment = text_fragments[1]

    # Buat bidang teks tersembunyi untuk teks mengambang di persegi panjang halaman yang ditentukan
    floating_field = ap.forms.TextBoxField(
        fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
    )
    # Atur teks yang akan ditampilkan sebagai nilai bidang
    floating_field.value = 'Ini adalah "bidang teks mengambang".'
    # Kami merekomendasikan untuk membuat bidang 'readonly' untuk skenario ini
    floating_field.read_only = True
    # Setel bendera 'hidden' untuk membuat bidang tidak terlihat saat membuka dokumen
    floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

    # Menetapkan nama bidang yang unik tidak diperlukan tetapi diizinkan
    floating_field.partial_name = "FloatingField_1"

    # Menetapkan karakteristik penampilan bidang tidak diperlukan tetapi membuatnya lebih baik
    floating_field.default_appearance = ap.annotations.DefaultAppearance(
        "Helv", 10, ap.Color.blue.to_rgb()
    )
    floating_field.characteristics.background = ap.Color.light_blue.to_rgb()
    floating_field.characteristics.border = ap.Color.dark_blue.to_rgb()
    floating_field.border = ap.annotations.Border(floating_field)
    floating_field.border.width = 1
    floating_field.multiline = True

    # Tambahkan bidang teks ke dokumen
    document.form.add(floating_field)
    # Buat tombol tak terlihat pada posisi fragmen teks
    button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
    # Buat aksi sembunyikan baru untuk bidang (anotasi) dan bendera ketidaknampakan yang ditentukan.
    # (Anda juga dapat merujuk bidang mengambang dengan nama jika Anda menentukannya di atas.)
    # Tambahkan aksi saat mouse masuk/keluar di bidang tombol tak terlihat

    button_field.actions.on_enter = ap.annotations.HideAction(
        floating_field.partial_name, False
    )
    button_field.actions.on_exit = ap.annotations.HideAction(
        floating_field.partial_name
    )

    # Tambahkan bidang tombol ke dokumen
    document.form.add(button_field)

    # Simpan dokumen
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
    "applicationCategory": "Library Manipulasi PDF untuk .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>