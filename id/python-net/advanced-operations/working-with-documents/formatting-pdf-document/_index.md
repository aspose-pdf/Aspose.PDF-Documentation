---
title: Format Dokumen PDF di Python
linktitle: Memformat Dokumen PDF
type: docs
weight: 11
url: /id/python-net/formatting-pdf-document/
description: Pelajari cara memformat dokumen PDF, menyematkan font, mengontrol pengaturan penampil, dan menyesuaikan opsi tampilan di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Memformat dokumen PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang memanipulasi dan memformat dokumen PDF menggunakan pustaka Aspose.PDF dalam Python. Artikel ini mencakup berbagai aspek kustomisasi PDF, termasuk pengaturan jendela dokumen dan properti tampilan halaman seperti memusatkan jendela, arah bacaan, dan menyembunyikan elemen UI. Artikel menjelaskan cara mengambil dan mengatur properti ini secara programatis menggunakan kelas `Document`. Selain itu, artikel membahas manajemen font, merinci cara menyematkan font Standard Type 1 dan font lain ke dalam PDF, memastikan portabilitas dokumen dan konsistensi visual di seluruh sistem. Artikel juga menyoroti teknik untuk mengatur nama font default, mengambil semua font dari PDF, dan meningkatkan penyematan font menggunakan `FontSubsetStrategy`. Selanjutnya, artikel menjelaskan penyesuaian faktor zoom dokumen PDF menggunakan kelas `GoToAction` dan mengonfigurasi properti preset dialog cetak, termasuk opsi pencetakan dupleks. Potongan kode menyertai setiap bagian, memberikan contoh praktis untuk mengimplementasikan fitur-fitur ini.
---

Panduan ini berguna ketika Anda perlu mengontrol perilaku penampil PDF, penyematan font, pengaturan tampilan default, atau preferensi pencetakan dalam dokumen yang dihasilkan oleh Python.

## Memformat Dokumen PDF

### Dapatkan Properti Jendela Dokumen dan Tampilan Halaman

Topik ini membantu Anda memahami cara mendapatkan properti jendela dokumen, aplikasi penampil, dan bagaimana halaman ditampilkan. Untuk mengatur properti ini:

Buka file PDF menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas. Sekarang, Anda dapat mengatur properti objek Document, seperti

- CenterWindow – Pusatkan jendela dokumen pada layar. Default: false.
- Direction – Urutan membaca. Ini menentukan bagaimana halaman ditata ketika ditampilkan berdampingan. Default: kiri ke kanan.
- DisplayDocTitle – Tampilkan judul dokumen di bilah judul jendela dokumen. Default: false (judul ditampilkan).
- HideMenuBar – Sembunyikan atau tampilkan bilah menu jendela dokumen. Default: false (bilah menu ditampilkan).
- HideToolBar – Sembunyikan atau tampilkan toolbar jendela dokumen. Default: false (toolbar ditampilkan).
- HideWindowUI – Sembunyikan atau tampilkan elemen jendela dokumen seperti bilah gulir. Default: false (elemen UI ditampilkan).
- NonFullScreenPageMode – Bagaimana dokumen ketika tidak ditampilkan dalam mode halaman penuh.
- PageLayout – Tata letak halaman.
- PageMode – Bagaimana dokumen ditampilkan saat pertama kali dibuka. Pilihannya adalah tampilkan thumbnail, layar penuh, tampilkan panel lampiran.

Potongan kode berikut menunjukkan cara Anda mendapatkan properti menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas.

```python
import aspose.pdf as ap


def get_document_window(input_pdf, output_pdf):
    """Print document window metadata for inspection."""
    document = ap.Document(input_pdf)

    print("CenterWindow:", document.center_window)
    print("Direction:", document.direction)
    print("DisplayDocTitle:", document.display_doc_title)
    print("FitWindow:", document.fit_window)
    print("HideMenuBar:", document.hide_menubar)
    print("HideToolBar:", document.hide_tool_bar)
    print("HideWindowUI:", document.hide_window_ui)
    print("NonFullScreenPageMode:", document.non_full_screen_page_mode)
    print("PageLayout:", document.page_layout)
    print("PageMode:", document.page_mode)
```

