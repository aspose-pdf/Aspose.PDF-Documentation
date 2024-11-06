---
title: Bekerja dengan Judul di PDF
type: docs
weight: 40
url: id/python-net/working-with-headings/
description: Buat penomoran dalam judul dokumen PDF Anda dengan Python. Aspose.PDF untuk Python via .NET menawarkan berbagai jenis gaya penomoran.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan Judul di PDF",
    "alternativeHeadline": "Buat Judul di PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, judul di pdf",
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
    "url": "/net/working-with-headings/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-headings/"
    },
    "dateModified": "2022-02-04",
    "description": "Buat penomoran dalam judul dokumen PDF Anda dengan Python. Aspose.PDF untuk Python via .NET menawarkan berbagai jenis gaya penomoran."
}
</script>


## Terapkan Gaya Penomoran pada Judul

Judul adalah bagian penting dari setiap dokumen. Penulis selalu berusaha membuat judul lebih menonjol dan bermakna bagi pembacanya. Jika ada lebih dari satu judul dalam sebuah dokumen, penulis memiliki beberapa opsi untuk mengatur judul-judul ini. Salah satu pendekatan paling umum untuk mengatur judul adalah menulis judul dalam Gaya Penomoran.

[Aspose.PDF untuk Python via .NET](/pdf/python-net/) menawarkan banyak gaya penomoran yang telah ditentukan sebelumnya. Gaya penomoran yang telah ditentukan sebelumnya ini disimpan dalam enumerasi, [NumberingStyle](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/). Nilai-nilai yang telah ditentukan sebelumnya dari enumerasi NumberingStyle dan deskripsinya diberikan di bawah ini:

|**Jenis Judul**|**Deskripsi**|
| :- | :- |
|NumeralsArabic|Tipe Arab, contohnya, 1,1.1,...|
|NumeralsRomanUppercase|Tipe Roman besar, contohnya, I,I.II, ...|
|NumeralsRomanLowercase|Tipe Roman kecil, contohnya, i,i.ii, ...|
|LettersUppercase|Tipe Inggris besar, contohnya, A,A.B, ...|

|LettersLowercase|Tipe Inggris kecil, contohnya, a,a.b, ...|
The [style](https://reference.aspose.com/pdf/python-net/aspose.pdf/heading/#properties) properti dari kelas [Heading](https://reference.aspose.com/pdf/python-net/aspose.pdf/heading/) digunakan untuk mengatur gaya penomoran dari judul.

|**Gambar: Gaya penomoran yang telah ditentukan sebelumnya**|
| :- |
Kode sumber, untuk mendapatkan keluaran yang ditunjukkan pada gambar di atas, diberikan di bawah dalam contoh.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.page_info.width = 612.0
    document.page_info.height = 792.0
    document.page_info.margin = ap.MarginInfo()
    document.page_info.margin.left = 72
    document.page_info.margin.right = 72
    document.page_info.margin.top = 72
    document.page_info.margin.bottom = 72

    page = document.pages.add()
    page.page_info.width = 612.0
    page.page_info.height = 792.0
    page.page_info.margin = ap.MarginInfo()
    page.page_info.margin.left = 72
    page.page_info.margin.right = 72
    page.page_info.margin.top = 72
    page.page_info.margin.bottom = 72

    float_box = ap.FloatingBox()
    float_box.margin = page.page_info.margin

    page.paragraphs.add(float_box)

    heading = ap.Heading(1)
    heading.is_in_list = True
    heading.start_number = 1
    heading.text = "Daftar 1"
    heading.style = ap.NumberingStyle.NUMERALS_ROMAN_LOWERCASE
    heading.is_auto_sequence = True

    float_box.paragraphs.add(heading)

    heading2 = ap.Heading(1)
    heading2.is_in_list = True
    heading2.start_number = 13
    heading2.text = "Daftar 2"
    heading2.style = ap.NumberingStyle.NUMERALS_ROMAN_LOWERCASE
    heading2.is_auto_sequence = True

    float_box.paragraphs.add(heading2)

    heading3 = ap.Heading(2)
    heading3.is_in_list = True
    heading3.start_number = 1
    heading3.text = "nilai, pada tanggal efektif dari rencana, dari properti yang akan didistribusikan di bawah rencana sehubungan dengan setiap yang diizinkan"
    heading3.style = ap.NumberingStyle.LETTERS_LOWERCASE
    heading3.is_auto_sequence = True

    float_box.paragraphs.add(heading3)
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk .NET Library",
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
    "applicationCategory": "Library Manipulasi PDF untuk Python melalui .NET",
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