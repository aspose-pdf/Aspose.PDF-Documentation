---
title: "Mengatur kedaluwarsa PDF di Python"
linktitle: "Mengatur kedaluwarsa PDF di Python"
type: docs
weight: 80
url: /id/java/set-pdf-expiration-in-python/
description: Pelajari cara mengatur tanggal kedaluwarsa untuk file PDF di Python menggunakan Aspose.PDF untuk akses dokumen yang sensitif waktu.
lastmod: "2026-09-30"
---
Untuk mengatur kedaluwarsa dokumen PDF menggunakan **Aspose.PDF Java for Python**, cukup panggil kelas **SetExpiration**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# save update document with new information
doc.save(self.dataDir + "set_expiration.pdf");

print "Update document information, please check output file."
```

**Mengunduh kode yang dapat dijalankan**

Download **Set PDF Expiration (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
