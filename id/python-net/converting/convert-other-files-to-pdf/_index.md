---
title: Mengonversi Format File Lain ke PDF dalam Python
linktitle: Konversi format file lain ke PDF
type: docs
weight: 80
url: /id/python-net/convert-other-files-to-pdf/
lastmod: "2026-06-12"
description: Pelajari cara mengonversi file EPUB, Markdown, PCL, XPS, PostScript, XML, dan LaTeX ke PDF dalam Python dengan Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cara Mengonversi format file lain ke PDF di Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang mengonversi berbagai format file ke PDF menggunakan Python, memanfaatkan kemampuan Aspose.PDF for Python via .NET. Dokumen ini menguraikan proses konversi untuk beberapa format, termasuk EPUB, Markdown, PCL, Text, XPS, PostScript, XML, XSL-FO, dan LaTeX/TeX. Setiap bagian menyediakan potongan kode spesifik dan instruksi untuk mengimplementasikan konversi ini. Artikel ini menekankan kegunaan fitur Aspose.PDF, seperti opsi pemuatan yang disesuaikan untuk setiap jenis file, untuk memastikan konversi yang akurat dan efisien. Selain itu, artikel ini menyoroti ketersediaan aplikasi konversi online bagi pengguna untuk mengeksplorasi fungsionalitas secara langsung. Panduan ini berfungsi sebagai sumber daya praktis bagi pengembang yang ingin mengintegrasikan kemampuan konversi PDF ke dalam aplikasi Python mereka.
---

Artikel ini menjelaskan cara **mengonversi berbagai jenis format file lain ke PDF menggunakan Python**. Ini mencakup topik‑topik berikut.

## Konversi OFD ke PDF

OFD singkatan dari Open Fixed-layout Document (juga disebut format Open Fixed Document). Ini adalah standar nasional Tiongkok (GB/T 33190-2016) untuk dokumen elektronik, yang diperkenalkan sebagai alternatif PDF.

Langkah-langkah Mengonversi OFD ke PDF di Python:

1. Atur opsi muat OFD menggunakan OfdLoadOptions().
1. Muat dokumen OFD.
1. Simpan sebagai PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_OFD_to_PDF(infile, outfile):
    load_options = ap.OfdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Konversi LaTeX/TeX ke PDF

Format file LaTeX adalah format file teks dengan markup dalam turunan LaTeX dari keluarga bahasa TeX dan LaTeX adalah format turunan dari sistem TeX. LaTeX (\u02C8le\u026At\u025Bk/lay-tek atau lah-tek) adalah sistem penyiapan dokumen dan bahasa markup dokumen. Ia banyak digunakan untuk komunikasi dan publikasi dokumen ilmiah di banyak bidang, termasuk matematika, fisika, dan ilmu komputer. Ia juga memainkan peran kunci dalam penyiapan dan publikasi buku serta artikel yang berisi materi multibahasa yang kompleks, seperti bahasa Korea, Jepang, karakter Tionghoa, dan Arab, termasuk edisi khusus.

LaTeX menggunakan program penataan huruf TeX untuk memformat outputnya, dan ia sendiri ditulis dalam bahasa makro TeX.

{{% alert color="success" %}}
**Coba konversi LaTeX/TeX ke PDF secara online**

