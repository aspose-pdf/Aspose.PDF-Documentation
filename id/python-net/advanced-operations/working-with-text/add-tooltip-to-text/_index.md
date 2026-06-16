---
title: Tambahkan Tooltip ke Teks PDF dalam Python
linktitle: Tooltip PDF
type: docs
weight: 20
url: /id/python-net/pdf-tooltip/
description: Pelajari cara menambahkan tooltip ke fragmen teks dalam dokumen PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan tooltip interaktif ke fragmen teks PDF menggunakan Python
Abstract: Artikel ini menyediakan dua contoh Python untuk menambahkan bantuan interaktif pada teks PDF menggunakan Aspose.PDF for Python via .NET. Contoh pertama menambahkan tooltip ke fragmen teks yang cocok dengan menempatkan elemen `ButtonField` yang tidak terlihat dan mengatur `alternate_name`. Contoh kedua membuat `TextBoxField` tersembunyi yang muncul saat mengarahkan kursor dengan menghubungkan peristiwa `HideAction` ke `ButtonField` yang tidak terlihat.
---

## Tambahkan Tooltip ke Teks yang Dicari dalam PDF

Potongan kode ini menunjukkan cara menumpuk yang tidak terlihat [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) elemen pada spesifik [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) objek dalam PDF untuk menampilkan tooltip ketika pengguna mengarahkan kursor di atasnya. Ini mendukung pesan tooltip pendek dan panjang menggunakan `alternate_name` properti dari `ButtonField`.

Gunakan halaman ini ketika Anda perlu membuat teks PDF lebih interaktif dengan menambahkan bantuan saat mengarahkan kursor, penjelasan inline, atau catatan kontekstual.

1. Buat yang baru [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Simpan dokumen awal.
1. Buka kembali dokumen PDF.
1. Cari teks target menggunakan [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. Tambahkan yang tidak terlihat [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) dengan tooltip singkat.
1. Cari teks target kedua.
1. Tambahkan yang tidak terlihat [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) dengan tooltip panjang di atas fragmen yang cocok.
1. Simpan dokumen akhir.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing
import sys
from os import path

# region PDF Tooltip
def add_tool_tip_to_searched_text(outfile):
    # Create PDF document
    with ap.Document() as document:
        document.pages.add().paragraphs.add(
            ap.text.TextFragment("Move the mouse cursor here to display a tooltip")
        )
        document.pages[1].paragraphs.add(
            ap.text.TextFragment(
                "Move the mouse cursor here to display a very long tooltip"
            )
        )
        document.save(outfile)

    # Open document with text
    with ap.Document(outfile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display a tooltip"
        )
        # Accept the absorber for the document pages
        document.pages.accept(absorber)
        # Get the extracted text fragments
        text_fragments = absorber.text_fragments

        # Loop through the fragments
        for fragment in text_fragments:
            # Create invisible button on text fragment position
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # alternate_name value will be displayed as tooltip by a viewer application
            field.alternate_name = "Tooltip for text."
            # Add button field to the document
            document.form.add(field)

        # Next will be sample of very long tooltip
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display a very long tooltip"
        )
        document.pages.accept(absorber)
        text_fragments = absorber.text_fragments

        for fragment in text_fragments:
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # Set very long text
            field.alternate_name = (
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                " sed do eiusmod tempor incididunt ut labore et dolore magna"
                " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
                " ullamco laboris nisi ut aliquip ex ea commodo consequat."
                " Duis aute irure dolor in reprehenderit in voluptate velit"
                " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
                " occaecat cupidatat non proident, sunt in culpa qui officia"
                " deserunt mollit anim id est laborum."
            )
            document.form.add(field)

        # Save document
        document.save(outfile)
```

## Buat Blok Teks Tersembunyi yang Muncul saat Hover di PDF

Tambahkan teks mengambang interaktif ke dokumen PDF. Ini menimpa teks yang tidak terlihat [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) pada frasa target dan memperlihatkan yang tersembunyi [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) ketika pengguna mengarahkan kursor ke atasnya. Teknik ini ideal untuk bantuan kontekstual, anotasi, atau penyajian konten dinamis.

1. Buat dokumen PDF baru.
1. Simpan PDF sehingga dapat dibuka kembali untuk penyiapan interaktivitas.
1. Buka kembali dokumen PDF.
1. Temukan teks target menggunakan [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. Buat yang tersembunyi [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).
1. Tambahkan bidang tersembunyi ke dokumen [`Form`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) koleksi.
1. Buat tidak terlihat [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/).
1. Tetapkan aksi mouse ("`on_enter`, `on_exit`) menggunakan [`HideAction`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/hideaction/) untuk menampilkan/menyembunyikan bidang tersembunyi.
1. Simpan dokumen akhir.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing
import sys
from os import path

def create_hidden_text_block(outfile):
    # Create PDF document
    with ap.Document() as document:
        #  Add paragraph with text
        document.pages.add().paragraphs.add(
            ap.text.TextFragment("Move the mouse cursor here to display floating text")
        )
        # Save PDF document
        document.save(outfile)

    # Open document with text
    with ap.Document(outfile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display floating text"
        )
        # Accept the absorber for the document pages
        document.pages.accept(absorber)
        # Get the first extracted text fragment
        text_fragments = absorber.text_fragments
        fragment = text_fragments[1]

        # Create hidden text field for floating text in the specified rectangle of the page
        floating_field = ap.forms.TextBoxField(
            fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
        )
        # Set text to be displayed as field value
        floating_field.value = 'This is the "floating text field".'
        # We recommend to make field 'readonly' for this scenario
        floating_field.read_only = True
        # Set 'hidden' flag to make field invisible on document opening
        floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

        # Setting a unique field name isn't necessary but allowed
        floating_field.partial_name = "FloatingField_1"

        # Setting characteristics of field appearance isn't necessary but makes it better
        floating_field.default_appearance = ap.annotations.DefaultAppearance(
            "Helv", 10, drawing.Color.blue
        )
        floating_field.characteristics.background = drawing.Color.light_blue
        floating_field.characteristics.border = drawing.Color.dark_blue
        floating_field.border = ap.annotations.Border(floating_field)
        floating_field.border.width = 1
        floating_field.multiline = True

        # Add text field to the document
        document.form.add(floating_field)
        # Create invisible button on text fragment position
        button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # Create new hide action for specified field (annotation) and invisibility flag.
        # (You also may refer floating field by the name if you specified it above.)
        # Add actions on mouse enter/exit at the invisible button field

        button_field.actions.on_enter = ap.annotations.HideAction(floating_field, False)
        button_field.actions.on_exit = ap.annotations.HideAction(floating_field)

        # Add button field to the document
        document.form.add(button_field)

        # Save document
        document.save(outfile)
```

## Topik Teks Terkait

- [Bekerja dengan teks dalam PDF menggunakan Python](/pdf/id/python-net/working-with-text/)
- [Gunakan FloatingBox untuk tata letak teks PDF di Python](/pdf/id/python-net/floating-box/)
- [Cari dan ekstrak teks PDF di Python](/pdf/id/python-net/search-and-get-text-from-pdf/)
- [Menambahkan teks ke PDF](/pdf/id/python-net/add-text-to-pdf-file/)