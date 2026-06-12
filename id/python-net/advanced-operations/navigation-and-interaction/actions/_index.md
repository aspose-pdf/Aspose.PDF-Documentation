---
title: Bekerja dengan Aksi PDF di Python
linktitle: Aksi
type: docs
weight: 20
url: /id/python-net/actions/
description: Pelajari cara menambahkan, memperbarui, dan menghapus tindakan dokumen, halaman, dan formulir dalam file PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Tambahkan tindakan dokumen, halaman, dan formulir ke file PDF dalam Python.
Abstract: Artikel ini membahas cara bekerja dengan tindakan dalam dokumen PDF menggunakan pustaka Aspose.PDF, mencakup interaksi tingkat dokumen, tingkat halaman, dan tingkat formulir. Tindakan PDF adalah pemicu yang telah ditentukan atau dapat disesuaikan yang merespons peristiwa pengguna, memungkinkan navigasi, eksekusi JavaScript, pemutaran multimedia, pengiriman formulir, dan lainnya. Panduan ini menunjukkan cara menambah, menyesuaikan, dan menghapus tindakan, seperti membuka URL pada peristiwa dokumen, membuat navigasi atau efek zoom khusus halaman, menambahkan tombol interaktif untuk mencetak dan menavigasi, menyembunyikan elemen formulir secara dinamis, dan mengirim data formulir ke endpoint web. Melalui contoh kode Python yang detail, pembaca belajar meningkatkan interaktivitas PDF, menyederhanakan alur kerja, dan mengintegrasikan PDF dengan sistem eksternal sambil memahami pertimbangan kompatibilitas penampil.
---

Aksi dalam PDF adalah tugas yang telah ditentukan sebelumnya yang dipicu oleh interaksi pengguna atau peristiwa dokumen. Mereka dapat digunakan untuk:

- Arahkan ke halaman tertentu atau file eksternal
- Buka tautan web
- Putar konten multimedia
- Jalankan JavaScript
- Kirim atau reset formulir
- Tampilkan/sembunyikan bidang
- Ubah tingkat zoom atau mode tampilan

Hampir semua tindakan menggunakan parameter bawaan tetapi ada beberapa yang dapat disesuaikan. Misalnya - Tindakan JavaScript.

## Tambahkan Tindakan Peluncuran PDF

Tambahkan aksi peluncuran berbasis JavaScript ke dokumen PDF menggunakan Python dan Aspose.PDF. Ini menetapkan aksi ke peristiwa dokumen utama seperti membuka, menyimpan, dan mencetak, memungkinkan URL diluncurkan secara otomatis ketika peristiwa tersebut terjadi pada penampil PDF yang mendukung.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_launch_actions(infile, outfile):
    """Add JavaScript launch actions for document events.

    Adds JavaScript actions that launch URLs when specific document events occur:
    - On document open: launches http://localhost:3000/open
    - Before saving: launches http://localhost:3000/save
    - Before printing: launches http://localhost:3000/print

    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to save the output PDF with document actions.

    Returns:
        None

    Example:
        >>> add_launch_actions("sample_data/input/add_launch_actions_in.pdf", "sample_data/output/add_launch_actions_out.pdf")

    Notes:
        - Uses `ap.annotations.JavascriptAction` with `app.launchURL()`.
        - URLs are opened in the default browser depending on viewer support.
    """

    document = ap.Document(infile)

    # Add JavaScript actions for document events
    document.open_action = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/open');"
    )
    document.actions.before_saving = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/save');"
    )
    document.actions.before_printing = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/print');"
    )

    document.save(outfile)
```

## Menghapus Tindakan dari Dokumen PDF

Untuk membersihkan (atau menghapus) tindakan cukup atur handler ke `None`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def remove_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]
    page.actions.remove_actions()

    document.save(outfile)
```

## Menambahkan Aksi ke halaman dalam Dokumen PDF

Pemicu serupa disediakan untuk halaman: `on_open`, `on_close`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]

    # Add GoTo action on page open - navigate to top of page
    action = ap.annotations.GoToAction(page)
    action.destination = ap.annotations.XYZExplicitDestination(
        page, 0, page.page_info.height, 1
    )
    page.actions.on_open = action

    # Add JavaScript action on page close
    page.actions.on_close = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/page/3');"
    )

    document.save(outfile)
