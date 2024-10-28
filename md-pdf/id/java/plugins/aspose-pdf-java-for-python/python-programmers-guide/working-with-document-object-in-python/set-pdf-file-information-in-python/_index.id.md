---
title: Mengatur Informasi File PDF di Python
type: docs
weight: 90
url: /java/set-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

Untuk memperbarui informasi dokumen Pdf menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **SetPdfFileInfo**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Dapatkan informasi dokumen
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF untuk java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("Informasi PDF");
doc_info.setTitle("Mengatur Informasi Dokumen PDF");

# simpan dokumen yang diperbarui dengan informasi baru

doc.save(self.dataDir + "Updated_Information.pdf")
print "Perbarui informasi dokumen, silakan periksa file keluaran."
```

**Unduh Kode Berjalan**

Unduh **Mengatur Informasi File PDF (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)