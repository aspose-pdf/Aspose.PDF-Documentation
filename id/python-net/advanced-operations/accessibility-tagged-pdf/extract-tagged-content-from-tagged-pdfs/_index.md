---
title: Ekstrak Konten Bertanda dari PDF
linktitle: Ekstrak Konten Bertanda
type: docs
weight: 20
url: /id/python-net/extract-tagged-content-from-tagged-pdfs/
description: Artikel ini menjelaskan cara mengekstrak konten bertanda dari dokumen PDF menggunakan Aspose.PDF untuk Python via .NET
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

Dalam artikel ini Anda akan belajar cara mengekstrak konten bertanda dari dokumen PDF menggunakan Python.

## Mendapatkan Konten PDF Bertanda

Untuk mendapatkan konten Dokumen PDF dengan Teks Bertanda, Aspose.PDF menawarkan properti [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) dari kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Potongan kode berikut menunjukkan cara mendapatkan konten dokumen PDF dengan Teks Bertanda:

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Work with Tagged PDF content
        # Set Title and Language for Document
        tagged_content.set_title("Simple Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Save Tagged PDF Document
        document.save(path_outfile)
```

## Mendapatkan Struktur Akar

Untuk mendapatkan struktur akar Dokumen PDF Bertanda, Aspose.PDF menawarkan properti [struct_tree_root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties) dari antarmuka [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) dan [root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties).

Potongan kode berikut menunjukkan cara mendapatkan struktur akar Dokumen PDF Bertanda:

```python

    import aspose.pdf as ap

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
```

## Mengakses Elemen Anak

Untuk mengakses elemen anak dari Dokumen PDF Bertanda, Aspose.PDF menawarkan kelas [ElementList](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/elementlist/). Potongan kode berikut menunjukkan cara mengakses elemen anak dari Dokumen PDF Bertanda:

```python

    import aspose.pdf as ap
    from aspose.pycore import *

    # Open PDF Document
    with ap.Document(path_infile) as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Access to root element(s)
        element_list = tagged_content.struct_tree_root_element.child_elements

        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = cast(ap.logical_structure.StructureElement, element)

                # Get properties
                title = structure_element.title
                language = structure_element.language
                actual_text = structure_element.actual_text
                expansion_text = structure_element.expansion_text
                alternative_text = structure_element.alternative_text

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
        document.save(path_outfile)
```
