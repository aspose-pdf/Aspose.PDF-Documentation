---
title: Menggabungkan File PDF di Python
type: docs
weight: 10
url: id/python-java/concatenate-pdf-files-in-python/
---

Untuk menggabungkan file PDF menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **ConcatenatePdfFiles**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Buka dokumen sumber
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Tambahkan halaman dokumen sumber ke dokumen target
pdf1.getPages().add(pdf1.getPages())

# Simpan file keluaran yang telah digabungkan (dokumen target)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "Dokumen baru telah disimpan, silakan periksa file keluaran"
```

**Unduh Kode yang Berjalan**

Unduh **Menggabungkan File PDF (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)