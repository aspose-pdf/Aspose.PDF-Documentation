---
title: Menyisipkan Halaman Kosong di Akhir File PDF di Python
type: docs
weight: 60
url: id/python-java/insert-an-empty-page-at-end-of-pdf-file-in-python/
---

<ins>Untuk Menyisipkan Halaman Kosong di akhir dokumen PDF menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **InsertEmptyPageAtEndOfFile**.

**Kode Python**
```

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# menyisipkan halaman kosong dalam PDF
pdf_document.getPages().add();

# Simpan file keluaran yang digabungkan (dokumen target)
pdf_document.save(self.dataDir + "output.pdf")

print "Halaman kosong berhasil ditambahkan!"

```

**Unduh Kode Berjalan**

Unduh **Menyisipkan Halaman Kosong di Akhir File PDF (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)