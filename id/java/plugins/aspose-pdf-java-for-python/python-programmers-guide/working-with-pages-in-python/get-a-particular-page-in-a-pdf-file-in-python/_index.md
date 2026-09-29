---
title: Dapatkan Halaman Tertentu dalam File PDF di Python
linktitle: Dapatkan Halaman Tertentu dalam File PDF di Python
type: docs
weight: 30
url: /id/java/get-a-particular-page-in-a-pdf-file-in-python/
description: Jelajahi cara mengekstrak halaman tertentu dari file PDF di Python menggunakan Aspose.PDF untuk penanganan dokumen yang detail.
lastmod: "2026-09-29"
---
Untuk mendapatkan Halaman Tertentu dalam dokumen PDF menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **GetPage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get the page at particular index of Page Collection
pdf_page = pdf.getPages().get_Item(1)

# create a new Document object
new_document = self.Document()

# add page to pages collection of new document object
new_document.getPages().add(pdf_page)

# save the newly generated PDF file
new_document.save(self.dataDir + "output.pdf")

print "Process completed successfully!

```

 **Unduh Kode yang Berjalan**

Unduh **Get Page (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)
