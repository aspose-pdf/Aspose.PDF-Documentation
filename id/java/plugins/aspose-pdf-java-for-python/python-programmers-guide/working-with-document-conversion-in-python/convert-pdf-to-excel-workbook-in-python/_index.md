---
title: Mengonversi PDF ke Buku Kerja Excel di Python
type: docs
weight: 20
url: id/java/convert-pdf-to-excel-workbook-in-python/
lastmod: "2021-06-05"
---

Untuk mengonversi dokumen PDF ke Buku Kerja Excel menggunakan **Aspose.PDF Java untuk Python**, cukup panggil modul **PdfToExcel**.

```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# Memulai objek ExcelSave Option
excelsave=self.ExcelSaveOptions();

# Simpan output ke format XLS
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "Dokumen telah berhasil dikonversi"
```

**Unduh Kode Berjalan**

Unduh **Konversi PDF ke Buku Kerja Excel (Aspose.PDF)** dari salah satu situs pemrograman sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)