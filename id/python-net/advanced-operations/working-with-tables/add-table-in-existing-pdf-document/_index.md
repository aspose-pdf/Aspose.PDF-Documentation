---
title: Menambahkan Tabel ke PDF menggunakan Python
linktitle: Menambahkan Tabel
type: docs
weight: 10
url: /id/python-net/adding-tables/
description: Aspose.PDF untuk Python via .NET adalah perpustakaan yang digunakan untuk membuat, membaca, dan mengedit Tabel PDF. Periksa fungsi lanjutan lainnya dalam topik ini.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Menambahkan Tabel ke PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan komprehensif untuk membuat dan memanipulasi tabel dalam dokumen PDF menggunakan pustaka Aspose.PDF untuk Python via .NET. Artikel ini merinci langkah‑langkah untuk menambahkan tabel ke file PDF yang sudah ada, termasuk mengatur batas tabel, margin, dan padding. Selanjutnya, artikel ini mengeksplorasi fungsionalitas lanjutan seperti menggabungkan kolom dan baris menggunakan `col_span` dan `row_span`, menerapkan berbagai pengaturan AutoFit, dan secara dinamis mengambil lebar tabel. Artikel ini juga mendemonstrasikan penyisipan gambar SVG ke dalam sel tabel serta memaksa pemisahan halaman atau merender tabel pada halaman baru. Potongan kode mengilustrasikan setiap fungsionalitas, menampilkan cara mengelola tata letak dan konten tabel secara efektif dalam dokumen PDF.
---

Menambahkan tabel ke dokumen PDF yang ada adalah kebutuhan umum untuk meningkatkan penyajian data, menyusun informasi, atau menghasilkan laporan. **Aspose.PDF untuk Python via .NET** menawarkan solusi komprehensif untuk tugas ini, memungkinkan pengembang menyisipkan tabel ke PDF yang ada secara mulus.

Panduan ini memberikan pendekatan langkah demi langkah untuk menambahkan tabel ke dokumen PDF yang ada menggunakan Aspose.PDF untuk Python via .NET. Panduan ini mencakup inisialisasi tabel, pengaturan lebar kolom, penentuan batas, pengisian baris dan sel, serta penyimpanan dokumen yang dimodifikasi. Selain itu, panduan ini mengeksplorasi fitur lanjutan, seperti penanganan batas sel, penerapan margin dan padding, serta penggunaan pengaturan AutoFit untuk secara dinamis menyesuaikan dimensi tabel.

Apakah Anda ingin meningkatkan daya tarik visual PDF Anda atau mengatur data dengan lebih efektif, panduan ini berfungsi sebagai sumber daya berharga untuk memanfaatkan kemampuan manipulasi tabel yang kuat dari Aspose.PDF untuk Python.

## Membuat Tabel Dasar

## Membuat Tabel

Contoh ini menunjukkan cara membuat Tabel dalam dokumen PDF dengan batas dan beberapa baris.

