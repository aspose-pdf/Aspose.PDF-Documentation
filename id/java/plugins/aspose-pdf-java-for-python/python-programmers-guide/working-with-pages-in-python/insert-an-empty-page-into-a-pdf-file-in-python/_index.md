---
title: "Menyisipkan halaman kosong ke dalam file PDF dengan Python"
linktitle: "Menyisipkan halaman kosong ke dalam file PDF dengan Python"
type: docs
weight: 70
url: /id/java/insert-an-empty-page-into-a-pdf-file-in-python/
description: Pelajari cara menyisipkan halaman kosong pada posisi apa pun dalam file PDF menggunakan Python dan Aspose.PDF untuk struktur dokumen yang fleksibel.
lastmod: "2026-09-30"
---
Untuk Menyisipkan Halaman Kosong ke dalam dokumen PDF menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **InsertEmptyPage**.

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().insert(1)

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**Mengunduh kode yang dapat dijalankan**

Download **Sisipkan Halaman Kosong (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)
