---
title: Hapus Halaman Tertentu dari File PDF di Python
type: docs
weight: 20
url: /python-java/delete-a-particular-page-from-the-pdf-file-in-python/
---

Untuk menghapus Halaman Tertentu dari dokumen PDF menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **DeletePage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# hapus halaman tertentu
pdf.getPages().delete(2)

# simpan file PDF yang baru dibuat
doc.save(self.dataDir + "output.pdf")

print "Halaman berhasil dihapus!"

```

**Unduh Kode yang Sedang Berjalan**

Unduh **Hapus Halaman (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)