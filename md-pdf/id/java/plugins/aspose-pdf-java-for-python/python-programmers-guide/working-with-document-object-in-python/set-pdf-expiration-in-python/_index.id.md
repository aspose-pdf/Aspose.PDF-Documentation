---
title: Menetapkan Kedaluwarsa PDF di Python
type: docs
weight: 80
url: /java/set-pdf-expiration-in-python/
lastmod: "2021-06-05"
---

Untuk menetapkan kedaluwarsa dokumen Pdf menggunakan **Aspose.PDF Java untuk Python**, cukup panggil kelas **SetExpiration**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# simpan dokumen yang diperbarui dengan informasi baru
doc.save(self.dataDir + "set_expiration.pdf");

print "Perbarui informasi dokumen, silakan periksa file keluaran."
```

**Unduh Kode Berjalan**

Unduh **Set PDF Expiration (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)