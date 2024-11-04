---
title: Dapatkan Informasi File PDF di Python
type: docs
weight: 40
url: /java/get-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

Untuk Mendapatkan Informasi File dari dokumen Pdf menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **GetPdfFileInfo**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Dapatkan informasi dokumen
doc_info = doc.getInfo();

# Tampilkan informasi dokumen
print "Penulis:-" + str(doc_info.getAuthor())
print "Tanggal Pembuatan:-" + str(doc_info.getCreationDate())
print "Kata Kunci:-" + str(doc_info.getKeywords())
print "Tanggal Modifikasi:-" + str(doc_info.getModDate())
print "Subjek:-" + str(doc_info.getSubject())
print "Judul:-" + str(doc_info.getTitle())
```

**Unduh Kode Berjalan**

Unduh **Dapatkan Informasi File PDF (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)