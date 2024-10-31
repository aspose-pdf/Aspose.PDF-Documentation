---
title: Menyisipkan Halaman Kosong ke dalam File PDF di Python
type: docs
weight: 70
url: /python-java/insert-an-empty-page-into-a-pdf-file-in-python/
---

<ins>Untuk Menyisipkan Halaman Kosong ke dalam dokumen Pdf menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **InsertEmptyPage**.

**Kode Python**
```

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# sisipkan halaman kosong ke dalam PDF
pdf_document.getPages().insert(1)

# Simpan file keluaran yang digabungkan (dokumen target)
pdf_document.save(self.dataDir + "output.pdf")

print "Halaman kosong berhasil ditambahkan!"

```

**Unduh Kode Berjalan**

Unduh **Insert an Empty Page (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)