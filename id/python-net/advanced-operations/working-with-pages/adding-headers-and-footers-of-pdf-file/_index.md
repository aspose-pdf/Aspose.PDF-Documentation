---
title: Tambah Header dan Footer PDF dalam Python
linktitle: Menambahkan Header dan Footer ke PDF
type: docs
weight: 50
url: /id/python-net/add-headers-and-footers-of-pdf-file/
description: Pelajari cara menambahkan header dan footer ke file PDF menggunakan Python dengan teks, gambar, dan konten terstruktur.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan header dan footer ke file PDF dengan Python
Abstract: Artikel ini menunjukkan cara menambahkan header dan footer ke dokumen PDF dengan Aspose.PDF for Python via .NET. Ini mencakup teks, penomoran halaman, HTML, gambar, tabel, dan konten header serta footer berbasis LaTeX.
---

Gunakan halaman ini untuk menambahkan konten header dan footer yang konsisten di seluruh halaman PDF dengan **Aspose.PDF for Python via .NET**.

Anda dapat membuat header dan footer dengan [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), dan [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) objek, lalu terapkan mereka melalui [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) pada setiap halaman.

## Menambahkan Header dan Footer sebagai Fragmen Teks

Tambahkan header dan footer teks sederhana ke semua halaman dalam PDF. Itu membuat [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objek, sisipan [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) elemen ke dalamnya, set [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) untuk penempatan yang tepat, dan menempelkannya ke setiap halaman dalam dokumen. Hasilnya adalah PDF di mana setiap halaman menampilkan teks header dan footer yang konsisten.

Potongan kode berikut menunjukkan cara menambahkan header dan footer sebagai fragmen teks dalam PDF menggunakan Python:

1. Buat fragmen teks untuk header dan footer.
1. Buat objek HeaderFooter dan tambahkan fragmen teks ke dalamnya.
1. Tentukan pengaturan margin untuk mengontrol penempatan header dan footer.
1. Muat dokumen PDF dari file input.
1. Iterasi melalui semua halaman dalam dokumen.
1. Tetapkan header dan footer pada setiap halaman.
1. Simpan PDF yang dimodifikasi ke file output.

```python
import aspose.pdf as ap

def add_header_and_footer_as_text(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Metode ini berguna untuk menambahkan judul yang konsisten, indikator halaman, atau penafian hukum di bagian atas dan bawah setiap halaman. Anda juga dapat memperluasnya untuk menyertakan gambar atau konten dinamis, seperti nomor halaman.

## Menambahkan Header dan Footer untuk Penomoran Halaman

Tambahkan penomoran halaman otomatis ke header dan footer dokumen PDF menggunakan Aspose.PDF for Python. Menggunakan variabel bawaan $p (nomor halaman saat ini) dan $P (total jumlah halaman), skrip secara dinamis menyisipkan penomoran halaman pada setiap halaman. Header menampilkan format 'Page X from Y', sementara footer menampilkan 'Page X / Y'. The [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) memastikan penempatan yang tepat pada setiap halaman.

1. Buat TextFragment untuk header menggunakan "Page $p dari $P" untuk menampilkan halaman saat ini dan total halaman.
1. Buat objek HeaderFooter dan tambahkan teks header ke dalamnya.
1. Buat sebuah TextFragment untuk footer menggunakan "Page $p / $P" untuk gaya penomoran alternatif.
1. Buat objek Footer dan tambahkan teks footer.
1. Tentukan pengaturan margin (kiri = 50, atas = 20) dan terapkan pada header dan footer.
1. Buka dokumen PDF dari file input.
1. Loop melalui semua halaman dan tetapkan header serta footer ke setiap halaman.
1. Simpan PDF yang diperbarui ke jalur output.

```python
import aspose.pdf as ap

def using_header_and_footer_for_page_numbering(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Menambahkan Header dan Footer sebagai Fragmen HTML

Terapkan header dan footer berformat HTML ke setiap halaman dokumen PDF menggunakan Aspose.PDF for Python. Dengan menggunakan [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), skrip memungkinkan pemformatan teks kaya—seperti tebal dan miring—untuk muncul di header dan footer. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) diterapkan untuk penempatan yang tepat, dan elemen yang diformat sama dilampirkan ke setiap halaman dalam dokumen.

Potongan kode berikut menunjukkan cara menambahkan header dan footer sebagai fragmen HTML ke PDF menggunakan Python:

1. Buat potongan header HTML menggunakan HtmlFragment—termasuk teks bergaya seperti '<strong>' untuk tebal.
1. Buat objek HeaderFooter dan tambahkan header HTML ke dalamnya.
1. Buat potongan footer HTML menggunakan '<i>' untuk penataan miring.
1. Buat objek Footer dan tambahkan HTML footer ke dalamnya.
1. Konfigurasikan margin (kiri = 50, atas = 20) dan tetapkan ke header dan footer.
1. Muat dokumen PDF menggunakan 'ap.Document()'.
1. Lakukan loop pada semua halaman dan tetapkan header serta footer untuk masing-masing.
1. Simpan PDF yang dimodifikasi ke jalur output yang ditentukan.

```python
import aspose.pdf as ap

def add_header_and_footer_as_html(input_file, output_file):
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Menggunakan HtmlFragment memungkinkan pemformatan kaya dengan gaya inline atau markup HTML, memberi Anda lebih banyak fleksibilitas desain dibandingkan teks biasa.

## Menambahkan Header dan Footer sebagai Gambar

Tambahkan header dan footer berbasis gambar ke setiap halaman dokumen PDF menggunakan Aspose.PDF for Python. File gambar yang sama digunakan untuk header dan footer pada setiap halaman. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) menempatkan gambar, dan gambar secara otomatis menyesuaikan untuk muat dalam area header/footer.

Potongan kode berikut menunjukkan cara menambahkan header dan footer sebagai gambar ke PDF menggunakan Python:

1. Muat gambar ke dalam objek 'ap.Image' dan siapkan untuk digunakan sebagai header.
1. Buat objek HeaderFooter dan lampirkan gambar header ke dalamnya.
1. Muat gambar yang sama lagi untuk digunakan sebagai footer.
1. Buat objek Footer dan tambahkan gambar footer ke dalamnya.
1. Muat dokumen PDF input menggunakan 'ap.Document()'.
1. Iterasikan semua halaman dokumen.
1. Terapkan margin (kiri = 50) untuk menempatkan header dan footer.
1. Tetapkan header dan footer ke setiap halaman dalam PDF.
1. Simpan PDF yang diperbarui ke file output yang ditentukan.

Teknik ini ideal untuk menambahkan merek pada dokumen dengan logo atau watermark di area header/footer.

```python
import aspose.pdf as ap

def add_header_and_footer_as_image(input_file, image_file, output_file):
    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Menambahkan Header dan Footer sebagai Tabel

Tambahkan header dan footer berbasis tabel yang terstruktur ke semua halaman dokumen PDF menggunakan Aspose.PDF untuk Python. [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) objek memberikan kontrol tata letak yang lebih baik, penyelarasan, dan pemformatan konsisten untuk header dan footer yang kompleks. Teks header dipusatkan sementara teks footer disejajarkan ke kiri, keduanya menggunakan font Arial 12pt. Lebar kolom dihitung secara dinamis berdasarkan dimensi halaman untuk memastikan penempatan yang tepat.

Potongan kode ini menambahkan header dan footer (menggunakan tabel) ke setiap halaman dokumen PDF dengan Aspose.PDF for Python via .NET.

1. Definisikan gaya teks menggunakan [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) untuk header dan footer (font, ukuran, perataan).
1. Buat [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objek untuk header dan footer.
1. Buat header [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) dengan satu baris dan sebuah sel yang berisi teks header.
1. Buat footer [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) dengan satu baris dan sel yang berisi teks footer.
1. Tambahkan tabel ke yang sesuai [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objek.
1. Setel footer [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) untuk penempatan horizontal yang tepat.
1. Buka [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan metode yang tepat.
1. Iterasikan semua halaman dan tetapkan header serta footer berbasis tabel pada setiap halaman.
1. Simpan yang dimodifikasi [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ke file output.

```python
import aspose.pdf as ap

def add_header_and_footer_as_table(input_file, output_file):
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Menambahkan Header dan Footer sebagai LaTeX

Tambahkan header dan footer yang berisi konten berformat LaTeX ke semua halaman dokumen PDF menggunakan Aspose.PDF for Python. LaTeX memungkinkan rendering simbol matematika, tanggal, tanda hak cipta, dan format lanjutan lainnya. Header mencakup tanggal dinamis, sementara footer menampilkan simbol hak cipta bersama dengan nomor halaman saat ini dan total jumlah halaman.

Potongan kode berikut menunjukkan cara menggunakan [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) di header dan footer untuk PDF menggunakan Aspose.PDF for Python via .NET.

1. Buka [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menggunakan metode yang tepat.
1. Tentukan total jumlah halaman untuk digunakan dalam footer dinamis.
1. Iterasikan semua halaman dokumen.
1. Buat sebuah [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objek untuk header.
1. Buat sebuah [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) untuk teks header yang berisi perintah LaTeX (mis., `\\today\\`).
1. Buat sebuah [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objek untuk footer.
1. Buat sebuah [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) untuk teks footer termasuk simbol LaTeX dan penomoran halaman.
1. Tambahkan [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) ke objek header/footer yang sesuai.
1. Mengikat header dan footer ke halaman saat ini.
1. Simpan yang dimodifikasi [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) ke file output.

```python
import aspose.pdf as ap

def add_header_and_footer_as_latex(input_file, output_file):
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTeX Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = (
                f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            )
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Topik Halaman Terkait

- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
- [Tambahkan nomor halaman ke PDF di Python](/pdf/id/python-net/add-page-number/)
- [Stempel halaman PDF menggunakan Python](/pdf/id/python-net/stamping/)
- [Format dokumen PDF dalam Python](/pdf/id/python-net/formatting-pdf-document/)