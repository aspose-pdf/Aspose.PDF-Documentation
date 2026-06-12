---
title: Ekstrak Konten Ber-tag dari PDF di Python
linktitle: Ekstrak Konten Ber-tag
type: docs
weight: 20
url: /id/python-net/extract-tagged-content-from-tagged-pdfs/
description: Pelajari cara mengekstrak konten PDF ber-tag di Python dengan Aspose.PDF for Python via .NET, termasuk akses ke konten ber-tag, struktur akar, dan elemen struktur anak.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Dalam artikel ini, Anda akan mempelajari cara mengekstrak konten ber-tag dari dokumen PDF menggunakan Python.

Gunakan contoh-contoh ini ketika Anda perlu memeriksa tagged PDF, membaca pohon struktur logis, atau memvalidasi bahwa elemen struktur dibuat dengan benar untuk alur kerja aksesibilitas.

## Mendapatkan Konten Tagged PDF

Untuk mendapatkan konten Dokumen PDF dengan Tagged Text, Aspose.PDF menawarkan [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) properti dari [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas.

Buat dokumen PDF berlabel penuh yang canggih dengan Daftar Isi (TOC) yang terstruktur dan hierarkis:

1. Buat objek Document baru.
1. Akses properti tagged_content.
1. Setel judul dokumen menggunakan 'set_title()'.
1. Setel bahasa dokumen menggunakan 'set_language()'.
1. Simpan dokumen.

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

# region Extract Tagged Content from PDF
def get_tagged_content(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Work with Tagged PDF content
        # Set Title and Language for Document
        tagged_content.set_title("Simple Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Mendapatkan Struktur Akar

Tagged PDF berisi pohon struktur logis yang mendefinisikan struktur semantik dokumen. StructTreeRoot mewakili akar pohon logis ini, sementara RootElement menyediakan antarmuka untuk berinteraksi dengan elemen struktur tingkat atas dokumen.

Potongan kode berikut menunjukkan cara mendapatkan struktur root dari Tagged PDF Document:

1. Buat dokumen tagged PDF baru.
1. Akses tagged content dan atur metadata.
1. Akses StructTreeRoot dan RootElement.
1. Simpan PDF ber-tag.

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def get_root_structure(outfile):

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Properties StructTreeRootElement and RootElement are used for access to
        # StructTreeRoot object of pdf document and to root structure element (Document structure element).
        struct_tree_root_element = tagged_content.struct_tree_root_element
        root_element = tagged_content.root_element

        print(f"StructTreeRootElement: {struct_tree_root_element}")
        print(f"RootElement: {root_element}")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Mengakses Elemen Anak

Tagged PDF berisi pohon struktur logis yang mendefinisikan hierarki semantik dokumen (judul, paragraf, formulir, daftar, dll.). Mengakses dan memodifikasi elemen struktur ini memungkinkan Anda untuk:

- Memeriksa metadata seperti judul, bahasa, actual_text, dan properti terkait aksesibilitas
- Perbarui properti untuk meningkatkan aksesibilitas atau lokalisasi
- Sesuaikan struktur dokumen logis secara programatik untuk kepatuhan PDF/UA

 Potongan kode berikut menunjukkan cara mengakses elemen anak dari Dokumen Tagged PDF:

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def access_child_elements(infile, outfile):

    # Open PDF Document
    with ap.Document(infile) as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Access to root element(s)
        element_list = tagged_content.struct_tree_root_element.child_elements

        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = cast(ap.logicalstructure.StructureElement, element)
                # Get properties
                print(
                    "StructureElement properties - "
                    f"title: {structure_element.title}, "
                    f"language: {structure_element.language}, "
                    f"actual_text: {structure_element.actual_text}, "
                    f"expansion_text: {structure_element.expansion_text}, "
                    f"alternative_text: {structure_element.alternative_text}"
                )

        # Access to child elements of first element in root element
        element_list = tagged_content.root_element.child_elements[1].child_elements
        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = element

                # Set properties
                structure_element.title = "title"
                structure_element.language = "fr-FR"
                structure_element.actual_text = "actual text"
                structure_element.expansion_text = "exp"
                structure_element.alternative_text = "alt"

        # Save Tagged PDF Document
        document.save(outfile)
```

## Topik Tagged PDF Terkait

- [Buat Tagged PDF](/pdf/id/python-net/create-tagged-pdf/) untuk membuat dokumen bertanda yang dapat diakses sebelum memeriksa strukturnya.
- [Mengatur Properti Elemen Struktur](/pdf/id/python-net/setting-structure-elements-properties/) untuk memperbarui properti semantik setelah mengekstrak elemen struktur.
- [Bekerja dengan Tabel dalam Tagged PDF](/pdf/id/python-net/working-with-table-in-tagged-pdfs/) untuk alur kerja aksesibilitas tabel ber‑tag.