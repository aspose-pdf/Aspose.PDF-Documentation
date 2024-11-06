---
title: Memanipulasi Tabel dalam PDF yang Ada
linktitle: Memanipulasi Tabel
type: docs
weight: 40
url: id/python-net/manipulate-tables-in-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Memanipulasi Tabel dalam PDF yang Ada",
    "alternativeHeadline": "Cara memperbarui konten Tabel dalam PDF yang Ada",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, manipulasi tabel",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


## Manipulasi tabel dalam PDF yang ada

Salah satu fitur awal yang didukung oleh Aspose.PDF for Python via .NET adalah kemampuannya untuk Bekerja dengan Tabel dan menyediakan dukungan yang baik untuk menambahkan tabel dalam file PDF yang dibuat dari awal atau file PDF yang sudah ada. Dalam rilis baru ini, kami telah mengimplementasikan fitur baru untuk mencari dan mengurai tabel sederhana yang sudah ada di halaman dokumen PDF. Sebuah kelas baru bernama [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) menyediakan kemampuan ini. Penggunaan TableAbsorber sangat mirip dengan kelas [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) yang ada. Cuplikan kode berikut menunjukkan langkah-langkah untuk memperbarui konten dalam sel tabel tertentu.

```python

    import aspose.pdf as ap

    # Muat file PDF yang ada
    pdf_document = ap.Document(input_file)
    # Buat objek TableAbsorber untuk menemukan tabel
    absorber = ap.text.TableAbsorber()
    # Kunjungi halaman pertama dengan absorber
    absorber.visit(pdf_document.pages[1])
    # Akses ke tabel pertama pada halaman, sel pertama mereka dan fragmen teks di dalamnya
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]
    # Ubah teks dari fragmen teks pertama dalam sel
    fragment.text = "hi world"
    pdf_document.save(output_file)
```


## Ganti Tabel Lama dengan yang Baru dalam Dokumen PDF

Jika Anda perlu menemukan tabel tertentu dan menggantinya dengan yang diinginkan, Anda dapat menggunakan metode [replace()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) dari kelas [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) untuk melakukannya. Contoh berikut menunjukkan fungsionalitas untuk mengganti tabel di dalam dokumen PDF:

```python

    import aspose.pdf as ap

    # Muat dokumen PDF yang ada
    pdf_document = ap.Document(input_file)
    # Buat objek TableAbsorber untuk menemukan tabel
    absorber = ap.text.TableAbsorber()
    # Kunjungi halaman pertama dengan absorber
    absorber.visit(pdf_document.pages[1])
    # Dapatkan tabel pertama di halaman
    table = absorber.table_list[0]
    # Buat tabel baru
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    row = new_table.rows.add()
    row.cells.add("Kol 1")
    row.cells.add("Kol 2")
    row.cells.add("Kol 3")

    # Ganti tabel dengan yang baru
    absorber.replace(pdf_document.pages[1], table, new_table)
    # Simpan dokumen
    pdf_document.save(output_file)
```


## Cara menentukan apakah tabel akan terputus di halaman saat ini

Kode ini menghasilkan dokumen PDF yang berisi tabel, menghitung ruang yang tersedia di halaman, dan memeriksa apakah menambahkan baris lebih banyak ke tabel akan menyebabkan pemutusan halaman berdasarkan batasan ruang. Hasilnya disimpan ke file keluaran.