1. Buat dokumen PDF baru.
1. Menambahkan halaman kosong ke dokumen.
1. Inisialisasi Tabel.
1. Atur batas tabel secara keseluruhan.
1. Atur batas untuk setiap sel.
1. Tambahkan Baris dan Sel.
1. Sisipkan tabel ke dalam halaman.
1. Simpan PDF ke jalur yang ditentukan.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    for row_count in range(0, 10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")
    # Add table object to first page of input document
    page.paragraphs.add(table)

    # Save updated document containing table object
    document.save(path_outfile)
```

### Menambahkan Gambar ke Sel Tabel

Potongan kode ini menunjukkan cara menyisipkan gambar ke dalam sel Tabel dalam dokumen PDF.

1. Buat dokumen PDF baru.
1. Inisialisasi Tabel.
1. Atur lebar kolom dalam poin.
1. Fragmen teks ditambahkan ke sel pertama.
1. Instance 'ap.Image()' ditambahkan ke sel kedua.
1. Atur jalur ke file gambar dengan 'img.file'.
1. 'img.fix_width' dan 'img.fix_height' mengontrol ukuran gambar di dalam sel.
1. Sisipkan Tabel ke halaman PDF.
1. Simpan PDF.

```python

    import aspose.pdf as ap
    from os import path

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"

    # Create row object and add it to table instance
    row = table.rows.add()
    # Create cell object and add it to row instance
    cell = row.cells.add()
    # Add textfragment to paragraphs collection of cell object
    cell.paragraphs.add(ap.text.TextFragment(image))
    # Create an image instance
    img = ap.Image()
    # Set image type as SVG
    # Path for source file
    img.file = path.join(self.data_dir, image)
    # Set width for image instance
    img.fix_width = 50
    # Set height for image instance
    img.fix_height = 50
    # Add another cell to row object
    cell = row.cells.add()
    # Add SVG image to paragraphs collection of recently added cell instance
    cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(path_outfile)
```

Anda dapat menambahkan gambar SVG ke dalam sel tabel dalam dokumen PDF:

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"
    for image in images:
        # Create row object and add it to table instance
        row = table.rows.add()
        # Create cell object and add it to row instance
        cell = row.cells.add()
        # Add textfragment to paragraphs collection of cell object
        cell.paragraphs.add(ap.text.TextFragment(image))
        # Create an image instance
        img = ap.Image()
        # Set image type as SVG
        img.file_type = ap.ImageFileType.SVG
        # Path for source file
        img.file = path.join(self.data_dir, image)
        # Set width for image instance
        img.fix_width = 50
        # Set height for image instance
        img.fix_height = 50
        # Add another cell to row object
        cell = row.cells.add()
        # Add SVG image to paragraphs collection of recently added cell instance
        cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(path_outfile)
```

### ColSpan dan RowSpan dalam Tabel

Contoh ini menunjukkan cara menggabungkan sel tabel secara vertikal dan horizontal untuk membuat tata letak tabel yang kompleks.

1. Atur batas tabel secara keseluruhan.
1. Atur batas sel default.
1. Gabungkan dua sel secara horizontal menjadi satu.
1. Gabungkan sel secara vertikal melintasi dua baris.
1. Baris 5 memperhitungkan rowspan dengan melewatkan kolom yang digabung.
1. Sisipkan tabel ke dalam halaman.
1. Simpan PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.black
    )
    # Add 1st row to table
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # Add table cells
        row1.cells.add("Test 1" + str(cellCount))

    # Add 2nd row to table
    row2 = table.rows.add()
    row2.cells.add("Test 2 1")
    cell = row2.cells.add("Test 2 2")
    cell.col_span = 2
    row2.cells.add("Test 2 4")

    # Add 3rd row to table
    row3 = table.rows.add()
    row3.cells.add("Test 3 1")
    row3.cells.add("Test 3 2")
    row3.cells.add("Test 3 3")
    row3.cells.add("Test 3 4")

    # Add 4th row to table
    row4 = table.rows.add()
    row4.cells.add("Test 4 1")
    cell = row4.cells.add("Test 4 2")
    cell.row_span = 2
    row4.cells.add("Test 4 3")
    row4.cells.add("Test 4 4")

    # Add 5th row to table
    row5 = table.rows.add()
    row5.cells.add("Test 5 1")
    row5.cells.add("Test 5 3")
    row5.cells.add("Test 5 4")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

![Demo ColSpan dan RowSpan](colspan_rowspan.png)

### Menerapkan Batas pada Tabel dan Sel

Contoh ini menunjukkan cara mengatur padding sel, margin tabel, dan mengendalikan pembungkusan kata untuk teks dalam sel tabel.

1. Atur lebar kolom.
1. Tentukan batas tabel dan sel.
1. Atur padding di dalam sel untuk jarak yang konsisten.
1. Terapkan padding ke semua sel secara default.
1. Tambahkan Teks dan Mengontrol Pembungkusan.
1. Tambahkan Baris dan Sel.
1. Simpan PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)
    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    tab1 = ap.Table()
    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(tab1)
    # Set with column widths of the table
    tab1.column_widths = "50 50 50"
    # Set default cell border using BorderInfo object
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Set table border using another customized BorderInfo object
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Set the default cell padding to the MarginInfo object
    tab1.default_cell_padding = margin
    # Create rows in the table and then cells in the rows
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    text = ap.text.TextFragment("col3 with large text string")
    # Row1.Cells.Add("col3 with large text string to be placed inside cell")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Save updated document containing table object
    document.save(path_outfile)
