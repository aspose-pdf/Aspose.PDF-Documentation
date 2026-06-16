---
title: Ekstrak Tautan
linktitle: Ekstrak Tautan
type: docs
weight: 70
url: /id/python-net/extract-links/
description: Contoh ini mengikat PDF masukan, mengekstrak semua tautan, dan mencetak koordinat serta URI-nya (jika tersedia).
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak Tautan dari PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara mengekstrak semua tautan dari dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara mengidentifikasi dan mengambil tautan web atau tautan lain yang dapat ditindaklanjuti yang tertanam dalam PDF.
---

PDF sering berisi elemen interaktif seperti tautan web, tautan dokumen, dan aksi khusus. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat mengekstrak semua anotasi tautan dari PDF secara programatik. Ini memungkinkan Anda untuk memeriksa atau memproses tautan, misalnya, untuk memvalidasi URL atau menganalisis pola navigasi dalam dokumen.

1. Buat sebuah instance PdfContentEditor.
1. Hubungkan dokumen PDF input.
1. Ekstrak semua tautan menggunakan 'extract_link()'.
1. Iterasi melalui tautan yang diekstrak.
1. Periksa apakah sebuah tautan adalah LinkAnnotation dan apakah aksinya adalah GoToURIAction.
1. Cetak koordinat persegi panjang dan URI.
1. Tampilkan pesan jika tidak ada tautan yang ditemukan.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def extract_links(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Extract links from the document
    links = content_editor.extract_link()

    count = 0
    for link in links:
        count += 1
        print(f"Link {count}: {link.rect}")
        if is_assignable(link, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"  URI: {action.uri}")

    if count == 0:
        print("No links found")
```
