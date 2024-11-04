---
title: Membuat PDF yang kompleks
linktitle: Membuat PDF yang kompleks
type: docs
weight: 30
url: /python-net/complex-pdf-example/
description: Aspose.PDF untuk Python via .NET memungkinkan Anda membuat dokumen yang lebih kompleks yang mengandung gambar, fragmen teks, dan tabel dalam satu dokumen.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Contoh [Hello, World](/pdf/python-net/hello-world-example/) menunjukkan langkah-langkah sederhana untuk membuat dokumen PDF menggunakan Python dan Aspose.PDF. Dalam artikel ini, kita akan melihat pembuatan dokumen yang lebih kompleks dengan Aspose.PDF untuk Python. Sebagai contoh, kita akan mengambil dokumen dari perusahaan fiktif yang mengoperasikan layanan feri penumpang. Dokumen kita akan mengandung gambar, dua fragmen teks (header dan paragraf), dan sebuah tabel.

Jika kita membuat dokumen dari awal, kita perlu mengikuti langkah-langkah tertentu:

1. Buat objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Pada langkah ini kita akan membuat dokumen PDF kosong dengan beberapa metadata tetapi tanpa halaman.
1. Tambahkan [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ke objek dokumen. Jadi, sekarang dokumen kita akan memiliki satu halaman.
1. Tambahkan [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) ke Halaman.
1. Buat [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) untuk header. Untuk header kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Tambahkan header ke [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) halaman.
1. Buat [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) untuk deskripsi. Untuk deskripsi kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Tambahkan (deskripsi) ke Paragraf halaman.
1. Buat tabel, tambahkan properti tabel.

1. Tambahkan (tabel) ke halaman [paragraf](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Simpan dokumen "Complex.pdf".

```python

    import aspose.pdf as ap

    # Inisialisasi objek dokumen
    document = ap.Document()
    # Tambahkan halaman
    page = document.pages.add()

    # Tambahkan gambar
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    # Tambahkan Header
    header = ap.text.TextFragment("Rute feri baru di Musim Gugur 2020")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Tambahkan deskripsi
    descriptionText = "Pengunjung harus membeli tiket secara online dan tiket dibatasi hingga 5.000 per hari. \
    Layanan feri beroperasi pada setengah kapasitas dan dengan jadwal yang dikurangi. Harap antre."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Tambahkan tabel
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Berangkat Kota")
    headerRow.cells.add("Berangkat Pulau")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = ap.Color.white_smoke
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

    document.save(output_pdf)
```