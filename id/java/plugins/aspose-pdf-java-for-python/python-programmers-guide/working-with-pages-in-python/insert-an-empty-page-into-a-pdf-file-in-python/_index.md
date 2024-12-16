---
title: Menyisipkan Halaman Kosong ke dalam Berkas PDF di Python
type: docs
weight: 70
url: /id/java/insert-an-empty-page-into-a-pdf-file-in-python/
lastmod: "2021-06-05"
---

Untuk menyisipkan halaman kosong ke dalam dokumen PDF menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **InsertEmptyPage**.

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# sisipkan halaman kosong dalam PDF
pdf_document.getPages().insert(1)

# Simpan berkas keluaran yang digabungkan (dokumen target)
pdf_document.save(self.dataDir + "output.pdf")

print "Halaman kosong berhasil ditambahkan!"

```

**Unduh Kode yang Berjalan**

Unduh **Menyisipkan Halaman Kosong (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)