---
title: Optimalkan Dokumen PDF untuk Web di Python
type: docs
weight: 60
url: /id/java/optimize-pdf-document-for-the-web-in-python/
lastmod: "2021-06-05"
---

Untuk mengoptimalkan dokumen PDF untuk web menggunakan **Aspose.PDF Java untuk Python**, cukup panggil metode **optimize_web** dari kelas **Optimize**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Optimalkan untuk web
doc.optimize();

# Simpan dokumen output
doc.save(self.dataDir + "Optimized_Web.pdf")

print "PDF telah dioptimalkan untuk Web, silakan periksa file output."
```

**Unduh Kode yang Berjalan**

Unduh **Optimalkan PDF untuk Web (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)