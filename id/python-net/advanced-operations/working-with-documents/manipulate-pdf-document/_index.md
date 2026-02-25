---
title: Manipulasi Dokumen PDF dengan Python via .NET
linktitle: Manipulasi Dokumen PDF
type: docs
weight: 20
url: /id/python-net/manipulate-pdf-document/
description: Artikel ini berisi informasi tentang cara memvalidasi Dokumen PDF untuk Standar PDF A menggunakan Python, cara bekerja dengan TOC, cara mengatur tanggal kedaluwarsa PDF, dan lain-lain.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Panduan tentang memanipulasi dokumen PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang memanipulasi dokumen PDF menggunakan Python, khususnya dengan pustaka Aspose.PDF. Artikel ini mencakup berbagai fungsionalitas, termasuk memvalidasi dokumen PDF untuk kepatuhan PDF/A-1a dan PDF/A-1b menggunakan metode `validate` dari kelas `Document`. Artikel ini juga menjelaskan cara menambahkan, menyesuaikan, dan mengelola Table of Contents (TOC) dalam file PDF, seperti mengatur berbagai TabLeaderTypes, menyembunyikan nomor halaman, dan menyesuaikan penomoran halaman dengan awalan. Selain itu, artikel ini menjelaskan cara mengatur tanggal kedaluwarsa untuk dokumen PDF dengan menyematkan JavaScript untuk pembatasan akses dan cara meratakan formulir yang dapat diisi dalam PDF sehingga tidak dapat diedit. Setiap bagian dilengkapi dengan potongan kode yang menunjukkan penerapan fitur-fitur ini menggunakan Aspose.PDF di Python.
---

## Manipulasi Dokumen PDF dengan Python

## Validasi Dokumen PDF untuk Standar PDF A (A 1A dan A 1B)

Untuk memvalidasi dokumen PDF untuk kompatibilitas PDF/A-1a atau PDF/A-1b, gunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) metode [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). Metode ini memungkinkan Anda menentukan nama file dimana hasil akan disimpan dan tipe validasi yang diperlukan dari enumerasi PdfFormat: PDF_A_1A atau PDF_A_1B.

Potongan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1A.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

Potongan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1b.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```

## Bekerja dengan TOC

### Tambahkan TOC ke PDF yang Ada

TOC dalam PDF merupakan singkatan dari "Table of Contents." Ini adalah fitur yang memungkinkan pengguna untuk dengan cepat menavigasi dokumen dengan memberikan gambaran tentang bagian-bagian dan judul-judulnya.

Untuk menambahkan TOC ke file PDF yang ada, gunakan kelas Heading di namespace [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/). Namespace [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) dapat membuat file PDF baru maupun memanipulasi file PDF yang ada. Untuk menambahkan TOC ke PDF yang ada, gunakan namespace Aspose.Pdf. Potongan kode berikut menunjukkan cara membuat daftar isi di dalam file PDF yang ada menggunakan Python via .NET.

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)

    # Get access to first page of PDF file
    tocPage = doc.pages.insert(1)

    # Create object to represent TOC information
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Set the title for TOC
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Create string objects which will be used as TOC elements
    titles = ["First page", "Second page", "Third page", "Fourth page"]
    for i in range(0, 2):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 2]

        # Destination page
        heading2.top = doc.pages[i + 2].rect.height

        # Destination coordinate
        segment2.text = titles[i]

        # Add heading to page containing TOC
        tocPage.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)
```

### Atur TabLeaderType yang berbeda untuk Tingkat TOC yang berbeda

Aspose.PDF untuk Python juga memungkinkan pengaturan TabLeaderType yang berbeda untuk tingkat TOC yang berbeda. Anda perlu mengatur properti [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) pada [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # set LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title

    # Add the list section to the sections collection of the Pdf document
    tocPage.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins
    # and
    # text format settings of each level

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    # Create a section in the Pdf document
    page = doc.pages.add()

    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Sample Heading" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Add the heading into Table Of Contents.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # save the Pdf
    doc.save(output_pdf)
```

### Sembunyikan Nomor Halaman di TOC

Jika Anda tidak ingin menampilkan nomor halaman bersama dengan judul dalam TOC, Anda dapat menggunakan properti [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) pada Kelas [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) dengan nilai false. Silakan periksa potongan kode berikut untuk menyembunyikan nomor halaman dalam daftar isi:

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Add the list section to the sections collection of the Pdf document
    toc_page.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins and
    # text format settings of each level

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "this is heading of level " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```

### Sesuaikan Nomor Halaman saat menambahkan TOC

Umumnya penomoran halaman dalam TOC disesuaikan saat menambahkan TOC dalam dokumen PDF. Misalnya, kita mungkin perlu menambahkan awalan sebelum nomor halaman seperti P1, P2, P3, dan seterusnya. Dalam kasus seperti itu, Aspose.PDF untuk Python menyediakan properti [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) pada kelas [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) yang dapat digunakan untuk menyesuaikan nomor halaman seperti yang ditunjukkan dalam contoh kode berikut.

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)
    # Get access to first page of PDF file
    toc_page = doc.pages.insert(1)
    # Create object to represent TOC information
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Set the title for TOC
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 1]
        # Destination page
        heading2.top = doc.pages[i + 1].rect.height
        # Destination coordinate
        segment2.text = "Page " + str(i)
        # Add heading to page containing TOC
        toc_page.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)

```

## Cara mengatur tanggal kedaluwarsa PDF

Kami menerapkan hak akses pada file PDF sehingga kelompok pengguna tertentu dapat mengakses fitur/objek tertentu dalam dokumen PDF. Untuk membatasi akses file PDF, biasanya kami menerapkan enkripsi dan mungkin memiliki kebutuhan untuk mengatur kedaluwarsa file PDF, sehingga pengguna yang mengakses/menampilkan dokumen menerima prompt yang valid mengenai kedaluwarsa file PDF.

```python

    import aspose.pdf as ap

    # Instantiate Document object
    doc = ap.Document()
    # Add page to pages collection of PDF file
    doc.pages.add()
    # Add text fragment to paragraphs collection of page object
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # Create JavaScript object to set PDF expiry date
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('The file is expired. You need a new one.');"
    )
    # Set JavaScript as PDF open action
    doc.open_action = javaScript

    # Save PDF Document
    doc.save(output_pdf)
```

## Meratakan PDF yang Dapat Diisi di Python

Dokumen PDF sering menyertakan formulir dengan widget interaktif yang dapat diisi seperti tombol radio, kotak centang, kotak teks, daftar, dll. Untuk membuatnya tidak dapat diedit untuk berbagai keperluan aplikasi, kami perlu meratakan file PDF.
Aspose.PDF menyediakan fungsi untuk meratakan PDF Anda di Python dengan hanya beberapa baris kode:

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Flatten Fillable PDF
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```


