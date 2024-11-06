---
title: Apa yang baru
linktitle: Apa yang baru
type: docs
weight: 10
url: id/python-net/whatsnew/
description: Halaman ini memperkenalkan fitur baru paling populer di Aspose.PDF untuk Python via .NET yang telah diperkenalkan dalam rilis terbaru.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-24"
---

## Apa yang baru di Aspose.PDF 23.12

Dari Aspose.PDF 23.12, dukungan ditambahkan untuk fitur konversi baru:

- Menerapkan konversi PDF ke Markdown

```python

    import aspose.pdf as ap

    input_pdf_path = DIR_INPUT + "input.pdf"
    markdown_output_file_path = DIR_OUTPUT + "output_md_file.md"

    doc = ap.Document(input_pdf_path)
    save_options = ap.pdftomarkdown.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    doc.save(markdown_output_file_path, save_options)
```

- Menerapkan konversi OFD ke PDF

```python

    import aspose.pdf as ap

    input_path = DIR_INPUT + "input.ofd"
    output_path = DIR_OUTPUT + "output.pdf"
    document = ap.Document(input_path, ap.OfdLoadOptions())
    document.save(output_path)
```


Dukungan untuk Python 3.6 telah dihentikan.

## Apa yang baru di Aspose.PDF 23.11

Sejak 23.11 dimungkinkan untuk menghapus teks tersembunyi. Cuplikan kode berikut dapat digunakan:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    text_absorber = ap.text.TextFragmentAbsorber()
    # Opsi ini dapat digunakan untuk mencegah fragmen teks lain bergerak setelah penggantian teks tersembunyi.
    text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
    document.pages.accept(text_absorber)

    for fragment in text_absorber.text_fragments:
        if fragment.text_state.invisible:
            fragment.text = ''

    document.save(output_file)
```    

## Apa yang baru di Aspose.PDF 23.8

Sejak versi 23.8 mendukung penambahan deteksi Pembaruan Inkremental.

Fungsi untuk mendeteksi Pembaruan Inkremental dalam dokumen PDF telah ditambahkan.
 Fungsi ini mengembalikan 'true' jika sebuah dokumen disimpan dengan pembaruan inkremental; jika tidak, fungsi ini mengembalikan 'false'.

```python

    import aspose.pdf as ap

    doc = ap.Document(file_path)
    updated = doc.has_incremental_update()
    print(updated)
```

Selain itu, 23.8 mendukung cara untuk bekerja dengan bidang kotak centang bersarang. Banyak formulir PDF yang dapat diisi memiliki bidang kotak centang yang bertindak sebagai grup radio:

- Buat bidang kotak centang multi-nilai:

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    checkbox = ap.forms.CheckboxField(page, ap.Rectangle(50, 50, 70, 70, True))
    # Setel nilai opsi grup kotak centang pertama
    checkbox.export_value = "option 1"
    # Tambahkan opsi baru tepat di bawah yang sudah ada
    checkbox.add_option("option 2")
    # Tambahkan opsi baru pada persegi panjang yang diberikan
    checkbox.add_option("option 3", ap.Rectangle(100, 100, 120, 120, True))
    document.form.add(checkbox)
    # Pilih kotak centang yang ditambahkan
    checkbox.value = "option 2"
    document.save(DIR_OUTPUT + "checkbox_group.pdf")
```

- Dapatkan dan atur nilai dari kotak centang multi-nilai:

```python

    import aspose.pdf as ap

    doc = ap.Document("example.pdf")
    form = doc.form
    checkbox = cast(ap.forms.CheckboxField, form.fields[0])

    # Nilai yang diizinkan dapat diambil dari koleksi AllowedStates
    # Atur nilai kotak centang menggunakan properti Value
    checkbox.value = checkbox.allowed_states[0]
    checkbox_value = checkbox.value  # nilai yang telah diatur sebelumnya, mis. "opsi 1"
    # Nilai harus berupa elemen dari AllowedStates
    checkbox.value = "option 2"
    checkbox_value = checkbox.value  # opsi 2
    # Hapus centang dengan mengatur Value ke "Off" atau mengatur Checked ke false
    checkbox.value = "Off"
    # atau, sebagai alternatif:
    # checkbox.checked = False
    checkbox_value = checkbox.value  # Off
```

- Perbarui status kotak centang saat pengguna mengklik:

