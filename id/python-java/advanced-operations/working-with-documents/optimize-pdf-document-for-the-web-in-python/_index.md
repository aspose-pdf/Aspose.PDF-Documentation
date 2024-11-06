---
title: Optimalkan Dokumen PDF untuk Web dalam Python
type: docs
weight: 60
url: id/python-java/optimize-pdf-document-for-the-web-in-python/
---

<ins>Untuk mengoptimalkan dokumen PDF untuk web menggunakan **Aspose.PDF Java for Python**, cukup panggil metode **optimize_web** dari kelas **Optimize**.

**Kode Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Optimalkan untuk web
doc.optimize();

#Simpan dokumen keluaran
doc.save(self.dataDir + "Optimized_Web.pdf")

print "PDF dioptimalkan untuk Web, silakan periksa file keluaran."
```


**Unduh Kode yang Berjalan**

Unduh **Optimalkan PDF untuk Web (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/Optimize/Optimize.py)