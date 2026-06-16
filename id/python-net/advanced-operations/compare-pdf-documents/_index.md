---
title: Bandingkan Dokumen PDF di Python
linktitle: Bandingkan PDF
type: docs
weight: 130
url: /id/python-net/compare-pdf-documents/
description: Pelajari cara membandingkan dokumen PDF di Python menggunakan perbandingan berdampingan dan output perbedaan grafis dengan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bandingkan halaman PDF dan dokumen lengkap dengan output perbedaan visual di Python
Abstract: Artikel ini menjelaskan cara membandingkan dokumen PDF dalam Aspose.PDF for Python via .NET. Pelajari cara membandingkan halaman tertentu atau seluruh file PDF dengan output berdampingan, serta cara menggunakan metode perbandingan grafis untuk menghasilkan laporan perbedaan berbasis gambar atau berbasis PDF.
---

## Cara Membandingkan Dokumen PDF

Saat bekerja dengan dokumen PDF, ada kalanya Anda perlu membandingkan isi dua dokumen untuk mengidentifikasi perbedaan. Perpustakaan Aspose.PDF for Python via .NET menyediakan rangkaian alat yang kuat untuk tujuan ini. Dalam artikel ini, kami akan mengeksplorasi cara membandingkan dokumen PDF menggunakan beberapa potongan kode sederhana.

Gunakan perbandingan berdampingan ketika Anda menginginkan output PDF yang menyoroti perubahan teks dan tata letak antar halaman. Gunakan perbandingan grafis ketika Anda memerlukan deteksi perbedaan berbasis gambar untuk alur kerja tinjauan visual, pemeriksaan regresi, atau laporan perbandingan PDF.

Fungsionalitas perbandingan dalam Aspose.PDF memungkinkan Anda membandingkan dua dokumen PDF halaman per halaman. Anda dapat memilih untuk membandingkan halaman tertentu atau seluruh dokumen. Dokumen perbandingan yang dihasilkan menyoroti perbedaan, sehingga memudahkan mengidentifikasi perubahan antara dua file.

Berikut adalah daftar cara yang mungkin untuk membandingkan dokumen PDF menggunakan perpustakaan Aspose.PDF for Python via .NET:

1. **Membandingkan Halaman Tertentu** - Bandingkan halaman pertama dari dua dokumen PDF.
1. **Membandingkan Seluruh Dokumen** - Bandingkan seluruh konten dari dua dokumen PDF.
1. **Bandingkan dokumen PDF secara grafis**:

- Bandingkan PDF dengan metode 'comparer.get_difference' - gambar individual di mana perubahan ditandai.
- Bandingkan PDF dengan metode 'comparer.compare_documents_to_pdf' - dokumen PDF dengan gambar di mana perubahan ditandai.

## Membandingkan Halaman Spesifik

Potongan kode pertama menunjukkan cara membandingkan halaman pertama dari dua dokumen PDF menggunakan kelas SideBySidePdfComparer.

1. Inisialisasi Dokumen.
1. Buat fungsi untuk melakukan perbandingan.
1. Proses Perbandingan:

- document1.pages[1] dan document2.pages[1]: - ini menentukan halaman pertama dari setiap dokumen untuk perbandingan. Perhatikan bahwa indeks halaman dimulai dari 1 di Aspose.PDF.
- SideBySideComparisonOptions - kelas ini memungkinkan penyesuaian perilaku perbandingan.
- additional_change_marks = True - mengaktifkan tampilan penanda perubahan tambahan, menyoroti perbedaan yang mungkin ada pada halaman lain, meskipun tidak ada pada halaman saat ini yang dibandingkan.
- comparison_mode = ComparisonMode.IgnoreSpaces - mengatur mode perbandingan untuk mengabaikan spasi dalam teks, fokus hanya pada perubahan dalam kata.

1. Hasil perbandingan disimpan sebagai file PDF baru bernama ComparingSpecificPages_out.pdf di data_dir yang ditentukan.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_specific_pages(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1.pages[1], document_2.pages[1], outfile, options
    )
```

## Membandingkan Seluruh Dokumen

Potongan kode kedua memperluas cakupan untuk membandingkan seluruh konten dua dokumen PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_entire_documents(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1, document_2, outfile, options
    )
```

Kode yang disediakan menunjukkan cara membandingkan dua dokumen PDF menggunakan Aspose.PDF for Python via .NET. Itu memanfaatkan kelas SideBySidePdfComparer untuk melakukan perbandingan halaman demi halaman, menghasilkan PDF baru yang menampilkan perbedaan secara berdampingan. Perbandingan dikonfigurasi dengan SideBySideComparisonOptions, di mana additional_change_marks diatur ke True untuk menyoroti perubahan tidak hanya pada halaman saat ini tetapi juga pada halaman lain, dan comparison_mode diatur ke IgnoreSpaces untuk memfokuskan pada perbedaan konten yang bermakna dengan mengabaikan variasi spasi.

## Bandingkan Menggunakan GraphicalPdfComparer

