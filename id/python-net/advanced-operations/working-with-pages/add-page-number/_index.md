---
title: Tambahkan Nomor Halaman ke PDF dengan Python
linktitle: Tambahkan Nomor Halaman
type: docs
weight: 30
url: /id/python-net/add-page-number/
description: Aspose.PDF untuk Python melalui .NET memungkinkan Anda menambahkan Stempel Nomor Halaman ke file PDF Anda menggunakan kelas PageNumber Stamp.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambahkan Nomor Halaman ke PDF dengan Python",
    "alternativeHeadline": "Cara menambahkan Stempel Nomor Halaman ke PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, stempel nomor halaman",
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
                "areaServed": "AS",
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
    "url": "/python-net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk Python melalui .NET memungkinkan Anda menambahkan Stempel Nomor Halaman ke file PDF Anda menggunakan kelas PageNumberStamp."
}
</script>


All the documents must have page numbers in it. The page number makes it easier for the reader to locate different parts of the document. **Aspose.PDF for Python via .NET** memungkinkan Anda untuk menambahkan nomor halaman dengan [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

Anda dapat menggunakan kelas [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) untuk menambahkan cap nomor halaman dalam file PDF.
 [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) kelas menyediakan properti yang diperlukan untuk membuat stempel berdasarkan nomor halaman seperti format, margin, penjajaran, nomor awal, dll. Untuk menambahkan stempel nomor halaman, Anda perlu membuat objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dan objek [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) menggunakan properti yang diperlukan. Setelah itu, Anda dapat memanggil metode [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) dari [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) untuk menambahkan stempel ke dalam PDF. Anda juga dapat mengatur atribut font dari stempel nomor halaman. Cuplikan kode berikut menunjukkan cara menambahkan nomor halaman dalam file PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Buat stempel nomor halaman
    page_number_stamp = ap.PageNumberStamp()
    # Apakah stempel adalah latar belakang
    page_number_stamp.background = False
    page_number_stamp.format = "Halaman # dari " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Atur properti teks
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.aqua

    # Tambahkan stempel ke halaman tertentu
    document.pages[1].add_stamp(page_number_stamp)

    # Simpan dokumen keluaran
    document.save(output_pdf)
```

## Contoh Langsung

[Tambahkan nomor halaman PDF](https://products.aspose.app/pdf/page-number) adalah aplikasi web gratis online yang memungkinkan Anda untuk menyelidiki bagaimana fungsionalitas penambahan nomor halaman bekerja.

[![Cara menambahkan nomor halaman di pdf menggunakan Python](page_number.png)](https://products.aspose.app/pdf/page-number)

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
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk Python",
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