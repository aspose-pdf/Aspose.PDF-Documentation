---
title: "Menghapus halaman tertentu dari file PDF di Python"
linktitle: "Menghapus halaman tertentu dari file PDF di Python"
type: docs
weight: 20
url: /id/java/delete-a-particular-page-from-the-pdf-file-in-python/
description: Pelajari cara menghapus halaman tertentu dari dokumen PDF di Python menggunakan Aspose.PDF, yang menyediakan pengeditan dokumen yang efisien.
lastmod: "2026-09-30"
---
Untuk menghapus Halaman Tertentu dari dokumen PDF menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **DeletePage**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# delete a particular page
pdf.getPages().delete(2)

# save the newly generated PDF file
doc.save(self.dataDir + "output.pdf")

print "Page deleted successfully!"

```

**Mengunduh kode yang dapat dijalankan**

Unduh **Delete Page (Aspose.PDF)** dari  salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)
