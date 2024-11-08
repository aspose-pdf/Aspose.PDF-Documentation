---
title: Konversi PDF ke TXT di Python
linktitle: Konversi PDF ke TXT
type: docs
weight: 20
url: /id/python-cpp/convert-pdf-to-txt/
lastmod: "2024-04-23"
description: Aspose.PDF untuk Python melalui pustaka C++ memungkinkan Anda mengonversi PDF ke format TXT menggunakan Python.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Konversi PDF ke TXT

Aspose.PDF untuk Python melalui C++ mendukung konversi dokumen PDF ke file Teks dengan langkah-langkah berikut:

1. Membuat jalur file input dan output
1. Membuat instance dari fasad ekstraktor PDF dengan [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. Mengikat file PDF ke ekstraktor dengan [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)
1. Mengekstrak teks dari file PDF menggunakan [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. Menulis teks yang diekstraksi ke file output
1. Simpan PDF output dengan metode 'document.save'.

Cuplikan kode di bawah ini menunjukkan cara mengonversi Gambar JPG ke PDF menggunakan Python melalui C++:

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Membuat path direktori data
    dataDir = os.path.join(os.getcwd(), "samples")

    # Membuat path file input
    input_file = os.path.join(dataDir, "sample.pdf")

    # Membuat path file output
    output_file = os.path.join(dataDir, "results", "pdf-to-txt.txt")

    # Membuat instance dari PDF extractor facade
    extactor = apCore.facades_pdf_extractor_create()

    # Mengikat file PDF ke extractor
    apCore.facades_facade_bind_pdf(extactor, input_file)

    # Mengekstrak teks dari file PDF
    text = apCore.facades_pdf_extractor_extract_text(extactor)

    # Menulis teks yang diekstrak ke file output
    with open(output_file, 'w') as f:
        f.write(text)
```