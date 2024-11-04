---
title: Mengonversi PDF ke Teks di Python
linktitle: Mengonversi PDF ke format lain
type: docs
weight: 90
url: /python-cpp/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: konversi, PDF, EPUB, LaText, Teks, XPS, Python
description: Topik ini menunjukkan cara mengonversi file PDF ke format file lain seperti Teks menggunakan Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Mengonversi PDF ke Teks

**Aspose.PDF for Python** mendukung konversi seluruh dokumen PDF dan halaman tunggal ke file Teks.

### Mengonversi dokumen PDF ke file Teks

Anda dapat mengonversi dokumen PDF ke file TXT menggunakan kelas 'TextDevice'.

1. Membuat jalur file input dan output
1. Membuat instance dari fasad ekstraktor PDF dengan [extractor_create]
(https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. Mengikat file PDF ke ekstraktor dengan [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)

1. Mengekstrak teks dari file PDF menggunakan [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. Menulis teks yang diekstrak ke file keluaran
1. Simpan PDF keluaran dengan metode 'document.save'.

Cuplikan kode berikut menjelaskan cara mengekstrak teks dari semua halaman.

```python

    from AsposePdfPython import *

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"

    extactor = extractor_create()
    extractor_bind_pdf(extactor,input_pdf)
    text = extractor_extract_text(extactor)

    with open(output_pdf, 'w') as f:
        f.write(text)
```