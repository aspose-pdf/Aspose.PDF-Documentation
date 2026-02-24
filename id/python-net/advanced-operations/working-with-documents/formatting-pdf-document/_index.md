---
title: Memformat Dokumen PDF menggunakan Python
linktitle: Memformat Dokumen PDF
type: docs
weight: 11
url: /id/python-net/formatting-pdf-document/
description: Buat dan format Dokumen PDF dengan Aspose.PDF untuk Python via .NET. Gunakan potongan kode berikut untuk menyelesaikan tugas Anda.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Memformat dokumen PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang memanipulasi dan memformat dokumen PDF menggunakan pustaka Aspose.PDF dalam Python. Artikel ini mencakup berbagai aspek penyesuaian PDF, termasuk pengaturan jendela dokumen dan properti tampilan halaman seperti memusatkan jendela, arah baca, dan menyembunyikan elemen UI. Artikel menjelaskan cara mengambil dan mengatur properti tersebut secara programatis menggunakan kelas `Document`. Selain itu, artikel membahas manajemen font, merinci cara menyematkan font Standard Type 1 dan font lain ke dalam PDF, memastikan portabilitas dokumen dan konsistensi visual di seluruh sistem. Artikel juga menyoroti teknik untuk menetapkan nama font default, mengambil semua font dari PDF, dan meningkatkan penyematan font menggunakan `FontSubsetStrategy`. Selanjutnya, artikel menjelaskan tentang penyesuaian faktor zoom dokumen PDF menggunakan kelas `GoToAction` serta mengkonfigurasi properti preset dialog cetak, termasuk opsi pencetakan duplex. Potongan kode menyertai setiap bagian, memberikan contoh praktis untuk mengimplementasikan fitur-fitur ini.
---

## Memformat Dokumen PDF

### Dapatkan Properti Jendela Dokumen dan Tampilan Halaman

Topik ini membantu Anda memahami cara mendapatkan properti jendela dokumen, aplikasi penampil, dan cara halaman ditampilkan. Untuk mengatur properti ini:

Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) . Sekarang, Anda dapat mengatur properti objek Document, seperti

- CenterWindow – Memusatkan jendela dokumen di layar. Default: false.
- Direction – Urutan baca. Ini menentukan bagaimana halaman disusun saat ditampilkan berdampingan. Default: kiri ke kanan.
- DisplayDocTitle – Tampilkan judul dokumen di bilah judul jendela dokumen. Default: false (judul ditampilkan).
- HideMenuBar – Sembunyikan atau tampilkan menu bar jendela dokumen. Default: false (menu bar ditampilkan).
- HideToolBar – Sembunyikan atau tampilkan toolbar jendela dokumen. Default: false (toolbar ditampilkan).
- HideWindowUI – Sembunyikan atau tampilkan elemen jendela dokumen seperti bilah gulir. Default: false (elemen UI ditampilkan).
- NonFullScreenPageMode – Bagaimana dokumen ditampilkan ketika tidak dalam mode halaman penuh.
- PageLayout – Tata letak halaman.
- PageMode – Bagaimana dokumen ditampilkan saat pertama kali dibuka. Pilihannya adalah menampilkan thumbnail, layar penuh, menampilkan panel lampiran.

Potongan kode berikut menunjukkan cara mendapatkan properti menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get different document properties
    # Position of document's window - Default: false
    print("CenterWindow :", document.center_window)

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    print("Direction :", document.direction)

    # Whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    print("DisplayDocTitle :", document.display_doc_title)

    # Whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    print("FitWindow :", document.fit_window)

    # Whether to hide menu bar of the viewer application - Default: false
    print("HideMenuBar :", document.hide_menubar)

    # Whether to hide tool bar of the viewer application - Default: false
    print("HideToolBar :", document.hide_tool_bar)

    # Whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    print("HideWindowUI :", document.hide_window_ui)

    # Document's page mode. How to display document on exiting full-screen mode.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # The page layout i.e. single page, one column
    print("PageLayout :", document.page_layout)

    # How the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    print("pageMode :", document.page_mode)

```

### Atur Properti Jendela Dokumen dan Tampilan Halaman

Topik ini menjelaskan cara mengatur properti jendela dokumen, aplikasi penampil, dan tampilan halaman. Untuk mengatur properti yang berbeda ini:

1. Buka file PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Atur properti objek Document.
1. Simpan file PDF yang diperbarui menggunakan metode save.

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

Masing-masing digunakan dan dijelaskan dalam kode di bawah ini. Potongan kode berikut menunjukkan cara mengatur properti menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set different document properties
    # Sepcify to position document's window - Default: false
    document.center_window = True

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    document.direction = ap.Direction.R2L

    # Specify whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    document.display_doc_title = True

    # Specify whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    document.fit_window = True

    # Specify whether to hide menu bar of the viewer application - Default: false
    document.hide_menubar = True

    # Specify whether to hide tool bar of the viewer application - Default: false
    document.hide_tool_bar = True

    # Specify whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    document.hide_window_ui = True

    # Document's page mode. specify how to display document on exiting full-screen mode.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Specify the page layout i.e. single page, one column
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Specify how the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_THUMBS

    # Save updated PDF file
    document.save(output_pdf)
```

