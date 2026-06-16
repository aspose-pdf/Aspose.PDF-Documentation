---
title: Simpan Metadata dengan XMP
linktitle: Simpan Metadata dengan XMP
type: docs
weight: 30
url: /id/python-net/save-metadata-with-xmp/
description: Simpan metadata PDF menggunakan XMP dengan Aspose.PDF for Python via .NET
lastmod: "2026-06-12"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menyimpan Metadata PDF dengan XMP Menggunakan Aspose.PDF for Python
Abstract: Panduan ini menunjukkan cara menyimpan metadata PDF menggunakan XMP (Extensible Metadata Platform) dengan Aspose.PDF for Python via .NET. XMP memastikan bahwa metadata standar dan khusus disematkan dalam format XML yang terstandarisasi di dalam PDF, meningkatkan kompatibilitas lintas aplikasi dan alur kerja.
---

Metadata PDF dapat disimpan dengan berbagai cara, dan XMP adalah metode modern serta terstandarisasi untuk menyematkan metadata di dalam file PDF. Dengan menggunakan Aspose.PDF, Anda dapat memperbarui bidang standar seperti Title, Subject, Keywords, dan Creator, lalu menyimpannya dalam format XMP untuk memastikan kompatibilitas yang lebih luas dan ketahanan di masa depan. Metode ini direkomendasikan dibandingkan metode penyimpanan metadata lama.

1. Muat file PDF.
1. Atur bidang metadata standar.
1. Simpan metadata dalam format XMP.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def save_info_with_xmp(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    # Save updated metadata
    pdf_info.save_new_info_with_xmp(outfile)
```
