---
title: Membuat PDF yang kompleks
linktitle: Membuat PDF yang kompleks
type: docs
weight: 30
url: /id/python-net/complex-pdf-example/
description: Aspose.PDF for Python via .NET memungkinkan Anda membuat dokumen yang lebih kompleks yang berisi gambar, text fragments, dan tabel dalam satu dokumen.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat PDF yang kompleks menggunakan Python
Abstract: Artikel ini memperluas proses pembuatan PDF dasar yang ditunjukkan dalam contoh "Hello, World" dengan menggambarkan cara membuat dokumen PDF yang lebih kompleks menggunakan Python dan Aspose.PDF. Dokumen contoh dikembangkan untuk sebuah perusahaan layanan feri penumpang fiktif dan mencakup sebuah gambar, dua text fragments (sebuah header dan sebuah paragraf), serta sebuah tabel. Prosesnya melibatkan beberapa langkah - menginstansiasi objek `Document` untuk membuat PDF kosong, menambahkan `Page`, dan kemudian menyisipkan `Image` ke dalam halaman. Sebuah `TextFragment` dibuat untuk header menggunakan font Arial dengan ukuran 24pt dan perataan tengah, yang kemudian ditambahkan ke paragraf halaman. `TextFragment` kedua ditambahkan untuk deskripsi, menggunakan font Times New Roman dengan ukuran 14pt dan perataan kiri. Selanjutnya, sebuah tabel dibuat dan diformat dengan lebar kolom, batas, dan padding khusus. Tabel tersebut mencakup baris header dengan sel yang disorot dan beberapa baris data yang dihasilkan melalui iterasi
---

The [Hello, World](/pdf/id/python-net/hello-world-example/) contoh menunjukkan langkah sederhana untuk membuat dokumen PDF menggunakan Python dan Aspose.PDF. Dalam artikel ini, kami akan melihat pembuatan dokumen yang lebih kompleks dengan Aspose.PDF for Python. Sebagai contoh, kami akan mengambil dokumen dari perusahaan fiktif yang mengoperasikan layanan feri penumpang. Dokumen kami akan berisi sebuah gambar, dua fragmen teks (judul dan paragraf), dan sebuah tabel.

Jika kita membuat dokumen dari awal, kita perlu mengikuti langkah-langkah tertentu:

1. Instansiasi sebuah [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek. Pada langkah ini kami akan membuat dokumen PDF kosong dengan beberapa metadata tetapi tanpa halaman.
1. Tambahkan sebuah [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ke objek dokumen. Jadi, sekarang dokumen kami akan memiliki satu halaman.
1. Tambahkan sebuah [Gambar](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) ke Halaman.
1. Buat sebuah [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) untuk header. Untuk header kami akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Tambahkan header ke halaman [paragraf](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Buat sebuah [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) untuk deskripsi. Untuk deskripsi kami akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Tambahkan deskripsi ke paragraf halaman.
1. Buat dan Gaya Tabel. Atur lebar kolom, batas, padding, dan font.
1. Tambahkan tabel ke halaman [paragraf](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Simpan dokumen "Complex.pdf".

```python
from datetime import timedelta
import aspose.pdf as ap


def run_complex(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    imageFileName = self.data_dir + "logo.png"
    page.add_image(imageFileName, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[
            i
        ].default_cell_text_state.foreground_color = ap.Color.white_smoke
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(self.data_dir + "Complex.pdf")
```
