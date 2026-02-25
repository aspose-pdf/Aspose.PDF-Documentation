---
title: Ekstrak Data dari Tabel dalam PDF dengan Python
linktitle: Ekstrak Data dari Tabel
type: docs
weight: 40
url: /id/python-net/extract-data-from-table-in-pdf/
description: Pelajari cara mengekstrak tabel dari PDF menggunakan Aspose.PDF untuk Python
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengekstrak Data dari Tabel dalam PDF via Python
Abstract: Artikel ini memberikan panduan komprehensif tentang cara mengekstrak dan memproses tabel secara programatik dari dokumen PDF menggunakan Aspose.PDF, sebuah pustaka Python. Artikel ini menyajikan skrip Python yang membuka dokumen PDF, melakukan iterasi melalui setiap halaman, dan mengekstrak tabel dengan memanfaatkan kelas `TableAbsorber`. Data tabel yang diekstrak kemudian disusun dan dicetak untuk analisis lebih lanjut. Bagian ini menjelaskan cara mengekstrak tabel dari wilayah yang ditandai secara khusus dalam PDF, seperti area yang dikelilingi oleh anotasi kotak. Skrip mengidentifikasi anotasi tersebut, menginisialisasi `TableAbsorber`, dan memeriksa apakah tabel berada dalam wilayah anotasi sebelum mengekstrak dan mencetak data. Bagian akhir merinci metode untuk mengonversi data tabel yang diekstrak dari PDF ke format file CSV.
---

## Ekstrak Tabel dari PDF secara programatik

Kode ini mengekstrak tabel PDF dan mengonversi data tabel dari file PDF menjadi format yang dapat dibaca dan terstruktur untuk pemrosesan atau analisis lebih lanjut.

1. Membuka Dokumen PDF
1. Mengiterasi Halaman PDF
1. Mengekstrak Data Tabel

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## Ekstrak tabel di area spesifik halaman PDF

Potongan kode ini mengekstrak data tabel dari wilayah yang ditandai secara khusus dalam PDF, seperti data dalam kotak yang disorot atau anotasi tertentu.

1. Buka dokumen PDF
1. Dapatkan halaman pertama
1. Temukan anotasi kotak pertama
1. Inisialisasi TableAbsorber
1. Iterasi tabel pada halaman
1. Periksa apakah tabel berada di dalam wilayah anotasi

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## Ekstrak Data Tabel dari PDF dan simpan dalam file Excel

Potongan kode berikut mengekstrak data tabel dari PDF dan mengekspornya sebagai file CSV untuk analisis lebih lanjut atau manipulasi dalam aplikasi spreadsheet seperti Excel atau Google Sheets.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    excel_save = apdf.ExcelSaveOptions()
    excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, excel_save)
```

