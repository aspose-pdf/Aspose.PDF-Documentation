---
title: Ganti Teks dalam PDF dengan Python
linktitle: Ganti Teks dalam PDF
type: docs
weight: 40
url: /id/python-net/replace-text-in-pdf/
description: Pelajari cara mengganti teks dalam file PDF dengan Python, termasuk mengganti teks di seluruh halaman, membatasi perubahan pada wilayah halaman, menggunakan regex, dan menghapus teks.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Ganti dan hapus teks dalam file PDF menggunakan Python
Abstract: Artikel ini menunjukkan cara mengganti teks dalam dokumen PDF dengan Aspose.PDF for Python via .NET. Artikel ini mencakup penggantian teks di semua halaman, penggantian wilayah halaman, pencocokan regex, penggantian font, penyesuaian tata letak teks, dan menghapus teks yang terlihat atau tersembunyi.
---

Halaman ini menunjukkan bagaimana cara **mengganti teks dalam PDF dengan Python** menggunakan Aspose.PDF for Python via .NET.

Gunakan contoh-contoh ini ketika Anda perlu memperbarui nilai teks, menghapus konten yang tidak diinginkan, mengganti teks di area halaman tertentu, atau menerapkan aturan penggantian teks di beberapa halaman PDF.

## Ganti Teks dalam PDF dengan Python

### Ganti Teks di Semua Halaman Dokumen PDF

{{% alert color="primary" %}}