### Atur Jendela Dokumen dan Properti Tampilan Halaman

Topik ini menjelaskan cara mengatur properti jendela dokumen, aplikasi penampil, dan tampilan halaman. Untuk mengatur properti yang berbeda ini:

1. Buka file PDF menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas.
1. Atur properti objek Document.
1. Simpan file PDF yang diperbarui menggunakan metode save.

Properti yang tersedia adalah:

- TengahJendela
- Arah
- TampilkanJudulDokumen
- Sesuaikan Jendela
- SembunyikanBilahMenu
- SembunyikanToolbar
- Sembunyikan UI Jendela
- ModeHalamanNonLayarPenuh
- Tata Letak Halaman
- ModeHalaman

Setiapnya digunakan dan dijelaskan dalam kode di bawah ini. Potongan kode berikut - menunjukkan cara mengatur properti menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas.

```python
import aspose.pdf as ap


def set_document_window(input_pdf, output_pdf):
    """Set document window properties and save the result."""
    document = ap.Document(input_pdf)

    document.center_window = True
    document.direction = ap.Direction.R2L
    document.display_doc_title = True
    document.fit_window = True
    document.hide_menubar = True
    document.hide_tool_bar = True
    document.hide_window_ui = True
    document.non_full_screen_page_mode = ap.PageMode.USE_OC
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT
    document.page_mode = ap.PageMode.USE_THUMBS

    document.save(output_pdf)
```

### Menyematkan Font Tipe 1 Standar

Beberapa dokumen PDF memiliki font dari satu set font khusus Adobe. Font dari set ini disebut “Standard Type 1 Fonts”. Set ini mencakup 14 font dan menyisipkan jenis font ini memerlukan penggunaan flag khusus yaitu [sematkan_font_standar](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). Berikut ini adalah potongan kode yang dapat digunakan untuk mendapatkan dokumen dengan semua font tersemat termasuk Standard Type 1 Fonts:

```python
import aspose.pdf as ap


def embedded_fonts(input_pdf, output_pdf):
    """Ensure fonts in an existing PDF are embedded."""
    document = ap.Document(input_pdf)
    document.embed_standard_fonts = True

    for page in document.pages:
        if page.resources.fonts:
            for page_font in page.resources.fonts:
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Menyematkan Font saat membuat PDF

Jika Anda perlu menggunakan font apa pun selain 14 font inti yang didukung oleh Adobe Reader, Anda harus menyematkan deskripsi font saat menghasilkan file PDF. Jika informasi font tidak disematkan, Adobe Reader akan mengambilnya dari Sistem Operasi jika font tersebut terpasang di sistem, atau akan membuat font pengganti sesuai dengan deskriptor font dalam PDF.

>Harap catat bahwa font yang disematkan harus diinstal pada mesin host, yaitu dalam kasus kode berikut ‘Univers Condensed’ font diinstal pada sistem.

Kami menggunakan properti 'is_embedded' untuk menyematkan informasi font ke dalam file PDF. Menetapkan nilai properti ini ke 'True' akan menyematkan file font lengkap ke dalam PDF, dengan menyadari fakta bahwa hal itu akan meningkatkan ukuran file PDF. Berikut ini cuplikan kode yang dapat digunakan untuk menyematkan informasi font ke dalam PDF.

```python
import aspose.pdf as ap


