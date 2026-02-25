---
title: Bekerja dengan Latar Belakang sebagai Artefak dengan Python
linktitle: Menambahkan latar belakang
type: docs
weight: 20
url: /id/python-net/add-backgrounds/
description: Tambahkan gambar latar belakang ke file PDF Anda dengan Python. Gunakan kelas BackgroundArtifact.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan latar belakang ke PDF dengan Python
Abstract: Artikel ini membahas penggunaan gambar latar belakang dalam dokumen PDF menggunakan Aspose.PDF untuk Python via .NET. Artikel ini menyoroti kemampuan menambahkan watermark atau desain halus ke dokumen dengan memanfaatkan kelas `BackgroundArtifact`, yang memungkinkan penyisipan gambar latar belakang ke dalam objek halaman individu. Artikel ini menyediakan contoh kode praktis yang menunjukkan cara mengimplementasikan fitur ini. Prosesnya melibatkan pembuatan dokumen PDF baru, menambahkan halaman, membuat objek `BackgroundArtifact`, mengatur gambar latar belakang, dan menambahkan artefak latar belakang ke koleksi artefak halaman. Akhirnya, dokumen yang dimodifikasi disimpan sebagai file PDF. Teknik ini memungkinkan presentasi visual dokumen PDF yang lebih baik.
---

Gambar latar belakang dapat digunakan untuk menambahkan watermark, atau desain halus lainnya, ke dokumen. Dalam Aspose.PDF untuk Python via .NET, setiap dokumen PDF adalah kumpulan halaman dan setiap halaman berisi kumpulan artefak. Kelas [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) dapat digunakan untuk menambahkan gambar latar belakang ke objek halaman.

Potongan kode berikut menunjukkan cara menambahkan gambar latar belakang ke halaman PDF menggunakan objek BackgroundArtifact dengan Python.

```python

import aspose.pdf as ap
import io

def add_background_image(input_image_file, output_pdf):
    # Create a new PDF document
    document = ap.Document()

    # Add a blank page to the document
    page = document.pages.add()

    # Create a BackgroundArtifact object
    background = ap.BackgroundArtifact()

    # Load the image as a binary stream
    with open(input_image_file, "rb") as image_stream:
        background.background_image = image_stream

        # Add the background artifact to the page
        page.artifacts.append(background)

    # Save the resulting PDF
    document.save(output_pdf)
```