Aspose.PDF for Python via .NET mempersembahkan aplikasi online Anda ["LaTex ke PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi LaTeX/TeX ke PDF dengan Aplikasi](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Langkah-langkah Mengonversi TEX ke PDF dengan Python:

1. Atur opsi pemuatan LaTeX menggunakan LatexLoadOptions().
1. Muat dokumen LaTeX.
1. Simpan sebagai PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TEX_to_PDF(infile, outfile):
    load_options = ap.LatexLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Ubah EPUB menjadi PDF

**Aspose.PDF for Python via .NET** memungkinkan Anda dengan mudah mengonversi file EPUB ke format PDF.

EPUB (singkatan dari electronic publication) adalah standar e-book gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub. EPUB dirancang untuk konten yang dapat mengalir ulang, yang berarti pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu.

<abbr title="electronic publication">EPUB</abbr> juga mendukung konten tata letak tetap. Format ini dimaksudkan sebagai satu format yang dapat digunakan secara internal oleh penerbit dan rumah konversi, serta untuk distribusi dan penjualan. Ini menggantikan standar Open eBook. Versi EPUB 3 juga didukung oleh Book Industry Study Group (BISG), sebuah asosiasi perdagangan buku terkemuka untuk praktik terbaik yang terstandarisasi, penelitian, informasi, dan acara, untuk pengemasan konten.

{{% alert color="success" %}}
**Coba konversi EPUB ke PDF secara online**

Aspose.PDF for Python via .NET mempersembahkan aplikasi online Anda ["EPUB ke PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Konversi Aspose.PDF EPUB ke PDF dengan Aplikasi](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

Langkah-langkah Mengonversi EPUB ke PDF dalam Python:

1. Muat Dokumen EPUB dengan EpubLoadOptions().
1. Konversi EPUB ke PDF.
1. Konfirmasi Cetak.

Berikut ini cuplikan kode yang menunjukkan cara mengonversi file EPUB ke format PDF dengan Python.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_EPUB_to_PDF(infile, outfile):
    load_options = ap.EpubLoadOptions()
    document = ap.Document(infile, load_options)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Konversi Markdown ke PDF

**Fitur ini didukung oleh versi 19.6 atau lebih tinggi.**

{{% alert color="success" %}}
**Coba konversi Markdown ke PDF secara online**

Aspose.PDF for Python via .NET mempersembahkan aplikasi online Anda ["Markdown ke PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi Markdown ke PDF dengan App](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Potongan kode ini oleh Aspose.PDF for Python via .NET membantu mengonversi file Markdown menjadi PDF, memungkinkan berbagi dokumen yang lebih baik, pelestarian format, dan kompatibilitas pencetakan.o

Potongan kode berikut menunjukkan cara menggunakan fungsionalitas ini dengan pustaka Aspose.PDF:

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_MD_to_PDF(infile, outfile):
    load_options = ap.MdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Konversi PCL ke PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) adalah bahasa printer Hewlett-Packard yang dikembangkan untuk mengakses fitur printer standar. Level PCL 1 hingga 5e/5c adalah bahasa berbasis perintah yang menggunakan urutan kontrol yang diproses dan ditafsirkan dalam urutan penerimaannya. Pada tingkat konsumen, aliran data PCL dihasilkan oleh driver printer. Output PCL juga dapat dengan mudah dihasilkan oleh aplikasi khusus.

{{% alert color="success" %}}
**Coba konversi PCL ke PDF secara online**

Aspose.PDF untuk .NET mempersembahkan Anda aplikasi online ["PCL ke PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi PCL ke PDF dengan Aplikasi](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

Untuk memungkinkan konversi dari PCL ke PDF, Aspose.PDF memiliki kelas [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) yang digunakan untuk menginisialisasi objek LoadOptions. Kemudian objek ini diteruskan sebagai argumen saat inisialisasi objek Document dan membantu mesin rendering PDF menentukan format input dokumen sumber.

Potongan kode berikut menunjukkan proses mengonversi file PCL ke format PDF.

Langkah-langkah Mengonversi PCL ke PDF di Python:

1. Muat opsi untuk PCL menggunakan PclLoadOptions().
1. Muat dokumen.
1. Simpan sebagai PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PCL_to_PDF(infile, outfile):
    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Konversi Teks Prabentuk ke PDF

**Aspose.PDF for Python via .NET** mendukung fitur mengonversi file teks biasa dan file teks berformat sebelumnya ke format PDF.

Mengonversi teks ke PDF berarti menambahkan fragmen teks ke halaman PDF. Untuk file teks, kita berurusan dengan 2 jenis teks: pra-pemformatan (misalnya, 25 baris dengan 80 karakter per baris) dan teks yang tidak diformat (teks biasa). Tergantung pada kebutuhan kita, kita dapat mengontrol penambahan ini sendiri atau mempercayakannya kepada algoritma perpustakaan.

{{% alert color="success" %}}
**Coba konversi TEXT ke PDF secara online**

Aspose.PDF for Python via .NET mempersembahkan aplikasi online Anda ["Teks ke PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi TEKS ke PDF dengan App](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

Langkah-langkah Mengonversi TEXT ke PDF dalam Python:

1. Baca file teks input baris per baris.
1. Atur font monospaced (Courier New) untuk penyelarasan teks yang konsisten.
1. Buat Dokumen PDF baru dan tambahkan halaman pertama dengan margin khusus serta pengaturan font.
1. Iterasi melalui baris file teks. Untuk mensimulasikan mesin tik, kami menggunakan font 'monospace_font' dengan ukuran 12.
1. Batasi pembuatan halaman hingga 4 halaman.
1. Simpan PDF akhir ke jalur yang ditentukan.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TXT_to_PDF(infile, outfile):
    with open(infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Konversi PostScript ke PDF

Contoh ini menunjukkan cara mengonversi file PostScript menjadi dokumen PDF menggunakan Aspose.PDF for Python via .NET.

1. Buat sebuah instance dari 'PsLoadOptions' untuk menginterpretasikan file PS dengan benar.
1. Muat file 'PostScript' ke dalam objek Document menggunakan opsi pemuatan.
1. Simpan dokumen dalam format PDF ke jalur output yang diinginkan.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PS_to_PDF(infile, outfile):
    load_options = ap.PsLoadOptions()

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Konversi XPS ke PDF

**Aspose.PDF for Python via .NET** mendukung fitur konversi <abbr title="XML Paper Specification">XPS</abbr> file ke format PDF. Periksa artikel ini untuk menyelesaikan tugas Anda.

Tipe file XPS terutama terkait dengan XML Paper Specification oleh Microsoft Corporation. XML Paper Specification (XPS), yang sebelumnya berkode nama Metro dan mencakup konsep pemasaran Next Generation Print Path (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dan penampilan dokumen ke dalam sistem operasi Windows-nya.

Cuplikan kode berikut menunjukkan proses mengonversi file XPS ke format PDF dengan Python.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XPS_to_PDF(infile, outfile):
    load_options = ap.XpsLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba konversi format XPS ke PDF secara online**

Aspose.PDF for Python via .NET mempersembahkan aplikasi online Anda ["XPS ke PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Konversi Aspose.PDF XPS ke PDF dengan Aplikasi](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Konversi XSL-FO ke PDF

Potongan kode berikut dapat digunakan untuk mengonversi XSLFO ke format PDF dengan Aspose.PDF for Python via .NET:

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## Konversi XML dengan XSLT ke PDF

Contoh ini menunjukkan cara mengonversi file XML menjadi PDF dengan terlebih dahulu mengubahnya menjadi HTML menggunakan templat XSLT dan kemudian memuat HTML ke dalam Aspose.PDF.

1. Buat sebuah instance dari 'HtmlLoadOptions' untuk mengonfigurasi konversi HTML-ke-PDF.
1. Muat file HTML yang telah diubah ke dalam objek Document Aspose.PDF.
1. Simpan dokumen sebagai PDF di jalur output yang ditentukan.
1. Hapus file HTML sementara setelah konversi berhasil.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## Konversi terkait

- [Konversi HTML ke PDF](/pdf/id/python-net/convert-html-to-pdf/) untuk skenario konversi HTML dan MHTML.
- [Konversi format gambar ke PDF](/pdf/id/python-net/convert-images-format-to-pdf/) ketika input Anda berupa PNG, JPEG, TIFF, SVG, atau gambar lainnya.
- [Konversi PDF ke format lain](/pdf/id/python-net/convert-pdf-to-other-files/) jika Anda juga memerlukan konversi terbalik seperti PDF ke EPUB, Markdown, atau teks.