```

![Margin dan Border dalam Tabel PDF](margin-border.png)

## Tata Letak dan Ukuran Tabel

### Penyesuaian otomatis kolom dan baris

Potongan kode ini menunjukkan cara secara otomatis menyesuaikan lebar kolom tabel agar sesuai dengan halaman.
Harap perhatikan bahwa pada parameter table.column_widths = "50 50 50" - itu dalam poin. Tetapi Anda juga dapat menentukan sentimeter (cm), inci, atau %.

1. Atur lebar kolom awal.
1. Secara otomatis menyesuaikan kolom agar sesuai dengan lebar halaman.
1. Tentukan batas sel dan tabel.
1. 'table.default_cell_padding' menggunakan 'MarginInfo()' untuk jarak yang konsisten di dalam sel.
1. Tambahkan Baris dengan 'table.rows.add()', dan tambahkan Sel dengan 'row.cells.add()'.
1. Simpan PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    page.paragraphs.add(table)

    table.column_widths = "50 50 50"
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW

    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5

    table.default_cell_padding = margin

    row1 = table.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = table.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")

    document.save(path_outfile)
```

### Menyesuaikan jarak di sekitar konten

Contoh ini menunjukkan cara membuat tabel yang melintasi beberapa halaman, menangani teks panjang dalam sel, dan menerapkan padding serta border.

1. Tambahkan tabel baru ke halaman menggunakan 'page.paragraphs.add(table)'.
1. Tentukan lebar kolom dengan 'table.column_widths'.
1. Atur border sel individu dengan 'table.default_cell_border'.
1. Atur border keseluruhan tabel dengan 'table.border'.
1. Tentukan padding default untuk sel menggunakan 'MarginInfo()'.
1. Tambahkan teks menggunakan 'TextFragment'.
1. Tambahkan baris lain.
1. Simpan PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object that will be nested inside outerTable that will break inside the same page
    table = ap.Table()
    # Add page
    page = document.pages.add()

    # Instantiate a table object
    table = ap.Table()

    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(table)

    # Set column widths of the table
    table.column_widths = "50 50 50"

    # Set default cell border using BorderInfo object
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

    # Set table border using another customized BorderInfo object
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5

    # Set the default cell padding to the MarginInfo object
    table.default_cell_padding = margin

    # Create rows and cells
    row1 = table.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()

    # Add a long text fragment into the third cell
    text = ap.text.TextFragment("col3 with large text string")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False

    # Add another row
    row2 = table.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")

    # Save PDF document
    document.save(path_outfile)