```

## Aksi dalam AcroForms

### Menggunakan tindakan navigasi

Standar PDF menyediakan serangkaian aksi bernama tertentu. Makna dari aksi-aksi tersebut ditentukan oleh namanya.
Dalam kode berikut, kami akan menggunakan aksi untuk navigasi.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_navigation_buttons(infile, outfile):
    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Add navigation buttons to each page
    for page in document.pages:
        for name, x_pos, action, is_readonly_fn in button_config:
            # Create button rectangle
            rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            # Disable button when not applicable
            button.read_only = is_readonly_fn(page.number, total_pages)
            button.actions.on_release_mouse_btn = NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

Kode ini menambahkan tombol navigasi ke setiap halaman dokumen PDF, memudahkan pengguna untuk berpindah antar halaman. Ia dimulai dengan menentukan jalur file lengkap untuk file input dan output menggunakan metode pembantu. Daftar button_config mendefinisikan empat jenis tombol navigasi—First Page, Previous Page, Next Page, dan Last Page—beserta posisi horizontalnya, aksi navigasi yang sudah ditetapkan yang mereka panggil, dan fungsi lambda yang menentukan apakah setiap tombol harus dalam mode read-only pada halaman tertentu (misalnya, tombol “First Page” dan “Previous Page” bersifat read-only pada halaman pertama).

Kode kemudian memuat PDF dan mengiterasi setiap halaman. Untuk setiap halaman, ia mengulang konfigurasi tombol, membuat area persegi panjang untuk setiap tombol dan menginstansiasi sebuah ButtonField di lokasi tersebut. Setiap tombol diberikan nama, status hanya-baca diatur berdasarkan halaman saat ini, dan tindakan kliknya ditetapkan ke tindakan navigasi yang sesuai. Tombol tersebut kemudian ditambahkan ke bidang formulir PDF.

Setelah semua tombol ditambahkan ke semua halaman, dokumen yang dimodifikasi disimpan. Jika ada kesalahan yang terjadi selama proses ini, kesalahan tersebut ditangkap dan dicetak. Pendekatan ini memastikan bahwa setiap halaman memiliki serangkaian kontrol navigasi yang konsisten, meningkatkan kegunaan PDF multi‑halaman. Salah satu hal halus adalah penggunaan lambda is_readonly_fn untuk menonaktifkan tombol navigasi ketika mereka tidak masuk akal (misalnya, "Next Page" pada halaman terakhir), yang membantu mencegah kebingungan pengguna.

### Menggunakan aksi cetak

Saat menggunakan formulir PDF, sering kali diperlukan untuk mencetak dokumen PDF tersebut. Tindakan ini dapat dilakukan menggunakan PDF Reader, tetapi kadang-kadang lebih nyaman melakukannya langsung dari dokumen menggunakan tombol khusus.

Sebenarnya, ini adalah contoh lain lagi tentang cara menggunakan aksi bernama. Kami akan menggunakan `PredefinedAction.FILE_PRINT` (mensimulasikan penggunaan menu File‑>Print), namun Anda juga dapat menggunakan `PredefinedAction.PRINT` atau `PredefinedAction.PRINT_DIALOG`, tergantung pada tujuan Anda sendiri.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_print(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    # Create print button with specific dimensions and position
    rect = Rectangle(10, 10, 100, 40, True)
    print_button = ButtonField(page, rect)
    print_button.partial_name = "printButton"
    print_button.value = "Print"
    print_button.actions.on_release_mouse_btn = NamedAction(PredefinedAction.FILE_PRINT)

    # Add border for better visibility
    border = ap.annotations.Border(print_button)
    border.width = 1
    print_button.border = border

    # Add button to the form on page 1
    document.form.add(print_button, 1)
    document.save(outfile)
```

Potongan kode ini menunjukkan cara menambahkan tombol "Print" ke halaman pertama dokumen PDF. Ia dimulai dengan memuat PDF dari jalur file input yang ditentukan dan memilih halaman pertama (document.pages[1]).

Area persegi panjang didefinisikan untuk posisi dan ukuran tombol pada halaman. ButtonField kemudian dibuat di lokasi ini, diberi nama "printButton," dan nilai tampilanannya diatur menjadi "Print." Tombol tersebut dikonfigurasi sehingga ketika diklik (khususnya, saat tombol mouse dilepaskan), ia memicu aksi "Print File" yang telah ditentukan sebelumnya, memunculkan dialog cetak pada penampil PDF.

Untuk meningkatkan tampilan tombol, sebuah border dibuat dan diberikan ke tombol, dengan lebar disetel menjadi 1 unit. Tombol kemudian ditambahkan ke bidang formulir PDF pada halaman pertama. Akhirnya, dokumen yang telah dimodifikasi disimpan ke jalur file output. Pendekatan ini menyediakan cara yang mudah bagi pengguna untuk mencetak dokumen langsung dari dalam PDF. Perhatikan bahwa efektivitas fitur ini bergantung pada dukungan penampil PDF terhadap bidang formulir interaktif dan tindakan yang telah ditentukan sebelumnya.

