---
title: Memperbarui Dimensi Halaman di Python
type: docs
weight: 90
url: id/python-java/update-page-dimensions-in-python/
---

<ins>Untuk memperbarui Dimensi halaman menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **UpdatePageDimensions**.

**Kode Python**
```s
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# dapatkan koleksi halaman
page_collection = pdf.getPages()

# dapatkan halaman tertentu
pdf_page = page_collection.get_Item(1)

# atur ukuran halaman sebagai A4 (11.7 x 8.3 inci) dan di Aspose.PDF, 1 inci = 72 poin
# jadi dimensi A4 dalam poin akan menjadi (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# simpan file PDF yang baru dihasilkan
pdf.save(self.dataDir + "output.pdf")

print "Dimensi berhasil diperbarui!"

```

**Unduh Kode yang Berjalan**

Unduh **Update Page Dimensions (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)