```

![Border, margin, dan padding](set-border-style-margins-and-padding-of-table_1.png)

### Menata Sudut Tabel

Aspose.PDF for Python via .NET menunjukkan cara menerapkan sudut melengkung pada tabel dan menyesuaikan radius border.

1. Buat instance tabel baru.
1. Inisialisasi border untuk semua sisi.
1. Atur radius sudut.
1. Terapkan gaya sudut melengkung.
1. Tambahkan Baris dan Sel.
1. Sisipkan tabel ke halaman PDF dengan 'page.paragraphs.add(table)'.
1. Simpan dokumen PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()

    # Create a table
    table = ap.Table()

    # Create a blank BorderInfo object
    b_info = ap.BorderInfo(ap.BorderSide.ALL)

    # Set the border a rounded border where radius of round is 15
    b_info.rounded_border_radius = 15

    # Set the table corner style as Round
    table.corner_style = ap.BorderCornerStyle.ROUND

    # Set the table border information
    table.border = b_info

    # Create a loop to add 10 rows
    for row_count in range(0, 10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

## Menambahkan Konten ke Tabel

### Menggunakan Fragmen HTML dalam Sel

Contoh ini menunjukkan cara menyisipkan konten berformat HTML ke dalam sel tabel.

1. Tentukan border tabel dan sel.
1. Tambahkan konten HTML.
1. Tambahkan Baris. Sebuah loop menambahkan beberapa baris dengan konten berformat HTML di setiap sel.
1. Sisipkan tabel ke halaman PDF dengan 'page.paragraphs.add(table)'.
1. Simpan dokumen PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(f"Column <strong>({row_count}, 1)</strong>")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(
                f"Column <span style='color:red'>({row_count}, 2)</span>"
            )
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(
                f"Column <span style='text-decoration: underline'>({row_count}, 3)</span>"
            )
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

### Menggunakan Fragmen LaTeX dalam Sel

Contoh ini menunjukkan cara menyisipkan konten berformat LaTeX ke dalam sel tabel untuk ekspresi matematis atau bergaya.

1. Tentukan border tabel dan sel.
1. Tambahkan Konten LaTeX.
1. Tambahkan Baris. Sebuah loop menambahkan beberapa baris dengan konten berformat LaTeX di setiap sel.
1. Sisipkan tabel ke dalam halaman PDF dengan 'page.paragraphs.add(table)'.
1. Simpan dokumen PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(f"Column $\\mathbf{{({row_count}, 1)}}$")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(
                f"Column $\\textcolor{{red}}{{({row_count}, 2)}}$"
            )
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(
                f"Column $\\underline{{({row_count}, 3)}}$"
            )
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

## Fitur Tabel Lanjutan

### Menyisipkan Tabel di Seluruh Halaman

Contoh ini menunjukkan cara membuat beberapa tabel dalam PDF, mengatur margin halaman, dan memaksa tabel mulai pada halaman baru.

1. Atur margin halaman menggunakan 'page_info.margin'.
1. Atur orientasi halaman ke lanskap dengan 'page_info.is_landscape'.
1. Tabel Pertama:
- definisikan dua kolom dengan lebar yang ditentukan.
- tambahkan Baris dalam loop dengan 'row.fixed_row_height'.
- isi Sel dengan fragmen teks.
1. Tabel Kedua:
- buat tabel baru dengan 'table1.column_widths'.
- paksa tabel untuk memulai pada halaman baru.
1. Tambahkan tabel pertama.
1. Tambahkan tabel kedua pada halaman baru.
1. Simpan Dokumen

```python

    import aspose.pdf as ap
    from os import path

    # The path to the documents directory
    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()

    # Set page and margin information
    page_info = document.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37
    page_info.is_landscape = True

    # First table with 120 rows
    table = ap.Table()
    table.column_widths = "50 100"

    cur_page = document.pages.add()

    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("Content 2"))

    cur_page.paragraphs.add(table)

    # Second table with 10 rows
    table1 = ap.Table()
    table1.column_widths = "100 100"

    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 3"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("Content 4"))

    table1.is_in_new_page = True  # Force table to new page
    cur_page.paragraphs.add(table1)

    # Save updated document containing table object
    document.save(path_outfile)
```

### Membuat Tabel Tanpa Garis

Contoh ini menunjukkan cara membuat tabel besar yang dapat terputus secara vertikal antar halaman, mengulang kolom, dan menerapkan warna latar belakang berbeda pada sel header.

1. Inisialisasi Tabel.
1. Atur batas default untuk semua sel.
1. Sel header menggunakan 'col_span' untuk menggabungkan beberapa kolom.
1. Atur latar belakang sel untuk membedakan visual dengan 'background_color set'
1. Tambahkan Baris.
1. Sisipkan tabel ke dalam halaman PDF dengan 'page.paragraphs.add(table)'.
1. Simpan dokumen PDF.

```python

    import aspose.pdf as ap
    from os import path

    # The path to the documents directory
    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)
    table.repeating_columns_count = 2
    page.paragraphs.add(table)

    # Add header Row
    row = table.rows.add()
    cell = row.cells.add("header 1")
    cell.col_span = 2
    cell.background_color = ap.Color.light_gray
    row.cells.add("header 3")

    cell2 = row.cells.add("header 4")
    cell2.col_span = 2
    cell2.background_color = ap.Color.light_blue
    row.cells.add("header 6")

    cell3 = row.cells.add("header 7")
    cell3.col_span = 2
    cell3.background_color = ap.Color.light_green
    cell4 = row.cells.add("header 9")

    cell4.col_span = 3
    cell4.background_color = ap.Color.light_coral
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")

    row_counter = 0
    while row_counter < 3:
        # Create rows in the table and then cells in the rows
        row1 = table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 8")
        row1.cells.add("col " + str(row_counter) + ", 9")
        row1.cells.add("col " + str(row_counter) + ", 10")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
        row_counter += 1

    document.save(path_outfile)