Saat berkolaborasi pada dokumen, terutama di lingkungan profesional, Anda sering berakhir dengan banyak versi file yang sama.
Kode yang disediakan menunjukkan cara membandingkan secara visual halaman tertentu dari dua dokumen PDF menggunakan Aspose.PDF for Python via .NET. Dengan menggunakan `GraphicalPdfComparer` kelas, ia menyoroti perbedaan antara halaman pertama dari dua PDF dan menghasilkan gambar yang sesuai untuk mewakili perbedaan tersebut.

Anda dapat mengatur properti kelas berikut:

- Resolution - resolusi dalam satuan DPI untuk gambar keluaran, serta untuk gambar yang dihasilkan selama perbandingan.
- Warna - warna dari tanda perubahan.
- Ambang - ambang perubahan dalam persen. Nilai defaultnya adalah nol. Menetapkan nilai selain nol memungkinkan Anda mengabaikan perubahan grafis yang tidak signifikan bagi Anda.

Dengan Aspose.PDF for Python via .NET, memungkinkan untuk membandingkan dokumen dan halaman serta menghasilkan hasil perbandingan ke dokumen PDF atau file gambar.

The `GraphicalPdfComparer` kelas memiliki metode yang memungkinkan Anda mendapatkan perbedaan gambar halaman dalam format yang cocok untuk pemrosesan lebih lanjut: `get_difference(document1.pages[1], document2.pages[1])`.

Metode ini mengembalikan sebuah objek dari `images_difference` tipe, yang berisi gambar halaman pertama yang sedang dibandingkan dan array perbedaan.

The `images_difference` objek memungkinkan Anda untuk menghasilkan gambar yang berbeda dan mendapatkan gambar dari halaman kedua yang dibandingkan dengan menerapkan array perbedaan pada gambar asli. Untuk melakukan ini, gunakan `difference_to_image` dan `get_destination_image` metode.

### Bandingkan PDF dengan Metode Get Difference

Kode yang disediakan mendefinisikan sebuah metode `get_difference` yang membandingkan dua dokumen PDF dan menghasilkan representasi visual dari perbedaan di antara keduanya.

Metode ini membandingkan halaman pertama dari dua file PDF dan menghasilkan dua gambar PNG:

- Satu gambar menyoroti perbedaan antara halaman-halaman tersebut dengan warna merah.
- Gambar lainnya adalah representasi visual dari halaman PDF tujuan (kedua).

Proses ini dapat berguna untuk membandingkan secara visual perubahan atau perbedaan antara dua versi dokumen.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_get_difference_method(infile1, infile2, outfile1, outfile2):
    # Open PDF documents
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)

    # Create comparer
    comparer = ap.comparison.GraphicalPdfComparer()

    # Compare specific pages
    images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

    # Get image showing differences in red over a white background
    diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
    diff_img.save(outfile1)

    # Get the second image representing the destination page
    dest_img = images_difference.get_destination_image()
    dest_img.save(outfile2)
```

### Bandingkan PDF dengan Metode CompareDocumentsToPdf

Potongan kode yang disediakan menggunakan `compare_documents_to_pdf` metode, yang membandingkan dua dokumen dan menghasilkan laporan PDF dari hasil perbandingan.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_compare_documents_to_pdf_method(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Create comparer and set options
    pdf_comparer = ap.comparison.GraphicalPdfComparer()
    pdf_comparer.threshold = 3.0
    pdf_comparer.color = ap.Color.blue
    pdf_comparer.resolution = ap.devices.Resolution(300)

    # Compare and output to a PDF file
    pdf_comparer.compare_documents_to_pdf(document_1, document_2, outfile)
```

Contoh ini menunjukkan cara melakukan perbandingan grafis dari dua dokumen PDF lengkap menggunakan Aspose.PDF for Python via .NET. Dengan memanfaatkan `GraphicalPdfComparer` kelas, itu menghasilkan file PDF baru yang secara visual menyoroti perbedaan antara dokumen-dokumen tersebut.

- Properti threshold diatur menjadi 3.0, yang berarti bahwa perbedaan kecil di bawah persentase ini diabaikan selama perbandingan, dengan fokus pada perubahan yang lebih signifikan.
- Perbedaan ditandai dengan warna biru dengan mengatur properti color ke ap.Color.blue, memungkinkan perbedaan visual yang jelas.
- Perbandingan dilakukan pada resolusi 300 DPI dengan mengatur properti resolusi, memastikan output yang detail dan jelas.

The `compare_documents_to_pdf` metode membandingkan semua halaman dari kedua dokumen dan menghasilkan hasilnya ke file PDF baru, compareDocumentsToPdf_out.pdf, dengan perbedaan yang disorot secara visual.

## Topik Terkait

- [Operasi PDF lanjutan di Python](/pdf/id/python-net/advanced-operations/)
- [Bekerja dengan dokumen PDF di Python](/pdf/id/python-net/working-with-documents/)
- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
- [Bekerja dengan teks PDF di Python](/pdf/id/python-net/working-with-text/)