def embedded_fonts_in_new_document(input_pdf, output_pdf):
    """Embed fonts while generating a document from scratch."""
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    text_state = ap.text.TextState()
    text_state.font = ap.text.FontRepository.find_font("Arial")
    text_state.font.is_embedded = True
    segment.text_state = text_state
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    document.save(output_pdf)
```

### Atur Nama Font Default saat Menyimpan PDF

Ketika dokumen PDF berisi font yang tidak tersedia dalam dokumen itu sendiri maupun di perangkat, API menggantikan font tersebut dengan font default. Jika font tersedia (terpasang di perangkat atau disematkan ke dalam dokumen), PDF output harus menggunakan font yang sama (tidak boleh diganti dengan font default). Nilai font default harus berisi nama font (bukan jalur ke file font). Kami telah mengimplementasikan fitur untuk mengatur nama font default saat menyimpan dokumen sebagai PDF. Potongan kode berikut dapat digunakan untuk mengatur font default:

```python
import aspose.pdf as ap


def set_default_font(input_pdf, output_pdf):
    """Assign a fallback font when saving a PDF."""
    document = ap.Document(input_pdf)

    save_options = ap.PdfSaveOptions()
    save_options.default_font_name = "Arial"
    document.save(output_pdf, save_options)
```

### Dapatkan Semua Font dari Dokumen PDF

Jika Anda ingin mendapatkan semua font dari sebuah dokumen PDF, Anda dapat menggunakan [utilitas_font](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) metode yang disediakan dalam [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas. Silakan periksa cuplikan kode berikut untuk mendapatkan semua font dari dokumen PDF yang ada:

```python
import aspose.pdf as ap


def get_all_fonts(input_pdf, output_pdf):
    """Print all fonts referenced by a document."""
    document = ap.Document(input_pdf)
    for font in document.font_utilities.get_all_fonts():
        print(font.font_name)
```

### Tingkatkan Penyematan Font menggunakan FontSubsetStrategy

Snippet kode berikut menunjukkan cara mengatur [Strategi Subset Font](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) digunakan [utilitas_font](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) properti:

```python
import aspose.pdf as ap


def improve_fonts_embedding(input_pdf, output_pdf):
    """Apply different font subset strategies to reduce file size."""
    document = ap.Document(input_pdf)

    document.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    document.font_utilities.subset_fonts(
        ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY
    )

    document.save(output_pdf)
```

### Dapatkan-Setel Faktor Zoom File PDF

Kadang-kadang, Anda ingin menentukan faktor zoom saat ini dari sebuah dokumen PDF. Dengan Aspose.Pdf, Anda dapat mengetahui nilai saat ini serta menetapkan satu nilai baru.

The [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) properti Destination kelas memungkinkan Anda untuk mendapatkan nilai zoom yang terkait dengan file PDF. Demikian pula, dapat digunakan untuk mengatur faktor zoom sebuah file.

#### Atur faktor zoom

Potongan kode berikut menunjukkan cara mengatur faktor zoom sebuah file PDF.

```python
import aspose.pdf as ap


def set_zoom_factor(input_pdf, output_pdf):
    """Set an initial zoom level via document open action."""
    document = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(
        ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5)
    )
    document.open_action = action
    document.save(output_pdf)
```

#### Dapatkan Faktor Zoom

Potongan kode berikut menunjukkan cara mendapatkan faktor zoom file PDF.

```python
import aspose.pdf as ap


def get_zoom_factor(input_pdf, output_pdf):
    """Print the zoom level configured in the document open action."""
    document = ap.Document(input_pdf)

    action = document.open_action
    if action and action.destination:
        print("Zoom:", action.destination.zoom)
    else:
        print("Zoom: not set")
```

## Topik Dokumen Terkait

- [Bekerja dengan dokumen PDF di Python](/pdf/id/python-net/working-with-documents/)
- [Buat file PDF di Python](/pdf/id/python-net/create-pdf-document/)
- [Manipulasi dokumen PDF dalam Python](/pdf/id/python-net/manipulate-pdf-document/)
- [Optimalkan file PDF dalam Python](/pdf/id/python-net/optimize-pdf/)
