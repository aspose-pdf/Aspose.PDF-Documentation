---
title: Tambahkan Teks ke PDF menggunakan Python
linktitle: Tambahkan Teks ke PDF
type: docs
weight: 10
url: id/python-net/add-text-to-pdf-file/
description: Artikel ini menjelaskan berbagai aspek bekerja dengan teks di Aspose.PDF. Pelajari cara menambahkan teks ke PDF, menambahkan fragmen HTML, atau menggunakan font OTF kustom.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambahkan Teks ke PDF menggunakan Python",
    "alternativeHeadline": "Cara menambahkan Teks ke PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generasi dokumen pdf",
    "keywords": "pdf, python, tambahkan teks ke pdf",
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
    "url": "/python-net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-02-04",
    "description": "Artikel ini menjelaskan berbagai aspek bekerja dengan teks di Aspose.PDF untuk Python. Pelajari cara menambahkan teks ke PDF, menambahkan fragmen HTML, atau menggunakan font OTF kustom."
}
</script>


## Menambahkan Teks

1. Buka dokumen PDF input menggunakan Aspose.PDF.
1. Pilih halaman tertentu ke mana Anda ingin menambahkan teks.
1. Buat objek TextFragment. Sebuah fragmen teks dibuat dengan konten 'teks utama'. Fragmen ini diposisikan pada koordinat (100, 600) di halaman.
1. Mengatur Properti Teks. Berbagai properti dari teks diatur, seperti ukuran font, jenis font (Times New Roman), warna latar belakang (abu-abu muda), dan warna latar depan (merah).
1. Buat Objek TextBuilder. Sebuah objek TextBuilder diinstansiasi dengan halaman yang dipilih.
1. Tambahkan Fragmen Teks. Fragmen teks yang dibuat sebelumnya ditambahkan ke halaman PDF menggunakan objek TextBuilder.
1. Panggil metode [document.save](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dan simpan file PDF keluaran.

Cuplikan kode berikut menunjukkan cara menambahkan teks dalam file PDF yang sudah ada:

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Dapatkan halaman tertentu
    page = document.pages[1]

    # Buat fragmen teks
    text_fragment = ap.text.TextFragment("main text")
    text_fragment.position = ap.text.Position(100, 600)

    # Atur properti teks
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Buat objek TextBuilder
    builder = ap.text.TextBuilder(page)

    # Tambahkan fragmen teks ke halaman PDF
    builder.append_text(text_fragment)

    # Simpan dokumen PDF hasil.
    document.save(output_pdf)             
```


## Memuat Font dari Stream

Cuplikan kode berikut menunjukkan cara memuat Font dari objek aliran saat menambahkan teks ke dokumen PDF.

```python

    import aspose.pdf as ap

    # Muat file PDF input
    document = ap.Document()
    document.pages.add()
    # Buat objek pembangun teks untuk halaman pertama dokumen
    text_builder = ap.text.TextBuilder(document.pages[1])
    # Buat fragmen teks dengan string sampel
    text_fragment = ap.text.TextFragment("Hello world")

    if input_ttf != "":
        # Muat font TrueType ke dalam objek stream
        font_stream = open(input_ttf, "rb")
        # Tetapkan nama font untuk string teks
        text_fragment.text_state.font = ap.text.FontRepository.open_font(
            font_stream, ap.text.FontTypes.TTF
        )
        # Tentukan posisi untuk Fragmen Teks
        text_fragment.position = ap.text.Position(10, 10)
        # Tambahkan teks ke TextBuilder agar dapat ditempatkan di atas file PDF
        text_builder.append_text(text_fragment)
        # Simpan dokumen PDF yang dihasilkan.
        document.save(output_pdf)
```


## Tambahkan Teks menggunakan TextParagraph

Cuplikan kode berikut menunjukkan cara menambahkan teks dalam dokumen PDF menggunakan kelas [TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/).

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document()
    # Tambahkan halaman ke koleksi halaman dari objek Document
    page = document.pages.add()
    builder = ap.text.TextBuilder(page)
    # Buat paragraf teks
    paragraph = ap.text.TextParagraph()
    # Atur indentasi baris berikutnya
    paragraph.subsequent_lines_indent = 20
    # Tentukan lokasi untuk menambahkan TextParagraph
    paragraph.rectangle = ap.Rectangle(100, 300, 200, 700, False)
    # Tentukan mode pembungkusan kata
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )
    # Buat fragmen teks
    fragment1 = ap.text.TextFragment("the quick brown fox jumps over the lazy dog")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment1.text_state.font_size = 12
    # Tambahkan fragmen ke paragraf
    paragraph.append_line(fragment1)
    # Tambahkan paragraf
    builder.append_paragraph(paragraph)

    # Simpan dokumen PDF yang dihasilkan.
    document.save(output_pdf)
```


## Tambahkan Hyperlink ke TextSegment

Kode ini menunjukkan cara membuat konten dinamis dan interaktif dalam dokumen PDF, termasuk hyperlink ke sumber daya eksternal.

Sebuah halaman PDF mungkin terdiri dari satu atau lebih objek TextFragment, di mana setiap objek TextFragment dapat memiliki satu atau lebih instance [TextSegment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textsegment/).

Silakan coba menggunakan potongan kode berikut untuk memenuhi persyaratan ini:

```python

    import aspose.pdf as ap

    # Buat instance dokumen
    document = ap.Document()
    # Tambahkan halaman ke koleksi halaman file PDF
    page1 = document.pages.add()
    # Buat instance TextFragment
    tf = ap.text.TextFragment("Sample Text Fragment")
    # Atur perataan horizontal untuk TextFragment
    tf.horizontal_alignment = ap.HorizontalAlignment.RIGHT
    # Buat textsegment dengan teks contoh
    segment = ap.text.TextSegment(" ... Text Segment 1...")
    # Tambahkan segmen ke koleksi segmen dari TextFragment
    tf.segments.append(segment)
    # Buat TextSegment baru
    segment = ap.text.TextSegment("Link to Google")
    # Tambahkan segmen ke koleksi segmen dari TextFragment
    tf.segments.append(segment)
    # Atur hyperlink untuk TextSegment
    segment.hyperlink = ap.WebHyperlink("www.google.com")
    # Atur warna latar depan untuk text segment
    segment.text_state.foreground_color = ap.Color.blue
    # Atur pemformatan teks sebagai italic
    segment.text_state.font_style = ap.text.FontStyles.ITALIC
    # Buat objek TextSegment lainnya
    segment = ap.text.TextSegment("TextSegment tanpa hyperlink")
    # Tambahkan segmen ke koleksi segmen dari TextFragment
    tf.segments.append(segment)
    # Tambahkan TextFragment ke koleksi paragraf dari objek halaman
    page1.paragraphs.add(tf)
    # Simpan dokumen PDF yang dihasilkan.
    document.save(output_pdf)
```


## Gunakan Font OTF

Aspose.PDF untuk Python via .NET menawarkan fitur untuk menggunakan font Custom/TrueType saat membuat/memanipulasi konten file PDF sehingga konten file ditampilkan menggunakan konten selain font sistem default.

```python

    import aspose.pdf as ap

    # Buat instance dokumen baru
    document = ap.Document()
    # Tambahkan halaman ke koleksi halaman file PDF
    page = document.pages.add()
    # Buat instance TextFragment dengan teks contoh
    fragment = ap.text.TextFragment("Teks Contoh dalam font OTF")
    # Atau Anda bahkan dapat menentukan jalur font OTF di direktori sistem
    fragment.text_state.font = ap.text.FontRepository.open_font(input_otf)
    # Tentukan untuk menyematkan font di dalam file PDF, sehingga ditampilkan dengan benar,
    # Bahkan jika font tertentu tidak terinstal/ada di mesin target
    fragment.text_state.font.is_embedded = True
    # Tambahkan TextFragment ke koleksi paragraf dari instance Page
    page.paragraphs.add(fragment)
    # Simpan dokumen PDF yang dihasilkan.
    document.save(output_pdf)
```


## Menambahkan String HTML menggunakan DOM

Kode Python berikut menggunakan pustaka Aspose.PDF untuk membuat dokumen PDF dengan fragmen HTML.

1. Membuat instance Document. Sebuah instance dari kelas Document dibuat, mewakili dokumen PDF.
1. Tambahkan Halaman ke dokumen PDF.
1. Membuat instance objek HtmlFragment dengan konten HTML
1. Atur Margin untuk fragmen HTML. Dalam hal ini, margin bawah diatur ke 10 poin dan margin atas diatur ke 200 poin.
1. Tambahkan Fragmen HTML ke Halaman.
1. Simpan File PDF.

```python

    import aspose.pdf as ap

    # Membuat instance objek Document
    doc = ap.Document()
    # Tambahkan halaman ke koleksi halaman dari file PDF
    page = doc.pages.add()
    # Membuat instance HtmlFragment dengan konten HTML
    title = ap.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")
    # Atur informasi margin bawah
    title.margin.bottom = 10
    # Atur informasi margin atas
    title.margin.top = 200
    # Tambahkan Fragmen HTML ke koleksi paragraf dari halaman
    page.paragraphs.add(title)
    # Simpan file PDF
    doc.save(output_pdf)
```


### Gaya garis khusus untuk Catatan Kaki

Contoh berikut menunjukkan cara menambahkan Catatan Kaki ke bagian bawah halaman Pdf dan mendefinisikan gaya garis khusus.

```python

    import aspose.pdf as ap

    # Buat instance Dokumen
    doc = ap.Document()
    # Tambahkan halaman ke koleksi halaman PDF
    page = doc.pages.add()
    # Buat objek GraphInfo
    graph = ap.GraphInfo()
    # Atur lebar garis sebagai 2
    graph.line_width = 2
    # Atur warna untuk objek graph
    graph.color = ap.Color.red
    # Atur nilai dash array sebagai 3
    graph.dash_array = [3]
    # Atur nilai dash phase sebagai 1
    graph.dash_phase = 1
    # Atur gaya garis catatan kaki untuk halaman sebagai graph
    page.note_line_style = graph
    # Buat instance TextFragment
    text = ap.text.TextFragment("Hello World")
    # Atur nilai Catatan Kaki untuk TextFragment
    text.foot_note = ap.Note("catatan kaki untuk teks uji 1")
    # Tambahkan TextFragment ke koleksi paragraf halaman pertama dokumen
    page.paragraphs.add(text)
    # Buat TextFragment kedua
    text = ap.text.TextFragment("Aspose.Pdf for .NET")
    # Atur Catatan Kaki untuk fragmen teks kedua
    text.foot_note = ap.Note("catatan kaki untuk teks uji 2")
    # Tambahkan fragmen teks kedua ke koleksi paragraf file PDF
    page.paragraphs.add(text)
    # Simpan dokumen PDF yang dihasilkan.
    doc.save(output_pdf)
```


### Sesuaikan Label Catatan Kaki

Cuplikan kode berikut menunjukkan cara membuat dokumen PDF dengan fragmen teks yang mengandung catatan kaki.

Secara default, nomor Catatan Kaki bertambah mulai dari 1. Namun, kita mungkin memiliki kebutuhan untuk menetapkan label Catatan Kaki kustom. Untuk memenuhi kebutuhan ini, silakan coba gunakan cuplikan kode berikut

```python

    import aspose.pdf as ap

    # Buat instance Dokumen
    document = ap.Document()
    # Tambahkan halaman ke koleksi halaman PDF
    page = document.pages.add()
    # Buat objek GraphInfo
    graph = ap.GraphInfo()
    # Atur lebar garis sebagai 2
    graph.line_width = 2
    # Atur warna untuk objek grafis
    graph.color = ap.Color.red
    # Atur nilai array garis putus-putus sebagai 3
    graph.dash_array = [3]
    # Atur nilai fase garis putus-putus sebagai 1
    graph.dash_phase = 1
    # Atur gaya garis catatan kaki untuk halaman sebagai grafis
    page.note_line_style = graph
    # Buat instance TextFragment
    text = ap.text.TextFragment("Hello World")
    # Atur nilai Catatan Kaki untuk TextFragment
    text.foot_note = ap.Note("catatan kaki untuk teks uji 1")
    # Tentukan label kustom untuk Catatan Kaki
    text.foot_note.text = " Aspose"
    # Tambahkan TextFragment ke koleksi paragraf halaman pertama dokumen
    page.paragraphs.add(text)
    # Simpan dokumen PDF yang dihasilkan.
    document.save(output_pdf)
```


## Menambahkan Gambar dan Tabel ke Catatan Kaki

Kode ini menunjukkan cara membuat dokumen PDF dengan fragmen teks yang berisi catatan kaki kompleks yang mencakup gambar, teks, dan tabel menggunakan Aspose.PDF untuk Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    text = ap.text.TextFragment("some text")
    page.paragraphs.add(text)

    text.foot_note = ap.Note()
    image = ap.Image()
    image.file = input_jpg
    image.fix_height = 20
    text.foot_note.paragraphs.add(image)
    foot_note = ap.text.TextFragment("teks catatan kaki")
    foot_note.text_state.font_size = 20
    foot_note.is_in_line_paragraph = True
    text.foot_note.paragraphs.add(foot_note)
    table = ap.Table()
    table.rows.add().cells.add().paragraphs.add(ap.text.TextFragment("Baris 1 Sel 1"))
    text.foot_note.paragraphs.add(table)

    # Simpan dokumen PDF yang dihasilkan.
    document.save(output_pdf)
```

## Cara Membuat EndNotes

Sebuah EndNote adalah kutipan sumber yang merujuk pembaca ke tempat tertentu di akhir makalah di mana mereka dapat menemukan sumber informasi atau kata-kata yang dikutip atau disebutkan dalam makalah.
 Saat menggunakan catatan akhir, kalimat yang dikutip atau diparafrase atau materi yang diringkas diikuti oleh nomor superskrip.

Kode ini menunjukkan cara menambahkan fragmen teks dengan catatan akhir ke dokumen PDF menggunakan Aspose.PDF untuk Python:

```python

    import aspose.pdf as ap

    # Buat instance Dokumen
    document = ap.Document()
    # Tambahkan halaman ke koleksi halaman PDF
    page = document.pages.add()
    # Buat instance TextFragment
    text = ap.text.TextFragment("Hello World")
    # Setel nilai EndNote untuk TextFragment
    text.end_note = ap.Note("contoh Catatan akhir")
    # Tentukan label khusus untuk FootNote
    text.end_note.text = " Aspose"
    # Tambahkan TextFragment ke koleksi paragraf dari halaman pertama dokumen
    page.paragraphs.add(text)
    # Simpan dokumen PDF yang dihasilkan.
    document.save(output_pdf)
```

## Teks dan Gambar sebagai Paragraf InLine

Tata letak default dari file PDF adalah tata letak aliran (Atas-Kiri ke Bawah-Kanan). Setiap elemen baru yang ditambahkan ke file PDF ditambahkan di aliran kanan bawah. Namun, kita mungkin memiliki kebutuhan untuk menampilkan berbagai elemen halaman yaitu Gambar dan Teks pada tingkat yang sama (satu setelah yang lain). Salah satu pendekatan dapat dengan membuat instance Tabel dan menambahkan kedua elemen ke objek sel individu. Namun, pendekatan lain bisa berupa paragraf InLine. Dengan mengatur properti IsInLineParagraph dari Gambar dan Teks sebagai true, paragraf-paragraf ini akan muncul sebaris dengan elemen halaman lainnya.

Cuplikan kode berikut menunjukkan cara menambahkan teks dan Gambar sebagai paragraf InLine dalam file PDF.

```python

    import aspose.pdf as ap

    # Membuat instance Dokumen
    document = ap.Document()
    # Tambahkan halaman ke koleksi halaman dari instance Dokumen
    page = document.pages.add()
    # Membuat TextFragment
    text = ap.text.TextFragment("Hello World.. ")
    # Tambahkan fragmen teks ke koleksi paragraf dari objek Halaman
    page.paragraphs.add(text)
    # Membuat instance gambar
    image = ap.Image()
    # Atur gambar sebagai paragraf sebaris sehingga muncul tepat setelah
    # Objek paragraf sebelumnya (TextFragment)
    image.is_in_line_paragraph = True
    # Tentukan jalur file gambar
    image.file = input_jpg
    # Atur Tinggi gambar (opsional)
    image.fix_height = 30
    # Atur Lebar Gambar (opsional)
    image.fix_width = 100
    # Tambahkan gambar ke koleksi paragraf dari objek halaman
    page.paragraphs.add(image)
    # Inisialisasi ulang objek TextFragment dengan konten yang berbeda
    text = ap.text.TextFragment(" Hello Again..")
    # Atur TextFragment sebagai paragraf sebaris
    text.is_in_line_paragraph = True
    # Tambahkan TextFragment yang baru dibuat ke koleksi paragraf dari halaman
    page.paragraphs.add(text)
    # Simpan dokumen PDF yang dihasilkan.
    document.save(output_pdf)
```

## Menentukan Spasi Karakter saat Menambahkan Teks

Cuplikan kode berikut menunjukkan cara menghasilkan dokumen PDF yang berisi fragmen teks dengan spasi karakter yang diperbesar.

Teks dapat ditambahkan di dalam koleksi paragraf dari file PDF dengan menggunakan instance TextFragment atau dengan menggunakan objek TextParagraph dan bahkan Anda dapat menstempel teks di dalam PDF dengan menggunakan kelas TextStamp.

### Menggunakan TextBuilder dan TextFragment

```python

    import aspose.pdf as ap

    # Buat instance Dokumen
    document = ap.Document()
    # Tambahkan halaman ke koleksi halaman dari Dokumen
    document.pages.add()
    # Buat instance TextBuilder
    builder = ap.text.TextBuilder(document.pages[1])
    # Buat instance fragmen teks dengan konten contoh
    wide_fragment = ap.text.TextFragment("Teks dengan spasi karakter yang diperbesar")
    wide_fragment.text_state.apply_changes_from(ap.text.TextState("Arial", 12))
    # Tentukan spasi karakter untuk TextFragment
    wide_fragment.text_state.character_spacing = 2.0
    # Tentukan posisi dari TextFragment
    wide_fragment.position = ap.text.Position(100, 650)
    # Tambahkan TextFragment ke instance TextBuilder
    builder.append_text(wide_fragment)
    # Simpan dokumen PDF yang dihasilkan.
    document.save(output_pdf)
```


### Menggunakan TextParagraph

```python

    import aspose.pdf as ap

    # Buat instance Dokumen
    document = ap.Document()
    # Tambahkan halaman ke koleksi halaman Dokumen
    document.pages.add()
    # Buat instance TextBuilder
    builder = ap.text.TextBuilder(document.pages[1])
    # Instansiasi instance TextParagraph
    paragraph = ap.text.TextParagraph()
    # Buat instance TextState untuk menentukan nama dan ukuran font
    state = ap.text.TextState(12.0)
    state.font = ap.text.FontRepository.find_font("Arial")
    # Tentukan jarak antar karakter
    state.character_spacing = 1.5
    # Tambahkan teks ke objek TextParagraph
    tt = "Ini adalah paragraf dengan jarak antar karakter"
    paragraph.append_line(tt, state)
    # Tentukan posisi untuk TextParagraph
    paragraph.position = ap.text.Position(100, 550)
    # Tambahkan TextParagraph ke instance TextBuilder
    builder.append_paragraph(paragraph)
    # Simpan dokumen PDF yang dihasilkan.
    document.save(output_pdf)
```

### Menggunakan TextStamp

```python

    import aspose.pdf as ap

    # Buat instance Dokumen
    document = ap.Document()
    # Tambahkan halaman ke koleksi halaman Dokumen
    page = document.pages.add()
    # Instansiasi instance TextStamp dengan teks contoh
    stamp = ap.TextStamp("Ini adalah teks cap dengan jarak antar karakter")
    # Tentukan nama font untuk objek Stamp
    stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    # Tentukan ukuran Font untuk TextStamp
    stamp.text_state.font_size = 12
    # Tentukan jarak antar karakter sebagai 1
    stamp.text_state.character_spacing = 1
    # Atur x_indent untuk Stamp
    stamp.x_indent = 100
    # Atur y_indent untuk Stamp
    stamp.y_indent = 500
    # Tambahkan cap teks ke instance halaman
    stamp.put(page)
    # Simpan dokumen PDF yang dihasilkan.
    document.save(output_pdf)
```


## Membuat Dokumen PDF Multi-Kolom

[Aspose.PDF untuk Python via .NET](https://docs.aspose.com/pdf/python-net/) juga menawarkan fitur untuk membuat beberapa kolom di dalam halaman dokumen PDF. Untuk membuat file PDF multi-kolom, kita dapat menggunakan kelas FloatingBox karena menyediakan properti column_info untuk menentukan jumlah kolom di dalam FloatingBox dan kita juga dapat menentukan jarak antara kolom dan lebar kolom menggunakan properti column_spacing dan width sesuai kebutuhan.

Jarak kolom berarti ruang antara kolom dan jarak default antara kolom adalah 1,25cm. Jika lebar kolom tidak ditentukan, maka [Aspose.PDF untuk Python via .NET](https://docs.aspose.com/pdf/python-net/) menghitung lebar untuk setiap kolom secara otomatis sesuai dengan ukuran halaman dan jarak kolom.

Sebuah contoh diberikan di bawah ini untuk mendemonstrasikan pembuatan dua kolom dengan objek Grafik (Garis) dan mereka ditambahkan ke koleksi paragraf dari FloatingBox, yang kemudian ditambahkan ke koleksi paragraf dari instance Page.

```python

    import aspose.pdf as ap

    document = ap.Document()
    # Tentukan info margin kiri untuk file PDF
    document.page_info.margin.left = 40
    # Tentukan info margin kanan untuk file PDF
    document.page_info.margin.right = 40
    page = document.pages.add()

    graph1 = ap.drawing.Graph(500, 2)
    # Tambahkan garis ke koleksi paragraf dari objek bagian
    page.paragraphs.add(graph1)

    # Tentukan koordinat untuk garis
    pos1 = [1.0, 2.0, 500.0, 2.0]
    l1 = ap.drawing.Line(pos1)
    graph1.shapes.append(l1)
    # Buat variabel string dengan teks yang mengandung tag html
    s = (
        '<font face="Times New Roman" size=4>'
        + "<strong> Cara Menghindari Penipuan Uang</<strong> "
        + "</font>"
    )
    # Buat paragraf teks yang mengandung teks HTML
    heading_text = ap.HtmlFragment(s)
    page.paragraphs.add(heading_text)

    box = ap.FloatingBox()
    # Tambahkan empat kolom di bagian
    box.column_info.column_count = 2
    # Tetapkan jarak antar kolom
    box.column_info.column_spacing = "5"

    box.column_info.column_widths = "105 105"
    text1 = ap.text.TextFragment("Oleh A Googler (Blog Resmi Google)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)
    text1.text_state.font_size = 10

    text1.text_state.font_style = ap.text.FontStyles.ITALIC
    # Buat objek grafik untuk menggambar garis
    graph2 = ap.drawing.Graph(50, 10)
    # Tentukan koordinat untuk garis
    pos2 = [1.0, 10.0, 100.0, 10.0]
    l2 = ap.drawing.Line(pos2)
    graph2.shapes.append(l2)

    # Tambahkan garis ke koleksi paragraf dari objek bagian
    box.paragraphs.add(graph2)

    text2 = ap.text.TextFragment(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales."
    )
    box.paragraphs.add(text2)
    page.paragraphs.add(box)
    # Simpan file PDF
    document.save(output_pdf)
```


## Bekerja dengan Tab Stops Kustom

Cuplikan kode Python ini menunjukkan cara membuat dokumen PDF yang berisi fragmen teks yang diatur menggunakan tab stop untuk mensimulasikan struktur tabel.

Berikut adalah contoh cara mengatur tab stop kustom.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()

    ts = ap.text.TabStops()
    ts1 = ts.add(100.0)
    ts1.alignment_type = ap.text.TabAlignmentType.RIGHT
    ts1.leader_type = ap.text.TabLeaderType.SOLID
    ts2 = ts.add(200.0)
    ts2.alignment_type = ap.text.TabAlignmentType.CENTER
    ts2.leader_type = ap.text.TabLeaderType.DASH
    ts3 = ts.add(300.0)
    ts3.alignment_type = ap.text.TabAlignmentType.LEFT
    ts3.leader_type = ap.text.TabLeaderType.DOT

    header = ap.text.TextFragment(
        "Ini adalah contoh pembentukan tabel dengan TAB stops", ts
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts)

    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts)
    text2 = ap.text.TextFragment("#$TABdata21 ", ts)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    document.save(output_pdf)
```


## Cara Menambahkan Teks Transparan dalam PDF

File PDF berisi objek Gambar, Teks, Grafik, lampiran, Anotasi dan saat membuat TextFragment, Anda dapat mengatur informasi warna latar depan, latar belakang serta pemformatan teks. Aspose.PDF untuk Python via .NET mendukung fitur untuk menambahkan teks dengan saluran warna Alpha.

Cuplikan kode berikut menunjukkan cara menambahkan teks dengan warna transparan.

```python

    import aspose.pdf as ap

    # Buat instance Dokumen
    document = ap.Document()
    # Buat halaman ke koleksi halaman file PDF
    page = document.pages.add()

    # Buat instance TextFragment dengan nilai contoh
    text = ap.text.TextFragment(
        "teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan teks transparan "
    )
    # Buat objek warna dari saluran Alpha
    color = ap.Color.from_argb(30, 0, 255, 0)
    # Atur informasi warna untuk instance teks
    text.text_state.foreground_color = color
    # Tambahkan teks ke koleksi paragraf dari instance halaman
    page.paragraphs.add(text)

    document.save(output_pdf)
```


## Menentukan LineSpacing untuk Font

Setiap font memiliki kotak abstrak, yang tingginya adalah jarak yang dimaksudkan antara garis-garis teks dalam ukuran jenis yang sama. Kotak ini disebut kotak em dan merupakan kisi desain di mana garis besar huruf didefinisikan. Banyak huruf dari font input memiliki titik yang ditempatkan di luar batas kotak em font, jadi untuk menampilkan font dengan benar, penggunaan pengaturan khusus diperlukan.

Cuplikan kode berikut memuat PDF, menambahkan fragmen teks dengan spasi baris tertentu menggunakan font TrueType, dan menyimpan dokumen PDF yang dimodifikasi:

```python

    import aspose.pdf as ap

    # Muat file PDF input
    document = ap.Document()
    # Buat TextFormattingOptions dengan LineSpacingMode.FULL_SIZE
    options = ap.text.TextFormattingOptions()
    options.line_spacing = ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE

    # Buat fragmen teks dengan string contoh
    text_fragment = ap.text.TextFragment("Hello world")

    # Muat font TrueType ke dalam objek stream
    font_stream = open(input_ttf, "rb")
    # Tetapkan nama font untuk string teks
    text_fragment.text_state.font = ap.text.FontRepository.open_font(
        font_stream, ap.text.FontTypes.TTF
    )
    # Tentukan posisi untuk Fragmen Teks
    text_fragment.position = ap.text.Position(100, 600)
    # Tetapkan TextFormattingOptions dari fragmen saat ini ke yang telah ditentukan (yang menunjuk ke LineSpacingMode.FULL_SIZE)
    text_fragment.text_state.formatting_options = options
    page = document.pages.add()
    page.paragraphs.add(text_fragment)

    # Simpan dokumen PDF yang dihasilkan
    document.save(output_pdf)
```


## Mendapatkan Lebar Teks Secara Dinamis

Cuplikan kode Python ini melakukan perbandingan antara pengukuran string yang diperoleh dari objek font dan objek status teks di Aspose.PDF:

```python

    import math as ap

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if mt.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Pengukuran string font tidak terduga!")

    if mt.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Pengukuran string font tidak terduga!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        print(str(c_code) + "-" + c + "-" + str(ts_measure))

        if mt.fabs(fn_measure - ts_measure) > 0.001:
            print("Pengukuran string font dan state tidak cocok!")

        c_code += 1
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>