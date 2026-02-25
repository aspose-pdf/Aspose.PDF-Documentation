---
title: Cara Membuat PDF menggunakan Python
linktitle: Buat Dokumen PDF
type: docs
weight: 10
url: /id/python-net/create-pdf-document/
description: Buat dan format Dokumen PDF dengan Aspose.PDF untuk Python via .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat File PDF dengan Python
Abstract: Aspose.PDF untuk Python via .NET adalah API serbaguna yang dirancang untuk pengembang dalam memanipulasi file PDF pada aplikasi Python yang menargetkan kerangka kerja .NET. API ini memungkinkan pengguna untuk membuat, memuat, memodifikasi, dan mengonversi dokumen PDF dengan mudah. Artikel ini memberikan panduan langkah demi langkah untuk membuat file PDF sederhana menggunakan Aspose.PDF. Prosesnya melibatkan inisialisasi objek `Document`, menambahkan `Page` ke dokumen, menyisipkan `TextFragment` ke paragraf halaman, dan menyimpan file sebagai PDF. Potongan kode Python yang disertakan menunjukkan langkah-langkah tersebut dengan membuat dokumen PDF yang berisi teks "Hello World!". API ini menyederhanakan penanganan PDF dengan kode minimal, meningkatkan produktivitas bagi pengembang yang bekerja dengan PDF di lingkungan .NET.
---

**Aspose.PDF for Python via .NET** adalah API manipulasi PDF yang memungkinkan pengembang untuk membuat, memuat, memodifikasi, dan mengonversi file PDF secara langsung dari Python untuk aplikasi .NET dengan hanya beberapa baris kode.

## Cara Membuat File PDF Sederhana

Untuk membuat PDF menggunakan Python via .NET dengan Aspose.PDF, Anda dapat mengikuti langkah-langkah berikut:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Tambahkan objek [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ke koleksi [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) dari objek Document
1. Tambahkan [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) ke koleksi [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) dari halaman
1. Simpan dokumen PDF yang dihasilkan

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # Save updated PDF
    document.save(output_pdf)
```