```

### Mengulang Baris Header pada Banyak Halaman

Contoh ini menunjukkan cara membuat tabel yang meluas ke beberapa halaman sambil menjaga baris header tetap terlihat di setiap halaman.

1. Inisialisasi Tabel.
1. Ulangi Baris Header termasuk font, ukuran, dan warna.
1. Atur Lebar Kolom dan terapkan Garis pada tabel.
1. Tambahkan baris Header.
1. Tambahkan banyak baris data untuk memaksa tabel melintasi beberapa halaman.
1. Sisipkan tabel ke dalam halaman PDF dengan 'page.paragraphs.add(table)'.
1. Simpan dokumen PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object
    table = ap.Table()

    # Set the table to break across pages
    table.broken = ap.TableBroken.VERTICAL

    # Set number of repeating header rows
    table.repeating_rows_count = 2

    text_state = ap.text.TextState()
    text_state.font_size = 12
    text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_state.foreground_color = ap.Color.red
    table.repeating_rows_style =  text_state

    # Set column widths
    table.column_widths = "100 100 100"

    # Set borders
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.black)

    # Add header rows that will repeat on each page
    header_row1 = table.rows.add()
    header_row1.cells.add("Header 1-1")
    header_row1.cells.add("Header 1-2")
    header_row1.cells.add("Header 1-3")

    # Set background color for header rows
    for cell in header_row1.cells:
        cell.background_color = ap.Color.light_gray

    header_row2 = table.rows.add()
    header_row2.cells.add("Header 2-1")
    header_row2.cells.add("Header 2-2")
    header_row2.cells.add("Header 2-3")

    for cell in header_row2.cells:
        cell.background_color = ap.Color.light_blue

    # Add many data rows to force table across multiple pages
    for i in range(1, 101):
        row = table.rows.add()
        row.cells.add(f"Data {i}-1")
        row.cells.add(f"Data {i}-2")
        row.cells.add(f"Data {i}-3")

    # Add table to page
    page.paragraphs.add(table)

    # Save document
    document.save(path_outfile)
```

### Mengulang Kolom

Fungsi 'add_repeating_columns' membuat dokumen PDF dengan tabel yang memiliki kolom berulang. Ini menyiapkan tabel dengan batas, menambahkan header, mengisi baris data, dan menyimpan file PDF yang dihasilkan ke lokasi yang ditentukan. Mengatur properti ini akan menyebabkan tabel terputus ke halaman berikutnya secara kolom dan mengulang jumlah kolom yang diberikan di awal halaman berikutnya.

1. Inisialisasi dokumen PDF baru.
1. Tambahkan halaman dengan dimensi khusus.
1. Atur Gaya Garis Tabel.
1. Inisialisasi Tabel.
1. Tambahkan tabel ke halaman PDF.
1. Tambahkan baris header.
1. Tambahkan baris data.
1. Simpan Dokumen PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()
    page.set_page_size(ap.PageSize.A5.height, ap.PageSize.A5.width)

    # Define border
    border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)

    # Create table
    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    table.repeating_columns_count = 5
    table.border = border
    table.default_cell_border = border

    # Add table to page
    page.paragraphs.add(table)

    # Add header row
    row = table.rows.add()
    for i in range(1, 6):
        cell = row.cells.add(f"header {i}")
        cell.background_color = ap.Color.light_gray

    for i in range(6, 18):
        row.cells.add(f"header {i}")

    # Add data rows
    for row_counter in range(1, 6):
        row = table.rows.add()
        for i in range(1, 6):
            cell = row.cells.add(f"cell {row_counter},{i}")
            cell.background_color = ap.Color.light_gray
        for i in range(6, 18):
            row.cells.add(f"cell {row_counter},{i}")

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```
