---
title: Formatting PDF Document menggunakan Python
linktitle: Formatting PDF Document
type: docs
weight: 11
url: id/python-net/formatting-pdf-document/
description: Buat dan format Dokumen PDF dengan Aspose.PDF untuk Python via .NET. Gunakan cuplikan kode berikut untuk menyelesaikan tugas Anda.
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatting PDF Document menggunakan Python",
    "alternativeHeadline": "Cara memformat Dokumen PDF di Python melalui .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, dotnet, python, format dokumen pdf",
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
                "areaServed": "AS",
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
    "url": "/python-net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/formatting-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "Buat dan format Dokumen PDF dengan Aspose.PDF untuk Python via .NET. Gunakan cuplikan kode berikut untuk menyelesaikan tugas Anda."
}
</script>


## Formatting PDF Document

### Mendapatkan Properti Jendela Dokumen dan Tampilan Halaman

Topik ini membantu Anda memahami cara mendapatkan properti dari jendela dokumen, aplikasi penampil, dan bagaimana halaman ditampilkan. Untuk mengatur properti ini:

Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Sekarang, Anda dapat mengatur properti objek Document, seperti

- CenterWindow – Memusatkan jendela dokumen di layar. Default: false.
- Direction – Urutan membaca. Ini menentukan bagaimana halaman diatur saat ditampilkan berdampingan. Default: kiri ke kanan.
- DisplayDocTitle – Menampilkan judul dokumen di bilah judul jendela dokumen. Default: false (judul ditampilkan).
- HideMenuBar – Menyembunyikan atau menampilkan bilah menu jendela dokumen. Default: false (bilah menu ditampilkan).
- HideToolBar – Menyembunyikan atau menampilkan bilah alat jendela dokumen. Default: false (bilah alat ditampilkan).
- HideWindowUI – Menyembunyikan atau menampilkan elemen jendela dokumen seperti bilah gulir.
  Default: false (elemen UI ditampilkan).
- NonFullScreenPageMode – Bagaimana dokumen ditampilkan ketika tidak dalam mode layar penuh.
- PageLayout – Tata letak halaman.
- PageMode – Bagaimana dokumen ditampilkan ketika pertama kali dibuka. Opsi termasuk menampilkan thumbnail, layar penuh, menampilkan panel lampiran.

Cuplikan kode berikut menunjukkan cara mendapatkan properti menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Dapatkan berbagai properti dokumen
    # Posisi jendela dokumen - Default: false
    print("CenterWindow :", document.center_window)

    # Urutan membaca yang dominan; menentukan posisi halaman
    # Ketika ditampilkan berdampingan - Default: L2R
    print("Direction :", document.direction)

    # Apakah bilah judul jendela harus menampilkan judul dokumen
    # Jika false, bilah judul menampilkan nama file PDF - Default: false
    print("DisplayDocTitle :", document.display_doc_title)

    # Apakah ukuran jendela dokumen harus diubah untuk menyesuaikan ukuran
    # Halaman pertama yang ditampilkan - Default: false
    print("FitWindow :", document.fit_window)

    # Apakah akan menyembunyikan bilah menu dari aplikasi penampil - Default: false
    print("HideMenuBar :", document.hide_menubar)

    # Apakah akan menyembunyikan bilah alat dari aplikasi penampil - Default: false
    print("HideToolBar :", document.hide_tool_bar)

    # Apakah akan menyembunyikan elemen UI seperti bilah gulir
    # Dan hanya menampilkan konten halaman - Default: false
    print("HideWindowUI :", document.hide_window_ui)

    # Mode halaman dokumen. Cara menampilkan dokumen saat keluar dari mode layar penuh.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # Tata letak halaman yaitu satu halaman, satu kolom
    print("PageLayout :", document.page_layout)

    # Bagaimana dokumen harus ditampilkan saat dibuka
    # Yaitu, menampilkan thumbnail, layar penuh, menampilkan panel lampiran
    print("pageMode :", document.page_mode)

```

### Setel Properti Jendela Dokumen dan Tampilan Halaman

Topik ini menjelaskan cara mengatur properti jendela dokumen, aplikasi penampil, dan tampilan halaman. Untuk mengatur properti yang berbeda ini:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Atur properti objek Document.
1. Simpan file PDF yang telah diperbarui menggunakan metode save.

Properti yang tersedia adalah:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Masing-masing digunakan dan dijelaskan dalam kode di bawah ini. Cuplikan kode berikut menunjukkan cara mengatur properti menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Atur berbagai properti dokumen
    # Tentukan untuk memposisikan jendela dokumen - Default: false
    document.center_window = True

    # Urutan membaca yang dominan; menentukan posisi halaman
    # Ketika ditampilkan berdampingan - Default: L2R
    document.direction = ap.Direction.R2L

    # Tentukan apakah bilah judul jendela harus menampilkan judul dokumen
    # Jika salah, bilah judul menampilkan nama file PDF - Default: false
    document.display_doc_title = True

    # Tentukan apakah akan mengubah ukuran jendela dokumen agar sesuai dengan ukuran
    # Halaman pertama yang ditampilkan - Default: false
    document.fit_window = True

    # Tentukan apakah akan menyembunyikan bilah menu dari aplikasi penampil - Default: false
    document.hide_menubar = True

    # Tentukan apakah akan menyembunyikan bilah alat dari aplikasi penampil - Default: false
    document.hide_tool_bar = True

    # Tentukan apakah akan menyembunyikan elemen UI seperti bilah gulir
    # Dan hanya menampilkan konten halaman - Default: false
    document.hide_window_ui = True

    # Mode halaman dokumen. tentukan bagaimana menampilkan dokumen saat keluar dari mode layar penuh.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Tentukan tata letak halaman yaitu satu halaman, satu kolom
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Tentukan bagaimana dokumen harus ditampilkan saat dibuka
    # Yaitu menampilkan thumbnail, layar penuh, menampilkan panel lampiran
    document.page_mode = ap.PageMode.USE_THUMBS

    # Simpan file PDF yang telah diperbarui
    document.save(output_pdf)
```