Anda dapat mencoba pencarian dan penggantian teks secara online dengan Aspose.PDF [aplikasi redaksi](https://products.aspose.app/pdf/redaction).

{{% /alert %}}

Penggantian teks merupakan kebutuhan umum saat memperbarui atau memperbaiki konten dalam dokumen PDF yang ada — misalnya, mengubah nama produk, memperbaiki typo, atau memperbarui terminologi di beberapa halaman.

Aspose.PDF for Python via .NET menawarkan metode yang kuat dan efisien untuk mencari dan mengganti teks secara programatis melalui [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) kelas.

Contoh ini menunjukkan cara menemukan semua kemunculan suatu frasa tertentu (dalam hal ini, "Black cat") dan menggantinya dengan frasa baru ("White dog") di seluruh dokumen PDF.

1. Tentukan Frasa Pencarian dan Penggantian. Atur teks yang ingin Anda temukan dan teks yang ingin diganti.
1. Muat Dokumen PDF.
1. Buat sebuah Text Absorber. Sebuah TextFragmentAbsorber diinisialisasi dengan frasa pencarian. Ia memindai dokumen untuk semua kemunculan frasa yang diberikan.
1. Terapkan Absorber ke Semua Halaman. Ini mengulangi semua halaman dan mengumpulkan fragmen teks yang cocok dengan frasa.
1. Ganti setiap fragmen yang ditemukan. Setiap kemunculan "Black cat" harus diubah menjadi "White dog".
1. Simpan PDF yang Diperbarui.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_on_all_pages(infile, outfile):
    search_phrase = "PDF"
    replace_phrase = "pdf"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Ganti Teks pada Wilayah Halaman Tertentu

Kadang-kadang, Anda mungkin perlu mengganti teks hanya dalam area tertentu dari halaman PDF alih-alih mencari seluruh dokumen — misalnya, memperbarui header, footer, atau sel tabel di dalam posisi yang diketahui.

Perpustakaan Aspose.PDF for Python via .NET memungkinkan fungsionalitas ini dengan memanfaatkan [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) bersamaan dengan pencarian teks berbasis wilayah.

Contoh ini menunjukkan cara menemukan dan mengganti semua kemunculan frasa target dalam wilayah persegi panjang yang ditentukan pada halaman tertentu.

1. Tentukan Frasa Pencarian dan Penggantian.
1. Muat Dokumen PDF.
1. Buat Text Absorber untuk Pencarian. Inisialisasi TextFragmentAbsorber untuk menemukan teks yang diinginkan.
1. Batasi Area Pencarian. Persegi panjang menentukan batas koordinat x dan y pada halaman.
1. Terapkan Absorber pada Halaman Tertentu. Ini melakukan pencarian dan mengumpulkan potongan teks yang cocok dalam area yang ditentukan.
1. Ganti Teks yang Ditemukan. Setiap kemunculan 'doc' dalam wilayah yang ditentukan menjadi 'DOC'.
1. Simpan PDF yang Diperbarui.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_in_particular_page_region(infile, outfile):
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Ubah Ukuran dan Pindahkan Teks Tanpa Mengubah Ukuran Font

Saat mengganti teks dalam PDF, kadang Anda ingin menyesuaikan atau memposisikan kembali teks baru dalam area tertentu tanpa mengubah ukuran font.
Aspose.PDF for Python via .NET menyediakan opsi untuk menyesuaikan tata letak teks dan spasi sambil menjaga ukuran font asli tetap utuh.

1. Muat Dokumen PDF.
1. Kumpulkan semua fragmen teks pada halaman menggunakan 'TextFragmentAbsorber'.
1. Pilih Fragmen untuk Dimodifikasi.
1. Geser dan ubah ukuran persegi panjang teks.
1. Sesuaikan Jarak Teks. Aktifkan penyesuaian jarak agar teks muat di dalam persegi panjang yang dimodifikasi.
1. Ganti teks fragmen.
1. Simpan PDF yang Diperbarui.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Ubah Ukuran dan Pindahkan Sebuah Paragraf dalam PDF

Saat bekerja dengan PDF, terkadang Anda perlu mengganti atau memperluas sebuah paragraf sambil tetap mempertahankan keselarasan visual dengan tata letak halaman. Aspose.PDF memungkinkan Anda mengubah ukuran persegi panjang pembatas paragraf dan menyesuaikan spasi agar sesuai dengan teks baru, semuanya tanpa mengubah ukuran font.

1. Muat Dokumen PDF.
1. Gunakan 'TextFragmentAbsorber' untuk mengumpulkan semua fragmen teks pada halaman.
1. Pilih Fragmen untuk Dimodifikasi.
1. Ubah ukuran dan geser paragraf. Gunakan kotak media halaman untuk menentukan batas dan sesuaikan persegi panjang.
1. Sesuaikan Spasi. Ini mengubah spasi antara kata/huruf alih-alih mengubah ukuran font.
1. Ganti teks fragmen.
1. Simpan PDF yang Dimodifikasi.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Ganti Teks dan Secara Otomatis Perluas Font untuk Mengisi Area Target

Ganti teks dalam PDF sambil secara otomatis mengubah ukuran dan memperluas font untuk mengisi area persegi panjang tertentu. Dengan menggunakan perpustakaan Aspose.PDF for Python via .NET, kode secara dinamis menyesuaikan ukuran font dan jarak spasi sehingga konten teks baru secara sempurna cocok dalam kotak pembatas yang telah ditentukan — tanpa perhitungan font manual.

1. Muat PDF.
1. Tangkap Fragmen Teks.
1. Pilih Fragmen Spesifik.
1. Definisikan Persegi Panjang Target.
1. Aktifkan Opsi Penyesuaian Teks.
1. Ganti Teks.
1. Simpan Dokumen.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_expand_font(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Ganti Teks dan Sesuaikan ke dalam Persegi Panjang

Ganti teks dalam dokumen PDF sambil memastikan konten baru sesuai dengan area persegi panjang teks asli dengan secara otomatis mengurangi ukuran font bila diperlukan.

Dengan menggunakan pustaka Aspose.PDF for Python via .NET, fungsi ini menyesuaikan tata letak teks dan ukuran Font secara dinamis, mempertahankan struktur dokumen sambil mencegah overflow.

1. Buat objek TextFragmentAbsorber untuk mengekstrak semua fragmen teks dari halaman pertama.
1. Akses Fragmen Teks Spesifik.
1. Atur Area Penggantian.
1. Konfigurasikan Opsi Penyesuaian Teks. Atur dua opsi penggantian kunci:
    - Penyesuaian ukuran font - 'SHRINK_TO_FIT' secara otomatis mengurangi ukuran font jika teks baru terlalu panjang.
    - Penyesuaian spasi - 'ADJUST_SPACE_WIDTH' menjaga spasi proporsional.
1. Ganti Teks.
1. Simpan PDF yang Dimodifikasi.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Secara Otomatis Ganti Teks Placeholder dan Atur Ulang Tata Letak PDF

Ganti teks placeholder di dalam PDF (mis., templat atau formulir) dengan data aktual seperti nama atau informasi perusahaan.
Secara otomatis menyesuaikan tata letak halaman untuk menampung teks baru sambil menerapkan pemformatan khusus (font, warna, ukuran).

1. Impor dan Muat PDF.
1. Buat Text Absorber untuk Placeholder.
1. Terapkan Absorber ke Semua Halaman.
1. Lakukan loop melalui Fragmen Teks yang Ditemukan.
1. Terapkan Pemformatan Teks Kustom.
1. Simpan Dokumen yang Diperbarui.

```python
import sys
import aspose.pdf as ap
from os import path

def automatically_rearrange_page_contents(input_file, output_file):
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### Ganti Teks Berdasarkan Ekspresi Reguler

Saat bekerja dengan dokumen PDF, Anda mungkin perlu mengganti teks yang mengikuti pola daripada frasa tertentu — misalnya, nomor telepon, kode, atau format mirip tanggal.

Aspose.PDF for Python via .NET memungkinkan Anda melakukan penggantian semacam itu menggunakan ekspresi reguler (regex) dengan kelas TextFragmentAbsorber.

Contoh ini menunjukkan cara menemukan pola teks (dalam hal ini, teks apa pun yang sesuai dengan format ####-####, seperti 1234-5678) dan menggantinya dengan string terformat 'ABC1-2XZY'. Ini juga memperlihatkan cara menyesuaikan font, warna, dan ukuran teks yang diganti.

Potongan kode berikut menunjukkan cara mengganti teks berdasarkan ekspresi reguler.

1. Muat Dokumen PDF.
1. Buat TextAbsorber berbasis Regex. Inisialisasi TextFragmentAbsorber dengan pola ekspresi reguler.
1. Aktifkan Mode Ekspresi Reguler. Parameter \u0027True\u0027 mengaktifkan mode pencarian ekspresi reguler.
1. Terapkan Absorber pada Halaman. Ini memindai halaman untuk semua fragmen teks yang cocok dengan pola regex yang ditentukan.
1. Ganti setiap kecocokan dengan teks baru dan terapkan gaya khusus.
1. Simpan Dokumen yang Dimodifikasi.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_based_on_regex(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## Ganti font atau hapus font yang tidak terpakai

### Ganti font di file PDF yang ada

Terkadang, Anda perlu menstandarisasi atau memperbarui font di seluruh PDF — misalnya, mengganti font yang usang atau bersifat proprietary dengan yang lebih mudah diakses. Perpustakaan Aspose.PDF for Python via .NET memungkinkan Anda mendeteksi dan mengganti font secara programatis, memastikan tipografi yang konsisten dan kompatibilitas dokumen.

Contoh ini menunjukkan cara mengganti semua instance dari font tertentu (misalnya, 'Arial-BoldMT') dengan font lain (misalnya, 'Verdana') di seluruh dokumen PDF.

Potongan kode berikut menunjukkan cara mengganti font di dalam dokumen PDF:

1. Buka Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber.
1. Gunakan Absorber untuk mengekstrak fragmen teks dari setiap halaman dalam dokumen.
1. Identifikasi dan Ganti Font. Skrip memeriksa apakah font saat ini dari fragmen adalah 'Arial-BoldMT'. Jika benar, ia menggantinya dengan font 'Verdana' menggunakan metode FontRepository.find_font().
1. Simpan Dokumen yang Dimodifikasi.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_fonts(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### Hapus font yang tidak digunakan

Seiring waktu, dokumen PDF dapat menumpuk font yang tidak digunakan atau tersemat yang meningkatkan ukuran file dan memperlambat pemrosesan. Font yang tidak digunakan ini sering tetap ada bahkan setelah pengeditan atau penggantian teks, terutama saat bekerja dengan PDF yang besar atau kompleks.

Pustaka Aspose.PDF for Python via .NET menyediakan cara yang efisien untuk menghapus font berlebih tersebut menggunakan kelas TextEditOptions. Ini tidak hanya mengoptimalkan dokumen Anda tetapi juga memastikan hanya font yang sebenarnya diterapkan pada teks yang terlihat yang digunakan.

Metode 'remove_unused_fonts()' adalah cara yang sederhana namun kuat untuk mengoptimalkan file PDF dengan menghapus data font yang berlebihan.

Contoh ini menunjukkan cara:

- Pindai PDF untuk font yang tidak terpakai.
- Hapus mereka dengan aman.
- Tetapkan kembali fragmen teks aktif ke font yang konsisten (mis., Times New Roman).

1. Buka Dokumen PDF.
1. Konfigurasikan Opsi Penyuntingan Teks. Ini memberi instruksi kepada mesin untuk menghapus semua font yang disematkan yang tidak sedang digunakan dalam teks yang terlihat.
1. Buat Text Absorber dengan Options. TextFragmentAbsorber mengekstrak fragmen teks dari dokumen untuk diedit.
1. Tugaskan ulang Font Standar. Setelah absorber mengumpulkan semua fragmen, iterasi melalui mereka dan terapkan font yang konsisten.
1. Simpan PDF yang sudah dibersihkan.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_unused_fonts(input_file, output_file):
    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(
        ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS
    )

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )

    # Save the updated PDF document
    document.save(output_file)
```

## Hapus semua Teks

### Hapus Teks dari PDF

Hapus semua konten teks dari file PDF sambil mempertahankan gambar, bentuk, dan struktur tata letak tetap.
Dengan menggunakan TextFragmentAbsorber, kode secara efisien memindai seluruh dokumen dan menghapus setiap fragmen teks yang ditemukan pada setiap halaman.

1. Muat Dokumen PDF.
1. Objek TextFragmentAbsorber dibuat untuk mendeteksi dan menangani fragmen teks dalam PDF.
1. Hapus Semua Konten Teks. Metode 'absorber.remove_all_text()' menghapus setiap elemen teks dari dokumen yang dimuat, sementara komponen non-teks tetap tidak tersentuh.
1. Simpan Dokumen yang Diperbarui.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber1(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### Hapus semua Teks dari Halaman Tertentu

Hapus semua teks dari satu halaman dokumen PDF menggunakan kelas TextFragmentAbsorber di Aspose.PDF.
Berbeda dengan penghapusan seluruh dokumen, metode ini melakukan pembersihan teks tingkat halaman, menghapus teks hanya dari halaman yang dipilih sementara semua halaman lain tetap tidak tersentuh.

1. Muat File PDF.
1. Buat Instance TextFragmentAbsorber.
1. Hapus Semua Teks dari Halaman Pertama.
1. Simpan PDF yang Dimodifikasi.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber2(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### Hapus semua teks dari area tertentu pada halaman PDF

Hapus semua teks dari area persegi panjang tertentu pada halaman menggunakan TextFragmentAbsorber Aspose.PDF.
Alih-alih menghapus seluruh halaman, metode ini melakukan penghapusan teks yang ditargetkan, memungkinkan kontrol yang tepat atas bagian halaman yang terpengaruh.

1. Muat Dokumen PDF.
1. Buat sebuah TextFragmentAbsorber.
1. Tentukan Area Target (Persegi Panjang).
1. Hapus Teks dari Wilayah yang Ditentukan.
1. Pertahankan Sisa Dokumen.
1. Simpan PDF yang Dimodifikasi.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber3(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(
            document.pages[1], ap.Rectangle(10, 200, 120, 600, True)
        )
        document.save(outfile)
```

### Hapus semua Teks tersembunyi dari dokumen PDF

Hapus semua teks dari area persegi panjang tertentu pada halaman menggunakan TextFragmentAbsorber Aspose.PDF.
Alih-alih menghapus seluruh halaman, metode ini melakukan penghapusan teks yang ditargetkan, memungkinkan kontrol yang tepat atas bagian halaman yang terpengaruh.

1. Muat Dokumen PDF.
1. Buat sebuah TextFragmentAbsorber.
1. Tentukan Area Target (Persegi Panjang).
1. Hapus Teks dari Wilayah yang Ditentukan.
1. Pertahankan Sisa Dokumen.
1. Simpan PDF yang Dimodifikasi.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_hidden_text(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(
            ap.text.TextReplaceOptions.ReplaceAdjustment.NONE
        )
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```

## Topik Teks Terkait

- [Bekerja dengan teks dalam PDF menggunakan Python](/pdf/id/python-net/working-with-text/)
- [Menambahkan teks ke PDF](/pdf/id/python-net/add-text-to-pdf-file/)
- [Cari dan ekstrak teks PDF di Python](/pdf/id/python-net/search-and-get-text-from-pdf/)
- [Format teks PDF di Python](/pdf/id/python-net/text-formatting-inside-pdf/)
