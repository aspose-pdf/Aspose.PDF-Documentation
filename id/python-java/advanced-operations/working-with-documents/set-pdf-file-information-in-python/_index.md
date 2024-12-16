---
title: Mengatur Informasi File PDF di Python
type: docs
weight: 90
url: /id/python-java/set-pdf-file-information-in-python/
---

<ins>Untuk memperbarui informasi dokumen Pdf menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **SetPdfFileInfo**.

**Kode Python**
```
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

# simpan dokumen dengan informasi baru

doc.save(self.dataDir + "Updated_Information.pdf")
print "Perbarui informasi dokumen, silakan periksa file keluaran."
```

**Unduh Kode yang Berjalan**

Unduh **Mengatur Informasi File PDF (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)