---
title: Menyisipkan Halaman Kosong ke dalam File PDF dengan Python
linktitle: Menyisipkan Halaman Kosong ke dalam File PDF dengan Python
type: docs
weight: 70
url: /id/java/insert-an-empty-page-into-a-pdf-file-in-python/
description: Pelajari cara menyisipkan halaman kosong pada posisi apa pun dalam file PDF menggunakan Python dan Aspose.PDF untuk struktur dokumen yang fleksibel.
lastmod: "2026-09-29"
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

**Unduh Kode yang Berjalan**

Download\u0412\u00A0**Sisipkan Halaman Kosong (Aspose.PDF)**\u0412\u00A0dari\u0412\u00A0salah satu situs pengkodean sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)