```python

    import aspose.pdf as ap
    from aspose.pycore import cast

    input_file = DIR_INPUT + "input.pdf"
    document = ap.Document(input_file)
    point = ap.Point(62,462)  # misalnya, koordinat klik mouse
    # Opsi 1: lihat melalui anotasi di halaman
    page = document.pages[5]
    for annotation in page.annotations:
        if(annotation.rect.contains(point)):
            widget = cast(ap.annotations.WidgetAnnotation, annotation)
            checkbox = cast(ap.forms.CheckboxField, widget.parent)
            if(annotation.active_state == "Off"):
                checkbox.value = widget.get_checked_state_name()
            else:
                checkbox.value = "Off"
        break
    # Opsi 2: lihat melalui bidang di AcroForm
    for widget in document.form:
        field = cast(ap.forms.Field, widget)
        if(field == None):
            continue
        checkBoxFound = False
        for annotation in field:
            if(annotation.rect.contains(point)):
                checkBoxFound = True
                if(annotation.active_state=="Off"):
                    annotation.parent.value = annotation.get_checked_state_name()
                else:
                    annotation.parent.value = "Off"
            if(checkBoxFound):
                break
```


## Apa yang baru di Aspose.PDF 23.7

Sejak versi 23.7 mendukung untuk menambahkan ekstraksi bentuk:

```python

    import aspose.pdf as ap

    input1_file = DIR_INPUT + "input_1.pdf"
    input2_file = DIR_INPUT + "input_2.pdf"

    source = ap.Document(input1_file)
    dest = ap.Document(input2_file)

    graphic_absorber = ap.vector.GraphicsAbsorber()
    graphic_absorber.visit(source.pages[1])
    area = ap.Rectangle(90, 250, 300, 400, True)
    dest.pages[1].add_graphics(graphic_absorber.elements, area)
```

Juga mendukung kemampuan untuk mendeteksi Overflow saat menambahkan teks:

```python

    import aspose.pdf as ap

    output_file = DIR_OUTPUT + "output.pdf"
    doc = ap.Document()
    paragraph_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan."
    fragment = ap.text.TextFragment(paragraph_content)
    rectangle = ap.Rectangle(100, 600, 500, 700, False)
    paragraph = ap.text.TextParagraph()
    paragraph.vertical_alignment = ap.VerticalAlignment.TOP
    paragraph.formatting_options.wrap_mode = ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.rectangle = rectangle
    is_fit_rectangle = fragment.text_state.is_fit_rectangle(paragraph_content, rectangle)

    while is_fit_rectangle == False:
        fragment.text_state.font_size -= 0.5
        is_fit_rectangle = fragment.text_state.is_fit_rectangle(paragraph_content, rectangle)

    paragraph.append_line(fragment)
    builder = ap.text.TextBuilder(doc.pages.add())
    builder.append_paragraph(paragraph)
    doc.save(output_file)
```


## Apa yang baru di Aspose.PDF 23.6

Dukungan kemampuan untuk mengatur judul halaman HTML, Epub:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_html = DIR_OUTPUT + "output_title.html"
    options = ap.HtmlSaveOptions()
    options.fixed_layout = True
    options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    options.parts_embedding_mode = ap.HtmlSaveOptions.PartsEmbeddingModes.EMBED_ALL_INTO_HTML
    options.title = "HALAMAN & JUDUL BARU"  # <-- ini ditambahkan

    document = ap.Document(input_pdf)
    document.save(output_html, options)
```

## Apa yang baru di Aspose.PDF 23.5

Sejak versi 23.5 mendukung penambahan opsi RedactionAnnotation FontSize. Gunakan potongan kode berikut untuk menyelesaikan tugas ini:

```python

    import aspose.pdf as ap

    doc = ap.Document(DIR_INPUT + "input.pdf")
    # Buat instance RedactionAnnotation untuk area halaman tertentu
    annot = ap.annotations.RedactionAnnotation(doc.pages[1], ap.Rectangle(367, 756.919982910156, 420, 823.919982910156, True))
    annot.fill_color = ap.Color.black
    annot.border_color = ap.Color.yellow
    annot.color = ap.Color.blue
    # Teks yang akan dicetak pada anotasi redaksi
    annot.overlay_text = "(Tidak Diketahui)"
    annot.text_alignment = ap.HorizontalAlignment.CENTER
    # Ulangi teks overlay pada anotasi redaksi
    annot.repeat = False
    # Properti baru di sini!
    annot.font_size = 20
    # Tambahkan anotasi ke koleksi anotasi halaman pertama
    doc.pages[1].annotations.add(annot, False)
    # Memperhalus anotasi dan menghapus isi halaman (yaitu, menghapus teks dan gambar
    # Di bawah anotasi yang direduksi)
    annot.redact()
    out_file = DIR_OUTPUT + "RedactPage_out.pdf"
    doc.save(out_file)