### Menyematkan Font Standard Type 1

Beberapa dokumen PDF memiliki font dari kumpulan font khusus Adobe. Font dari kumpulan ini disebut “Standard Type 1 Fonts”. Kumpulan ini mencakup 14 font dan penyematan jenis font ini memerlukan penggunaan bendera khusus yaitu [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). Berikut adalah potongan kode yang dapat digunakan untuk menghasilkan dokumen dengan semua font disematkan termasuk Standard Type 1 Fonts:

```python

    import aspose.pdf as ap

    # Load an existing PDF Document
    document = ap.Document(input_pdf)
    # Set EmbedStandardFonts property of document
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Check if font is already embedded
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Embedding Fonts while creating PDF

Jika Anda perlu menggunakan font apa pun selain 14 font inti yang didukung oleh Adobe Reader, Anda harus menyematkan deskripsi font saat menghasilkan file PDF. Jika informasi font tidak disematkan, Adobe Reader akan mengambilnya dari Sistem Operasi jika font tersebut terpasang di sistem, atau akan membuat font pengganti berdasarkan deskriptor font dalam PDF.

>Harap dicatat bahwa font yang disematkan harus terpasang pada mesin host, misalnya pada kode berikut font ‘Univers Condensed’ terpasang di sistem.

Kami menggunakan properti 'is_embedded' untuk menyematkan informasi font ke dalam file PDF. Mengatur nilai properti ini menjadi 'True' akan menyematkan file font lengkap ke dalam PDF, dengan fakta bahwa hal ini akan meningkatkan ukuran file PDF. Berikut adalah potongan kode yang dapat digunakan untuk menyematkan informasi font ke dalam PDF.

```python

    import aspose.pdf as ap

    # Instantiate Pdf object by calling its empty constructor
    doc = ap.Document()

    # Create a section in the Pdf object
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Save PDF Document
    doc.save(output_pdf)
```

### Atur Nama Font Default saat Menyimpan PDF

Ketika dokumen PDF berisi font yang tidak tersedia dalam dokumen itu sendiri maupun di perangkat, API mengganti font tersebut dengan font default. Jika font tersedia (dipasang di perangkat atau disematkan dalam dokumen), PDF keluaran harus menggunakan font yang sama (tidak diganti dengan font default). Nilai font default harus berisi nama font (bukan path ke file font). Kami telah mengimplementasikan fitur untuk mengatur nama font default saat menyimpan dokumen sebagai PDF. Potongan kode berikut dapat digunakan untuk mengatur font default:

```python

    import aspose.pdf as ap

    # Load an existing PDF document with missing font
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Specify Default Font Name
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### Dapatkan Semua Font dari Dokumen PDF

Jika Anda ingin mendapatkan semua font dari dokumen PDF, Anda dapat menggunakan metode [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) yang disediakan dalam kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Silakan periksa potongan kode berikut untuk mendapatkan semua font dari dokumen PDF yang sudah ada:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### Tingkatkan Penyematan Font menggunakan FontSubsetStrategy

Potongan kode berikut menunjukkan cara mengatur [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) yang digunakan pada properti [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties):

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # All fonts will be embedded as subset into document in case of SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### Dapatkan-Setel Faktor Zoom File PDF

Terkadang, Anda ingin menentukan faktor zoom saat ini dari dokumen PDF. Dengan Aspose.Pdf, Anda dapat mengetahui nilai saat ini serta menentukannya.

Properti Destination kelas [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) memungkinkan Anda mendapatkan nilai zoom yang terkait dengan file PDF. Demikian pula, properti ini dapat digunakan untuk mengatur faktor zoom file.

#### Atur Faktor Zoom

Potongan kode berikut menunjukkan cara mengatur faktor zoom dari file PDF.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Save the document
    doc.save(output_pdf)
```

#### Dapatkan Faktor Zoom

Potongan kode berikut menunjukkan cara mendapatkan faktor zoom file PDF.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    # Create GoToAction object
    action = doc.open_action

    # Get the Zoom factor of PDF file
    print(action.destination.zoom)
```

### Mengatur Properti Prasetel Dialog Cetak

Aspoose.PDF memungkinkan pengaturan anggota [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) pada dokumen PDF. Ini memungkinkan Anda mengubah properti DuplexMode untuk dokumen PDF yang secara default diatur ke simplex. Hal ini dapat dicapai menggunakan dua metodologi berbeda seperti yang ditunjukkan di bawah.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### Mengatur Properti Prasetel Dialog Cetak menggunakan PDF Content Editor

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("The file has duplex flip short edge")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```


