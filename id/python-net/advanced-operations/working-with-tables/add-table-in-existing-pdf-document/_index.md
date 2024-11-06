---
title: Membuat atau Menambahkan Tabel Dalam PDF menggunakan Python 
linktitle: Membuat atau Menambahkan Tabel
type: docs
weight: 10
url: id/python-net/add-table-in-existing-pdf-document/
description: Aspose.PDF untuk Python melalui .NET adalah perpustakaan yang digunakan untuk membuat, membaca, dan mengedit Tabel PDF. Periksa fungsi lanjutan lainnya dalam topik ini.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Membuat atau Menambahkan Tabel Dalam PDF menggunakan Python ",
    "alternativeHeadline": "Cara menambahkan Tabel Dalam PDF dengan Python melalui .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, buat tabel dalam pdf, tambahkan tabel",
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
    "url": "/python-net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF untuk Python melalui .NET adalah perpustakaan yang digunakan untuk membuat, membaca, dan mengedit Tabel PDF. Periksa fungsi lanjutan lainnya dalam topik ini."
}
</script>


## Membuat Tabel menggunakan Python

Tabel sangat penting saat bekerja dengan dokumen PDF. Mereka menyediakan fitur hebat untuk menampilkan informasi secara sistematis. Namespace Aspose.PDF berisi kelas bernama [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), [Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/), dan [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) yang menyediakan fungsionalitas untuk membuat tabel saat menghasilkan dokumen PDF dari awal.

Tabel dapat dibuat dengan membuat objek dari Kelas Table.

```python

    table = ap.Table()
```

### Menambahkan Tabel dalam Dokumen PDF yang Ada

Untuk menambahkan tabel ke file PDF yang ada dengan Aspose.PDF untuk Python via .NET, lakukan langkah-langkah berikut:

1. Muat file sumber.
1. Inisialisasi tabel dan atur kolom serta barisnya.
1. Atur pengaturan tabel (kami telah mengatur batas).
1. Isi tabel.
1. Tambahkan tabel ke halaman.
1. Simpan file.


Cuplikan kode berikut menunjukkan cara menambahkan teks dalam file PDF yang ada.

```python

    import aspose.pdf as ap

    # Memuat dokumen PDF sumber
    doc = ap.Document(input_file)
    # Menginisialisasi instance baru dari Table
    table = ap.Table()
    # Mengatur warna border tabel sebagai LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # Mengatur border untuk sel tabel
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # Membuat loop untuk menambahkan 10 baris
    for row_count in range(0, 10):
        # Menambahkan baris ke tabel
        row = table.rows.add()
        # Menambahkan sel tabel
        row.cells.add("Kolom (" + str(row_count) + ", 1)")
        row.cells.add("Kolom (" + str(row_count) + ", 2)")
        row.cells.add("Kolom (" + str(row_count) + ", 3)")
    # Menambahkan objek tabel ke halaman pertama dokumen input
    doc.pages[1].paragraphs.add(table)
    # Menyimpan dokumen yang diperbarui yang mengandung objek tabel
    doc.save(output_file)
```

### ColSpan dan RowSpan dalam Tabel

Aspose.PDF untuk Python via .NET menyediakan properti [col_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) untuk menggabungkan kolom dalam tabel dan properti [row_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) untuk menggabungkan baris.


Kami menggunakan properti `col_span` atau `row_span` pada objek `Cell` yang membuat sel tabel. Setelah menerapkan properti yang diperlukan, sel yang dibuat dapat ditambahkan ke tabel.

