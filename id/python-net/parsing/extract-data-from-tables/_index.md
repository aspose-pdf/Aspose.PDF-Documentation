---
title: Ekstrak Data dari Tabel dalam PDF dengan Python
linktitle: Ekstrak Data dari Tabel
type: docs
weight: 40
url: /id/python-net/extract-data-from-table-in-pdf/
description: Pelajari cara mengekstrak data tabel dari file PDF dengan Aspose.PDF for Python dan mengekspor hasilnya untuk pemrosesan lebih lanjut.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengekstrak Data dari Tabel dalam PDF via Python
Abstract: Artikel ini menjelaskan cara mengekstrak dan memproses data tabel dari dokumen PDF dengan Aspose.PDF for Python. Artikel ini menunjukkan cara memindai setiap halaman dengan TableAbsorber, membaca baris dan sel dari tabel yang terdeteksi, membatasi ekstraksi ke wilayah beranotasi tertentu, dan mengekspor konten PDF ke format CSV untuk digunakan dalam alat spreadsheet dan pemrosesan lanjutan.
---

## Ekstrak Tabel dari PDF secara terprogram

Gunakan [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) untuk mendeteksi tabel pada setiap halaman dari sebuah [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Setelah mengunjungi sebuah halaman, iterasi melalui `table_list`, kemudian jalani setiap baris dan sel untuk merekonstruksi konten tabel dalam format teks yang dapat dibaca.

1. Buka PDF sebagai `Document`.
1. Iterasi melalui halaman dalam `document.pages`.
1. Buat sebuah `TableAbsorber` untuk setiap halaman dan panggil `visit(page)`.
1. Loop melalui tabel, baris, dan sel yang terdeteksi.
1. Baca fragmen teks dari setiap sel dan susun output baris yang diekstrak.

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)

# Open PDF document
document = apdf.Document(path_infile)

# Iterate through each page in the document
for page in document.pages:
    absorber = apdf.text.TableAbsorber()
    absorber.visit(page)

    for table in absorber.table_list:
        print("Table")
        for row in table.row_list:
            row_text = []
            for cell in row.cell_list:
                cell_text = []
                for fragment in cell.text_fragments:
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Ekstrak tabel di area khusus halaman PDF

Jika Anda perlu mengekstrak hanya tabel yang terletak di dalam wilayah yang ditandai, gabungkan [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) dengan sebuah [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/). Dalam contoh ini, persegi panjang anotasi digunakan sebagai batas, dan hanya tabel yang sepenuhnya berada dalam wilayah tersebut yang diproses.

1. Buka PDF sebagai `Document`.
1. Pilih halaman target.
1. Temukan anotasi kotak yang menandai wilayah yang diminati.
1. Buat sebuah `TableAbsorber` dan kunjungi halaman itu.
1. Bandingkan setiap persegi panjang tabel yang terdeteksi dengan persegi panjang anotasi.
1. Proses hanya tabel yang berada sepenuhnya di dalam area yang ditandai.

```python
import aspose.pdf as apdf
from os import path

# The path to the documents directory
path_infile = path.join(self.dataDir, infile)

# Open PDF document
document = apdf.Document(path_infile)

# Get the first page (index starts from 1 in Aspose.PDF)
page = document.pages[1]

# Find the first square annotation
square_annotation = next(
    (
        ann
        for ann in page.annotations
        if ann.annotation_type == apdf.annotations.AnnotationType.SQUARE
    ),
    None,
)

if square_annotation is None:
    print("No square annotation found.")
    return

# Initialize the TableAbsorber
absorber = apdf.text.TableAbsorber()
absorber.visit(page)

# Iterate through tables on the page
for table in absorber.table_list:
    table_rect = table.rectangle
    annotation_rect = square_annotation.rect

    # Check if the table is inside the annotation region
    is_in_region = (
        annotation_rect.llx < table_rect.llx
        and annotation_rect.lly < table_rect.lly
        and annotation_rect.urx > table_rect.urx
        and annotation_rect.ury > table_rect.ury
    )

    if is_in_region:
        for row in table.row_list:
            row_text = []
            for cell in row.cell_list:
                cell_text = []
                for fragment in cell.text_fragments:
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Ekspor Data Tabel dari PDF ke CSV

Saat Anda memerlukan data yang diekstrak dalam format yang mudah digunakan di spreadsheet, simpan PDF menggunakan [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) dan atur format keluaran ke CSV. File hasilnya dapat dibuka di Excel, Google Sheets, atau diimpor ke alur kerja analitik.

1. Buka PDF sumber sebagai [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat sebuah `ExcelSaveOptions` instansi.
1. Atur `excel_save.format` ke `ExcelSaveOptions.ExcelFormat.CSV`.
1. Simpan dokumen ke jalur CSV target.

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

document = apdf.Document(path_infile)
excel_save = apdf.ExcelSaveOptions()
excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
document.save(path_outfile, excel_save)
```