### Menyematkan Font Standar Tipe 1

Beberapa dokumen PDF memiliki font dari set font khusus Adobe. Font dari set ini disebut "Font Standar Tipe 1". Set ini mencakup 14 font dan menyematkan jenis font ini memerlukan penggunaan flag khusus yaitu [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). Berikut adalah potongan kode yang dapat digunakan untuk mendapatkan dokumen dengan semua font disematkan termasuk Font Standar Tipe 1:

```python

    import aspose.pdf as ap

    # Memuat Dokumen PDF yang ada
    document = ap.Document(input_pdf)
    # Atur properti EmbedStandardFonts pada dokumen
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Periksa apakah font sudah disematkan
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Menyematkan Font saat membuat PDF

Jika Anda perlu menggunakan font selain dari 14 font inti yang didukung oleh Adobe Reader, Anda harus menyematkan deskripsi font saat membuat file PDF. Jika informasi font tidak disematkan, Adobe Reader akan mengambilnya dari Sistem Operasi jika sudah terinstal di sistem, atau akan membangun font pengganti sesuai dengan deskriptor font dalam PDF.

>Harap dicatat bahwa font yang disematkan harus diinstal pada mesin host yaitu dalam kasus kode berikut ini font 'Univers Condensed' diinstal di sistem.

Kami menggunakan properti 'is_embedded' untuk menyematkan informasi font ke dalam file PDF. Mengatur nilai properti ini ke 'True' akan menyematkan file font lengkap ke dalam PDF, dengan mengetahui fakta bahwa itu akan meningkatkan ukuran file PDF. Berikut adalah potongan kode yang dapat digunakan untuk menyematkan informasi font ke dalam PDF.

```python

    import aspose.pdf as ap

    # Memulai objek Pdf dengan memanggil konstruktor kosongnya
    doc = ap.Document()

    # Buat sebuah bagian dalam objek Pdf
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" Ini adalah teks sampel menggunakan font Kustom.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Simpan Dokumen PDF
    doc.save(output_pdf)
```


### Atur Nama Font Default saat Menyimpan PDF

Ketika dokumen PDF mengandung font yang tidak tersedia dalam dokumen itu sendiri dan pada perangkat, API mengganti font tersebut dengan font default. Jika font tersedia (terpasang pada perangkat atau tertanam dalam dokumen), PDF keluaran harus memiliki font yang sama (tidak boleh diganti dengan font default). Nilai dari font default harus mengandung nama font (bukan jalur ke file font). Kami telah mengimplementasikan fitur untuk mengatur nama font default saat menyimpan dokumen sebagai PDF. Potongan kode berikut dapat digunakan untuk mengatur font default:

```python

    import aspose.pdf as ap

    # Muat dokumen PDF yang ada dengan font yang hilang
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Tentukan Nama Font Default
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### Dapatkan Semua Font dari Dokumen PDF

Jika Anda ingin mendapatkan semua font dari dokumen PDF, Anda dapat menggunakan metode [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) yang disediakan dalam kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
 Silakan periksa potongan kode berikut untuk mendapatkan semua font dari dokumen PDF yang ada:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### Tingkatkan Penyematan Font menggunakan FontSubsetStrategy

Potongan kode berikut menunjukkan cara mengatur [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) yang digunakan properti [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties):

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # Semua font akan disematkan sebagai subset ke dalam dokumen jika SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # Subset font akan disematkan untuk font yang sepenuhnya disematkan tetapi font yang tidak disematkan ke dalam dokumen tidak akan terpengaruh.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### Dapatkan-Setel Faktor Zoom dari File PDF

Terkadang, Anda ingin menentukan berapa faktor zoom dokumen PDF saat ini. Dengan Aspose.Pdf, Anda dapat mengetahui nilai saat ini serta menetapkan satu.

Properti Destinasi dari kelas [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) memungkinkan Anda untuk mendapatkan nilai zoom yang terkait dengan file PDF. Demikian pula, ini dapat digunakan untuk menetapkan faktor zoom sebuah file.

#### Setel Faktor Zoom

Cuplikan kode berikut menunjukkan cara mengatur faktor zoom dari sebuah file PDF.

```python

    import aspose.pdf as ap

    # Menginisialisasi objek Dokumen baru
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Simpan dokumen
    doc.save(output_pdf)
```

#### Dapatkan Faktor Zoom

Cuplikan kode berikut menunjukkan cara mendapatkan faktor zoom dari sebuah file PDF.

```python

    import aspose.pdf as ap

    # Menginisialisasi objek Dokumen baru
    doc = ap.Document(input_pdf)

    # Buat objek GoToAction
    action = doc.open_action

    # Dapatkan faktor Zoom dari file PDF
    print(action.destination.zoom)
```


### Menyetel Properti Preset Dialog Cetak

Aspose.PDF memungkinkan pengaturan anggota [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) dari dokumen PDF. Ini memungkinkan Anda mengubah properti DuplexMode untuk dokumen PDF yang diatur ke simplex secara default. Hal ini dapat dicapai menggunakan dua metodologi berbeda seperti yang ditunjukkan di bawah ini.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### Menyetel Properti Preset Dialog Cetak menggunakan Editor Konten PDF

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("File memiliki duplex flip short edge")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```