```python

    import aspose.pdf as ap

    # Inisialisasi objek Document dengan memanggil konstruktor kosongnya
    pdf_document = ap.Document()
    pdf_document.pages.add()
    # Menginisialisasi instance baru dari Table
    table = ap.Table()
    # Atur warna batas tabel sebagai LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Atur batas untuk sel tabel
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Tambahkan baris ke-1 ke tabel
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # Tambahkan sel tabel
        row1.cells.add("Test 1" + str(cellCount))

    # Tambahkan baris ke-2 ke tabel
    row2 = table.rows.add()
    row2.cells.add("Test 2 1")
    cell = row2.cells.add("Test 2 2")
    cell.col_span = 2
    row2.cells.add("Test 2 4")

    # Tambahkan baris ke-3 ke tabel
    row3 = table.rows.add()
    row3.cells.add("Test 3 1")
    row3.cells.add("Test 3 2")
    row3.cells.add("Test 3 3")
    row3.cells.add("Test 3 4")

    # Tambahkan baris ke-4 ke tabel
    row4 = table.rows.add()
    row4.cells.add("Test 4 1")
    cell = row4.cells.add("Test 4 2")
    cell.row_span = 2
    row4.cells.add("Test 4 3")
    row4.cells.add("Test 4 4")

    # Tambahkan baris ke-5 ke tabel
    row5 = table.rows.add()
    row5.cells.add("Test 5 1")
    row5.cells.add("Test 5 3")
    row5.cells.add("Test 5 4")

    # Tambahkan objek tabel ke halaman pertama dokumen input
    pdf_document.pages[1].paragraphs.add(table)
    # Simpan dokumen yang diperbarui berisi objek tabel
    pdf_document.save(output_file)
```


Hasil dari eksekusi kode di bawah ini adalah tabel yang digambarkan pada gambar berikut:

![Demo ColSpan dan RowSpan](colspan_rowspan.png)

## Bekerja dengan Batas, Margin, dan Padding

Harap dicatat bahwa ini juga mendukung fitur untuk mengatur gaya batas, margin, dan padding sel untuk tabel. Sebelum masuk ke detail teknis lebih lanjut, penting untuk memahami konsep batas, margin, dan padding yang disajikan di bawah ini dalam diagram:

![Batas, margin, dan padding](set-border-style-margins-and-padding-of-table_1.png)

Dalam gambar di atas, Anda dapat melihat bahwa batas dari tabel, baris, dan sel saling tumpang tindih. Dengan menggunakan Aspose.PDF, sebuah tabel dapat memiliki margin dan sel dapat memiliki padding. Untuk mengatur margin sel, kita harus mengatur padding sel.

### Batas

Untuk mengatur batas dari objek [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/), dan [Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/), gunakan properti Table.border, Row.border, dan Cell.border.
 Perbatasan sel juga dapat diatur menggunakan properti [default_cell_border](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) dari kelas [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) atau Row. Semua properti terkait perbatasan yang dibahas di atas diberikan sebagai instance dari kelas Row, yang dibuat dengan memanggil konstruktor. Kelas Row memiliki banyak overload yang mengambil hampir semua parameter yang diperlukan untuk menyesuaikan perbatasan.

### Margin atau Padding

