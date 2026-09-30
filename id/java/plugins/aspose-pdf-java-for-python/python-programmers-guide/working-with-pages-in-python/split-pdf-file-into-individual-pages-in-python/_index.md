---
title: "Memisahkan file PDF menjadi halaman individual dalam Python"
linktitle: "Memisahkan file PDF menjadi halaman individual dalam Python"
type: docs
weight: 80
url: /id/java/split-pdf-file-into-individual-pages-in-python/
description: Jelajahi cara memisahkan PDF menjadi halaman individual dalam Python menggunakan Aspose.PDF, memungkinkan ekstraksi dan manajemen halaman yang mudah.
lastmod: "2026-09-30"
---
Untuk memisahkan dokumen PDF menjadi halaman individual menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **SplitAllPages**.

```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# loop through all the pages
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# create a new Document object
new_document = self.Document();

# get the page at particular index of Page Collection
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Split process completed successfully!";
```

**Mengunduh kode yang dapat dijalankan**

Unduh **Split Pages (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
