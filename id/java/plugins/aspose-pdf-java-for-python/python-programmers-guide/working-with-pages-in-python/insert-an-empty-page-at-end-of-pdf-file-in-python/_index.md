---
title: Menyisipkan Halaman Kosong di Akhir File PDF dalam Python
type: docs
weight: 60
url: /id/java/insert-an-empty-page-at-end-of-pdf-file-in-python/
lastmod: "2021-06-05"
---

Untuk menyisipkan halaman kosong di akhir dokumen PDF menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **InsertEmptyPageAtEndOfFile**.

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# sisipkan halaman kosong di PDF
pdf_document.getPages().add();

# Simpan file keluaran yang telah digabungkan (dokumen target)
pdf_document.save(self.dataDir + "output.pdf")

print "Halaman kosong berhasil ditambahkan!"

```

**Unduh Kode Berjalan**

Unduh **Menyisipkan Halaman Kosong di Akhir File PDF (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)