```


Dukungan untuk Python 3.5 telah dihentikan. Dukungan untuk Python 3.11 telah ditambahkan.

## Apa yang baru di Aspose.PDF 23.3

Versi 23.3 memperkenalkan dukungan untuk menambahkan resolusi ke sebuah gambar. Dua metode dapat digunakan untuk menyelesaikan masalah ini:

```python

    import aspose.pdf as ap

    input_file = DIR_INPUT + "input.jpg"
    table = ap.Table()
    table.column_widths = "600"
    image = ap.Image()
    image.is_apply_resolution = True
    image.file = input_file
    for i in range(0, 2):
        row = table.rows.add()
        cell = row.cells.add()
        cell.paragraphs.add(image)

    page.paragraphs.add(table)
```

Gambar akan ditempatkan dengan resolusi skala atau Anda dapat mengatur properti FixedWidth atau FixedHeight dalam kombinasi dengan IsApplyResolution

## Apa yang baru di Aspose.PDF 23.1

Sejak versi 23.1 mendukung pembuatan anotasi PrinterMark.

Tanda printer adalah simbol grafis atau teks yang ditambahkan ke sebuah halaman untuk membantu personel produksi dalam mengidentifikasi komponen dari pekerjaan multi-pelat dan mempertahankan keluaran yang konsisten selama produksi.
 Contoh yang umum digunakan dalam industri percetakan meliputi:

- Target registrasi untuk menyelaraskan pelat
- Rampa abu-abu dan batang warna untuk mengukur warna dan kepadatan tinta
- Tanda potong yang menunjukkan di mana media keluaran harus dipangkas

Kami akan menunjukkan contoh opsi dengan batang warna untuk mengukur warna dan kepadatan tinta. Ada kelas abstrak dasar PrinterMarkAnnotation dan dari itu turunannya ColorBarAnnotation - yang sudah mengimplementasikan garis-garis ini. Mari kita periksa contohnya:

```python

    import aspose.pdf as ap

    out_file = DIR_OUTPUT  + "ColorBarTest.pdf"
    doc = ap.Document()
    page = doc.pages.add()
    page.trim_box = ap.Rectangle(20, 20, 580, 820, True)
    add_annotations(page)
    doc.save(out_file)


def add_annotations(page: ap.Page):
    rect_black = ap.Rectangle(100, 300, 300, 320, True)
    rect_cyan = ap.Rectangle(200, 600, 260, 690, True)
    rect_magenta = ap.Rectangle(10, 650, 140, 670, True)
    color_bar_black = ap.annotations.ColorBarAnnotation(page, rect_black, ap.annotations.ColorsOfCMYK.BLACK)
    color_bar_cyan = ap.annotations.ColorBarAnnotation(page, rect_cyan, ap.annotations.ColorsOfCMYK.CYAN)
    color_ba_magenta = ap.annotations.ColorBarAnnotation(page, rect_magenta, ap.annotations.ColorsOfCMYK.BLACK)
    color_ba_magenta.color_of_cmyk = ap.annotations.ColorsOfCMYK.MAGENTA
    color_bar_yellow = ap.annotations.ColorBarAnnotation(page, ap.Rectangle(400, 250, 450, 700, True), ap.annotations.ColorsOfCMYK.YELLOW)
    page.annotations.add(color_bar_black, False)
    page.annotations.add(color_bar_cyan, False)
    page.annotations.add(color_ba_magenta, False)
    page.annotations.add(color_bar_yellow, False)
```
Also mendukung ekstraksi gambar vektor. Cobalah menggunakan kode berikut untuk mendeteksi dan mengekstrak grafik vektor:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_pdf = DIR_OUTPUT + "output.svg"
    doc = ap.Document(input_pdf)
    doc.pages[1].try_save_vector_graphics(output_pdf)
```