---
title: Membuat PDF yang sesuai dengan PDF/3-A dan melampirkan faktur ZUGFeRD dalam Python
linktitle: Melampirkan ZUGFeRD ke PDF
type: docs
weight: 10
url: /id/python-net/attach-zugferd/
description: Pelajari cara menghasilkan dokumen PDF dengan ZUGFeRD dalam Aspose.PDF untuk Python via .NET
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Melampirkan ZUGFeRD ke PDF

Kami merekomendasikan langkah-langkah berikut untuk melampirkan ZUGFeRD ke PDF:

1. Impor pustaka Aspose.PDF dan beri alias ap untuk kemudahan.
1. Tentukan jalur ke direktori di mana file PDF input dan output berada.
1. Tentukan jalur ke file PDF yang akan diproses.
1. Muat file PDF dari variabel jalur dan buat objek Document.
1. Buat objek FileSpecification untuk file XML yang berisi metadata faktur. Gunakan variabel jalur dan string deskripsi untuk membuat objek FileSpecification.

1. Tetapkan properti `mime_type` dan `af_relationship` dari objek FileSpecification ke `text/xml` dan `ALTERNATIVE`, masing-masing.
1. Tambahkan objek fileSpecification ke koleksi file tersemat objek dokumen. Ini melampirkan file XML ke dokumen PDF sebagai file metadata faktur.
1. Konversikan dokumen PDF ke format PDF/A-3A. Gunakan jalur ke file log, enumerasi `PdfFormat.PDF_A_3A`, dan enumerasi `ConvertErrorAction.DELETE` untuk mengonversi objek dokumen.
1. Simpan dokumen PDF dengan ZUGFeRD yang terlampir.

```python
import aspose.pdf as ap

# Tentukan jalur ke direktori di mana file PDF input dan output berada
_dataDir = "./"

# Muat file PDF yang akan diproses
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Buat objek FileSpecification untuk file XML yang berisi metadata faktur
description = "Metadata faktur yang sesuai dengan standar ZUGFeRD"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Tetapkan tipe MIME dan properti AFRelationship dari file tersemat
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Tambahkan file tersemat ke koleksi file tersemat dokumen PDF
document.embedded_files.add("factur",fileSpecification)

# Konversikan dokumen PDF ke format PDF/A-3A
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Simpan dokumen PDF dengan ZUGFeRD yang terlampir
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```