---
title: Konversi PDF ke PDF/A, PDF/E, dan PDF/X dalam Python
linktitle: Ubah PDF menjadi PDF/A, PDF/E, dan PDF/X
type: docs
weight: 120
url: /id/python-net/convert-pdf-to-pdf_x/
lastmod: "2026-06-12"
description: Pelajari cara mengonversi file PDF ke PDF/A, PDF/E, dan PDF/X dalam Python dengan Aspose.PDF for Python via .NET untuk alur kerja pengarsipan, aksesibilitas, dan pencetakan.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cara mengonversi PDF ke format PDF/x
Abstract: Artikel ini menyediakan panduan komprehensif tentang mengonversi PDF ke format PDF/A, PDF/E, dan PDF/X menggunakan Aspose.PDF for Python.
---

**PDF ke format PDF/x berarti kemampuan untuk mengonversi PDF ke format tambahan, yaitu PDF/A, PDF/E, dan PDF/X.**

## Ubah PDF menjadi PDF/A

**Aspose.PDF for Python** memungkinkan Anda mengkonversi file PDF menjadi <abbr title="Portable Document Format / A">PDF/A</abbr> file PDF yang mematuhi. Sebelum melakukannya, file harus divalidasi. Topik ini menjelaskan caranya.

{{% alert color="primary" %}}

Harap dicatat kami mengikuti Adobe Preflight untuk memvalidasi kepatuhan PDF/A. Semua alat di pasar memiliki “representasi” mereka sendiri terhadap kepatuhan PDF/A. Silakan periksa artikel ini tentang alat validasi PDF/A untuk referensi. Kami memilih produk Adobe untuk memverifikasi bagaimana Aspose.PDF menghasilkan file PDF karena Adobe berada di pusat segala hal yang terkait dengan PDF.

{{% /alert %}}

Konversi file menggunakan metode Convert pada kelas Document. Sebelum mengonversi PDF menjadi file yang mematuhi PDF/A, validasi PDF menggunakan metode Validate. Hasil validasi disimpan dalam file XML dan kemudian hasil tersebut juga diteruskan ke metode Convert. Anda juga dapat menentukan tindakan untuk elemen yang tidak dapat dikonversi menggunakan enumerasi ConvertErrorAction.

{{% alert color="success" %}}
**Coba konversi PDF ke PDF/A secara daring**

