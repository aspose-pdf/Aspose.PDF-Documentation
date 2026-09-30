---
title: "Mendapatkan informasi file PDF dalam Python"
linktitle: "Mendapatkan informasi file PDF dalam Python"
type: docs
weight: 40
url: /id/java/get-pdf-file-information-in-python/
description: Jelajahi cara mengambil informasi file PDF yang detail seperti metadata dan properti dalam Python menggunakan Aspose.PDF untuk manajemen dokumen.
lastmod: "2026-09-30"
---
Untuk Mendapatkan Informasi File Dokumen Pdf menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **GetPdfFileInfo**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

# Show document information
print "Author:-" + str(doc_info.getAuthor())
print "Creation Date:-" + str(doc_info.getCreationDate())
print "Keywords:-" + str(doc_info.getKeywords())
print "Modify Date:-" + str(doc_info.getModDate())
print "Subject:-" + str(doc_info.getSubject())
print "Title:-" + str(doc_info.getTitle())
```

**Mengunduh kode yang dapat dijalankan**

Unduh **Dapatkan Informasi File PDF (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
