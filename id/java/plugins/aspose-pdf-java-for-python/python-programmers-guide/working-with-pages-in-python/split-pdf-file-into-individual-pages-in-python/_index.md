---
title: Pisahkan File PDF Menjadi Halaman Individu di Python
type: docs
weight: 80
url: /id/java/split-pdf-file-into-individual-pages-in-python/
lastmod: "2021-06-05"
---

Untuk memisahkan dokumen PDF menjadi halaman individu menggunakan **Aspose.PDF Java untuk PHP**, cukup panggil kelas **SplitAllPages**.

```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# loop melalui semua halaman
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# buat objek Document baru
new_document = self.Document();

# dapatkan halaman pada indeks tertentu dari Koleksi Halaman
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# simpan file PDF yang baru dibuat
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Proses pembagian selesai dengan sukses!";
```

**Unduh Kode yang Berjalan**

Unduh **Split Pages (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)