Aspose.PDF for Python menyajikan aplikasi online kepada Anda ["PDF ke PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi PDF ke PDF/A dengan Aplikasi](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

Metode 'document.validate()' memvalidasi apakah file PDF mematuhi standar PDF/A-1B (versi PDF yang distandarisasi ISO untuk pengarsipan jangka panjang). Hasil validasi disimpan dalam file log.

### Konversi PDF ke PDF/A-1B

Potongan kode berikut menunjukkan cara mengonversi file PDF ke format PDF/A-1B:

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Panggil metode convert dengan parameter berikut:
    - Jalur file log - menyimpan detail proses konversi dan pemeriksaan kepatuhan.
    - Format target - 'ap.PdfFormat.PDF_A_1B' (standar arsip).
    - Error action - 'ap.ConvertErrorAction.DELETE' — secara otomatis menghapus elemen yang mencegah kepatuhan.
1. Simpan file yang telah dikonversi sesuai PDF/A ke jalur output.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA(infile, outfile):
    """Convert PDF to PDF/A-1B format."""

    document = ap.Document(infile)
    document.convert(
        outfile.replace(".pdf", "-log.xml"),
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

### Konversi PDF ke PDF 2.0 dan PDF/A-4

Contoh ini menunjukkan cara mengonversi dokumen PDF ke format standar yang lebih baru: PDF 2.0 dan PDF/A-4.
Kedua konversi membantu memastikan kepatuhan terhadap spesifikasi modern dan persyaratan arsip.

1. Muat dokumen input menggunakan ap.Document.
1. Lakukan konversi pertama ke PDF 2.0 dengan memanggil document.convert dengan:
    - Jalur file log untuk detail konversi.
    - Format target - 'ap.PdfFormat.V_2_0'.
    - Tindakan kesalahan - 'ap.ConvertErrorAction.DELETE' untuk menghapus elemen yang tidak sesuai.
1. Lakukan konversi kedua ke PDF/A-4 menggunakan metode yang sama, memastikan file juga mematuhi standar arsip.
1. Simpan dokumen hasil di jalur output yang ditentukan.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA4(infile, outfile):
    logfile = outfile.replace(".pdf", "_log.xml")

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)
    document.convert(logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### Konversi PDF ke PDF/A-3A dengan File Tertanam

Potongan kode berikut menunjukkan cara menyematkan file eksternal ke dalam PDF dan kemudian mengonversi PDF ke format PDF/A-3A, yang mendukung lampiran dan cocok untuk pengarsipan jangka panjang dengan konten yang disematkan.

1. Muat PDF input menggunakan 'ap.Document'.
1. Buat objek 'FileSpecification' yang menunjuk ke file yang akan disematkan (misalnya "aspose-logo.jpg") dengan deskripsi.
1. Tambahkan spesifikasi file ke koleksi 'embedded_files' PDF.
1. Konversi dokumen ke PDF/A-3A menggunakan 'document.convert', dengan menentukan:
    - Jalur file log.
    - Format target - 'ap.PdfFormat.PDF_A_3A'.
    - Tindakan kesalahan - 'ap.ConvertErrorAction.DELETE' untuk menghapus elemen yang tidak sesuai.
1. Simpan PDF yang telah dikonversi ke jalur output.
1. Cetak pesan konfirmasi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_attachment(infile, attachement_file, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    document = ap.Document(infile)

    fileSpecification = ap.FileSpecification(attachement_file, "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(
        logfile, ap.PdfFormat.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE
    )
    document.save(outfile)
```

### Konversi PDF ke PDF/A-1B dengan Substitusi Font

Fungsi ini mengonversi PDF ke format PDF/A-1B sambil menangani font yang hilang dengan menggantinya dengan font yang tersedia. Hal ini memastikan PDF yang dikonversi tetap konsisten secara visual dan mematuhi standar arsip.

1. Muat PDF menggunakan 'ap.Document'.
1. Konversi PDF ke PDF/A-1B menggunakan 'document.convert', dengan menentukan:
    - Jalur file log.
    - Format target - 'ap.PdfFormat.PDF_A_1B'.
    - Tindakan kesalahan - 'ap.ConvertErrorAction.DELETE' untuk menghapus elemen yang tidak sesuai.
1. Simpan PDF yang telah dikonversi ke jalur output.
1. Cetak pesan konfirmasi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_replace_missing_fonts(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### Konversi PDF ke PDF/A-1B dengan Penandaan Otomatis

Fungsi ini mengonversi dokumen PDF menjadi format PDF/A-1B sambil secara otomatis menandai konten untuk aksesibilitas dan konsistensi struktural. Penandaan otomatis meningkatkan kegunaan dokumen untuk pembaca layar dan memastikan struktur semantik yang tepat.

1. Muat PDF menggunakan 'ap.Document'.
1. Buat 'PdfFormatConversionOptions' dengan menentukan:
    - Jalur file log.
    - Format target - 'ap.PdfFormat.PDF_A_1B'.
    - Tindakan kesalahan - 'ap.ConvertErrorAction.DELETE' untuk menghapus elemen yang tidak sesuai.
1. Konfigurasikan 'AutoTaggingSettings':
    - Aktifkan 'enable_auto_tagging = True'.
    - Set 'heading_recognition_strategy = AUTO' untuk secara otomatis mendeteksi heading.
1. Tetapkan pengaturan auto-tagging ke opsi konversi.
1. Konversi PDF menggunakan 'document.convert(options)'.
1. Simpan PDF yang telah dikonversi ke jalur output.
1. Cetak pesan konfirmasi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_automatic_tagging(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
    )

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = (
        ap.HeadingRecognitionStrategy.AUTO
    )

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Konversi PDF ke PDF/E

Potongan kode ini menunjukkan cara mengonversi dokumen PDF ke format PDF/E-1, yang merupakan standar ISO yang disesuaikan untuk rekayasa dan dokumentasi teknis. Format ini mempertahankan tata letak yang tepat, grafis, dan metadata yang diperlukan untuk alur kerja rekayasa.

1. Muat PDF sumber menggunakan 'ap.Document'.
1. Buat 'PdfFormatConversionOptions' dengan menentukan:
    - Jalur file log untuk melacak masalah konversi.
    - Format target - 'ap.PdfFormat.PDF_E_1'.
    - Tindakan kesalahan - 'ap.ConvertErrorAction.DELETE' untuk menghapus elemen yang tidak sesuai.
1. Konversi PDF menggunakan 'document.convert(options)'.
1. Simpan PDF yang telah dikonversi ke jalur output yang ditentukan.
1. Cetak pesan konfirmasi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_E(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
    )

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Konversi PDF ke PDF/X

Potongan kode berikut mengonversi dokumen PDF ke format PDF/X-4, yang merupakan standar ISO yang umum digunakan dalam industri percetakan dan penerbitan. PDF/X-4 memastikan akurasi warna, mempertahankan transparansi, dan menyertakan profil ICC untuk output yang konsisten di seluruh perangkat.

1. Muat PDF sumber menggunakan 'ap.Document'.
1. Buat 'PdfFormatConversionOptions' dengan menentukan:
    - Jalur file log.
    - Format target - 'ap.PdfFormat.PDF_X_4'.
    - Tindakan kesalahan - 'ap.ConvertErrorAction.DELETE' untuk menghapus elemen yang tidak sesuai.
1. Sediakan **file profil ICC** untuk manajemen warna melalui 'icc_profile_file_name'.
1. Tentukan sebuah **OutputIntent** dengan pengidentifikasi kondisi (mis., "FOGRA39") untuk persyaratan pencetakan.
1. Konversi PDF menggunakan 'document.convert()'.
1. Simpan PDF yang telah dikonversi ke jalur output yang ditentukan.
1. Cetak pesan konfirmasi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_X(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE
    )

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(
        path.dirname(infile), "ISOcoated_v2_eci.icc"
    )
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Konversi terkait

- [Konversi PDF ke Word](/pdf/id/python-net/convert-pdf-to-word/) untuk alur kerja konten yang dapat diedit setelah validasi standar.
- [Konversi PDF ke HTML](/pdf/id/python-net/convert-pdf-to-html/) ketika output target Anda siap untuk web alih-alih PDF berbasis standar.
