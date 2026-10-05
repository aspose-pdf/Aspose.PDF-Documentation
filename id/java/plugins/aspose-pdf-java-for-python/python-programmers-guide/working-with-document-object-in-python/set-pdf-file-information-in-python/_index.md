---
title: "Mengatur informasi file PDF di Python"
linktitle: "Mengatur informasi file PDF di Python"
type: docs
weight: 90
url: /id/java/set-pdf-file-information-in-python/
description: Pelajari cara mengatur informasi file PDF seperti penulis, judul, dan lainnya di Python menggunakan Aspose.PDF untuk mengatur dokumen.
lastmod: "2026-09-30"
---
Untuk memperbarui informasi dokumen Pdf menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **SetPdfFileInfo**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("PDF Information");
doc_info.setTitle("Setting PDF Document Information");

# save update document with new information

doc.save(self.dataDir + "Updated_Information.pdf")
print "Update document information, please check output file."
```

**Mengunduh kode yang dapat dijalankan**

Unduh **Atur Informasi File PDF (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