```python

    import aspose.pdf as ap

    # Membuat objek kelas PDF
    pdf = ap.Document()
    # Menambahkan bagian ke koleksi bagian dokumen PDF
    page = pdf.pages.add()
    # Membuat objek tabel
    table1 = ap.Table()
    table1.margin.top = 300
    # Menambahkan tabel dalam koleksi paragraf dari bagian yang diinginkan
    page.paragraphs.add(table1)
    # Menetapkan lebar kolom tabel
    table1.column_widths = "100 100 100"
    # Menetapkan batas sel default menggunakan objek BorderInfo
    table1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Menetapkan batas tabel menggunakan objek BorderInfo yang disesuaikan
    table1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Membuat objek MarginInfo dan menetapkan margin kiri, bawah, kanan, dan atas
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Menetapkan padding sel default ke objek MarginInfo
    table1.default_cell_padding = margin
    # Jika Anda meningkatkan penghitung menjadi 17, tabel akan terputus
    # Karena tidak dapat ditampung lagi di halaman ini
    for row_counter in range(0, 17):
        # Membuat baris dalam tabel dan kemudian sel dalam baris
        row1 = table1.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
    # Mendapatkan informasi Tinggi Halaman
    page_height = pdf.page_info.height
    # Mendapatkan informasi total tinggi Margin Atas & Bawah Halaman,
    # Margin Atas Tabel dan tinggi tabel.
    total_objects_height = page.page_info.margin.top + page.page_info.margin.bottom + table1.margin.top + \
                           table1.get_height(None)
    # Menampilkan Tinggi Halaman, Tinggi Tabel, Margin Atas tabel dan Margin Atas
    # Dan informasi Margin Bawah Halaman
    print("Tinggi dokumen PDF = " + str(pdf.page_info.height) + "\nInfo Margin Atas = " + str(page.page_info.margin.top)
          + "\nInfo Margin Bawah = " + str(page.page_info.margin.bottom) + "\n\nInfo Margin Atas Tabel = "
          + str(table1.margin.top) + "\nTinggi Baris Rata-rata = " + str(table1.rows[0].min_row_height) + " \nTinggi tabel "
          + str(table1.get_height(None)) + "\n ----------------------------------------" + "\nTotal Tinggi Halaman ="
          + str(page_height) + "\nTinggi kumulatif termasuk Tabel =" + str(total_objects_height))
    # Memeriksa jika kita mengurangi jumlah Margin atas Halaman + Margin Bawah Halaman
    # + Margin Atas Tabel dan tinggi tabel dari tinggi Halaman dan kurang
    # Dari 10 (rata-rata baris bisa lebih dari 10)
    if (page_height - total_objects_height) <= 10:
        # Jika nilainya kurang dari 10, maka tampilkan pesan.
        # Yang menunjukkan bahwa baris lain tidak dapat ditempatkan dan jika kita menambahkan
        # Baris baru, tabel akan terputus. Ini tergantung pada nilai tinggi baris.
        print("Tinggi Halaman - Tinggi Objek < 10, jadi tabel akan terputus")
    # Menyimpan dokumen pdf
    pdf.save(output_file)
```


## Menambahkan Kolom Berulang dalam Tabel

Dalam kelas [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), Anda dapat mengatur [repeating_rows_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) yang akan mengulang baris jika tabel terlalu panjang secara vertikal dan meluap ke halaman berikutnya. Namun, dalam beberapa kasus, tabel terlalu lebar untuk muat pada satu halaman dan perlu dilanjutkan ke halaman berikutnya. Untuk memenuhi tujuan ini, kami telah mengimplementasikan properti [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) dalam kelas [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/). Mengatur properti ini akan menyebabkan tabel terputus ke halaman berikutnya secara kolom dan mengulang jumlah kolom yang ditentukan di awal halaman berikutnya. Cuplikan kode berikut menunjukkan penggunaan properti [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties):

```python

    import aspose.pdf as ap

    # Buat dokumen baru
    doc = ap.Document()
    page = doc.pages.add()
    # Instansiasi tabel luar yang mengisi seluruh halaman
    outer_table = ap.Table()
    outer_table.column_widths = "100%"
    outer_table.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Instansiasi objek tabel yang akan ditempatkan di dalam outerTable yang akan terputus di dalam halaman yang sama
    my_table = ap.Table()
    my_table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    my_table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # Tambahkan outerTable ke paragraf halaman
    # Tambahkan tabel saya ke outerTable
    page.paragraphs.add(outer_table)
    body_row = outer_table.rows.add()
    body_cell = body_row.cells.add()
    body_cell.paragraphs.add(my_table)
    my_table.repeating_columns_count = 5
    page.paragraphs.add(my_table)
    # Tambahkan Baris header
    row = my_table.rows.add()
    row.cells.add("header 1")
    row.cells.add("header 2")
    row.cells.add("header 3")
    row.cells.add("header 4")
    row.cells.add("header 5")
    row.cells.add("header 6")
    row.cells.add("header 7")
    row.cells.add("header 11")
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")
    for row_counter in range(0, 6):
        # Buat baris dalam tabel dan kemudian sel dalam baris
        row1 = my_table.rows.add()
        row1.cells.add("kolom " + str(row_counter) + ", 1")
        row1.cells.add("kolom " + str(row_counter) + ", 2")
        row1.cells.add("kolom " + str(row_counter) + ", 3")
        row1.cells.add("kolom " + str(row_counter) + ", 4")
        row1.cells.add("kolom " + str(row_counter) + ", 5")
        row1.cells.add("kolom " + str(row_counter) + ", 6")
        row1.cells.add("kolom " + str(row_counter) + ", 7")
        row1.cells.add("kolom " + str(row_counter) + ", 11")
        row1.cells.add("kolom " + str(row_counter) + ", 12")
        row1.cells.add("kolom " + str(row_counter) + ", 13")
        row1.cells.add("kolom " + str(row_counter) + ", 14")
        row1.cells.add("kolom " + str(row_counter) + ", 15")
        row1.cells.add("kolom " + str(row_counter) + ", 16")
        row1.cells.add("kolom " + str(row_counter) + ", 17")
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Python melalui .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk Python melalui .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>