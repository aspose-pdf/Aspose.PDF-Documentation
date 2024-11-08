---
title: Manipulasi Dokumen PDF dalam Python melalui .NET
linktitle: Manipulasi Dokumen PDF
type: docs
weight: 20
url: /id/python-net/manipulate-pdf-document/
description: Artikel ini berisi informasi tentang cara memvalidasi Dokumen PDF untuk Standar PDF A menggunakan Python, cara bekerja dengan TOC, cara mengatur tanggal kedaluwarsa PDF, dan lain-lain.
keywords: "manipulasi pdf python"
lastmod: "2023-04-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulasi Dokumen PDF melalui Python",
    "alternativeHeadline": "Cara memanipulasi file PDF dengan Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generasi dokumen pdf",
    "keywords": "pdf, dotnet, python, manipulasi file pdf",
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
    "url": "/python-net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "Artikel ini berisi informasi tentang cara memvalidasi Dokumen PDF untuk Standar PDF A menggunakan Python, cara bekerja dengan TOC, cara mengatur tanggal kedaluwarsa PDF, dan lain-lain."
}
</script>


## Manipulasi Dokumen PDF dalam Python

## Validasi Dokumen PDF untuk Standar PDF A (A 1A dan A 1B)

Untuk memvalidasi dokumen PDF agar sesuai dengan PDF/A-1a atau PDF/A-1b, gunakan metode [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dari kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Metode ini memungkinkan Anda untuk menentukan nama file tempat hasil akan disimpan dan tipe validasi yang diperlukan dari enumerasi PdfFormat: PDF_A_1A atau PDF_A_1B.

Cuplikan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1A.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Validasi PDF untuk PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

Cuplikan kode berikut menunjukkan cara memvalidasi dokumen PDF untuk PDF/A-1b.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Validasi PDF untuk PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```


## Bekerja dengan TOC

### Tambahkan TOC ke PDF yang Ada

TOC dalam PDF adalah singkatan dari "Table of Contents" (Daftar Isi). Ini adalah fitur yang memungkinkan pengguna untuk menavigasi dokumen dengan cepat dengan memberikan gambaran umum tentang bagian dan judulnya.

Untuk menambahkan TOC ke file PDF yang ada, gunakan kelas Heading dalam namespace [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/). Namespace [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) dapat membuat baru dan memanipulasi file PDF yang ada. Untuk menambahkan TOC ke PDF yang ada, gunakan namespace Aspose.Pdf. Cuplikan kode berikut menunjukkan cara membuat daftar isi di dalam file PDF yang ada menggunakan Python melalui .NET.

```python

    import aspose.pdf as ap

    # Muat file PDF yang ada
    doc = ap.Document(input_pdf)

    # Akses halaman pertama dari file PDF
    tocPage = doc.pages.insert(1)

    # Buat objek untuk mewakili informasi TOC
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Daftar Isi")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Atur judul untuk TOC
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Buat objek string yang akan digunakan sebagai elemen TOC
    titles = ["Halaman pertama", "Halaman kedua", "Halaman ketiga", "Halaman keempat"]
    for i in range(0, 2):
        # Buat objek Heading
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Tentukan halaman tujuan untuk objek heading
        heading2.destination_page = doc.pages[i + 2]

        # Halaman tujuan
        heading2.top = doc.pages[i + 2].rect.height

        # Koordinat tujuan
        segment2.text = titles[i]

        # Tambahkan heading ke halaman yang berisi TOC
        tocPage.paragraphs.add(heading2)

    # Simpan dokumen yang telah diperbarui
    doc.save(output_pdf)
```


### Mengatur TabLeaderType yang berbeda untuk Level TOC yang berbeda

Aspose.PDF untuk Python juga memungkinkan mengatur TabLeaderType yang berbeda untuk level TOC yang berbeda. Anda perlu mengatur properti [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) dari [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # mengatur LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Daftar Isi")
    title.text_state.font_size = 30
    toc_info.title = title

    # Tambahkan bagian daftar ke koleksi bagian dari dokumen Pdf
    tocPage.toc_info = toc_info
    # Definisikan format daftar empat level dengan mengatur margin kiri
    # dan
    # pengaturan format teks setiap level

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    # Buat bagian dalam dokumen Pdf
    page = doc.pages.add()

    # Tambahkan empat judul di bagian
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Contoh Judul" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Tambahkan judul ke Daftar Isi.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # simpan Pdf
    doc.save(output_pdf)
```


### Sembunyikan Nomor Halaman dalam Daftar Isi

Jika Anda tidak ingin menampilkan nomor halaman, bersama dengan judul dalam Daftar Isi, Anda dapat menggunakan properti [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) dari Kelas [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) sebagai false. Silakan cek cuplikan kode berikut untuk menyembunyikan nomor halaman dalam daftar isi:

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Daftar Isi")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Tambahkan bagian daftar ke koleksi bagian dari dokumen Pdf
    toc_page.toc_info = toc_info
    # Definisikan format daftar empat level dengan mengatur margin kiri dan
    # pengaturan format teks dari setiap level

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # Tambahkan empat judul dalam bagian
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "ini adalah judul dari level " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```


### Sesuaikan Nomor Halaman saat menambahkan TOC

Umum untuk menyesuaikan penomoran halaman dalam TOC saat menambahkan TOC dalam dokumen PDF. Misalnya, kita mungkin perlu menambahkan beberapa awalan sebelum nomor halaman seperti P1, P2, P3, dan seterusnya. Dalam kasus seperti itu, Aspose.PDF untuk Python menyediakan properti [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) dari kelas [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) yang dapat digunakan untuk menyesuaikan nomor halaman seperti yang ditunjukkan dalam contoh kode berikut.

```python

    import aspose.pdf as ap

    # Memuat file PDF yang ada
    doc = ap.Document(input_pdf)
    # Dapatkan akses ke halaman pertama file PDF
    toc_page = doc.pages.insert(1)
    # Buat objek untuk mewakili informasi TOC
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Daftar Isi")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Atur judul untuk TOC
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Buat objek Heading
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Tentukan halaman tujuan untuk objek heading
        heading2.destination_page = doc.pages[i + 1]
        # Halaman tujuan
        heading2.top = doc.pages[i + 1].rect.height
        # Koordinat tujuan
        segment2.text = "Halaman " + str(i)
        # Tambahkan heading ke halaman yang berisi TOC
        toc_page.paragraphs.add(heading2)

    # Simpan dokumen yang diperbarui
    doc.save(output_pdf)

```


## Cara Mengatur Tanggal Kadaluwarsa PDF

Kami menerapkan hak akses pada file PDF sehingga sekelompok pengguna tertentu dapat mengakses fitur/objek tertentu dari dokumen PDF. Untuk membatasi akses file PDF, kami biasanya menerapkan enkripsi dan kami mungkin memiliki persyaratan untuk mengatur kedaluwarsa file PDF, sehingga pengguna yang mengakses/melihat dokumen mendapatkan prompt yang valid mengenai kedaluwarsa file PDF.

```python

    import aspose.pdf as ap

    # Memperkenalkan objek Dokumen
    doc = ap.Document()
    # Menambahkan halaman ke koleksi halaman file PDF
    doc.pages.add()
    # Menambahkan potongan teks ke koleksi paragraf dari objek halaman
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Halo Dunia..."))
    # Membuat objek JavaScript untuk mengatur tanggal kedaluwarsa PDF
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('File ini telah kadaluwarsa. Anda memerlukan yang baru.');"
    )
    # Mengatur JavaScript sebagai tindakan pembukaan PDF
    doc.open_action = javaScript

    # Menyimpan Dokumen PDF
    doc.save(output_pdf)
```


## Flatten Fillable PDF di Python

Dokumen PDF sering kali menyertakan formulir dengan widget interaktif yang dapat diisi seperti tombol radio, kotak centang, kotak teks, daftar, dll. Untuk membuatnya tidak dapat diedit untuk berbagai tujuan aplikasi, kita perlu meratakan file PDF tersebut. Aspose.PDF menyediakan fungsi untuk meratakan PDF Anda di Python dengan hanya beberapa baris kode:

```python

    import aspose.pdf as ap

    # Muat form PDF sumber
    doc = ap.Document(input_pdf)

    # Ratakan PDF yang Dapat Diisi
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Simpan dokumen yang diperbarui
    doc.save(output_pdf)