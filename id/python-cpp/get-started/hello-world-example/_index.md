---
title: Contoh Hello World menggunakan bahasa Python
linktitle: Contoh Hello World
type: docs
weight: 20
url: /id/python-cpp/hello-world-example/
description: Contoh ini menunjukkan cara membuat dokumen PDF sederhana "Hello, World!" menggunakan Aspose.PDF untuk Python
lastmod: "2023-07-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Contoh Hello World menggunakan bahasa Python",
    "alternativeHeadline": "Contoh Aspose.PDF Python (via C++)",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, Python, pembuatan dokumen",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-cpp.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://https://www.youtube.com/@AsposePDF",
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
    "url": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "Contoh ini menunjukkan cara membuat dokumen PDF sederhana menggunakan Aspose.PDF untuk Python.",
    "articleBody": "Kasus penggunaan sederhana dapat membantu menunjukkan fitur dari bahasa pemrograman atau perangkat lunak. Ini biasanya dilakukan dengan contoh \"Hello World\".\n\nAspose.PDF untuk Python via C++ adalah API PDF yang kuat yang memungkinkan pengembang untuk membuat, memanipulasi, dan mengkonversi dokumen PDF dalam aplikasi Python mereka. Ini mendukung bekerja dengan berbagai format file seperti PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX, dan format file gambar. Dalam artikel ini, kami akan menunjukkan kepada Anda bagaimana membuat dokumen PDF dengan teks \"Hello World!\" menggunakan API Aspose.PDF. Anda perlu menginstal Aspose.PDF untuk Python via C++ di lingkungan Anda sebelum menjalankan contoh kode berikut.\n1. Impor modul AsposePdfPython.\n2. Buat objek dokumen PDF baru menggunakan fungsi document_create.\n3. Dapatkan koleksi halaman dari dokumen menggunakan fungsi document_get_pages.\n4. Tambahkan halaman baru ke koleksi halaman menggunakan fungsi page_collection_add_page.\n5. Dapatkan koleksi paragraf dari halaman menggunakan fungsi page_get_paragraphs.\n6. Membuat objek gambar baru menggunakan fungsi image_create.\n7. Mengatur nama file dari objek gambar menjadi \"sample.jpg\" menggunakan fungsi image_set_file.\n8. Menambahkan objek gambar ke koleksi paragraf menggunakan fungsi paragraphs_add_image.\n9. Menyimpan dokumen ke file bernama \"document.pdf\" menggunakan fungsi document_save.\n10. Menutup pegangan dokumen menggunakan fungsi close_handle."
}
</script>


A simple use case can help to demonstrate the features of a programming language or software. This is usually done with a "Hello World" example.

Aspose.PDF for Python via C++ adalah API PDF yang kuat yang memungkinkan pengembang untuk membuat, memanipulasi, dan mengonversi dokumen PDF dalam aplikasi Python mereka. Ini mendukung bekerja dengan berbagai format file seperti PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX, dan format file gambar. Dalam artikel ini, kami akan menunjukkan kepada Anda cara membuat dokumen PDF dengan teks "Hello World!" menggunakan Aspose.PDF API. Anda perlu menginstal Aspose.PDF for Python via C++ di lingkungan Anda sebelum menjalankan contoh kode berikut.

1. Impor modul `AsposePdfPython`.
1. Buat objek dokumen PDF baru menggunakan fungsi `document_create`.
1. Dapatkan koleksi halaman dari dokumen menggunakan fungsi `document_get_pages`.
1. Tambahkan halaman baru ke koleksi halaman menggunakan fungsi `page_collection_add_page`.

1. Dapatkan koleksi paragraf dari halaman menggunakan fungsi `page_get_paragraphs`.
1. Membuat objek gambar baru menggunakan fungsi `image_create`.
1. Menetapkan nama file objek gambar menjadi "sample.jpg" menggunakan fungsi `image_set_file`.
1. Menambahkan objek gambar ke koleksi paragraf menggunakan fungsi `paragraphs_add_image`.
1. Menyimpan dokumen ke file bernama "document.pdf" menggunakan fungsi `document_save`.
1. Menutup handle dokumen menggunakan fungsi `close_handle`.

Kode berikut adalah program Hello World yang menunjukkan bagaimana Aspose.PDF untuk Python melalui C++ bekerja.

```python
from AsposePdfPython import *

doc = document_create()
pages = document_get_pages(doc)
page = page_collection_add_page(pages)
paragraphs = page_get_paragraphs(page)
image = image_create()
image_set_file(image,"sample.jpg")
paragraphs_add_image(paragraphs,image)

document_save(doc, "document.pdf")
close_handle(doc)
```