### Menggunakan aksi Sembunyikan

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_hide(infile, outfile):
    document = ap.Document(infile)
    # Collect all checkbox fields in the document
    checkboxes = [
        field for field in document.form if is_assignable(field, CheckboxField)
    ]

    # Create the hide button
    rect = Rectangle(10, 410, 140, 440, True)
    hide_button = ButtonField(document.pages[1], rect)
    hide_button.partial_name = "HideButton"
    hide_button.value = "Hide Checkboxes"

    # Add HideAction to button - will hide all checkboxes when clicked
    hide_button.actions.on_release_mouse_btn = HideAction(checkboxes, True)

    # Add button to the form on page 1
    document.form.add(hide_button, 1)

    # Save the modified PDF
    document.save(outfile)
```

Potongan kode ini menambahkan tombol ke halaman pertama PDF yang, saat diklik, menyembunyikan semua bidang kotak centang dalam dokumen. Ini dimulai dengan menyelesaikan jalur file input dan output lengkap menggunakan metode pembantu. PDF dimuat, dan semua bidang kotak centang dikumpulkan dengan memfilter bidang formulir untuk instance dari `ap.CheckboxField`.

Sebuah area persegi panjang didefinisikan untuk posisi tombol baru di dekat bagian atas halaman. Sebuah ButtonField dibuat pada lokasi ini, bernama “HideButton,” dan berlabel “Hide Checkboxes.” Tombol tersebut dikonfigurasi sehingga ketika diklik (pada pelepasan tombol mouse), ia memicu HideAction yang menyembunyikan semua kotak centang yang dikumpulkan.

Tombol kemudian ditambahkan ke bidang formulir pada halaman pertama, dan PDF yang dimodifikasi disimpan ke file output. Jika ada kesalahan yang terjadi selama proses ini, kesalahan tersebut ditangkap dan dicetak. Fitur ini memberikan pengguna cara cepat untuk menyembunyikan semua kotak centang di PDF, yang dapat berguna untuk menyesuaikan tampilan atau alur kerja dokumen.

### Menerapkan Aksi Kirim

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_submit_action(infile, outfile):
    document = ap.Document(infile)

    # Create the submit action
    submit_action = SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
    )

    # Create the submit button
    rect = Rectangle(10, 10, 100, 40, True)
    submit_button = ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    # Add the button to the form on page 1
    document.form.add(submit_button, 1)

    # Save the document
    document.save(outfile)
```

Fungsi ini menambahkan tombol "Submit" ke halaman pertama dari formulir PDF, memungkinkan pengguna mengirim data formulir ke endpoint web yang ditentukan. Fungsi ini dimulai dengan membuat jalur lengkap untuk file PDF input dan output, kemudian memuat PDF input menggunakan perpustakaan Aspose.PDF.

A `SubmitFormAction` dibuat untuk menentukan perilaku ketika tombol diklik. url aksi disetel menggunakan a `FileSpecification` menunjuk ke http://localhost:3000/submit, yang berarti data formulir akan dikirim ke URL ini. Properti flags menggabungkan `EXPORT_FORMAT` dan `SUBMIT_COORDINATES`, memastikan bahwa data formulir diekspor dalam format standar dan bahwa koordinat klik tombol disertakan dalam pengajuan.

Sebuah area persegi panjang didefinisikan untuk posisi dan ukuran tombol pada halaman. Sebuah ButtonField dibuat di lokasi ini pada halaman pertama, diberikan nama "SubmitButton," dan nilai tampilannya diatur ke "Submit." Aksi submit ditetapkan pada acara pelepasan mouse tombol, sehingga aksi tersebut dipicu ketika pengguna mengklik tombol.

Akhirnya, tombol ditambahkan ke bidang formulir pada halaman pertama, dan PDF yang dimodifikasi disimpan ke file output. Jika ada kesalahan yang terjadi selama proses ini, kesalahan tersebut ditangkap dan dicetak. Pendekatan ini menyediakan cara yang ramah pengguna bagi pengguna PDF untuk mengirim data formulir langsung ke endpoint server.

## Topik Navigasi Terkait

- [Navigasi dan interaksi dalam PDF menggunakan Python](/pdf/id/python-net/navigation-and-interaction/)
- [Bekerja dengan penanda buku di PDF menggunakan Python](/pdf/id/python-net/bookmarks/)
- [Bekerja dengan tautan dalam PDF menggunakan Python](/pdf/id/python-net/links/)
