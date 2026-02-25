---
title: Membuat PDF yang mematuhi PDF/3-A dan melampirkan faktur ZUGFeRD dalam Python
linktitle: Lampirkan ZUGFeRD ke PDF
type: docs
weight: 10
url: /id/python-net/attach-zugferd/
description: Pelajari cara membuat dokumen PDF dengan ZUGFeRD di Aspose.PDF untuk Python melalui .NET
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara melampirkan ZUGFeRD ke dokumen PDF
Abstract: Artikel ini menyediakan panduan langkah demi langkah tentang cara melampirkan ZUGFeRD (format untuk faktur elektronik) ke dokumen PDF menggunakan pustaka Aspose.PDF. Prosedur dimulai dengan mengimpor pustaka yang diperlukan dan menyiapkan jalur direktori untuk file masukan dan keluaran. Ini melibatkan memuat file PDF target ke dalam objek Document, dan membuat objek FileSpecification untuk file metadata faktur XML. Properti penting seperti `mime_type` dan `af_relationship` diatur untuk memastikan integrasi metadata yang tepat. File XML kemudian ditambahkan ke koleksi file tersemat PDF, secara efektif melampirkannya sebagai metadata. Selanjutnya, dokumen PDF dikonversi ke format PDF/A-3A, yang cocok untuk pengarsipan dokumen elektronik, sebelum menyimpan PDF akhir dengan ZUGFeRD tersemat. Artikel ini diakhiri dengan cuplikan kode Python yang menunjukkan penerapan langkah-langkah ini, menampilkan integrasi ZUGFeRD dengan PDF untuk manajemen dokumen yang lebih baik.
---

## Lampirkan ZUGFeRD ke PDF

Kami menyarankan langkah-langkah berikut untuk melampirkan ZUGFeRD ke PDF:

1. Impor pustaka Aspose.PDF dan beri alias ap untuk kemudahan.
1. Tentukan jalur ke direktori tempat file PDF masukan dan keluaran berada.
1. Tentukan jalur ke file PDF yang akan diproses.
1. Muat file PDF dari variabel jalur dan buat objek Document.
1. Buat objek FileSpecification untuk file XML yang berisi metadata faktur. Gunakan variabel jalur dan string deskripsi untuk membuat objek FileSpecification.
1. Atur properti `mime_type` dan `af_relationship` pada objek FileSpecification menjadi `text/xml` dan `ALTERNATIVE`, masing-masing.
1. Tambahkan objek fileSpecification ke koleksi file tersemat pada objek dokumen. Ini melampirkan file XML ke dokumen PDF sebagai file metadata faktur.
1. Konversi dokumen PDF ke format PDF/A-3A. Gunakan jalur ke file log, enumerasi `PdfFormat.PDF_A_3A`, dan enumerasi `ConvertErrorAction.DELETE` untuk mengkonversi objek dokumen.
1. Simpan dokumen PDF dengan ZUGFeRD terlampir.

```python
import aspose.pdf as ap

# Define the path to the directory where the input and output PDF files are located
_dataDir = "./"

# Load the PDF file that will be processed
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Create a FileSpecification object for the XML file that contains the invoice metadata
description = "Invoice metadata conforming to ZUGFeRD standard"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Set the MIME type and the AFRelationship properties of the embedded file
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Add the embedded file to the PDF document's embedded files collection
document.embedded_files.add("factur",fileSpecification)

# Convert the PDF document to the PDF/A-3A format
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Save the PDF document with the attached ZUGFeRD
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```

