---
title: "Memperbarui dimensi halaman di Python"
linktitle: "Memperbarui dimensi halaman di Python"
type: docs
weight: 90
url: /id/java/update-page-dimensions-in-python/
description: Pahami cara memperbarui dimensi halaman dalam dokumen PDF di Python menggunakan Aspose.PDF untuk kontrol tata letak dokumen yang lebih baik.
lastmod: "2026-09-30"
---
Untuk memperbarui Dimensi halaman menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **UpdatePageDimensions**.

```python
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get page collection
page_collection = pdf.getPages()

# get particular page
pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file
pdf.save(self.dataDir + "output.pdf")

print "Dimensions updated successfully!"

```

**Mengunduh kode yang dapat dijalankan**

Download **Perbarui Dimensi Halaman (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
