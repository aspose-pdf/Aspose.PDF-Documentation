---
title: Memutar Halaman PDF Menggunakan Python
linktitle: Memutar Halaman PDF
type: docs
weight: 110
url: /id/python-net/rotate-pages/
description: Topik ini menjelaskan cara memutar orientasi halaman dalam file PDF yang ada secara programatis dengan Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara memutar Halaman dalam PDF dengan Python
Abstract: Artikel ini memberikan panduan tentang cara secara programatis memperbarui atau mengubah orientasi halaman dalam file PDF yang ada menggunakan Python. Dengan memanfaatkan Aspose.PDF untuk Python via .NET, pengguna dapat dengan mudah beralih antara orientasi lanskap dan potret dengan menyesuaikan properti MediaBox halaman. Artikel ini menyertakan potongan kode Python yang menunjukkan cara mengulang halaman dalam dokumen PDF, memodifikasi dimensi dan posisi MediaBox mereka, serta menyesuaikan CropBox jika diperlukan. Selain itu, artikel menjelaskan cara mengatur sudut rotasi halaman menggunakan metode 'rotate' untuk mencapai orientasi yang diinginkan. Proses berakhir dengan menyimpan file PDF yang telah diperbarui.
---

Topik ini menjelaskan cara memperbarui atau mengubah orientasi halaman dalam file PDF yang ada secara programatis dengan Python.

## Ubah Orientasi Halaman

Fungsi ini memutar setiap halaman dari sebuah PDF [`Dokumen`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 90 derajat searah jarum jam menggunakan Aspose.PDF untuk Python.
Fungsi ini berguna untuk memperbaiki masalah orientasi halaman, seperti dokumen hasil pindai yang berada miring. PDF asli tetap tidak berubah, dan versi yang diputar disimpan sebagai file baru.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_page(infile, outfile):
    """
    Rotate all pages in a PDF document by 90 degrees clockwise.

    Demonstrates how to rotate PDF pages using the Aspose.PDF library.
    This function applies a 90-degree clockwise rotation to every page
    in the input document and saves the result to a new file.

    Args:
        infile (str): Path to the input PDF file to rotate.
        outfile (str): Path where the rotated PDF will be saved.

    Returns:
        None: The function modifies the PDF pages and saves to the output path.

    Note:
        - Applies 90-degree clockwise rotation (ap.Rotation.ON90) to all pages
        - Rotates every page in the document uniformly
        - The original document is not modified; a new file is created
        - Rotation options include: ON90 (90°), ON180 (180°), ON270 (270°)
        - Useful for correcting page orientation or adjusting layout

    Example:
        >>> rotate_page("input.pdf", "rotated_output.pdf")
        # Rotates all pages 90 degrees clockwise and saves to rotated_output.pdf
    """
    document = ap.Document(infile)
    for page in document.pages:
        # `page` is a `Page` object; `rotate` uses the `Rotation` enum
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```


