---
title: Mendapatkan Halaman Tertentu dalam File PDF di Python
type: docs
weight: 30
url: /python-java/get-a-particular-page-in-a-pdf-file-in-python/
---

Untuk mendapatkan Halaman Tertentu dalam dokumen PDF menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **GetPage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# mendapatkan halaman pada indeks tertentu dari Koleksi Halaman
pdf_page = pdf.getPages().get_Item(1)

# buat objek Dokumen baru
new_document = self.Document()

# tambahkan halaman ke koleksi halaman dari objek dokumen baru
new_document.getPages().add(pdf_page)

# simpan file PDF yang baru dihasilkan
new_document.save(self.dataDir + "output.pdf")

print "Proses selesai dengan sukses!

```

**Unduh Kode Berjalan**

Unduh **Get Page (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)