Padding sel dapat dikelola menggunakan properti [default_cell_padding](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/#properties) dari kelas Table. Semua properti terkait padding diberikan sebagai instance dari kelas [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) yang mengambil informasi tentang parameter `left`, `right`, `top`, dan `bottom` untuk membuat margin khusus.
Pada contoh berikut, lebar batas sel diatur ke 0,1 poin, lebar batas tabel diatur ke 1 poin dan padding sel diatur ke 5 poin.

![Margin dan Border dalam Tabel PDF](margin-border.png)

```python

    import aspose.pdf as ap

    # Memperkenalkan objek Dokumen dengan memanggil konstruktor kosongnya
    doc = ap.Document()
    page = doc.pages.add()
    # Memperkenalkan objek tabel
    tab1 = ap.Table()
    # Menambahkan tabel dalam koleksi paragraf dari bagian yang diinginkan
    page.paragraphs.add(tab1)
    # Mengatur lebar kolom tabel
    tab1.column_widths = "50 50 50"
    # Mengatur batas sel default menggunakan objek BorderInfo
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Mengatur batas tabel menggunakan objek BorderInfo yang disesuaikan
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Membuat objek MarginInfo dan mengatur margin kiri, bawah, kanan, dan atas
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Mengatur padding sel default ke objek MarginInfo
    tab1.default_cell_padding = margin
    # Membuat baris dalam tabel dan kemudian sel dalam baris
    row1 = tab1.rows.add()
    row1.cells.add("kol1")
    row1.cells.add("kol2")
    row1.cells.add()
    my_text = ap.text.TextFragment("kol3 dengan string teks panjang")
    # Row1.Cells.Add("kol3 dengan string teks panjang untuk ditempatkan di dalam sel")
    row1.cells[2].paragraphs.add(my_text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Menyimpan Pdf
    doc.save(output_file)
```


Untuk membuat tabel dengan sudut melengkung, gunakan nilai [BorderInfo class](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) [rounded_border_radius](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/#properties) dan atur gaya sudut tabel ke bulat.

```python
    
    import aspose.pdf as ap
    
    tab1 = ap.Table()
    graph = ap.GraphInfo()
    graph.color = ap.Color.red
    # Buat objek BorderInfo kosong
    b_info = ap.BorderInfo(ap.BorderSide.ALL, graph)
    # Atur border menjadi border melengkung dengan radius lengkung 15
    b_info.rounded_border_radius = 15
    # Atur gaya Sudut tabel sebagai Bulat
    tab1.corner_style = ap.BorderCornerStyle.ROUND
    # Atur informasi border tabel
    tab1.border = b_info
```

## Menerapkan Pengaturan AutoFit Berbeda ke Tabel

Ketika merancang tabel menggunakan alat visual seperti Microsoft Word, Anda sering menggunakan salah satu fitur AutoFit untuk menyesuaikan ukuran tabel dengan lebar yang diinginkan dengan mudah.
 Sebagai contoh, Anda dapat menggunakan opsi "AUTO_FIT_TO_WINDOW" untuk menyesuaikan lebar tabel dengan halaman atau AUTO_FIT_TO_CONTENT. Secara default, ketika menggunakan Aspose.Pdf untuk membuat tabel baru, itu menggunakan [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) dengan nilai "Customized". Dalam cuplikan kode berikut, kami mengatur parameter objek [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) dan objek [BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) dalam tabel. Uji contoh dan evaluasi hasilnya.

```python

    import aspose.pdf as ap

    # Memprakarsai objek Pdf dengan memanggil konstruktor kosongnya
    doc = ap.Document()
    # Buat bagian dalam objek Pdf
    sec1 = doc.pages.add()
    # Memprakarsai objek tabel
    tab1 = ap.Table()
    # Tambahkan tabel dalam koleksi paragraf dari bagian yang diinginkan
    sec1.paragraphs.add(tab1)
    # Atur lebar kolom tabel
    tab1.column_widths = "50 50 50"
    tab1.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW
    # Atur batas sel default menggunakan objek BorderInfo
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Atur batas tabel menggunakan objek BorderInfo yang dikustomisasi lainnya
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Buat objek MarginInfo dan atur margin kiri, bawah, kanan, dan atasnya
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Atur padding sel default ke objek MarginInfo
    tab1.default_cell_padding = margin
    # Buat baris dalam tabel dan kemudian sel dalam baris
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Simpan dokumen yang diperbarui yang berisi objek tabel
    doc.save(output_file)
```

### Dapatkan Lebar Tabel

Terkadang, diperlukan untuk mendapatkan lebar tabel secara dinamis. Kelas Aspose.PDF.Table memiliki metode [get_width()](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#methods) untuk tujuan ini. Misalnya, Anda belum menetapkan lebar kolom tabel secara eksplisit dan menetapkan [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) ke 'AUTO_FIT_TO_CONTENT'. Dalam hal ini, Anda dapat mendapatkan lebar tabel sebagai berikut.

```python

    import aspose.pdf as ap

    # Buat dokumen baru
    doc = ap.Document()
    # Tambahkan halaman dalam dokumen
    page = doc.pages.add()
    # Inisialisasi tabel baru
    table = ap.Table()
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # Tambahkan baris dalam tabel
    row = table.rows.add()
    # Tambahkan sel dalam tabel
    cell = row.cells.add("Teks Sel 1")
    cell = row.cells.add("Teks Sel 2")
    # Dapatkan lebar tabel
    print(table.get_width())
```

## Tambahkan Gambar SVG ke Sel Tabel

Aspose.PDF untuk Python via .NET menyediakan kemampuan untuk memasukkan sel tabel ke dalam file PDF.
 Ketika membangun tabel, Anda dapat menyertakan teks dan gambar di dalam sel-sel ini. Selain itu, API menawarkan fungsi untuk mengubah file SVG ke dalam format PDF. Dengan memanfaatkan fungsi-fungsi ini secara bersamaan, Anda dapat memuat gambar SVG dan menempatkannya di dalam sel tabel.

Cuplikan kode berikut menunjukkan proses pembuatan objek tabel dan menyematkan gambar SVG di dalam salah satu selnya.

```python

    import aspose.pdf as ap

    # Membuat objek Dokumen
    doc = ap.Document()
    # Membuat instance gambar
    img = ap.Image()
    # Mengatur tipe gambar sebagai SVG
    img.file_type = ap.ImageFileType.SVG
    # Jalur untuk file sumber
    img.file = DIR_INPUT_TABLE + "SVGToPDF.svg"
    # Mengatur lebar untuk instance gambar
    img.fix_width = 50
    # Mengatur tinggi untuk instance gambar
    img.fix_height = 50
    # Membuat instance tabel
    table = ap.Table()
    # Mengatur lebar untuk sel tabel
    table.column_widths = "100 100"
    # Membuat objek baris dan menambahkannya ke instance tabel
    row = table.rows.add()
    # Membuat objek sel dan menambahkannya ke instance baris
    cell = row.cells.add()
    # Menambahkan textfragment ke koleksi paragraf dari objek sel
    cell.paragraphs.add(ap.text.TextFragment("Sel pertama"))
    # Menambahkan sel lain ke objek baris
    cell = row.cells.add()
    # Menambahkan gambar SVG ke koleksi paragraf dari instance sel yang baru saja ditambahkan
    cell.paragraphs.add(img)
    # Membuat objek halaman dan menambahkannya ke koleksi halaman dari instance dokumen
    page = doc.pages.add()
    # Menambahkan tabel ke koleksi paragraf dari objek halaman
    page.paragraphs.add(table)
    # Menyimpan file PDF
    doc.save(output_file)
```

## Sisipkan Pemisah Halaman antara baris tabel

Secara default, ketika Anda membuat tabel dalam file PDF, tabel tersebut akan meluas ke beberapa halaman jika melebihi batas bawah tabel. Namun, ada situasi di mana kita perlu memaksakan pemisah halaman setelah sejumlah baris tertentu telah ditambahkan ke tabel. Cuplikan kode berikut menguraikan proses penyisipan pemisah halaman ketika 10 baris telah dimasukkan ke dalam tabel.

```python

    import aspose.pdf as ap

    # Memperkenalkan instance Dokumen
    doc = ap.Document()
    # Tambahkan halaman ke koleksi halaman file PDF
    doc.pages.add()
    # Buat instance tabel
    tab = ap.Table()
    # Atur gaya batas untuk tabel
    tab.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # Atur gaya batas default untuk tabel dengan warna batas Merah
    tab.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # Tentukan lebar kolom tabel
    tab.column_widths = "100 100"
    # Buat loop untuk menambahkan 200 baris ke tabel
    for counter in range(0, 201):
        row = ap.Row()
        tab.rows.add(row)
        cell1 = ap.Cell()
        cell1.paragraphs.add(ap.text.TextFragment("Cell " + str(counter) + ", 0"))
        row.cells.add(cell1)
        cell2 = ap.Cell()
        cell2.paragraphs.add(ap.text.TextFragment("Cell " + str(counter) + ", 1"))
        row.cells.add(cell2)
        # Ketika 10 baris telah ditambahkan, render baris baru di halaman baru
        if counter % 10 == 0 and counter != 0:
            row.is_in_new_page = True
    # Tambahkan tabel ke koleksi paragraf file PDF
    doc.pages[1].paragraphs.add(tab)
    # Simpan dokumen PDF
    doc.save(output_file)
```


## Render a Table on a New Page

Secara default, paragraf ditambahkan ke koleksi Paragraf objek Halaman. Namun, adalah mungkin untuk merender tabel di halaman baru alih-alih langsung setelah objek tingkat paragraf yang sebelumnya ditambahkan pada halaman tersebut.

### Contoh: Cara Merender Tabel di Halaman Baru menggunakan Python

Untuk merender tabel di halaman baru, gunakan properti [is_in_new_page](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) dalam kelas [BaseParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf/baseparagraph/). Cuplikan kode berikut menunjukkan caranya.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    page_info = doc.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37

    page_info.is_landscape = True

    table = ap.Table()
    table.column_widths = "50 100"
    # Halaman ditambahkan.
    cur_page = doc.pages.add()
    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Konten 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("HHHHH"))
    paragraphs = cur_page.paragraphs
    paragraphs.add(table)

    table1 = ap.Table()
    table1.column_widths = "100 100"
    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("LAAAAAAA"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("LAAGGGGGG"))
    table1.is_in_new_page = True
    # Saya ingin menyimpan tabel 1 ke halaman berikutnya...
    paragraphs.add(table1)
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk Python via .NET",
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