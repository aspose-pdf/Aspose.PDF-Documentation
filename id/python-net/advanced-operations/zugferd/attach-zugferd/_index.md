---
title: Membuat PDF yang mematuhi PDF/3-A dan melampirkan faktur ZUGFeRD dengan Python
linktitle: Lampirkan ZUGFeRD ke PDF
type: docs
weight: 10
url: /id/python-net/attach-zugferd/
description: Pelajari cara membuat dokumen PDF dengan ZUGFeRD di Aspose.PDF for Python via .NET
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara melampirkan ZUGFeRD ke dokumen PDF
Abstract: Artikel ini menyediakan panduan langkah demi langkah tentang cara melampirkan ZUGFeRD (format untuk faktur elektronik) ke dokumen PDF menggunakan pustaka Aspose.PDF. Prosedurnya dimulai dengan mengimpor pustaka yang diperlukan dan menyiapkan jalur direktori untuk file input dan output. Ini melibatkan memuat file PDF target ke dalam objek Document, dan membuat objek FileSpecification untuk file metadata faktur XML. Properti penting seperti `mime_type` dan `af_relationship` diatur untuk memastikan integrasi metadata yang tepat. File XML kemudian ditambahkan ke koleksi file tersemat PDF, secara efektif melampirkannya sebagai metadata. Selanjutnya, dokumen PDF dikonversi ke format PDF/A-3A, yang cocok untuk arsip dokumen elektronik, sebelum menyimpan PDF akhir dengan ZUGFeRD yang tersemat. Artikel ini diakhiri dengan potongan kode Python yang menunjukkan implementasi langkah-langkah tersebut, menampilkan integrasi ZUGFeRD dengan PDF untuk manajemen dokumen yang lebih baik.
---

## Lampirkan ZUGFeRD ke PDF

Kami merekomendasikan langkah-langkah berikut untuk melampirkan ZUGFeRD ke PDF:

1. Impor pustaka Aspose.PDF dan beri alias ap untuk kemudahan.
1. Tentukan path ke direktori tempat file PDF input dan output berada.
1. Tentukan path ke file PDF yang akan diproses.
1. Muat file PDF dari variabel path dan buat objek Document.
1. Buat objek FileSpecification untuk file XML yang berisi metadata faktur. Gunakan variabel path dan string deskripsi untuk membuat objek FileSpecification.
1. Atur `mime_type` dan `af_relationship` properti dari objek FileSpecification ke `text/xml` dan `ALTERNATIVE`, masing-masing.
1. Tambahkan objek fileSpecification ke koleksi file tertanam dari objek dokumen. Ini melampirkan file XML ke dokumen PDF sebagai file metadata faktur.
1. Konversi dokumen PDF ke format PDF/A-3A. Gunakan jalur ke file log, the `PdfFormat.PDF_A_3A` enumerasi, dan `ConvertErrorAction.DELETE` enumerasi untuk mengubah objek dokumen.
1. Simpan dokumen PDF dengan ZUGFeRD yang terlampir.

```python
import sys
import os
import aspose.pdf as ap

def attach_invoice_zugferd_format(infile, invoice, outfile):
    document = ap.Document(infile)

    # Create a FileSpecification object for the XML file that contains the invoice metadata
    description = "Invoice metadata conforming to ZUGFeRD standard"
    file_specification = ap.FileSpecification(invoice, description)

    # Set the MIME type and the AFRelationship properties of the embedded file
    file_specification.mime_type = "text/xml"
    file_specification.af_relationship = ap.AFRelationship.ALTERNATIVE

    # Add the embedded file to the PDF document's embedded files collection
    document.embedded_files.add("factur", file_specification)

    # Convert the PDF document to the PDF/A-3A format
    log_path = outfile.replace(".pdf", "_log.xml")
    document.convert(log_path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
